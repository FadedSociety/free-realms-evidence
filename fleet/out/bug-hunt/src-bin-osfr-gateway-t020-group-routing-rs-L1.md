<!-- fleet job=bug-hunt id=src-bin-osfr-gateway-t020-group-routing-rs-L1 status=nothing_found turns=5 usd=0.0041 tokens(read,write,in,out)=[60297, 20900, 12, 1861] model=claude-haiku-5-5 -->
# prototype/osfr-tools/src/bin/osfr_gateway/t020_group_routing.rs lines 1-800 of 1190

Window: `prototype/osfr-tools/src/bin/osfr_gateway/t020_group_routing.rs` lines 1-800. No reportable defects.

Why: the whole file is test code. `osfr-gateway.rs:4627-4629` declares it as `#[cfg(test)] #[path = "osfr_gateway/t020_group_routing.rs"] mod t020_group_routing;`, so every item in the window (`Rig`, `options`, `sessions`, `seed_world`, `rig`, `fixtures_present`, `server_rig`, the `impl Server { test_membership }` probe, the packet builders, and the `#[test]` functions at lines 133, 351, 471, 537, 590, 640, 692, 790) is compiled only for `cargo test`. Per the brief, code in `#[cfg(test)]` is not a defect, and none of the window's helpers is reachable from a production client packet path.

The only production-facing code these helpers touch is `Session::route_application`, `SharedWorld` and `social`, which are outside this window. I did not audit them, since they are not in the assigned lines.
