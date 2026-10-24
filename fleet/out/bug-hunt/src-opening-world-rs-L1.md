<!-- fleet job=bug-hunt id=src-opening-world-rs-L1 status=nothing_found turns=9 usd=0.0071 tokens(read,write,in,out)=[100387, 24027, 20, 6084] model=claude-haiku-5-5 -->
# prototype/osfr-tools/src/opening_world.rs lines 1-100 of 100

No defects found in `prototype/osfr-tools/src/opening_world.rs` lines 1-100 that a remote client can reach.

What I checked:

- **`load` (lines 25-45):** `template_file` is checked to be a single `Normal` path component before `directory.join`, so it cannot escape the content directory. The template must be exactly 334 bytes, have the `[35,0,2,0]` header, and match the SHA-256 in `combat.json`. All of this is server content read at startup, not client input. The hex comparison is case-sensitive, which only fails closed.
- **`spawn` (lines 63-84):** Every fixed offset (4..12, 12..16, 16..20, 37..49, 69..73, 77..81, 106..110, 133..137, 237..241) is below 334, so the template-length check guarantees no out-of-range slice. The `interaction_radius.ceil() as i32` cast cannot panic, and `opening.rs:344-345` already restricts radius to finite values in 0.1..=100. The name splice is bounded by server content.
- **`initialization` (lines 47-61):** Enemies and other zones are filtered out, and the relevance count is built from the same filtered list, so the count and the entries match. `gameplay.rs:1764-1781` passes only server-side actors.
- **`menu` (lines 86-99):** Reached from `gameplay.rs:4495-4516` only after the client's guid is looked up in server-side `opening.actors()`, with zone and radius checks at `gameplay.rs:4504-4509`. The client cannot supply the name or label.

Not reported:

- `spawn` never writes `actor.heading`. `notes/Autopilot/T328.md:155-159` records this as a known, out-of-scope limitation (cosmetic facing). It is not a crash, a save corruption, or a client-trust issue.
- `menu` uses the "Interact" label for every non-`npc` kind. This is intentional and locale-verified per the comment on line 91.
