"""client_ids.py: check the DeepSeek client-id results and offer them to objective_specs.py (lead, 2026-10-25).

Reads references/quest-lines/client-ids/result-worklist-*.json (one row per objective: found, evidence, confidence)
and accepts a row only when its ids exist in the client tables:
  minigame_id  client Resources/MiniGameData.txt         model_id     client Resources/Models.txt
  resource_id  the captured item catalogue definitions    position     3 numbers, not one of our reconstructed
  trigger      a ClientTrigger the server parses              (poi_anchor/unanchored) NPC positions
Low confidence, a list of several targets (split objectives) or a failed check leaves the row a candidate with
the reason, for the fix pass. `objective_specs.py resolve` applies accepted rows (`overlay()`).
Run `python client_ids.py` for the check report.
"""
import glob
import json
from pathlib import Path

LAB = Path(r"C:\Users\Bryce\Documents\Projects\CartoonMMO\lab")
CI = LAB / "references" / "quest-lines" / "client-ids"
RES = LAB / "working" / "OSFR.Client" / "OSFR Client" / "Resources"
CONTENT = Path(r"C:\Users\Bryce\Documents\Projects\CartoonMMO\autopilot-int\prototype\osfr-tools\data\content")
TRIGGERS = {"look_at": {"guid", "offset_tenths", "range", "angle_degrees"}, "ui_event": {"event"},
            "first_movement": {"mouse"}}  # quest_engine.rs ClientTrigger (deny_unknown_fields)


def table_ids(name):
    rows = (RES / name).read_text(encoding="utf-8", errors="replace").splitlines()
    return {int(r.split("^", 1)[0]) for r in rows if r[:1].isdigit()}


def tables():
    cat = json.load(open(LAB / "reports" / "native-20261024T0455Z-new" / "content" / "item-catalogue.json",
                         encoding="utf-8"))["definitions"]
    fake = set()
    for f in (CONTENT / "npcs").glob("*.json"):
        for r in json.load(open(f, encoding="utf-8")).get("records", []):
            if r.get("placement") in ("poi_anchor", "unanchored") and r.get("position"):
                fake.add(tuple(round(v, 2) for v in r["position"]))
    return {"minigame": table_ids("MiniGameData.txt"), "model": table_ids("Models.txt"),
            "item": {d["id"] for d in cat}, "fake_positions": fake}


def check(kind, found, t):
    """None when the found fields hold up against the client tables, else why not."""
    num = lambda v: isinstance(v, (int, float)) and not isinstance(v, bool)  # noqa: E731
    if kind == "finish_minigame":
        return None if found.get("minigame_id") in t["minigame"] else f"minigame {found.get('minigame_id')} not in MiniGameData"
    if kind == "defeat":
        return None if found.get("model_id") in t["model"] else f"model {found.get('model_id')} not in Models.txt"
    if kind == "gather_resource":
        return None if found.get("resource_id") in t["item"] else f"item {found.get('resource_id')} not in the catalogue"
    if kind == "visit_position":
        p = found.get("position")
        if not (isinstance(p, list) and len(p) == 3 and all(map(num, p))):
            return "position is not 3 numbers"
        return "position is one of our reconstructed NPC offsets" if tuple(round(v, 2) for v in p) in t["fake_positions"] else None
    if kind == "client_reported":
        trig = found.get("trigger") or {}
        fields = TRIGGERS.get(trig.get("type"))
        if not isinstance(found.get("client_id"), int) or fields is None:
            return f"trigger {trig.get('type')!r} is not one the server parses"
        return None if set(trig) - {"type"} == fields else f"trigger fields {sorted(set(trig) - {'type'})} != {sorted(fields)}"
    return f"kind {kind} not checked"


def overlay():
    """(quest key 'qN', objective index) -> {accepted, fields, why, evidence, confidence}."""
    t, out = tables(), {}
    for f in sorted(glob.glob(str(CI / "result-worklist-*.json"))):
        for r in json.load(open(f, encoding="utf-8")):
            found, why = r.get("found"), None
            if not found:
                why = "not found"
            elif isinstance(found, list):
                why = "several targets: split the objective" if len(found) > 1 else None
                found = found[0] if len(found) == 1 else found
            if why is None and r.get("confidence") == "low":
                why = "low confidence"
            if why is None:
                why = check(r["kind"], found, t)
            out[(f"q{r['quest_id']}", r["objective"])] = {"accepted": why is None, "fields": found, "why": why,
                                                          "evidence": r.get("evidence", []),
                                                          "confidence": r.get("confidence"), "notes": r.get("notes"),
                                                          "file": Path(f).name}
    return out


if __name__ == "__main__":
    t0 = {"minigame": {1}, "model": {2}, "item": {3}, "fake_positions": {(1.0, 2.0, 3.0)}}
    assert check("finish_minigame", {"minigame_id": 1}, t0) is None
    assert check("visit_position", {"position": [1.0, 2.0, 3.0]}, t0), "a reconstructed offset is not a position"
    assert check("client_reported", {"client_id": 5, "trigger": {"type": "first_movement", "mouse": False}}, t0) is None
    assert check("client_reported", {"client_id": 5, "trigger": {"type": "open_window"}}, t0)
    from collections import Counter
    o = overlay()
    by = Counter((v["file"].replace("result-worklist-", "").rsplit("-", 1)[0], v["accepted"]) for v in o.values())
    why = Counter(v["why"].split(" ")[0] + " " + v["why"].split(" ")[-1] for v in o.values() if v["why"])
    print(json.dumps({f"{k} {'ok' if a else 'no'}": n for (k, a), n in sorted(by.items())}, indent=1))
    print(why.most_common(12))
