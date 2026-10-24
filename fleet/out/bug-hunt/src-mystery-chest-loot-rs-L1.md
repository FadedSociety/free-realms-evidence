<!-- fleet job=bug-hunt id=src-mystery-chest-loot-rs-L1 status=nothing_found turns=12 usd=0.0121 tokens(read,write,in,out)=[230623, 31829, 26, 11694] model=claude-haiku-5-5 -->
# prototype/osfr-tools/src/mystery_chest_loot.rs lines 1-197 of 197

No reportable defect in `mystery_chest_loot.rs` lines 1-197.

What I checked:

- **Client-controlled ids (handle, lines 104-123):** `request` ids are only used to search the server's own inventory. `parse_request` rejects non-positive ids (mystery_chest.rs:132). The chest must match `i.id == id`, be non-rental, have `consumed_count == 0`, and have a definition in `self.rewards`. The key is server-found. No client value is trusted as authority.
- **Index panic at line 151 (`self.rewards[&chest.definition_id]`):** safe, because the chest was selected by `self.rewards.contains_key(&i.definition_id)` at line 115.
- **Modulo at line 162:** `choices` is non-empty, enforced at line 70 (`rewards.is_empty()`). `choices.len() as u64` cannot be zero.
- **`digest[..8].try_into().unwrap()` (line 161):** the SHA-256 digest is always 32 bytes, so this cannot panic and its input is not client data.
- **Atomicity (lines 164-194):** all mutations (`consume` chest, `consume` key, `grant`) go to `staged`, a clone. `item_reward(...)?` and the `ok_or_else` at line 183 fail before `*inventory = staged`, so a failure leaves inventory unchanged. `Inventory::consume` and `grant_with_tint` also stage their own work (inventory.rs:1063, 975).
- **Reward item lookup (lines 168-183):** the granted stack is uniquely identified by the `is_none_or(count changed)` test. Reward definitions are validated at load to exclude KEY, chest-type items, and non-positive icon/name ids.
- **Outcome flags:** `changed` comes from `consume(chest)`, which always sets it to true. The gameplay caller (gameplay.rs:5125-5137) uses it correctly.
- **Load (lines 42-95):** file size is bounded by `take(MAX_CONTENT+1)`. Counts are capped at 64. Binding and reward definitions are validated through `presentation()`, which returns `Err` for unknown ids (inventory.rs:564-569). Duplicate bindings are rejected.
- **Pending confirmation (lines 124-136):** the W90 comment matches the code. A Use for a different instance does not clear `pending`.

Observations I did not report, because I could not show them as defects:

- **Predictable outcome (lines 154-162):** the reward is a SHA-256 of player guid, chest id/count and key id/count. The client can compute it in advance. The comment at line 152 calls this a placeholder, and gaining a chosen reward would require buying keys, so I judged it a design question rather than a free-item exploit.
- **Full inventory (line 165-167 via inventory.rs:1009-1010):** with 4096 items and no freed slot, `grant` returns `Err("inventory is full")`, which propagates out of `handle` via `?`. I did not verify whether the session layer disconnects the client or only logs the error, so I left it unreported.
- **Pending cleared before fallible steps (line 135):** if a later step fails, `pending` is already `None`. The player must re-check. This is a minor UX effect with no state corruption.
