<!-- fleet job=note-refresh id=Pieces-055-Ranged-enemy-attacks status=done turns=20 usd=0.0278 tokens(read,write,in,out)=[847997, 79469, 42, 18706] model=claude-haiku-5-5 -->
# notes/Research/Pieces/055 Ranged enemy attacks.md

**Verdict:** minor drift. The code, the constants, the lifecycle, the test counts and the checker all match the tip. Two community-corpus sentences are wrong about the Sanctuary copies they cite.

**Corrections:**

1. Section "Community and other evidence", paragraph 1.
   - `old:` the only ability-family serializer is `Ability.cs` (the `36/5` toolbar slot,
   - `new:` the ability-family serializers are `AbilityPacketSetDefinition` (the `36/5` toolbar slot, whose `AbilitySet` writes each `Ability` from `Ability.cs`,
   - `why:` The pinned copy `refs:Sanctuary/src/Sanctuary.Packet/BaseAbilityPacket/` holds four ability serializers, not one: `AbilityPacketSetDefinition.cs` (OpCode 5, line 8, writes `AbilitySet`), `AbilityPacketFailed.cs` (OpCode 1, writes `StringId`, line 21), `AbilityPacketAbilityDefinition.cs` (OpCode 13) and `AbilityPacketClientRequestStartAbility.cs` (OpCode 10, deserializer). `Ability.cs:24,56` holds `float Range`. None of them is `35/62`, `36/4`, `36/14` or `36/18`, so the "neither ships a serializer for them" half of the sentence stays true.

2. Section "Community and other evidence", paragraph 1, last sentence.
   - `old:` So the community corpus corroborates the vocabulary and adds nothing
   - `new:` So the community corpus corroborates the vocabulary and adds only one payload serializer (`36/4`, `AbilityPacketLaunchAndLand.cs`, in the later `Sanctuary-main-20261019` copy, not the pinned one) and nothing
   - `why:` `refs:Sanctuary-main-20261019/src/Sanctuary.Packet/BaseAbilityPacket/AbilityPacketLaunchAndLand.cs:10` (`ISerializablePacket`). That copy has no serializer for `35/62`, `36/14` or `36/18` in its `BasePlayerUpdatePacket` or `BaseAbilityPacket` directories. Its `SnowballInteraction.cs:56` also constructs it.

**Checked and holding:**
- `PacketCodes.cs` lines 17/20/21 (`BaseCombatPacket` 32, `BasePlayerUpdatePacket` 35, `BaseAbilityPacket` 36) at `refs:OpenSourceFreeRealms/ofrserver/Server/LibSOE/Core/PacketCodes.cs`.
- Client constructor immediates: `FUN_00a2ed30` (3), `FUN_00a2ee30` (14), `FUN_008d0b10` (62), `FUN_00a29c20` (1), `FUN_00a2a030` (9), `FUN_00a2a470` (7). `FUN_008d00e0` stores `_DAT_0175b420` at dwords 8 and 9, which are the `+0x20`/`+0x24` the note cites. `client_sql` fn table.
- `piece_055.rs`:
  - `begin_cast` rejects with `OutOfRange`, `Busy` or `Invalid` before starting (lines 233-246).
  - `advance` emits `LaunchProjectile` when flight is positive and `DetonateProjectile` when it is zero (267-282).
  - `interrupt` emits `36/18` only while casting (297-306).
  - `resolve` is single-shot and maps to `32/4`, `32/5` or `32/6` (309-325).
- Module has 12 `#[test]` functions (`prototype/osfr-tools/tests/piece_055.rs`), matching "12 passed". `tests/pieces/test_piece_055.py` has 6 test methods, matching "Ran 6 tests".
- `scripts/pieces/piece_055.py`: 11-entry `EXPECTED_PROJECTILE_CLASSES` (line 111), `CLIENT_EXE_SHA256` (48), `EXPECTED_ASSET_ROWS` (126-130), exit 2 on problems (646). `NoCastTargeting` = 288 in `locale` and `scripts/pieces/piece_035.py:89`.
- `encode_start_casting` (36/3) exists at `piece_035.rs:351`, so "item 035's encoder" is correct.
- The `Projectile*` class list and the `AbilityPacketFailed` one-string-id shape hold.

**Unsure:**
- The capture histogram (46 messages; 23 × `35/2`, 1 × `36/5`, 2 × `38/16`; no `35/62`/`36/4`/`36/14`/`36/18`/`36/3`) and the manifest rows (`arrow_projectile.adr` 1685399903 / 132 bytes, `bolt_projectile.adr`, `bone_projectile.cdt`). The lab captures and manifest are not reachable from these roots, so I did not confirm them.
- The `FreeRealms.exe` hash `26cc1c52…` and the dword at VA `0x175b420` are not verifiable from these roots either.
- Gaps section: "`36/4` `LaunchAndLand` remains a name without a role". The later `Sanctuary-main-20261019` copy uses it in `SnowballInteraction.cs:56`. That may give a usage hint, but it is not a recovered role, so I left the claim.
- The header's "Status: ready for review" and the crate-wide `cargo test` red-state paragraph are time-stamped. I did not check the current state of `tests/piece_044.rs` or `piece_063.rs`.
