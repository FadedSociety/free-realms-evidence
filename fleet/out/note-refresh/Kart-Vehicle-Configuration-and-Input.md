<!-- fleet job=note-refresh id=Kart-Vehicle-Configuration-and-Input status=done turns=34 usd=0.0408 tokens(read,write,in,out)=[1716974, 86822, 70, 25570] model=claude-haiku-5-5 -->
# notes/Research/Kart Vehicle Configuration and Input.md

**Verdict:** minor drift. The dispatcher bindings, parser chains, payload sizes, the 33/11 and 33/34 field layouts, the 33/7 and 33/17 header words and the local-guid path all match the tip. The one stale area is the claim that the 33/6 field boundaries are unrecovered: the repo now records and decodes the first 48 bytes and the control byte.

**Corrections:**

1. old: `but the exact field boundaries are **not recovered**; the count and length are pinned, the semantics are not.`
   new: `but the first 48 bytes are nine basis floats (bytes 0-35) and the translation at byte 36 (x, y, z at 36/40/44). The control byte is at 76, and the word at 81..85 is validated as 1 on the weapon-effects path. The velocity triples, id pair and control bit map are **not recovered**; the count and length are pinned.`
   why: repo:prototype/osfr-tools/src/kart_service.rs:1976-1994 decodes basis at 0..35, position at 36..47, `payload[76]` and `payload[81..85] == 1` (opt-in under `content.weapon_effects`). repo:prototype/osfr-tools/src/kart_weapons.rs:625-626 documents "nine basis floats and then the position at byte offset 36". repo:notes/Build Guides/Gameplay/Kart Racing.md:93 records the same layout with the control byte at 76 and the bit map still unrecovered.

2. old: `* \`33/6\` field boundaries inside its 85-byte payload.`
   new: `* \`33/6\` velocity triples, id pair and control bit map inside its 85-byte payload (the basis and translation boundaries are recorded above).`
   why: same as correction 1 (repo:prototype/osfr-tools/src/kart_service.rs:1980-1994; repo:notes/Build Guides/Gameplay/Kart Racing.md:93).

**Checked and holding (no change):**
- Dispatcher bindings. Subtype 11 calls `00b9c910`/`00ba7460`, which calls `00ba7370`. Subtype 34 calls `00ba3670`, which calls `00ba0680`. Subtype 5 parses through `00ba1070`. Subtype 6 has no receive case, and neither do 7 or 17 (client:FUN_00ba74d0 has no `case 0x6`).
- `00ba0680` reads i32, i32, f32, four float4 (via `008e2410`), i32, i32, which is 84 bytes.
- `00ba7370` reads the owner u64 at +0x10/+0x14, four 12-byte vectors, then bytes at +0xe4c and +0xe18. That is 58 fixed bytes, and the frame-table arithmetic (payload minus 58) is consistent.
- `00ba48a0` writes header `0x21` with `7` for GateHit and `0x11` for PickupHitRequest, and takes the guid from `+0x2cc` then `+0xe60/+0xe64`.
- Repo sizes match: `SERVER_DATA_PAYLOAD_LEN` 85, `GATE_HIT_PAYLOAD_LEN` 24, `SET_RACE_CONFIG` 84 (kart_entry.rs:85-88; kart_service.rs:174-176).
- The `33/34` template (716, 82, 423, and the 16638/16634 pair) is in repo:prototype/osfr-tools/data/content/kart_entry.json:4-26.
- The cross-linked notes all exist.

**Unsure:**
- The `33/34` trailing pair. kart_entry.json:25-26 carries `16638, 16634` verbatim. repo:notes/Build Guides/Gameplay/Kart Racing.md:69 lists 16638 as the missile explosion and 16634 as the mine explosion composite effect. That is a possible meaning, but nothing establishes it, so the note's "unmapped" stays.
- The "no 2917 / 7494 in the executable export" claim. The repo maps job 48 to name id 2917 (repo:prototype/osfr-tools/src/kart_racing.rs:64-67; restoration/piece_041.rs:50-55). My client grep for 2917 was too noisy to settle it.
- The lab proof, checker and frame counts (4,679, 31, 33, 6) live under `lab/`, which is not in the repo, so I could not check them. kart_service.rs:19-21 independently cites 31 gate hits over 51.6 s, which agrees.
- Other stale text outside this note. repo:notes/Build Guides/Gameplay/Kart Racing.md:177 still lists "33/5 and 33/6 interiors" as unmapped. repo:prototype/osfr-tools/src/kart_service.rs:9 cites a `Kart Motion Layout` note that does not exist in `notes/`. repo:notes/Native Map/Shards/S0363 00ba48a0-00ba7460.md:33 still asks for the 33/6 mapping.
