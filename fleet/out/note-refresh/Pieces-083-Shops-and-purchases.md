<!-- fleet job=note-refresh id=Pieces-083-Shops-and-purchases status=done turns=18 usd=0.0252 tokens(read,write,in,out)=[756931, 72044, 38, 17175] model=claude-haiku-5-5 -->
# notes/Research/Pieces/083 Shops and purchases.md

**Verdict:** current, with minor drift. The module, its check order, refusals, staged commit, price formula, constants and test counts all match the tip. One stated blocker no longer holds.

**Corrections:**

- `old:` include module files that do not exist yet, so cargo stops before their targets.
  `new:` included module files that did not exist when this was logged. At the tip all four `#[path]` targets exist (`src/restoration/piece_051.rs`, `piece_062.rs`, `piece_075.rs`, `piece_097.rs`), so that stated cause no longer holds. The crate-wide run was not repeated here.
  `why:` repo:prototype/osfr-tools/src/restoration/ (listing shows piece_051.rs, piece_062.rs, piece_075.rs and piece_097.rs); repo:prototype/osfr-tools/tests/piece_051.rs:31, piece_062.rs:34, piece_075.rs:33, piece_097.rs:23 (the `#[path = "../src/restoration/piece_NNN.rs"]` includes resolve).

**Checked and holding (no change):**

- Packet constants, result codes and the 28-byte request layout: `src/restoration/piece_083.rs:74-96` and `:120-139`. Request read offsets are 4, 12, 16, 20, 24. Tests: `tests/piece_083.rs:124-184`.
- The 13 owned vectors: 13 `#[test]` items in `tests/piece_083.rs`.
- The 12 Python checker tests in `tests/pieces/test_piece_083.py` (lines 88-178).
- Catalogue bounds (4 MiB, 4,096 merchants, 65,536 rows): `piece_083.rs:94-97`.
- The check order (5, 3, 4, 6, 10, 4, 7) and the refusal mapping: `piece_083.rs:425-485`.
- Tint refused with 6 rather than rewritten: `piece_083.rs:452-457`.
- Staged clone, written before commit: `piece_083.rs:493-539`.
- Per-character `owned_limit`: `piece_083.rs:462-468`.
- Member price in float32 with a truncating cast: `piece_083.rs:238-247`. Rows 1, 2 and 34 at 10% give 4, 288 and 185 (`tests/piece_083.rs:189-191`).
- The module is not registered in `src/lib.rs` (no `restoration` match there), matching the "lead integration" gap.
- Sub-opcode 5 is refused as `SubOpcode` and not parsed (`tests/piece_083.rs:182`).
- Reference claims: the `// TODO: Implement other item types` whitelist and the tint rewrite (`refs:FreeRealms-Legacy/src/Sanctuary.Gateway/Handlers/BaseCoinStorePacket/CoinStoreSellToClientRequestPacketHandler.cs:64-65, 92-93`).
- Client claims: `setCoinStoreCanPurchaseItem`, `CanBuyItem` and `GetMaxItemsPurchasable` in `ui:ScriptsBase.lua:53352-53359`. `MaxPerOrder`, `MaxPurchasable` and `QuantityAvailable` appear in `ScriptsBase.lua`.
- Path citations: `src/restoration/piece_083.rs`, `tests/piece_083.rs`, `scripts/pieces/piece_083.py`, `tests/pieces/test_piece_083.py`, `src/inventory.rs:325` (`pub struct Inventory`), and the cross-links.

**Unsure:**

- The lab-only claims cannot be checked from the repo: the RED/GREEN logs and `lab/reports/piece-083-20261009T042532Z/`, the `shops.json` and `findings.json` bundle, and the `cargo --test` counts for the lib and neighbour suites (24, 12, 8, 1). The Delegated Task Readiness record does show the same report folder name.
- The checker's source-data claims cannot be checked from the repo: 58,795 rows, 58,697 at a 10% discount, 98 without a discount, 926 member-only, 1,207 single-use, 6,604 tintable, and the SHA-256 `40a3cc79…`. The hash is pinned in `scripts/pieces/piece_083.py:90` and `scripts/pieces/piece_013.py:70`. The counts were not recomputed.
- Command path: the note says "from `prototype/osfr-tools` with `scripts/cargo.ps1`". `prototype/osfr-tools/scripts` does not exist at the tip. The file is at repo-root `scripts/cargo.ps1`, referenced as `../scripts/cargo.ps1` from `launcher/build.ps1`. The `../lab/tools` path is outside the repo, so I left the note unchanged.
- Context, not a correction: `notes/Design/Build Ledger.md:62` lists the live coin store (165/4, 165/5) as "Wired, never run natively" through `src/coin_shop.rs` and `npc_interaction.rs`. This note's statement that this module is not wired is still correct, because the purchase ledger here has no live caller.
