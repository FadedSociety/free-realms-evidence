"""file_bug_briefs.py: turn confirmed bug-verify verdicts into build briefs (lead, 2026-10-22).

Each confirmed medium finding outside lead-only files gets its own brief in lab/autopilot/incoming/ (the tick numbers
it); confirmed lows outside lead-only files share one brief. Findings in lead-only files (autopilot DENY_RE) are only
listed, for the lead. Prints what it wrote.
"""
import re
from pathlib import Path

FLEET = Path(__file__).resolve().parent
INCOMING = FLEET.parent / "autopilot" / "incoming"
LEAD_ONLY = re.compile(r"src/(login|login_auth|account|account_store|identity|session|soe|soe_send|net_policy|"
                       r"security_log|trade|character_store|game_store|studio)\.rs|src/bin/osfr-(login|account)\.rs|"
                       r"launcher/")


def slug(text):
    return re.sub(r"[^a-z0-9]+", "-", text.lower()).strip("-")[:48]


confirmed = []
for verify in sorted((FLEET / "out" / "bug-verify").glob("*.md")):
    text = verify.read_text(encoding="utf-8")
    if not re.search(r"\*\*Verdict:\*\*\s*`?confirmed", text, re.I):
        continue
    sev = re.search(r"\*\*Severity if confirmed:\*\*\s*`?([a-z]+)", text, re.I)
    sev = sev.group(1).lower() if sev else "medium"
    claim = text.split("\n")[1][2:]
    path = re.search(r"((?:prototype/osfr-tools/)?src/[\w/.-]+\.rs|session\.rs)", claim)
    source = verify.stem.rsplit("-f", 1)[0]
    confirmed.append({"sev": sev, "claim": claim, "path": path.group(1) if path else "?", "verify": verify.name,
                      "hunt": f"{source}.md"})

body_rule = ("The finding was raised by a first-pass reviewer and confirmed by an independent skeptic (Claude Haiku "
             "fleet, read-only). Read both, then re-check the claim yourself at the tip before changing anything; if "
             "it does not hold, stop and report `AUTOPILOT: BLOCKED` with the evidence.\n\n"
             "Write a failing test first (it must fail on the current code for the stated reason), then the smallest "
             "fix, keeping hubs from growing.\n")
lead, lows = [], []
for f in confirmed:
    if LEAD_ONLY.search(f["path"]) or f["path"] == "session.rs":
        lead.append(f)
    elif f["sev"] in ("medium", "high"):
        name = f"fleet-fix-{slug(f['path'].split('/')[-1] + '-' + f['claim'].split(':')[-1])}.md"
        (INCOMING / name).write_text(
            f"title: Fix confirmed defect at {f['path']}\n---\n\n## Finding\n\n{f['claim']}\n\n"
            f"- First pass: `lab/fleet/out/bug-hunt/{f['hunt']}`\n- Verification: `lab/fleet/out/bug-verify/{f['verify']}`"
            f"\n\n## Work\n\n{body_rule}", encoding="utf-8", newline="\n")
        print("brief", name)
    else:
        lows.append(f)
if lows:
    lines = "\n".join(f"- {f['claim']} (`lab/fleet/out/bug-verify/{f['verify']}`)" for f in lows)
    (INCOMING / "fleet-fix-confirmed-low-defects.md").write_text(
        f"title: Fix {len(lows)} confirmed low-severity defects from the fleet bug hunt\n---\n\n## Findings\n\n{lines}\n\n"
        f"## Work\n\nEach is small. {body_rule}Skip any that do not hold at the tip and say why.\n",
        encoding="utf-8", newline="\n")
    print("brief fleet-fix-confirmed-low-defects.md with", len(lows), "findings")
for f in lead:
    print("LEAD-ONLY", f["sev"], f["claim"], "->", f["verify"])
