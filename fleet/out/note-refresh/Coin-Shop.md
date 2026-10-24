<!-- fleet job=note-refresh id=Coin-Shop status=done turns=22 usd=0.0216 tokens(read,write,in,out)=[683282, 53718, 46, 16184] model=claude-haiku-5-5 -->
# notes/Research/Coin Shop.md

**Verdict:** badly stale in the Status, Marketplace and buy-back bullets. The Coin Shop service is registered and wired into the gameplay session, Station Cash (T230) now answers Marketplace orders, and the buy-back window is 10, not 20. The protocol facts and the reconstructed result codes still hold.

**Corrections:**

1. `old:` The lead still needs to register the module and integrate its inventory snapshot, replies, and commerce ledger with the gateway/save path.
   `new:` The module is registered (`lib.rs:12`) and held by the gameplay session (`gameplay.rs:228`, `:969`); its replies route through `gameplay/npc.rs:687`, `:765` and `:821`. The session saves only the Station Cash wallet (`gameplay.rs:1373-1376`); the transaction ledger is in-memory (`coin_shop.rs:230`), and no `src` caller sets membership (`coin_shop.rs:315`). No native-client acceptance was run by this worker.
   `why:` repo:prototype/osfr-tools/src/lib.rs:12; repo:prototype/osfr-tools/src/gameplay.rs:228,969,1373-1376; repo:prototype/osfr-tools/src/gameplay/npc.rs:687,765,821; repo:prototype/osfr-tools/src/coin_shop.rs:230,315

2. `old:` The Marketplace request layout is not recovered; sub 3 is refused before parsing and gets a result 0 plus the client-readable message.
   `new:` Sub 3 is decoded and answered by `station_cash::place_order` when Station Cash is enabled (`stores.json` `station_cash.enabled: true`); with it off, sub 3 gets a result 0 plus the client-readable message.
   `why:` repo:prototype/osfr-tools/src/coin_shop.rs:1081-1103 (order path at 1089-1101, refusal at 1082-1088); repo:prototype/osfr-tools/data/content/stores.json:53

3. `old:` Marketplace order preview/order and `NpcMerchantV2` purchase requests receive failure replies; no balance or inventory changes.
   `new:` Marketplace order preview (sub 1) and order (sub 3) go to the Station Cash path when it is enabled, and get a result 0 reply when it is off (`coin_shop.rs:1070-1103`). `NpcMerchantV2` purchase requests (sub 43) still receive failure replies with no balance or inventory change (`coin_shop.rs:1138-1141`).
   `why:` repo:prototype/osfr-tools/src/coin_shop.rs:1070-1103,1138-1141

4. `old:` Buy-back uses the latest 20 successful sales (R), charges the resale amount again (R), and is single-use.
   `new:` Buy-back uses the latest 10 successful sales by default (R; the window is data-driven and `stores.json` sets no `buy_back_window`), charges the resale amount again (R), and is taken per unit: each sale's remaining quantity is decremented, so partial buy-backs are allowed until it reaches zero.
   `why:` repo:prototype/osfr-tools/src/coin_shop.rs:40 (DEFAULT_BUY_BACK_WINDOW = 10), :76-77, :872 (window trim), :909-963 (remaining quantity); no `buy_back_window` key in repo:prototype/osfr-tools/data

5. `old:` Wallet balance is zero (R).
   `new:` Wallet balance is the character's Station Cash wallet, zero for a fresh character.
   `why:` repo:prototype/osfr-tools/src/coin_shop.rs:1105 (`station_cash::wallet_packet(self.sc_wallet.balance)`), :226-227

6. `old:` 1. Register `coin_shop` and keep one service per character or adapt it to the gateway's transaction boundary.
   `new:` 1. `coin_shop` is already registered (`lib.rs:12`) and held once per character session (`gameplay.rs:969`); adapt it to the gateway's transaction boundary. Membership is still unset: no `src` caller of `set_member_status` exists yet.
   `why:` repo:prototype/osfr-tools/src/lib.rs:12; repo:prototype/osfr-tools/src/gameplay.rs:969; repo:prototype/osfr-tools/src/coin_shop.rs:315

**Unsure:**
- Gate 1's "Sync current inventory before commerce handling": `sync_inventory` is defined at `coin_shop.rs:311`, and the only `src` hit besides it is a trades call in `bin/osfr-gateway.rs:2504`. I could not confirm that the Coin Shop receives a live sync in `gameplay.rs`.
- The "Checks run" section is dated history (the note says the tests remain unexecuted). Later Autopilot reports (F179, F190, F248) record `tests/coin_shop.rs` at 11 passing. I left it as history.
- The member-price and `Cost` mapping (`Cost * (100 - MemberDiscount) / 100`, sell = half of `Cost`) is only partly visible in the code. Item 8 (`stores.json` line 62: 15 / 13 / 7) matches the note. Rows carry `member_discount_percent` with `member_price_coins: null` for many items, so the stored member price is not uniformly present. The arithmetic was not traced to a generator script.
- The Marketplace "Account info defaults to `US`/`USD`" (`coin_shop.rs:1237-1242`) and the empty product and state/country lists (`coin_shop.rs:1121-1127`) still match the code. The sub-18 gift refusal with code 8 (`coin_shop.rs:1021-1029`) matches too.
