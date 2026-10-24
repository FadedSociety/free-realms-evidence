<!-- fleet job=pin-audit id=tests-mount-stats-rs status=nothing_found turns=4 usd=0.0026 tokens(read,write,in,out)=[14220, 12653, 10, 1683] model=claude-haiku-5-5 -->
# tests/mount_stats.rs

No findings in `prototype/osfr-tools/tests/mount_stats.rs` for the screened lines 531, 532 and 542.

The `8.0` on each line is the third argument to `MountCatalog::new` (`on_foot_speed: f32`, `src/mounts.rs:196-201`). The test passes it as a literal input, and the test never compares it to a data file. The constructor only checks `0 < on_foot_speed <= MAX_SPEED`, a code constant, so the `is_ok` on line 542 holds for any positive value under that cap. Retuning any data file would not break it.

The `RideStats::default()` and `nan` values are also fixture inputs. Line 532's `nan` is the test's own NaN-valued `RideStats`, and line 531 uses the same pattern through `with_stats`. The `wolf` definition comes from the loaded catalogue, so its data is read rather than pinned.
