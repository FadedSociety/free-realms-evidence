<!-- fleet job=note-refresh id=Ordinary-Crafting-Quit-Acceptance status=done turns=13 usd=0.0157 tokens(read,write,in,out)=[344067, 54083, 28, 11022] model=claude-haiku-5-5 -->
# notes/Research/Ordinary Crafting Quit Acceptance.md

**Verdict:** minor drift. The code claims all hold at the tip (sub-op 6 routing, pre-win guards, `cancel()` with `39/19` and no transaction, four regressions per service plus one routing test, request bytes). The native-acceptance status is stale: a native Cooking Playing Quit was accepted after this note was written.

**Corrections:**

1. `old:` Fresh native acceptance remains pending.
   `new:` Native acceptance of the Cooking Playing Quit (pre-win, instance 46000004) is recorded in `notes/Reviews/Native Crafting Quit 005748.md`. Fresh native acceptance of the Offered (pregame) quit, and of Smelting and Forging quit, remains pending.
   `why:` `notes/Reviews/Native Crafting Quit 005748.md:3,7` (client `27000684e7bd02ff…` at 009416, reply `39/19` at 009418, `39/7` ACK at 009420); `notes/Tasks.md:129`; `notes/Build Guides/Gameplay/Minigame Framework.md:112`. Tasks.md:92 still lists Offered and Smelting/Forging quit as open gates, which matches the replacement.

2. `old:` no original server Quit6 handler or ordinary-quit capture exists, so the response stays a labelled local choice
   `new:` no original server Quit6 handler or original-server response capture exists. A native Cooking Playing Quit (005748) captured the client's pre-win `39/6` and the reply from our Rust server, but there is no Offered-state capture, so the response stays a labelled local choice.
   `why:` `notes/Reviews/Native Crafting Quit 005748.md:3,7` (the 005748 review keeps the response as "a reconstructed local remove-only cancellation policy"); `prototype/osfr-tools/src/cooking.rs:386-399` (the sub-6 branch that gives the local response).

**Checked and holding (no change):**
- `src/cooking.rs:386-399`, `src/smelting.rs:373-386`, `src/forging.rs:401-414`: sub 6 requires `group == -1`, `game == -1`, the current instance, and a pre-win phase (Cooking/Smelting `Offered|Playing`; Forging anything except `Won|Lost`). Each delegates to `cancel()`.
- Malformed-length checks run before the active-run check (`cooking.rs:373`, `smelting.rs:361`, `forging.rs:389`).
- `cancel()` sends `header_with_game(19, …)` and creates no transaction (`cooking.rs:338-353`, `smelting.rs:326-339`, `forging.rs:325-340`).
- Four `native_ordinary_quit_*` tests per service (`cooking.rs:998,1034,1073,1127`; `smelting.rs:936,971,1008,1058`; `forging.rs:1358,1393,1430,1480`), plus one test in `gameplay/ordinary_quit_routing.rs:38`. That is 13 in total.
- Routing: `gameplay/crafting.rs:63-71` forwards `39` packets to the owning forging, cooking and smelting services.
- Request bytes: I recomputed the instance LE bytes for 46000001, 77000001 and 139000001 and they match the table.
- Client: `FUN_009be8e0` calls `FUN_009bdc60(6,-1,-1)` and `FUN_00939100` calls `009be8e0` on the not-active branch (client fn table).

**Unsure:**
- The 179-passed / 29-ignored suite counts and the RED/GREEN receipts live in `lab/`, which is not in the repo roots I could read. The independent review (`notes/Reviews/Ordinary Crafting Quit Independent Review.md`) recounts 208 listed / 179 passed / 29 ignored, which is consistent with the note.
- "Fresh native acceptance" in the Native gate section (pregame branch) is still a pending gate per `notes/Tasks.md:92`. I did not find evidence that it ran.
