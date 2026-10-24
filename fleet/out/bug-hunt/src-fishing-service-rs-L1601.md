<!-- fleet job=bug-hunt id=src-fishing-service-rs-L1601 status=nothing_found turns=6 usd=0.0038 tokens(read,write,in,out)=[36282, 15363, 14, 3062] model=claude-haiku-5-5 -->
# prototype/osfr-tools/src/fishing_service.rs lines 1601-1623 of 1623

Window `prototype/osfr-tools/src/fishing_service.rs` 1601-1623 contains only the serde schema structs `Species` (1599-1614) and `Lure` (1616-1623). No defect found in this window.

What I checked:
- **Trust boundary:** `CONTENT` is `LazyLock<Content>` parsed from `include_str!("../data/content/fishing.json")` (fishing_service.rs:47, 84-86). The fields are compiled-in static data, not packet or save input, so no client value reaches these fields directly.
- **Arithmetic on these fields** (fishing_service.rs:938, 940, 1260-1288): `selection_weight` and `bonus_percent` are u32 widened to u64 before `weight * bonus / 100` and `checked_add` on the total. For u32 inputs this cannot overflow u64, and the total is checked. `difficulty.saturating_mul(rarity)` is saturating. `choose_grade` sums u64 values. None of these is a defect.
- **Unchecked content invariants** (`weight_kg` min <= max, `minimum_level`, etc.) can only be wrong through a bad bundled file. The bundled values I grepped are sane (selection_weight 12-100, weights present), and `validate_content` (182-215) covers the non-empty and cross-link invariants. This is not a client-reachable defect.
- `icon_id` is `#[serde(default)]`, which is intentional.

No finding in this window meets the defect criteria.
