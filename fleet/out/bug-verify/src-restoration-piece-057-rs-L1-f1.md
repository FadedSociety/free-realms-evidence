<!-- fleet job=bug-verify id=src-restoration-piece-057-rs-L1-f1 status=done turns=4 usd=0.0033 tokens(read,write,in,out)=[23187, 15917, 10, 2135] model=claude-haiku-5-5 -->
# medium: prototype/osfr-tools/src/restoration/piece_057.rs:429-431

**Verdict:** refuted (as a live defect in the server). The code-level gap is real, but nothing in the shipped server can reach it.

**Severity if confirmed:** n/a. If integration later wires this module in, the gap would be medium, not high: a player could take a drop only if the integration code itself builds the request from a claimed killer.

**Evidence:**

1. **Module tree (refutes).** `src/lib.rs` declares `pub mod` for the live modules (`abilities`, `account`, `encounter`, `enemies`, `fishing`, ...) and does not declare `restoration` or `piece_057`. A search of `prototype/osfr-tools` for `piece_057` and `LootLedger` finds only:
   - `tests/piece_057.rs:12-13`: `#[path = "../src/restoration/piece_057.rs"] mod piece_057;`
   - `tests/piece_057.rs:18, 165, 203, 230`: uses of `LootLedger::new()`.
   - Docs and notes (`notes/Reviews/Delegated Task Readiness.v1.json:1443`, `notes/Research/Pieces/057 Loot and enemy rewards.md:127`) that record "Lead registers `restoration::piece_057` in the shared module list" as an open step.
   - No `src/**` file or `#[path]` in `osfr-gateway.rs` or `osfr-login.rs` includes it. `LootLedger` has no caller outside the test target, so the defect is test-only.

2. **Input reach (not reached).** There is no packet handler or save path that constructs `LootRequest` or calls `register_defeat`. The only defeat handling in the notes is the existing `35/3` removal branch, which the readiness note says is not yet linked to this ledger.

3. **Line facts (accurate, but moot).** Lines 429-431 (`register_defeat` stores only `KillId`) and 433-439 (`claimant != killer` check against caller-supplied fields) match the claim. Lines 24-25 and 414-415 do overstate the policy: the ledger does not enforce killer-only looting against a registered killer. That is a documentation accuracy point for when the module is integrated, not a runtime defect today.

**Corrected fix:** not needed for the current tree. When integration lands, the proposed fix is sound: store the credited killer in the defeat record and have `grant` compare `request.claimant` against that stored value instead of the caller's `killer` field. Record that as an integration requirement, not as a current bug.
