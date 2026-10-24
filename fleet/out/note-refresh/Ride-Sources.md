<!-- fleet job=note-refresh id=Ride-Sources status=done turns=9 usd=0.0121 tokens(read,write,in,out)=[155992, 37874, 20, 11582] model=claude-haiku-5-5 -->
# notes/Research/Ride Sources.md

**Verdict:** badly stale. The note describes the W169 design, which T230 replaced. Rides are no longer sold by the Seaside vendors for coins. They are listed in the Station Cash Marketplace for SC, and the vendors keep no ride stock. The W169 price policy was removed.

**Corrections:**

1. `old:` Now all 54 have a priced `stores.json` row for one canonical item and are in the stock of the Seaside vendor Delvin (`vendors.json`); 3 are also in the stock of the Seaside "Mysterious Merchant" Cragara, matching a real original merchant channel.
   `new:` Now all 54 have an `sc_price` row for one canonical item in `stores.json` and are listed in the Station Cash Marketplace Rides category (139). 52 are listed for SC; Chrome Drake and Polar Bear are `earn_only` and never listed. Delvin and Cragara no longer stock rides (T230 moved them to Station Cash).
   `why:` `repo:prototype/osfr-tools/data/content/vendors.json:47095-47111` (Delvin and Cragara both `item_ids: []`, "Rides moved to the Station Cash Marketplace (T230)"); `repo:prototype/osfr-tools/data/content/stores.json:53` (`station_cash` block, category_id 139); `repo:prototype/osfr-tools/src/station_cash.rs:42` (earn_only rides never listed); `repo:notes/Autopilot/T230.md:28-35`.

2. `old:` Buying goes through the existing `buy_vendor` path, grants the item, and `MountCatalog::owned_mounts` then lists the ride.
   `new:` Buying goes through a Station Cash order (66/1/3, staged through `station_cash`), grants the item, and `MountCatalog::owned_mounts` then lists the ride.
   `why:` `repo:notes/Autopilot/T230.md:21-24` (66/1/3 preview/order through `station_cash`); `repo:prototype/osfr-tools/src/station_cash.rs:42`.

3. `old:` **Price rule.** coins = round(SC price x 20, to 50). `stores.json` carries a top-level `ride_price_policy` (`coins_per_sc` 20, `round_to_coins` 50, `min_coins` 2,000, `max_coins` 30,000, member discount 10 percent).
   `new:` **Price rule.** Station Cash = round(`sc_price` x `station_cash.sc_price_scale`), scale 0.25. `stores.json` carries a `station_cash` block (`sc_price_scale` 0.25, `max_price_sc` 100000) and each ride row has `sc_price`; the W169 `ride_price_policy` coin conversion was removed.
   `why:` `repo:prototype/osfr-tools/data/content/stores.json:53` (station_cash block); `grep` finds no `ride_price_policy` in `stores.json` (only `repo:notes/Autopilot/T230.md:10,31`); `repo:prototype/osfr-tools/src/station_cash.rs:146-148`.

4. `old:` holds all 54; this is the reconstructed stable.
   `new:` held all 54 until T230; it now keeps no ride stock, and the rides are sold from the Station Cash Marketplace instead.
   `why:` `repo:prototype/osfr-tools/data/content/vendors.json:47095-47102` (`item_ids: []`, "empty_after_t230_sc_move").

5. `old:` **Cragara** (9500000569) holds Dwarftech Chopper, Pogo Stick and Robgoblin Mech (reference evidence).
   `new:` **Cragara** (9500000569) held Dwarftech Chopper, Pogo Stick and Robgoblin Mech until T230; the vendor record is now empty (rides moved to Station Cash).
   `why:` `repo:prototype/osfr-tools/data/content/vendors.json:47104-47111`.

6. `old:** Coin rate of 20 coins per SC.**` (the bold lead of choice 1; the rest of that line is coin arithmetic)
   `new:` **Coin rate removed (T230); rides now list at round(`sc_price` x 0.25) SC.** The coin figures below are the superseded W169 values.
   `why:` `repo:prototype/osfr-tools/data/content/stores.json:53` (`sc_price_scale` 0.25); `repo:notes/Autopilot/T230.md:28-31` ("The W169 `ride_price_policy` coin conversion is gone").

7. `old:` are plain purchases at 10,000 coins.
   `new:` are `earn_only` rewards: never listed and never sold for SC or coins.
   `why:` `repo:prototype/osfr-tools/tests/ride_sources.rs:5-6` ("`Chrome Drake` and `Polar Bear` carry `earn_only` and must never be listed"); `repo:prototype/osfr-tools/src/coin_shop.rs:159`; `repo:notes/Autopilot/T230.md:29-30`.

8. `old:` Delvin lists all 54 in one window.
   `new:` The Station Cash Marketplace lists 52 of the 54 rides in one Rides category (139); Delvin keeps none.
   `why:` `repo:prototype/osfr-tools/src/station_cash.rs:187-227` (earn_only split); `repo:prototype/osfr-tools/data/content/vendors.json:47095-47102`.

**Unsure:**

- **Membership gate.** The note says `buy_once` has no `RESULT_NOT_A_MEMBER` path. That is still true for `coin_shop.rs` (`RESULT_NOT_A_MEMBER` is defined at `repo:prototype/osfr-tools/src/coin_shop.rs:67` and not used). I did not check whether the SC order path in `station_cash.rs` enforces membership, so the "not enforced" claim is unsettled.
- **Coverage counters.** `vendors.json:63,69` show `items_resolved` 1063 and `items_with_stores_price` 1061. T230.md:33-35 says the counters are pinned at 1,051 mapped / 1,049 priced. The file and T230 disagree, so I could not confirm the "+57" claim in the note.
- **Lab artifacts.** `lab/runs/claude/W169/` (`apply_ride_sources.py`, `final.md`) is not present in this checkout, so I could not verify the script, its idempotence, or the test-run claims.
- **Member price and `member_only`.** I did not check whether `vendors.json` still keeps `member_only` null for rides, or the 10 percent member price in SC orders.
- **Line 115** ("The vendor window with a 54-item list ... has not been run natively") refers to a vendor window that no longer carries rides, so it is probably stale too, but I did not check the native side.
- **Other claims** (wiki prices, bundle IDs, client locale IDs, NPC IDs for Troy Ridewrangler) are outside the repo and were not checked.
