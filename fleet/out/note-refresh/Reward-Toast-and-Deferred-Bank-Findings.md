<!-- fleet job=note-refresh id=Reward-Toast-and-Deferred-Bank-Findings status=done turns=33 usd=0.0415 tokens(read,write,in,out)=[1905027, 94225, 70, 21328] model=claude-haiku-5-5 -->
# notes/Research/Reward Toast and Deferred Bank Findings.md

**Verdict:** minor drift. Almost every checkable claim holds at the tip. One status sentence in section 5 is misleading because the quest turn-in already emits the 50/1 reward bundle.

**Corrections:**

- `old:` The newly traced reward presentation has not been integrated or visually accepted in a fresh original-client run.
  `new:` The reward bundle (50/1) is already emitted on the quest turn-in path, sent with the grant. It has not been visually accepted in a fresh original-client run. The Build Ledger notes the turn-in screen shows no reward line. The deferred-bank packets (50/6, 50/7) are not sent by our code.
  `why:` `repo:prototype/osfr-tools/src/quest_engine.rs:2034` calls `rewards::apply_grant`, and `:2052-2054` maps its packets to `OutboundMessage::Reward`. `repo:prototype/osfr-tools/src/rewards.rs:165` pushes `encode_display_bundle`. A search of `src` finds no `RewardPacketNonMember`, `deferred` or 50/6 or 50/7 sender. `repo:notes/Design/Build Ledger.md:94` says the turn-in screen shows no reward line.

**Checked and holding (no change):**

- Body layout matches the note. `rewards.rs:212-237` writes success at body 0, coins at 1, XP/stars at 5, unresolved at 9, kind at 13, row count at 61 and a trailing i32 at 65. That gives 69 bytes, or 72 with the 3-byte header.
- The Sanctuary field names are as described. `refs:Sanctuary/src/Sanctuary.Packet.Common/RewardBundleBase.cs:11-14`.
- Section 5 progression claims. The grant path sends 38/19 (`inventory.rs:867`, `rewards.rs:130`), then 38/18 before 38/14 (`profiles.rs:343-361`, `rewards.rs:175-197`).
- Client functions and addresses. `0x00b8a640`, `0x00b89ca0`, `0x00b892b0`, `0x00b894a0`, `0x0091c290/2e0/380`, `0x00be8980` and `0x00b88ad0` (opcode 0x32) exist as the note describes in the client DB. `0x00b899f0` has the kind-16 branch calling `CallHandler:ShowMysteryChestReward`.
- Lua callbacks. `ShowXpCoinBankReward` is the name used at `ui:ScriptsBase.lua:4497`. `UnifiedMessageWindow` calls `showMembershipStarsCoinsReward_lua` at `ScriptsBase.lua:55651`. `XpButton` calls `setXp_lua` at `ScriptsBase.lua:57232`.
- Subtype 2 passes type 8, and `NotificationHandler:ItemReceived` returns early for type 8 (`ScriptsBase.lua:11686-11687`).
- Locale IDs 2, 3, 23, 990, 992, 2517, 4923 and 388887 match their described strings.
- Probe counts (36 checks, 104 AS files, 85,932 IDs, 14 truncated multiline strings) match `repo:MODLOG.md:565`.

**Unsure:**

- The `0x00b89ca0` template-branch table (XP/coins to RewardPatternOne/Two). I only read part of the decompile, and the branch conditions were not fully resolved.
- The subtype-6 offset-to-field mapping (XP at body 4 into +0x40, coins at body 8 into +0x3c). The handler's stack-local decompile is ambiguous, but it agrees with `notes/Build Guides/Gameplay/Rewards and Collections.md:90`.
- The 6,155-entry pack comparison and the "native-tested in our local opening campaign" claim. The evidence is outside `repo` (lab reports). `repo:notes/Design/Opening Playthrough.md:50` shows a native turn-in run, which only partly supports it.
