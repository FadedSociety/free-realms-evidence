<!-- fleet job=bug-hunt id=src-gameplay-rs-L1 status=nothing_found turns=9 usd=0.0135 tokens(read,write,in,out)=[173091, 41604, 20, 13057] model=claude-haiku-5-5 -->
# prototype/osfr-tools/src/gameplay.rs lines 1-800 of 5475

No reportable defects in `prototype/osfr-tools/src/gameplay.rs` lines 1-800. I read the whole window (plus lines 1315-1350 and `gameplay/power_up_use.rs`, which the window calls) and checked the candidates below against their callers.

Checked and dropped:
- **gameplay.rs:510-512** `self.encounter.as_mut().unwrap()`: `abilities` and `encounter` are only assigned together in `load` (lines 681-697), and nothing in gameplay.rs sets either to `None`. So `abilities` being `Some` implies `encounter` is `Some`, and the unwrap cannot fire.
- **gameplay.rs:361-382** `item_change_packet` echoes client-supplied slot/profile into a 35/6 broadcast. The bytes are the 42/2 unequip body (`slot`, `profile`), which the notes confirm. The caller (`inventory_visibility`, line 1327-1342) only broadcasts when `changed` is true and the profile is not inactive. The slot is one the inventory accepted, so this is not a defect.
- **gameplay.rs:486-490 / encounter/shared.rs:363** the shared-field ability slot is bounded to `0..=9` by the parser before it reaches `slot > 0` / `job_slot`.
- **gameplay.rs:493-501** the power-up path restores the field presence before `result?`, so the early return does not leak presence.
- **gameplay.rs:296-321** `Outcome::absorb` merge rules are correct (`other.or(self)` precedence).
- **gameplay.rs:713-751** the forging marker and `opening.json` size checks are bounded (`take(524_289)`, `> 4096`, `> 16` bindings). `seen.insert` runs before the actor check, so duplicates are caught.

Out-of-scope observation (not reported as a finding): **gameplay.rs:739** `opening.as_ref().unwrap()` in the forging-campaign branch. It can panic only if `forging-campaign.json` exists, `opening.json` does not, and the marker lacks a string `opening_sha256`. That is a hand-edited content directory, not client or save input, and it is not remotely reachable. The `Gameplay::load` directory is the operator content dir (gateway.rs:817, 1080), not per-player data. If the owner wants it fixed anyway, replace the unwrap with `.ok_or_else(|| invalid("forging campaign requires opening content"))?`.
