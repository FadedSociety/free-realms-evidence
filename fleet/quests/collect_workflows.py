"""collect_workflows.py: fold subscription workflow runs (Claude Code workflows of Haiku subagents) into one list per
domain, the same shape world_lines.py writes for the API fleet (lead, 2026-10-23).

  python collect_workflows.py <domain> <task-output-json>@<run id> [...]

Each task output is the workflow's result file ({"result": [{key, status, version, rounds, wireable}, ...]}); the
answers and critic verdicts come from the workflow's journal.jsonl next to it (agent labels infer:/revise:/critic:<key>).
Writes references/quest-lines/<domain plural>.json (key, status, version, rounds, wireable, answer, last_critiques).
"""
import json
import re
import sys
from pathlib import Path

OUT = Path(r"C:\Users\Bryce\Documents\Projects\CartoonMMO\lab\references\quest-lines")
WORKFLOWS = Path(r"C:\Users\Bryce\.claude\projects\C--Users-Bryce-Documents-Projects-CartoonMMO"
                 r"\206f3367-8b57-49c8-991d-c27ffc764984\subagents\workflows")


def journal_rows(run_id):
    labels, answers, verdicts = {}, {}, {}
    for line in open(WORKFLOWS / run_id / "journal.jsonl", encoding="utf-8"):
        try:
            row = json.loads(line)
        except json.JSONDecodeError:
            continue
        if row.get("type") == "started":
            labels[row.get("agentId")] = row.get("label") or ""
        elif row.get("type") == "result" and isinstance(row.get("result"), dict):
            m = re.match(r"(infer|revise|critic):([^:]+)", labels.get(row.get("agentId"), ""))
            if m:
                if m.group(1) == "critic":
                    verdicts.setdefault(m.group(2), []).append(row["result"])
                else:
                    answers[m.group(2)] = row["result"]
    return answers, verdicts


def main():
    domain, outputs = sys.argv[1], sys.argv[2:]
    index = {}
    if (OUT / f"{domain}-index.json").exists():
        index = json.load(open(OUT / f"{domain}-index.json"))
    rows = {}
    for arg in outputs:  # <task output file>@<workflow run id> (the output file does not name its run)
        path, run_id = arg.rsplit("@", 1)
        result = json.loads(Path(path).read_text(encoding="utf-8")).get("result") or []
        answers, verdicts = journal_rows(run_id)
        for r in result:
            key = r["key"]
            rows[index.get(key, key)] = {"key": index.get(key, key), "status": r["status"], "version": r.get("version"),
                                         "rounds": r.get("rounds"), "wireable": r.get("wireable"),
                                         "answer": answers.get(key), "last_critiques": verdicts.get(key, [])[-2:]}
    ordered = [rows[k] for k in sorted(rows)]
    plural = domain[:-1] + "ies" if domain.endswith("y") else domain + "s"
    (OUT / f"{plural}.json").write_text(json.dumps(ordered, indent=1, ensure_ascii=False), encoding="utf-8")
    counts = {}
    for r in ordered:
        counts[r["status"]] = counts.get(r["status"], 0) + 1
    print(json.dumps({"domain": domain, "records": counts,
                      "final_wireable": sum(1 for r in ordered if r["status"] == "final" and r["wireable"]),
                      "with_answer": sum(1 for r in ordered if r["answer"])}))


if __name__ == "__main__":
    main()
