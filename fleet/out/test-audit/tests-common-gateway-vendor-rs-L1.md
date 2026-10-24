<!-- fleet job=test-audit id=tests-common-gateway-vendor-rs-L1 status=nothing_found turns=9 usd=0.0062 tokens(read,write,in,out)=[110431, 23124, 20, 4456] model=claude-haiku-5-5 -->
# prototype/osfr-tools/tests/common/gateway_vendor.rs lines 1-187 of 187

Reviewed `prototype/osfr-tools/tests/common/gateway_vendor.rs` lines 1-187. This file holds shared helpers and no `#[test]` functions, so the test-level categories (cannot fail, asserts nothing, name overclaims, silent skip) do not apply directly. I checked the helpers that could hide a gate hole:

- **165/6 offsets (`sell_completion`, lines 159-178):** checked against the encoder in `src/coin_shop.rs:1155-1189`. Result at 4, kind at 12, merchant u64 at 16, transaction at 24, definition at 36, quantity at 44, price at 48, remaining at 52, total 56 bytes. All match, and the 56-byte size check is the client reader size, so it is intentional rather than incidental.
- **66/44 status (`merchant_status`, lines 104-108):** the status dword at offset 48 matches the reader comment. Its length and header asserts are fixed client layout, not incidental detail.
- **Framing (`wrap`, `inner_packets`, lines 32-45):** the 7-byte prefix (3 header bytes plus a u32 length) is consistent with the wrapper and the `[7..]` slicing.
- **`connect_with` (lines 62-83):** the doc says it sets no role and that `load_gameplay` supplies the default. The consumer in `tests/vendor_buy_sell_gateway.rs:666-673` asserts `Player` as a separate check, which is not the helper testing its own setup.
- **Silent skips:** `fixture_root()` (lines 58-60) points outside the repo at `lab/build/w178-vendor-gateway`, which is not checked in. However, its callers do not early-return on a missing fixture. `VendorFixture::new` (`tests/common/vendor_fixture.rs:54-58`) builds the pack via `round70_content::build` and panics on missing data via `expect`/`unwrap_or_else`, so a missing fixture fails loudly rather than passing.

No finding in this window meets the five criteria.
