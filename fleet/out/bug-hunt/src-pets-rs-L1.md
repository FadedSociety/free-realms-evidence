<!-- fleet job=bug-hunt id=src-pets-rs-L1 status=nothing_found turns=8 usd=0.0111 tokens(read,write,in,out)=[133723, 35927, 18, 10633] model=claude-haiku-5-5 -->
# prototype/osfr-tools/src/pets.rs lines 1-800 of 1819

Window `prototype/osfr-tools/src/pets.rs` lines 1-800 read in full, plus the adjacent callers needed to judge reach (`adopt_with_replies` 800-824, `adopt_vendor_grant` 827-845, `rename` 849-867, `summon_by_item_owned` caller at 1100-1150, `insert_pet`/`validate_roster` 1459-1528). No defect I could tie to a line and show reachable from a client packet or save.

Checked and dropped:
- **Decode bounds (`PetRequest::decode`, 531-609):** `body[4]` is read only after `body.len() != 5` is rejected; `word()` uses `get(offset..offset+4)` so it cannot panic; subtype 6 checks `body.len() < 4` before `word(0)`, rejects `length` outside 1..=256 before `body[4..]`, and requires `body.len() == length + 4`, so the slice is in range. The `as usize` cast of a `u32` is lossless on supported targets. Subtype 24 and 32 length checks precede use. No allocation is sized from a client value.
- **Subtype 4 action semantics (558-563):** `(1,0)` is rejected, `(0,_)` is dismiss, and anything else errors. Matches the documented client layout.
- **`validate()` (260-357):** `names.first[0]` is indexed only after `names.first.len() != 60` short-circuits, so it is safe. Content-only checks; no client input reaches them.
- **`adopt_with_replies` atomicity (793-824):** the roster and inventory are mutated on clones and committed only after `insert_pet`, `validate_roster`, and `consume` all succeed. No partial mutation before `?`.
- **`adopt_vendor_grant` (827-845):** `grant_id == 0` is rejected, retries are deduplicated, and the roster is committed only after validation.
- **`insert_pet` overflow (1459-1465):** `checked_add` guards `next_pet_id`. The `MAX_PETS` ceiling is enforced later by `validate_roster` on the cloned roster, so over-cap growth is rejected before commit.
- **`roster_snapshot` (681-683):** returns `None` when the roster is empty, which would drop `vendor_grants`. Only the gateway's session map (`osfr-gateway.rs:680`) calls `remove`; nothing shrinks `roster.pets`, so this cannot lose grants in practice.
- **`pet_guid` XOR (730-731):** owner guids come from the sequential `next_character_guid` counter, so the bit-62 collision with another owner is not reachable.
- **`MODEL_IDS` coverage (29-56, 364-371):** the only bound ADRs in `pets.json` are `dragon_m_basic.adr` and `groundhog_m.adr`, both mapped; the other `model` values are prose placeholders.

Out of window and not examined: equipment mutation (1275-1297, 1332, 1369) is not validated by `validate_roster` (1487-1528). That belongs to the 800+ windows and may be worth a look there.
