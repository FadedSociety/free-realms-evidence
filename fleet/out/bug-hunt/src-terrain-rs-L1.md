<!-- fleet job=bug-hunt id=src-terrain-rs-L1 status=done turns=8 usd=0.0078 tokens(read,write,in,out)=[97907, 22246, 18, 8143] model=claude-haiku-5-5 -->
# prototype/osfr-tools/src/terrain.rs lines 1-281 of 281

Window: `prototype/osfr-tools/src/terrain.rs` 1-281. One finding, low severity. Nothing reachable by an ordinary player.

- **[low] prototype/osfr-tools/src/terrain.rs:108-114 - `height_at` computes `c + 1` and `r + 1` on `i64` values produced by a saturating `as i64` cast, so a huge finite coordinate overflows.**
  - **Failure scenario:** a role-trusted staff account sends `realm goto 1e38 1e38` (or `realm place <model> at 1e38,1e38`). The text parser accepts any finite `f32`. `fx = (x - min_x) / cell` is about 2.5e37, and `fx.floor() as i64` saturates to `i64::MAX`. The `c + 1` on line 112/114 then overflows. In a debug build this panics and kills the handler task. In a release build (no `overflow-checks` in the Cargo profile, so this is the default) it wraps to `i64::MIN`, `node()` returns `None`, and the function returns `None`, which is the correct result. So the defect is a debug-build panic only.
  - **Reach:** `gameplay.rs:3629` (`goto` with x/z, via `ground_height` at `gameplay.rs:1215`) and `gameplay.rs:3827` (`place ... at`) pass the parsed values straight through. The only filter is `is_finite()` (`gameplay.rs:3626`, `gameplay.rs:3815`), and `height_at` also only checks `is_finite()` (`terrain.rs:103`). Both paths sit under the `realm` command family, which is gated by the account-store role (`set_role_commands`, `gameplay.rs:1203`). That is why I rate it low.
  - **Fix:** clamp or reject out-of-grid coordinates before the cast, for example `if !(fx.abs() < 2.0e9 && fz.abs() < 2.0e9) { return None; }` at the top of `height_at`, or use `c.checked_add(1)` / `saturating_add(1)`.

Considered and dropped:
- `HeightGrid::from_bytes` (terrain.rs:158-159): `count * 2` can overflow in release or debug when the header's cols*rows is near 2^63. This needs a crafted `.hgt` file in the operator-controlled terrain directory, not client input, so I did not report it.
- `HeightGrid::new` (terrain.rs:43-44): `ceil() as u32 + 1` can overflow for enormous extents. The only caller is a fixed-parameter test and the offline tool, so it is not client-reachable.
- `add_triangle` NaN weights when the triangle's coordinates overflow f32: the input is GCNK geometry from the offline rasteriser, not from clients.
- The barycentric formulas, the seam epsilon, the highest-wins merge, and the documented mean fallback in `height_at` all match their doc comments.
