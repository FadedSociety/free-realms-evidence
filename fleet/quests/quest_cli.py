"""quest_cli.py: the fleet's lookup/locale tools plus a model-free id check, as a command line for Claude Code
subagents (lead, 2026-10-23). Run with lab/tools/fleet-venv/Scripts/python.exe -I.

  quest_cli.py lookup "<FTS5 query>" [client,wiki,articles,video]   tagged client text / wiki / articles / video
  quest_cli.py locale <id | regex>                                   one client string, or a regex search
  quest_cli.py ids <id> [<id> ...]                                   each id: exists? FLAG? text
"""
import sqlite3
import sys
from pathlib import Path

LAB = Path(r"C:\Users\Bryce\Documents\Projects\CartoonMMO\lab")
sys.path.insert(0, str(LAB / "fleet"))
import fleet  # noqa: E402


def ids(values):
    idx = sqlite3.connect(f"file:{LAB / 'references' / 'quest-lines' / 'index.sqlite'}?mode=ro", uri=True)
    out = []
    for v in values:
        row = idx.execute("SELECT type, hint, flag, text FROM strings WHERE id = ?", (int(v),)).fetchone()
        text = fleet.tool_locale(str(int(v))).split(": ", 1)[-1]
        if text == "(no such id)":
            out.append(f"locale:{v} DOES NOT EXIST")
        else:
            typ, hint, flag, _ = row or ("?", None, None, None)
            out.append(f"locale:{v} [{typ} | {hint or '-'}{' | FLAG ' + flag if flag else ''}] {text[:200]}")
    return "\n".join(out)


def main():
    if len(sys.argv) < 3:
        print(__doc__)
        return 2
    cmd, arg = sys.argv[1], sys.argv[2]
    if cmd == "lookup":
        sources = sys.argv[3].split(",") if len(sys.argv) > 3 else None
        print(fleet.tool_lookup(arg, sources, 8))
    elif cmd == "locale":
        print(fleet.tool_locale(arg))
    elif cmd == "ids":
        print(ids(a for a in sys.argv[2:] if a.isdigit()))
    else:
        print(__doc__)
        return 2
    return 0


if __name__ == "__main__":
    sys.exit(main())
