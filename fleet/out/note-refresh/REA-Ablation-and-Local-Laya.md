<!-- fleet job=note-refresh id=REA-Ablation-and-Local-Laya status=done turns=10 usd=0.0103 tokens(read,write,in,out)=[187892, 35527, 22, 8003] model=claude-haiku-5-5 -->
# notes/Research/REA Ablation and Local Laya.md

**Verdict:** minor drift. Most of the note concerns tools and results that live in `lab/` and cannot be checked at the tip. The one checkable claim about our pipeline is overstated: the REA MCP is not disabled for every native-map worker.

**Corrections:**

- `old:` disabled for native-map workers to save ~230 MB RAM each.
  `new:` disabled for native-map workers launched with `--trim-tools` (off by default); `costpilot.py` and `recheck_run.py` always pass the same flags. The dispatcher's comment estimates ~300 MB RAM for unused plugins and servers together.
  `why:` `repo:scripts/native_map/dispatch.py:28` sets `-c mcp_servers.rea.enabled=false` inside `TOOL_FLAGS`. `repo:scripts/native_map/dispatch.py:207` applies those flags only `if self.a.trim_tools`. `repo:scripts/native_map/dispatch.py:638` defines `--trim-tools` as `store_true`, so it defaults to off. `repo:scripts/native_map/costpilot.py:55` and `repo:scripts/native_map/recheck_run.py:21` always include `D.TOOL_FLAGS`. The RAM comment is at `repo:scripts/native_map/dispatch.py:19-21` and gives ~300 MB, not ~230 MB.

**Checked and consistent (no change):**
- The lead's single centralized Ghidra import at `lab/decompiled/ghidra-full-20261010b` matches `repo:MODLOG.md:49-52`.
- Workers exposed to `nmq show` and `nmq bytes` match `repo:scripts/native_map/nmq.py:3-15`.
- Workers keeping REA's methodology documents matches `repo:scripts/native_map/mapper-prompt.md:7`.
- REA 6.3.0 with MCP reconnection pending, Ablation 2.49.0 failing the PE32 smoke test, and Laya 0.4.1 scoring 3–4/8 match `repo:AGENTS.md:60` and `repo:MODLOG.md:83-93`.
- The Laya/Jev reconciliation that re-reads the DB "with the no-return fix" fits the 2026-10-11 fix named in `repo:scripts/native_map/recheck.py:1`.

**Unsure:**
- Whether the REA MCP has since been reconnected in live Codex sessions. `AGENTS.md:60` still says "reconnection pending," and no later evidence was found at the tip.
- The accuracy tables, token budgets, costs, model hashes and file counts (Laya, Jev, Ablation pins and licence text). They point at `lab/reports/` and `lab/references/`, which are outside the repo, so they could not be verified.
- The Jev row for `scripts/native_map/costpilot.py` and the OpenRouter routing ("Codex Router, metered"). The code shows Codex `model_provider=codex-router` and OpenRouter model IDs, but the Jev eval script itself is not in the repo.</result>
