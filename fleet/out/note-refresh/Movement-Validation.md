<!-- fleet job=note-refresh id=Movement-Validation status=done turns=14 usd=0.0208 tokens(read,write,in,out)=[383510, 58269, 30, 19321] model=claude-haiku-5-5 -->
# notes/Research/Movement Validation.md

**Verdict:** Badly stale on integration status, with three moved citations and one test count that no longer matches the tree. The validator constants, the discontinuity rules, the capture arithmetic (98 + 1 runs, 14,982 updates, state counts and per-run table all sum correctly) and the native addresses I checked still hold.

**Corrections:**

1. `old:` No gateway or library file was changed. In gateway integration, mint tokens only from server-owned relocation/zone events, commit the server target at that point, persist the token returned by the validator, and treat Ignore as neither a commit nor a correction. Preserve ordinary reject/clamp behavior after timeout.
   `new:` The gateway is integrated: `gateway.rs` calls `movement::validate` on each opcode-125 report (gateway.rs:1522), mints zone-change tokens from server-owned zone transitions (gateway.rs:980, 1858, 1876) and developer-teleport tokens (gateway.rs:1739), persists the returned token (gateway.rs:1534), and treats Ignore as neither a commit nor a correction (gateway.rs:1536-1545). Ordinary reject/clamp behavior applies after timeout.
   `why:` repo:prototype/osfr-tools/src/gateway.rs:14-15, 980, 1400, 1522-1545, 1739, 1858, 1876. The gateway already imports and uses the validator, so the integration instructions describe finished work.

2. `old:` Shared gateway and library files remain for lead integration.
   `new:` The gateway is wired to the validator (`src/gateway.rs:14-15`, `1522`), and the module is exported from `src/lib.rs:56`.
   `why:` repo:prototype/osfr-tools/src/gateway.rs:14-15, 1522; repo:prototype/osfr-tools/src/lib.rs:56. Also see `notes/Design/Integration Queue.md:20`, which already lists the module as ready.

3. `old:` Result: 10 passed, 0 failed.
   `new:` Result: 8 passed, 0 failed (the test file defines 8 `#[test]` functions; see the Unsure note on the logged run).
   `why:` repo:prototype/osfr-tools/tests/movement.rs:51, 90, 104, 152, 183, 212, 226, 272 (eight `#[test]` functions, and `movement.rs` itself has no tests).

4. `old:` in each manifest frame (line 342); elapsed time is measured from a monotonic run start (line 253).
   `new:` in each manifest frame (lines 397-400); elapsed time is measured from a monotonic run start (line 276, with `elapsed` computed at line 343).
   `why:` repo:scripts/run-local-baseline.py:276, 343, 397-400. Line 342 is a preview-exit check, and line 253 is the asset-manifest SHA-256.

5. `old:` The test then applies the gateway tunnel and combined-message layouts from src/gateway.rs:202-215 and 410-443.
   `new:` The test then applies the gateway tunnel and combined-message layouts from src/gateway.rs:247-261 (`tunnel`), 655 (`application_messages`) and 1414 (the combined flag).
   `why:` repo:prototype/osfr-tools/src/gateway.rs:202-215 are the primitive readers (`u64`, `vector`), and 410-443 is trace code. The tunnel is at 247-261, and `application_messages` is at 655.

**Unsure:**
- The live gateway uses base speed 10.0 with mount and buff at 1.0 (`gateway.rs:1519-1531`). The note's 12 units/s applies only to the replay profile (`tests/movement.rs:43-48`), so it is not false, but a reader could confuse the two. You may want a sentence saying so.
- Run-log claim: `lab/build/W53b/movement-final.log` is not in the repo, so I could not confirm the "10 passed" result. The file's eight tests are the basis for correction 3.
- `0090e0f4` (receive handler that copies bit 4): no `fn` row exists in the client DB for that address (the `0090e0%` query returned nothing), so I could not check it. `008b3180` (GetEntitySpeed) matches the note: it reads `+0x650` and `+0x3ec` and selects `DAT_0175d738` or `DAT_0175b420`.
- `0092e860` "adds 0x32 (50 ms)" and the 36-byte opcode-125 layout at `008e5940`: I did not decode these.
- The 95/4 manifest and live-index split, the 14,982 total, the 59 position-bearing runs and the 13 / 26 / 26 / 58 aggregates all reconcile with the per-run table. The replay itself (`tests/movement.rs`) was not run, and the capture data is not in the repo.
- Mounts.md:23 (150 percent, no stacking) and Mounts.md:218 (no client ride-speed constant) match the cited claims.
