<!-- fleet job=note-refresh id=Edenfps-Toolkit-and-Sanctuary-Branch-Review status=nothing_found turns=16 usd=0.0187 tokens(read,write,in,out)=[522758, 63008, 34, 11112] model=claude-haiku-5-5 -->
# notes/Research/Edenfps Toolkit and Sanctuary Branch Review.md

**Verdict:** current. I found no false claim about our code or status in `notes/Research/Edenfps Toolkit and Sanctuary Branch Review.md`, and no moved citation. Most of the note describes external repositories, which I could only spot-check.

**Corrections:** none.

**Checked and holding at the tip:**
- Pins. The FR ADR Toolkit `5acfdf8d6006fa6f43d1d3605f076a6be7393e72` matches `recovery-manifest.json:101` and the same pin in `notes/Research/Community Asset Validation.md:13`. Our pinned Sanctuary `4f028dcc274f628b65ef665fd59b184f5f3d3e3e` matches `recovery-manifest.json:98`. The PC-2009 pin `b1182d67` matches `notes/Reviews/Delegated Fishing Readiness.md:5`.
- Client version `1.910.1.530630` matches `recovery-manifest.json:140` and `:154`.
- "Same commit already used in [[Community Asset Validation]]". Confirmed; that note exists and cites the same commit.
- Probe figures. Chatdy at 4,256 vertices, 6,317 triangles, 92 bones and 32 slots, and Warpstone at 998 vertices and 978 triangles, match `notes/Research/Community Asset Validation.md:19-23` and `MODLOG.md:560`.
- "Toolkit DMOD reader accepts 36/52-byte layouts, not our cave's 44-byte layout; use the validated ForgeLightToolkit reader." Our own `prototype/osfr-tools/src/restoration/piece_098.rs:11-12` and `:665-706` accept only 52 and 36 strides, and this matches the toolkit mirror. `notes/Research/Starting Dungeon Audit.md:11` records the 44-byte rejection, and `:42` records the ForgeLightToolkit read of the cave meshes. So the "validated ForgeLightToolkit reader" wording holds.
- Toolkit license. `Community Asset Validation.md:13` states AGPL-3.0, which agrees with the note.
- Sanctuary licensing. `refs:Sanctuary/LICENSE` exists (AGPL text). `refs:Sanctuary-PC2009-20261009` has no LICENSE file in its root listing, which agrees with the note's "no tracked LICENSE" claim.
- The housing claim. `refs:Sanctuary-PC2009-20261009/src/Sanctuary.Gateway/Handlers/BaseHousingPacket/ClientHousingPacketEnterRequestHandler.cs:36-76` has the zone transfer commented out, which matches the note.
- The fishing packet paths exist in the PC-2009 reference (`BaseFishingPacket` classes and handler dispatch).
- `[[SOE Protocol Rust Crate Assessment]]` exists under `notes/Research/`. `MODLOG.md:560` records the memory-note handoff the note describes.
- The 21 prior blob hashes match `MODLOG.md:560`.

**Unsure:**
- The C# path counts against pinned `4f028dcc` (561 common, 444/440 identical, 117/121 changed, 119/121 additional) are not re-derived here. I found no tip evidence contradicting them.
- `analysis/world-loading-checkpoints.md` is not in the reference copies I searched (`refs`), so its contents and the "different executable" claim could not be checked.
- The Kart, loading, and fishing behavioural claims (`0x400000` flag, Trout `FishId=418`, the 630-byte zero blob, OnConnectMsg-only mining) describe external reference code. I did not verify them line by line.
- The `C:/Users/Bryce/...` receipt and inventory files are in the private lab and were not readable from the tip.
