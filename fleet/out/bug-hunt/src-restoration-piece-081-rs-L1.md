<!-- fleet job=bug-hunt id=src-restoration-piece-081-rs-L1 status=done turns=13 usd=0.0105 tokens(read,write,in,out)=[201001, 27895, 28, 9909] model=claude-haiku-5-5 -->
# prototype/osfr-tools/src/restoration/piece_081.rs lines 1-305 of 305

Window `prototype/osfr-tools/src/restoration/piece_081.rs` lines 1-305 (read in full, plus the production caller `src/inventory.rs:1012-1016` and validation `src/inventory.rs:707-740`). I found no panic, overflow, unbounded growth, or client-trusted authority in this window. Checked and ruled out: `allocate_from_snapshot` (`i64` arithmetic cannot overflow because `highest` is an `i32`; `next+1` is only reached when `next <= i32::MAX`); `allocate` (the `+ 1` is only reached after `try_from` succeeds, so `next <= i32::MAX`); `persist` before hand-out with no in-memory mutation on failure; `atomic_write` cleanup; `read_bounded` (bounded `take`, regular-file check); `highest` (duplicate and sub-1 rejection). Live ids and the stored counter both come from server-written saves, not from packet fields.

Two low-severity findings:

- **[low] prototype/osfr-tools/src/restoration/piece_081.rs:63-75 - `allocate_from_snapshot` floors a legacy save (`stored == None`) at `max(live id)+1`, so ids of rows retired before the counter existed can be issued again.**
  - Failure scenario: a pre-counter save holds ids 2..=10, id 10 was removed earlier, and the save has no `next_instance_id`. The next grant gets `next = max(1, 9+1) = 10`, so id 10 is reissued to a new item and the returned high-water mark is 11.
  - Reach: `inventory.rs:1012-1016` passes `staged.state.next_instance_id` (None for legacy saves; `validate_state` at `inventory.rs:734` accepts None) and the live ids. Nothing else records retired ids.
  - Why it is not already stopped: the comment at lines 61-62 says only "legacy snapshots lack it", and the module's own gap list (lines 33-35) covers only a lost document, not legacy saves. Impact is limited to stale references to the old id (for example, a cached instance id in another subsystem); I could not confirm one that is reachable.
  - Fix: document this as an explicit gap in the module header, or, for legacy saves, derive a floor from a source that records retired ids before allowing a grant.

- **[low] prototype/osfr-tools/src/restoration/piece_081.rs:116-118 - `open` accepts a stored counter above the allocatable bound (`> i32::MAX + 1`), which is inconsistent with `allocate_from_snapshot` (line 69), `inventory.rs:736`, and the test `counter_refuses_to_exceed_the_instance_id_bound`.**
  - Failure scenario: the document contains `next_instance_id = i64::MAX`. `open` returns a counter with that value and does not persist it. Every `allocate` then fails with `Exhausted` (line 141), so the counter is silently unusable instead of being rejected as `Corrupt` on open.
  - Reach: a corrupted server-side counter file only. `open` has no production caller in `src/` (the production path is `allocate_from_snapshot`), so this is confined to the restoration module and its tests.
  - Fix: in `CounterDocument::from_bytes` (line 211) also reject `next_instance_id > i64::from(i32::MAX) + 1` with `CounterError::Corrupt`.
