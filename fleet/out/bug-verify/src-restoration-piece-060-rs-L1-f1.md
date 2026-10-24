<!-- fleet job=bug-verify id=src-restoration-piece-060-rs-L1-f1 status=done turns=4 usd=0.0041 tokens(read,write,in,out)=[32719, 20749, 10, 2361] model=claude-haiku-5-5 -->
# medium: `prototype/osfr-tools/src/restoration/piece_060.rs:545-562`

**Verdict:** refuted

**Severity if confirmed:** n/a. The defect is real only inside an unwired module, so the server cannot hit it.

**Evidence:**

1. **Module tree (decisive).** `piece_060.rs` is not in the real server build. No file under `prototype/osfr-tools/src` contains `piece_060`. The `restoration` module is not declared in `src/lib.rs`. The only `#[path]` includes of `restoration/` files in `src` are for `piece_056` (`src/abilities.rs`), `piece_098` (`src/bin/osfr-terrain.rs`), `piece_077` (`src/gameplay.rs`), `piece_025` (`src/housing_service.rs`) and `piece_081` (`src/inventory.rs`). The only include of `piece_060.rs` is `tests/piece_060.rs:28-30` (`#[path = "../src/restoration/piece_060.rs"] #[allow(dead_code)] mod piece_060;`). Its header (`tests/piece_060.rs:3-5`) says the lead has not yet registered the module. So the defect exists only in test builds.

2. **No caller reaches it.** The claimed reach is "the owning engine forwards a client's socket drop to `Lifecycle::disconnect` and the grace timer to `Registry::reap`." A search for `.disconnect(`, `.reap(` and `zone_ready(` across `prototype/osfr-tools` finds no caller of `piece_060`'s `Lifecycle`/`Registry`. The live `zone_ready` path is `encounter.rs:1467` (`on_zone_ready`), called from `gameplay.rs:1790` and `:3054`. That is a different implementation, and the claimed bug does not apply to it.

3. **The cited lines are accurate as code, but the premise fails.** `piece_060.rs:371-395` does gate on `!member.is_connected() || Ready`, and `disconnect` (`:545-562`) and `reap` (`:583-610`) do not re-run that gate. So the stall is correct as a reading of an unwired module. The doc comment at `:369-370` is consistent with the gate, and the stall is a missing re-check in a module the server does not compile. It cannot strand a live player.

**Corrected fix:** not needed for the server. If the lead registers `piece_060` later, re-check this item at that point, since the disconnect/reap gap would then become reachable. The suggested fix (re-run the gate in `disconnect` and `reap`, returning the `41/107` packets) would be correct for that case.
