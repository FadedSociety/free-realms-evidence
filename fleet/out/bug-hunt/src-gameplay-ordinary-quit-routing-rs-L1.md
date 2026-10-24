<!-- fleet job=bug-hunt id=src-gameplay-ordinary-quit-routing-rs-L1 status=nothing_found turns=4 usd=0.0012 tokens(read,write,in,out)=[11415, 4940, 10, 866] model=claude-haiku-5-5 -->
# prototype/osfr-tools/src/gameplay/ordinary_quit_routing.rs lines 1-87 of 87

No defects in `prototype/osfr-tools/src/gameplay/ordinary_quit_routing.rs` lines 1-87.

The whole window is test code. `gameplay.rs:5453-5454` declares `#[cfg(test)] mod ordinary_quit_routing;`, so none of it is compiled into the server binary. Under the review rules, test code is not a defect, and the helpers (`quit`, `remove`, `character`, `snapshot`) are only ever fed fixed test values. The one client-shaped input, `malformed`, is built locally in the test and is only passed to `handle_in_world` to check that it rejects. I did not read the production paths it exercises (`handle_in_world`, the cooking cancel), since they are outside the window and the window does not touch them.
