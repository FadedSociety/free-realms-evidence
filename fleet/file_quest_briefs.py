"""file_quest_briefs.py: first wave of quest-building briefs from the fleet's quest dossiers (lead, 2026-10-22).

Ranks every `done` dossier by evidence (distinct locale ids cited plus repo citations), takes the top N quest givers
and writes briefs of 10 givers each to lab/autopilot/incoming/ (the tick numbers them). The rest wait for a later
wave; out/quest-dossier/wave.txt records which givers were sent.
"""
import re
import sys
from pathlib import Path

FLEET = Path(__file__).resolve().parent
OUT = FLEET / "out" / "quest-dossier"
INCOMING = FLEET.parent / "autopilot" / "incoming"
N = int(sys.argv[1]) if len(sys.argv) > 1 else 60
sent_file = OUT / "wave.txt"
sent = set(sent_file.read_text().split()) if sent_file.exists() else set()

scored = []
for f in OUT.glob("*.md"):
    text = f.read_text(encoding="utf-8")
    if "status=done" not in text.split("\n")[0] or f.stem in sent:
        continue
    locale = len(set(re.findall(r"locale\s*`?(\d{2,9})", text)))
    repo = len(re.findall(r"repo:[\w/ .-]+:\d+", text))
    scored.append((locale * 2 + repo, f.stem, text.split("\n")[1][2:]))
scored.sort(reverse=True)
wave = scored[:N]
for n in range(0, len(wave), 10):
    group = wave[n:n + 10]
    lines = "\n".join(f"- {title} (`lab/fleet/out/quest-dossier/{stem}.md`, evidence score {score})"
                      for score, stem, title in group)
    (INCOMING / f"fleet-quests-wave1-{n // 10 + 1}.md").write_text(
        f"title: Build evidenced quests from fleet dossiers (wave 1, set {n // 10 + 1})\n---\n\n## Why\n\n"
        "Quest definitions lived on the old server and are lost; the client shipped their text. A read-only Claude "
        "Haiku agent built an evidence dossier per quest giver (title, offer/objective/completion text ids, steps, "
        "targets, rewards marked (R)). These ten givers have the best-evidenced dossiers.\n\n## Quest givers\n\n"
        f"{lines}\n\n## Work\n\nRead each dossier and re-check its ids with the client text before relying on them. "
        "Build the quests whose title, offer text and every step are evidenced, as data in the right "
        "`prototype/osfr-tools/data/content/quests/*.json` (follow the existing quests' schema and how they cite "
        "sources; reconstructed parts are `(R)`). Skip a quest with an unevidenced step and list it in your report. "
        "Each built quest needs a test that accepts, progresses and turns it in through the real request path, and "
        "the enabled-quest reachability checks must stay green.\n",
        encoding="utf-8", newline="\n")
    print("brief set", n // 10 + 1, "givers", len(group))
sent_file.write_text("\n".join(sorted(sent | {stem for _, stem, _ in wave})) + "\n")
print("remaining done dossiers not yet sent:", len(scored) - len(wave))
