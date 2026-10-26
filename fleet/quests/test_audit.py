"""test_audit.py: evidence packs for the test-suite audit (lead, 2026-10-26; world_lines.py --domain testaudit).

One pack per integration test file (prototype/osfr-tools/tests/*.rs, 445 on 2026-10-26). Pre-joined so a Haiku
agent compares instead of exploring: the file's tests with their doc lines, its crate imports and shared helper
modules, the task that created it and the last one that changed it, a content excerpt, and the five most similar
other test files (shared imports and test-name words) with their test names and origin tasks.
"""
import re
import subprocess
from collections import Counter
from pathlib import Path

REPO = Path(r"C:\Users\Bryce\Documents\Projects\CartoonMMO\autopilot-int")
TESTS = REPO / "prototype" / "osfr-tools" / "tests"
TEST_FN = re.compile(r"((?:\s*///[^\n]*\n)*)\s*#\[test\]\s*(?:#\[[^\]]*\]\s*)*fn\s+(\w+)")


def git_tasks(rel):
    log = subprocess.run(["git", "-C", str(REPO), "log", "--format=%s", "--", rel], capture_output=True,
                         text=True, encoding="utf-8", errors="replace").stdout.splitlines()
    ids = [m.group(0) for s in log if (m := re.search(r"\b[TFDL]\d{3}\b", s))]
    return {"created_by": ids[-1] if ids else None, "last_changed_by": ids[0] if ids else None}


def summarize(path):
    text = path.read_text(encoding="utf-8", errors="replace")
    tests = [{"name": m.group(2), "doc": " ".join(l.strip()[3:].strip() for l in m.group(1).splitlines() if l.strip())[:200]}
             for m in TEST_FN.finditer(text)]
    uses = sorted(set(re.findall(r"osfr_tools::(\w+)", text)))
    helpers = sorted(set(re.findall(r"(?:mod|#\[path\s*=\s*\")\s*\"?(?:\.\./)?(?:support|common)/(\w+)", text)))
    words = Counter(w for t in tests for w in t["name"].split("_") if len(w) > 3)
    return {"text": text, "tests": tests, "uses": uses, "helpers": helpers, "words": words}


def testaudit_packs(_ev):
    files = sorted(TESTS.glob("*.rs"))
    info = {f.stem: summarize(f) for f in files}
    packs = {}
    for f in files:
        me = info[f.stem]
        score = []
        for other, o in info.items():
            if other == f.stem:
                continue
            s = 2 * len(set(me["uses"]) & set(o["uses"])) + sum((me["words"] & o["words"]).values())
            if s:
                score.append((s, other))
        similar = [{"file": f"tests/{o}.rs", "shared_score": s, **git_tasks(f"prototype/osfr-tools/tests/{o}.rs"),
                    "tests": [t["name"] for t in info[o]["tests"]][:40]}
                   for s, o in sorted(score, reverse=True)[:5]]
        rel = f"prototype/osfr-tools/tests/{f.name}"
        packs[f.stem] = {"title": f"tests/{f.name}", "file": rel, **git_tasks(rel), "lines": me["text"].count("\n"),
                         "tests": me["tests"], "crate_modules_used": me["uses"], "shared_helpers": me["helpers"],
                         "excerpt": me["text"][:9000], "most_similar_files": similar}
    return packs
