<!-- fleet job=note-refresh id=Pieces-085-Player-trading status=nothing_found turns=16 usd=0.0150 tokens(read,write,in,out)=[364450, 42874, 34, 12020] model=claude-haiku-5-5 -->
# notes/Research/Pieces/085 Player trading.md

**Verdict:** current. Every checkable claim about our code and status holds at the tip. The file paths, the unregistered module, the test counts and the reconstructed session rules all match. I found no claim to correct.

**Checked and holding:**
- `prototype/osfr-tools/src/restoration/piece_085.rs` exists (570 lines). It is not registered: no `piece_085` or `restoration` module declaration in `src/lib.rs` (`lib.rs:98` is the unrelated `pub mod trade;`). `tests/piece_085.rs:41` `#[path]`-includes it, as the note says.
- `tests/piece_085.rs` has 13 `#[test]` functions (lines 50, 99, 114, 125, 143, 154, 170, 219, 245, 271, 311, 337, 366), matching "13 tests".
- `scripts/pieces/piece_085.py` exists with the checker functions the note relies on.
- `tests/pieces/test_piece_085.py` has 12 `test_` methods (lines 112–189), matching "12 stdlib tests".
- The base opcode `0x3b` is written in `FUN_00c6a7b0` (`param_1[1] = 0x3b`), and `piece_085.rs:32` pins `SOE_BASE_TRADE_OPCODE = 0x3b`.
- The 18-row enum is in `piece_085.rs:35–57`. `refs` `OpenSourceFreeRealms/ofrserver/Server/LibSOE/Core/PacketCodes.cs:38` has `BaseTradePacket = 59`, and lines 973–975 have the same row values as the note (`TradeInvitePacket = 2` … `TradeItemRemovedPacket = 19`).
- The reader shapes match the decompile. `FUN_00c6c110` reads a u32 then a bool, and `FUN_00c6c180`, `FUN_00c6c8f0`, `FUN_00c6c960` and `FUN_00c6ce30` exist as the note names them. The `TradeHandler` event strings (`TradeCompleted`, `OtherAccepted`) are in `FUN_00c6df10`.
- The reconstructed policy matches the code. `TradeError::OfferChanged` (`piece_085.rs:139`) and the revision bump in `offer_item`/`offer_coins` (lines 386–408) implement the stale-lock rule. `complete()` (lines 441–514) clones both inventories and replaces them only after validation, which is the whole-or-nothing transfer. `TradeClose::PartnerDisconnected` (lines 313–317, 526–532) implements the disconnect policy.
- The python checker's finding ids (`packet-field-order-partly-unrecovered`, `invite-partner-name-region-unrecovered`, `offer-item-field-order-inferred`, `wiki-has-no-player-trading-page`) all appear in `scripts/pieces/piece_085.py:223–257`.

**Unsure:**
- The note says the `TradeOfferItemPacket` field order "is marked inferred" and that the code marks unrecovered field order "on each codec below" (`piece_085.rs:26–27`). The `TradeOffer` codec (lines 253–282) carries no such marker. The "inferred" label exists only as a checker finding id, so the label may live in the lab bundle, not the source. I could not settle this from the source.
- The note says the `TradeAcceptPacket`/`TradeLockPacket` second field is "carried as a slot". The code has a `TradeUpdateLock` codec (lines 285–310) but no accept codec and no lock codec with a second field. The claim may refer to the lab checker, which I did not inspect.
- The pseudocode line numbers (e.g. 1735082 for the session-id comparison, 1347882/1843558 for NoTrade) are not verifiable with the decompiled-client tools. The `FUN_00c6c8f0`/`FUN_00c6c960` wrappers shown do not contain the session comparison, so it must sit in the dispatcher I did not locate. `NoTrade` strings do occur in `FUN_00a76a60` and `FUN_00cf76e0`.
- The checker's "0 mismatches" and the lab bundle path (`../lab/reports/piece-085-20261009T053901Z/`) sit outside the repo and cannot be checked from here.
