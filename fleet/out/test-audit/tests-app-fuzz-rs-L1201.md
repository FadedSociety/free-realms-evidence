<!-- fleet job=test-audit id=tests-app-fuzz-rs-L1201 status=done turns=10 usd=0.0123 tokens(read,write,in,out)=[199402, 36245, 22, 11466] model=claude-haiku-5-5 -->
# prototype/osfr-tools/tests/app_fuzz.rs lines 1201-2180 of 2180

Window reviewed: `prototype/osfr-tools/tests/app_fuzz.rs` lines 1201-2180, with the helpers it depends on (`words`, `bundle`, `wrap`, `Fixture::new/unloaded/gateway/active`, `unchanged`, `bounded`, `follow_up`, `hostile`, `seeds`) read at 110-150, 158-200, 330-400, 580-720. Most tests in the window are sound: each compares the full snapshot before and after, or asserts a concrete reply, application, or coin delta. The shop test's offsets check out (`NPC` is u64, so the 165/4 buy is 28 bytes and `huge[24..28]` is the quantity). The fixture copies content into a per-test directory, so the `remove_file` calls in the fallback test cannot leak into other tests, and `Fixture::new` asserts the content exists, so nothing skips silently.

- **[medium] prototype/osfr-tools/tests/app_fuzz.rs:1926 t3_non_opening_combat_inventory_and_quest_fallback_are_routed - the name says combat, inventory and quest requests are routed on the non-opening path, but the body only checks that hostile mutations leave the snapshot unchanged.**
  - Why it cannot catch a regression: the only routing check is `follow_up`, which covers the time request (family 52). If the gateway dropped or misrouted every combat, inventory or quest request, these hostile inputs would still produce no mutation and the test would pass. The `count` is only printed, never asserted. The `unchanged` helper (607-619) also ignores `Err` results, so a gateway that rejects everything still passes.
  - Fix: before and after the hostile loop, send one valid seed per handler (the `combat`, `inventory` and `quest_engine` seeds from `seeds()`) and assert a non-empty reply or application from each. Otherwise rename the test to `t3_non_opening_hostile_inputs_leave_state_unchanged`.

- **[low] prototype/osfr-tools/tests/app_fuzz.rs:1662 t3_active_movies_reject_hostile_headers_and_out_of_phase_rewards - the test fails on a wall-clock bound (`elapsed < 60s`) that has nothing to do with movie behaviour.**
  - Why it cannot catch a regression: it does not test any movie rule. It only fails on a slow or loaded machine, so it adds flakiness to the gate and no coverage.
  - Fix: remove the timing assertion and keep the `println!` for reporting. If a runtime budget is wanted, enforce it in a separate benchmark or a CI timing job, not in this correctness test.

No findings of the "cannot fail" or "silently skipped" kinds in this window. The canary test at 2001 correctly expects a panic and is not a finding.
