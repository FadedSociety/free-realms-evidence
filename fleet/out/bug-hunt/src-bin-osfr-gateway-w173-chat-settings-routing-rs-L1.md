<!-- fleet job=bug-hunt id=src-bin-osfr-gateway-w173-chat-settings-routing-rs-L1 status=nothing_found turns=5 usd=0.0038 tokens(read,write,in,out)=[41917, 17608, 12, 2411] model=claude-haiku-5-5 -->
# prototype/osfr-tools/src/bin/osfr_gateway/w173_chat_settings_routing.rs lines 1-567 of 567

## W173 `w173_chat_settings_routing.rs` lines 1-567: no defects found

I read the whole window (lines 1-567). It is test-only code, so it is out of scope under the rules.

- **Why it is test-only:** `prototype/osfr-tools/src/bin/osfr-gateway.rs:4620-4622` declares the module as `#[cfg(test)] #[path = "osfr_gateway/w173_chat_settings_routing.rs"] mod w173_chat_settings_routing;`. Every function in the window (`rig`, `channel_packet`, `wrap`, `log_in`, `bubble_packet`, `chat`, `send`, `drain_budget_later`, and the `#[test]` functions) exists only in the test build.
- **Candidates checked and dropped:**
  - Unchecked `as i32` / `as u32` length casts in `channel_packet` and `wrap` (lines 116, 123): test helpers with fixed, small inputs.
  - `unwrap()` calls throughout: test fixtures, not client-facing.
  - `drain_budget_later` loop (lines 205-208): it terminates because the budget refuses once the instant is 5 s later.
  - Lock held across the probe in `combat_bundle_children_are_budgeted_once` (lines 401-408): test-only, no deadlock in the test body.
- **Production code:** the tests exercise production paths (`Session::route_application`, `dispatch_message`, `ClaimWindow` budgets, `chat_settings`). I did not audit those outside the window, because the window's own code gives no defect to trace.

Nothing to report.
