"""enemy_hp_video.py: enemy health from gameplay video (lead, 2026-10-26; Bryce: "Do the enemy health from gameplay
video first"). Memory enemy-hp-from-video: count damage-to-death per enemy, cross-check the health-bar fraction.

  python enemy_hp_video.py aggregate   -> lab/references/quest-lines/enemy-hp-video.json (+ .md summary)

`frame_items()` (job hp-frame in jobs.py) is the local resolver: each enemy name (enemies.json definitions and
field_enemies.json rows) is matched by its exact client text to the OCR sightings of the archived videos
(video-archive/sightings.sqlite); every distinct frame from 6 s before to 20 s after a sighting cluster becomes one
vision item, at most WINDOWS clusters per enemy and FRAMES frames per cluster. The frame reader reports the target
frame, health-bar fraction and floating damage numbers; `aggregate` turns each cluster's readings into an estimate:
max health = damage dealt to the target / health fraction lost, and the hits counted to a defeat.
"""
import collections
import json
import re
import sqlite3
import sys
from pathlib import Path

CMMO = Path(r"C:\Users\Bryce\Documents\Projects\CartoonMMO")
LAB = CMMO / "lab"
CONTENT = CMMO / "autopilot-int" / "prototype" / "osfr-tools" / "data" / "content"
VIDEO = LAB / "video-archive"
LOCALE = LAB / "references" / "opening-journal-text-v2" / "locale" / "en_us_data.dat"
OUT = LAB / "fleet" / "out" / "hp-frame"
REF = LAB / "references" / "quest-lines"
WINDOWS, FRAMES, GAP, BEFORE, AFTER = 3, 20, 30, 6, 20


def locale():
    loc = {}
    for line in open(LOCALE, encoding="utf-8-sig", errors="replace"):
        p = line.rstrip("\r\n").split("\t", 2)
        if len(p) == 3:
            loc[p[0]] = p[2].strip()
    return loc


def enemies():
    """{lowercase display name: [{source, id, level, max_health, damage}]} for every enemy row we ship."""
    loc = locale()
    rows = collections.defaultdict(list)
    for r in json.load(open(CONTENT / "enemies.json", encoding="utf-8"))["definitions"]:
        name = loc.get(str(r.get("name_string_id"))) or r.get("kind") or ""
        rows[name.lower()].append({"source": "enemies.json", "id": r["id"], "name": name, "level": r.get("level"),
                                   "max_health": r.get("max_health"), "damage": r.get("damage")})
    for r in json.load(open(CONTENT / "field_enemies.json", encoding="utf-8"))["enemies"]:
        rows[(r.get("name") or "").lower()].append({"source": "field_enemies.json", "id": r["guid"],
                                                    "name": r.get("name"), "level": r.get("level"),
                                                    "max_health": r.get("max_health"), "damage": r.get("damage")})
    rows.pop("", None)
    return rows, loc


def clusters():
    """{name: [(video, t0, t1, sightings)]}: the WINDOWS densest sighting clusters per enemy name."""
    rows, loc = enemies()
    ids = collections.defaultdict(list)
    for k, v in loc.items():
        if v.lower() in rows:
            ids[v.lower()].append(k)
    con = sqlite3.connect(f"file:{VIDEO / 'sightings.sqlite'}?mode=ro", uri=True)
    out = {}
    for name, sids in ids.items():
        seen = sorted(set(con.execute(f"SELECT video, t FROM sighting WHERE string_id IN ({','.join('?' * len(sids))})",
                                      sids)))
        found = []
        for video, t in seen:
            if found and found[-1][0] == video and t - found[-1][2] <= GAP:
                found[-1][2], found[-1][3] = t, found[-1][3] + 1
            else:
                found.append([video, t, t, 1])
        out[name] = sorted(found, key=lambda c: -c[3])[:WINDOWS]
    return out, rows


def frame_items():
    found, rows = clusters()
    items = []
    for name, cl in sorted(found.items()):
        known = "; ".join(f"{r['source']} {r['id']}: level {r['level']}, max_health {r['max_health']} (R)"
                          for r in rows[name])
        for n, (video, t0, t1, _) in enumerate(cl):
            frames = sorted(VIDEO.glob(f"out/{video}/frames/*.jpg"))
            pick = [f for f in frames if t0 - BEFORE <= int(f.stem) <= t1 + AFTER][:FRAMES]
            for f in pick:
                rid = re.sub(r"[^A-Za-z0-9]+", "-", f"{name}-{n}-{video}-{f.stem}").strip("-")
                prompt = (f"Enemy this clip was picked for: {rows[name][0]['name']} (its name was read on screen in "
                          f"video {video} between {t0} s and {t1} s; this frame is at {int(f.stem)} s).\n"
                          f"Our current server rows for it: {known}.\n\nRead the frame and submit the JSON result.")
                items.append({"id": rid, "title": f"{rows[name][0]['name']} {video} {int(f.stem)}s", "prompt": prompt,
                              "image": str(f)})
    return items


def result(path):
    text = path.read_text(encoding="utf-8")
    m = re.search(r"\{.*\}", text, re.S)
    try:
        return json.loads(m.group(0)) if m else None
    except json.JSONDecodeError:
        return None


