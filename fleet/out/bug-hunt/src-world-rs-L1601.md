<!-- fleet job=bug-hunt id=src-world-rs-L1601 status=nothing_found turns=4 usd=0.0021 tokens(read,write,in,out)=[11702, 7239, 10, 2133] model=claude-haiku-5-5 -->
# prototype/osfr-tools/src/world.rs lines 1601-1624 of 1624

Window `prototype/osfr-tools/src/world.rs` 1601-1624 is entirely inside `#[cfg(test)] mod tests` (the module opens at line 1559). Per the brief, code in `#[cfg(test)]` is not a defect, so there is nothing to report from the window itself.

I also checked the production code the two tests exercise, to see whether the tests' claims contradict the implementation:

- `available_public_id` (world.rs:1185-1189) scans `(1..=max)` and returns `InstanceIdsExhausted` when nothing is free. This matches the test at 1599-1608: with ids 1..=3 occupied, `available_public_id(3)` is `Err`, and `available_public_id(4)` is `Ok(4)`.
- `instance_id_available` (world.rs:1175-1180) excludes registered zone ids, which matches the test at 1614-1623 (zone 1 registered, so the public probe skips 1 and returns 2).
- `available_instance_id` (world.rs:1425-1444) has a bounded `checked_add` successor and a 16-row cap on non-public instances. The loop terminates after at most about 32 occupied ids (16 instances plus at most 16 public mappings), so the scan is bounded.
- `register_runtime_zone` (world.rs:977-984) caps the zone count at 16 and rejects zone ids that do not fit in `i32`.

I did not verify the initial value of `next_instance_id`, which the assertion `available_instance_id() == Ok((2, 3))` depends on. That is outside the window and does not produce a defect.
