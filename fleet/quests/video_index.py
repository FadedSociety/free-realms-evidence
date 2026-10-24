"""video_index.py: the reviewed video frames (video-archive/review/haiku/*.jsonl) as an FTS5 index for the fleet's
`lookup` tool (lead, 2026-10-23). Each row is one frame: its key (video id/frame), screen kind, zone, and the NPCs,
dialog, quest, store, landmarks and other text the frame reviewer read off it.

  python video_index.py      -> lab/references/quest-lines/video.sqlite
"""
import json
import sqlite3
from pathlib import Path

LAB = Path(r"C:\Users\Bryce\Documents\Projects\CartoonMMO\lab")


def flat(v):
    if isinstance(v, dict):
        return " ".join(flat(x) for x in v.values())
    if isinstance(v, list):
        return " ".join(flat(x) for x in v)
    return "" if v is None else str(v)


def main():
    out = LAB / "references" / "quest-lines" / "video.sqlite"
    out.unlink(missing_ok=True)
    con = sqlite3.connect(out)
    con.execute("CREATE VIRTUAL TABLE frames USING fts5(key UNINDEXED, screen, zone, body)")
    n = 0
    for path in sorted((LAB / "video-archive" / "review" / "haiku").glob("*.jsonl")):
        for line in open(path, encoding="utf-8"):
            try:
                r = json.loads(line)
            except json.JSONDecodeError:
                continue
            body = " | ".join(f"{k}: {flat(r.get(k))}" for k in ("npcs", "dialog", "quest", "store", "landmarks",
                                                                 "job_level", "items_seen", "other_text")
                              if flat(r.get(k)).strip())
            con.execute("INSERT INTO frames VALUES(?,?,?,?)", (r.get("key"), r.get("screen"), r.get("zone"), body))
            n += 1
    con.commit()
    print(json.dumps({"frames": n}))


if __name__ == "__main__":
    main()