def aggregate():
    found, rows = clusters()
    report = []
    for name, cl in sorted(found.items()):
        windows = []
        for n, (video, t0, t1, hits) in enumerate(cl):
            stem = re.sub(r"[^A-Za-z0-9]+", "-", f"{name}-{n}-{video}").strip("-")
            reads = []
            for p in sorted(OUT.glob(f"{stem}-*.md")):
                r = result(p)
                if r:
                    reads.append({"t": int(p.stem.rsplit("-", 1)[1]), **r})
            reads.sort(key=lambda r: r["t"])
            on = [r for r in reads if (r.get("target") or {}).get("name") and
                  name in str(r["target"]["name"]).lower()]
            fr = [(r["t"], r["target"].get("health_fraction")) for r in on
                  if isinstance(r["target"].get("health_fraction"), (int, float))]
            dealt = [d["value"] for r in on for d in r.get("damage_numbers") or []
                     if d.get("on") == "target" and isinstance(d.get("value"), (int, float))]
            texts = [r["target"].get("health_text") for r in on if r["target"].get("health_text")]
            lost = (max(f for _, f in fr) - min(f for _, f in fr)) if len(fr) > 1 else None
            # One fight per segment: a bar that jumps back up by 0.15 or more is a new enemy (or a respawn).
            # Damage in a segment counts positive hits on the target once; a number repeated in the next
            # frame is the same floating number still rising.
            fights, cur, prev = [], [], None
            for r in on:
                f = r["target"].get("health_fraction")
                if isinstance(f, (int, float)) and prev is not None and f - prev >= 0.15:
                    fights.append(cur)
                    cur = []
                cur.append(r)
                prev = f if isinstance(f, (int, float)) else prev
            fights.append(cur)
            seg_est, last_hits = [], set()
            for seg in fights:
                fs = [r["target"]["health_fraction"] for r in seg
                      if isinstance(r["target"].get("health_fraction"), (int, float))]
                hits = []
                for r in seg:
                    now = {d["value"] for d in r.get("damage_numbers") or []
                           if d.get("on") == "target" and isinstance(d.get("value"), (int, float)) and d["value"] > 0}
                    hits += sorted(now - last_hits)
                    last_hits = now
                if len(fs) > 1 and fs[0] - min(fs) >= 0.2 and hits:
                    seg_est.append({"from": seg[0]["t"], "to": seg[-1]["t"], "fraction_lost": round(fs[0] - min(fs), 2),
                                    "hits": hits, "max_health": round(sum(hits) / (fs[0] - min(fs)))})
            est = sorted(s["max_health"] for s in seg_est)[len(seg_est) // 2] if seg_est else None
            # Bar speed between the fullest reading and the emptiest one after it: seconds a full bar lasts.
            top = max(fr, key=lambda x: (x[1], -x[0])) if fr else None
            low = min((x for x in fr if x[0] > top[0]), key=lambda x: x[1], default=None) if top else None
            drop = (top[1] - low[1]) if low else 0
            attackers = max((r.get("attackers_visible") or 0 for r in on), default=0)
            windows.append({"video": video, "seconds": [t0, t1], "frames_read": len(reads), "frames_on_target": len(on),
                            "fractions": fr, "damage_on_target": dealt, "health_texts": texts,
                            "levels_read": sorted({r["target"].get("level") for r in on if r["target"].get("level")}),
                            "player_levels": sorted({(r.get("player") or {}).get("level") for r in reads
                                                     if (r.get("player") or {}).get("level")}),
                            "player_jobs": sorted({(r.get("player") or {}).get("job") for r in reads
                                                   if (r.get("player") or {}).get("job")}),
                            "attackers_max": attackers,
                            "defeated": any(r.get("target_defeated") for r in on),
                            "seconds_full_bar": round((low[0] - top[0]) / drop, 1) if drop >= 0.2 else None,
                            "fights": seg_est, "estimate_max_health": est})
        ests = [w["estimate_max_health"] for w in windows if w["estimate_max_health"]]
        report.append({"name": rows[name][0]["name"], "rows": rows[name], "windows": windows,
                       "estimate_max_health": sorted(ests)[len(ests) // 2] if ests else None,
                       "health_texts": sorted({t for w in windows for t in w["health_texts"]})})
    unseen = sorted(r[0]["name"] for k, r in rows.items() if not found.get(k))
    report = [e for e in report if e["windows"]]
    (REF / "enemy-hp-video.json").write_text(json.dumps({"enemies": report, "not_in_video": unseen}, indent=1),
                                             encoding="utf-8")
    lines = ["# Enemy health from gameplay video (lead, 2026-10-26)", "",
             "| Enemy | Our max_health (R) | Damage-based estimate | Full bar lasts (s), player level/job, attackers "
             "| Health texts read |", "|---|---|---|---|---|"]
    for e in report:
        ours = ", ".join(str(r["max_health"]) for r in e["rows"])
        speed = "; ".join(f"{w['seconds_full_bar']}s L{'/'.join(map(str, w['player_levels'])) or '?'} "
                          f"{'/'.join(w['player_jobs']) or '?'} x{w['attackers_max']} ({w['video']})"
                          for w in e["windows"] if w["seconds_full_bar"])
        lines.append(f"| {e['name']} | {ours} | {e['estimate_max_health'] or '-'} | {speed or '-'} | "
                     f"{', '.join(e['health_texts'][:4]) or '-'} |")
    lines += ["", f"Not in any archived video ({len(unseen)}): " + ", ".join(unseen)]
    (REF / "enemy-hp-video.md").write_text("\n".join(lines) + "\n", encoding="utf-8")
    print(json.dumps({"enemies": len(report), "with_estimate": sum(1 for e in report if e["estimate_max_health"]),
                      "not_in_video": len(unseen)}))


if __name__ == "__main__":
    if sys.argv[1:] == ["aggregate"]:
        aggregate()
    else:
        items = frame_items()
        print(json.dumps({"items": len(items), "enemies": len({i["title"].rsplit(" ", 2)[0] for i in items})}))
