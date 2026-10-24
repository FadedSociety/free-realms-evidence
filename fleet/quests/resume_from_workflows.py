"""resume_from_workflows.py: turn stopped subscription workflow runs into the API round loop's state, so
world_lines.py finishes them on the fleet (lead, 2026-10-23).

  python resume_from_workflows.py <domain> <run id> [<run id> ...]

Replays each journal in order: infer/revise:<key> sets the answer (a new version clears the lens passes),
critic:<key>:<lens> records a verdict and a pass. A key whose current answer passed every lens is final.
Writes references/quest-lines/<domain>-state.json (world_lines.rounds format) and <domain>-packs.json (from the
per-key pack files), with numbered keys (n000) mapped to real ones through <domain>-index.json.
"""
import json
import re
import sys
from pathlib import Path

OUT = Path(r"C:\Users\Bryce\Documents\Projects\CartoonMMO\lab\references\quest-lines")
WORKFLOWS = Path(r"C:\Users\Bryce\.claude\projects\C--Users-Bryce-Documents-Projects-CartoonMMO"
                 r"\206f3367-8b57-49c8-991d-c27ffc764984\subagents\workflows")
LENSES = {"event": ("evidence", "calendar")}


def main():
    domain, runs = sys.argv[1], sys.argv[2:]
    index = json.load(open(OUT / f"{domain}-index.json")) if (OUT / f"{domain}-index.json").exists() else {}
    lenses = LENSES.get(domain, ("evidence", "world"))
    state = {}
    for run in runs:
        labels = {}
        for line in open(WORKFLOWS / run / "journal.jsonl", encoding="utf-8"):
            try:
                row = json.loads(line)
            except json.JSONDecodeError:
                continue
            if row.get("type") == "started":
                labels[row.get("agentId")] = row.get("label") or ""
                continue
            if row.get("type") != "result" or not isinstance(row.get("result"), dict):
                continue
            m = re.match(r"(infer|revise|critic):([^:]+)(?::(\w+))?", labels.get(row.get("agentId"), ""))
            if not m:
                continue
            key = index.get(m.group(2), m.group(2))
            s = state.setdefault(key, {"answer": None, "version": 0, "passed": [], "final": False, "critiques": [],
                                       "rounds": 0})
            if m.group(1) in ("infer", "revise"):
                s.update(answer=row["result"], version=s["version"] + 1, passed=[])
            else:
                s["critiques"] = (s["critiques"] + [row["result"]])[-4:]
                s["rounds"] += 1
                if row["result"].get("pass") and m.group(3) not in s["passed"]:
                    s["passed"].append(m.group(3))
            s["final"] = bool(s["answer"]) and all(l in s["passed"] for l in lenses)
    packs = {}
    for key in index.values() if index else state:
        p = OUT / f"{domain}-packs" / f"{key}.json"
        if p.exists():
            packs[key] = json.load(open(p, encoding="utf-8"))
            state.setdefault(key, {"answer": None, "version": 0, "passed": [], "final": False, "critiques": [],
                                   "rounds": 0})
    (OUT / f"{domain}-packs.json").write_text(json.dumps(packs, indent=1, ensure_ascii=False), encoding="utf-8")
    (OUT / f"{domain}-state.json").write_text(json.dumps(state, ensure_ascii=False), encoding="utf-8")
    print(json.dumps({"domain": domain, "records": len(state), "final": sum(s["final"] for s in state.values()),
                      "answered_not_final": sum(1 for s in state.values() if s["answer"] and not s["final"]),
                      "unanswered": sum(1 for s in state.values() if not s["answer"]),
                      "with_one_lens_passed": sum(1 for s in state.values() if not s["final"] and s["passed"])}))


if __name__ == "__main__":
    main()
