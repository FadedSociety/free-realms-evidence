<!-- fleet job=bug-hunt id=src-quest-journal-rs-L1 status=nothing_found turns=8 usd=0.0093 tokens(read,write,in,out)=[107459, 28294, 18, 9284] model=claude-haiku-5-5 -->
# prototype/osfr-tools/src/quest_journal.rs lines 1-343 of 343

## Window: `prototype/osfr-tools/src/quest_journal.rs` lines 1-343 (whole file)

No defect I could tie to a line and show reachable from client input or a save. Nothing submitted as a finding.

What I checked, and why each candidate was dropped:

- **Decode (`decode`, `quest_id`, lines 63-90):** the 47/12, 47/13 and 49/15 prefixes match the documented wire layout. Each body must be exactly its length (4 bytes for ids, `[0]` or `[1]` for the lock byte). Negative ids and 0 are rejected with `Malformed`. No panic path, and no unbounded input.
- **Breadcrumb flow (`breadcrumb`, lines 109-137) and `translate` (208-215):** the original id is rewritten through the crosswalk before `handle`, so an unlisted id is refused. Active, Offered and not-listed cases all route correctly. The new offer path (`QuestEngine::offer`, quest_engine.rs:1573) mutates only after `offer_denial` returns `None`, and `offer_denial` (quest_engine.rs:1653-1656) returns `Unavailable` for a missing definition before `self.definitions[&quest_id]` (quest_engine.rs:1585) is indexed. So that index cannot panic. No mutation precedes a fallible step.
- **Select and Lock (`handle`, lines 101-105):** `select_quest` (quest_engine.rs:1540) requires an Active quest owned by the character. `set_auto_switch_selected` takes a bool from a validated byte, and its `!locked` inversion matches the doc comment and quest_engine.rs:1560.
- **Crosswalk loading (`load_crosswalk`, lines 161-204):** size is capped at 1 MiB before reading. Positive id ranges, duplicate originals, empty or duplicate POI ids, name length and the `(R)` source rule are all validated, and any failure returns an error. Duplicate regional targets are allowed, but they are content-authoring, not a client-reachable defect.
- **Pin encoding and location (`Pin::encode`, `locate`, `tracked_pin`, lines 249-324):** the wire layout matches the doc (a, 0, c, guid, 0, vec4 with w=1.0, zone). Non-finite positions are filtered. Server-side state, not client packets, supplies the pin. `tracked_pin` returns `None` when the first placed objective is outside the current zone; that matches its doc comment, so it is not a logic error.
- **Tracker (lines 330-343):** `update` sends a clear only when a pin was previously shown, which matches its doc comment.

Callers checked: `gameplay/npc.rs:216-260` (decode, translate and handle in order, with `?` on decode errors and no state change before them), `gameplay.rs:2195-2214` (pin sync from server-held state), `gameplay/npc_quests.rs:34-90` (crosswalk load and registration).

Non-finding noted only: a malformed 49/15 or 47/13 body returns an `io::Error` through `npc.rs:218`. That is the intended reject path, not a crash.
