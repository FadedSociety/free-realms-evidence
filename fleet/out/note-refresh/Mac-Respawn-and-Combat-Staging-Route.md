<!-- fleet job=note-refresh id=Mac-Respawn-and-Combat-Staging-Route status=done turns=7 usd=0.0094 tokens(read,write,in,out)=[103617, 35110, 16, 7999] model=claude-haiku-5-5 -->
# notes/Research/Mac Respawn and Combat Staging Route.md

**Verdict:** minor drift. The route geometry and the status claims hold against the tip. One height statement is arithmetically and directionally wrong.

**Corrections:**

- `old:` The endpoint render floor lies 0.66318 m below the reported Mac Y.
  `new:` The endpoint render floor lies 4.19591 m above the reported Mac Y (floor −48.51963 against Mac −52.71554).
  `why:` The note's own coordinates on lines 3 and 30 give the difference. −48.51963 − (−52.71554) = +4.19591, so the floor is higher, not lower. The stated 51.15215 m 3D distance only reproduces with a 4.19591 m vertical term (√(25.1656² + 4.19591² + 44.33542²) ≈ 51.152); a 0.66318 m term gives ≈ 50.98 m. The note's own "downhill staging→Mac" wording on line 34 also implies the floor is above Mac. Repo evidence for the pursuit radius is `prototype/osfr-tools/src/restoration/piece_053.rs:34` (`AGGRO_PURSUIT_RANGE: f32 = 40.0`), which supports the "outside Mac's reported 40 m pursuit radius" framing.

**Checked and holding (no change):**

- The 40 m pursuit radius matches `piece_053.rs:33-34` and `tests/piece_053.rs:57`.
- The waypoint table has 14 rows, matching "14 walking waypoints".
- Segment lengths recompute from the table: respawn→(−1940.3143,445.18912) = 48.21 m; the join (445.19→456→(−1918,455)→Road704) = 43.60 m; Road704→703→713→714→staging = 89.89 m. The total of 48.21 + 43.60 + 89.89 = 181.70 m matches the note's approach length.
- `[[Pappy to Bartle Main Road Detour]]` exists at `notes/Research/Pappy to Bartle Main Road Detour.md`.
- The "individual-triangle clipping" method is consistent with the Pappy note's description; terrain rasterisation lives in `prototype/osfr-tools/src/terrain.rs`.

**Unsure:**

- The "straight downhill staging→reported Mac chord is 50.97977 m" figure is the horizontal (X/Z) length: √(25.1656² + 44.33542²) ≈ 50.980. The same endpoint is quoted as 51.15215 m in 3D on line 30. The note does not say which is which, so a reader could mix them up. I did not change it, because the number is right for the 2D measure.
- The Mac position `[-1842.8344,-52.71554,350.66458]`, HP values and the artifact-removal state come from the lab handoff, which is outside the repo (`C:/Users/...`). I could not verify them, nor the handoff SHA256 or the "426 sources" count.
- The "at least 88.62 m from the reported Mac" clearance and the "no source/content changed" claim could not be checked from the tip without the lab outputs and git history.
- Native history (the 183551 boulder backout) is recorded in `notes/MODLOG.md` and the Pappy note, but I did not confirm the specific clearance numbers (1.17452 m, 2.97816 m, 2.27863 m).
