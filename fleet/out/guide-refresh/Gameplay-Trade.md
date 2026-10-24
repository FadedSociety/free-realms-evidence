<!-- fleet job=guide-refresh id=Gameplay-Trade status=done turns=26 usd=0.0326 tokens(read,write,in,out)=[1177458, 88566, 54, 19503] model=claude-haiku-5-5 -->
# notes/Build Guides/Gameplay/Trade.md

**Verdict:** minor drift. The client-side evidence I spot-checked holds (TradeHandler at ScriptsBase.lua:25282, the 10-second TradeAcceptTimer, the CodeStringMappings ids, the Trade module registrar at `00c05ce0`). The stale part is the server side: the note still says the click-to-trade path is unresolved, but the repo now routes it.

**Corrections:**

1. `old:` The `Trade` entry in the radial menu is server-sent; what happens on a click is not traced.
   `new:` The `Trade` entry in the radial menu is server-sent. On the server side the click is resolved: it arrives as a `26/10` choice on the server-built menu (the same message as Inspect, label 3299, entry id 1002), and the server turns it into a `59/2` invite. The client side of that click is still not traced.
   `why:` repo:prototype/osfr-tools/src/player_radial.rs:16-17 and 27-31 (the 26/10 choice; "the server turns the choice into a 59/2 invite (`trade.rs`)"); repo:prototype/osfr-tools/src/player_radial.rs:49-52 (TRADE_ENTRY_ID 1002, TRADE_LABEL 3299); repo:prototype/osfr-tools/src/bin/osfr-gateway.rs:2054-2077 (the 26/19 select and the 26/10 choice route to `Chosen::Trade` and `trades.invite`).

2. `old:` How a click on Trade becomes a request is not traced (see Open questions).
   `new:` A click on Trade is a `26/10` choice on the server-built menu, the same message as Inspect; the server turns it into a `59/2` invite (the client side is still open, see Open questions).
   `why:` repo:prototype/osfr-tools/src/player_radial.rs:16-17, 27-31; repo:prototype/osfr-tools/src/bin/osfr-gateway.rs:2070-2076.

3. `old:` The click-to-request path is unresolved (Open questions); the server needs a request that names a target player.
   `new:` The click reaches the server as a `26/10` choice on entry `1002` and becomes a `59/2` invite through `trades.invite`; the entry is offered only where `trades.can_invite` allows it.
   `why:` repo:prototype/osfr-tools/src/bin/osfr-gateway.rs:2057-2063 (`trade: trades.can_invite(...)`) and 2070-2076 (`Chosen::Trade(target)` → `trades.invite`); repo:prototype/osfr-tools/src/player_radial.rs:27-31.

**Unsure:**

- **Card-trade counts in the CharacterCreate row.** The header (repo-client `Resources/CharacterCreate/ItemDefinitions.txt:1`) confirms 302 data rows (303 lines), NO_TRADE as the 15th column and MAX_STACK_SIZE as the 11th. The search tool caps output at about 20 lines, so I could not count the rows with NO_TRADE 1 (246) or 0 (56), or MAX_STACK_SIZE 1 (221) or -1 (81). Left as written.
- **Feature counts in the Overview.** "About 130 of the mapped functions" and "About 360 of the 455 `net.trade` functions" are not checkable with the tools here. The client_sql `fn` table has no `net.trade` namespace rows.
- **Card trade transport is not built, and the note does not say otherwise.** Items 13 and 14 of "What the Rust server must do" describe `TradeCommand_*` transport and posted trades. The source has no `TradeCommand` sender or posted-trade handling. The only related code is the rules layer, `game_rules.rs:236-250` (`encode_trade_allowed_flag_entries`) and the TCG match code in `restoration/piece_010.rs`. Consider adding a status line saying the card-trade transport is missing. This is not a false claim, so I did not propose a correction.
- **Out-of-note stale comment.** repo:prototype/osfr-tools/src/restoration/piece_099.rs:38-40 says "the local server does not dispatch family 59 or 175 at all today". That is now false: repo:prototype/osfr-tools/src/gateway.rs:507-508 routes family 59 subs 3 and 6-10 to "trade", and Build Ledger line 47 records the live lifecycle. The note does not repeat this claim; the code owner may want to fix the comment.
- **"No trade datagram has been decoded for this guide"** (line 14). This is scoped to the guide's sources, so I left it. The repo has recovered six client-to-server layouts in `piece_099.rs:167-196`, sourced from a pinned community reader rather than from a capture.
