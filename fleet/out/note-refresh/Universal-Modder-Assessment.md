<!-- fleet job=note-refresh id=Universal-Modder-Assessment status=done turns=12 usd=0.0142 tokens(read,write,in,out)=[284933, 46822, 26, 10939] model=claude-haiku-5-5 -->
# notes/Research/Universal Modder Assessment.md

**Verdict:** minor drift. The scanner, pack-tool, and Sanctuary claims still hold at the tip. The two stale items are the "next steps" lines, which describe a real-client baseline that has since been run and passed.

**Corrections:**

1. `old:` **Immediate application:** establish the real-client baseline and record its local protocol sequence, then use those observations to verify the next Rust transport and login slice.
   `new:` **Immediate application:** the real-client baseline is already established (the client log records World Ready on 2026-10-07, and the Rust gateway passed actual-client login, world entry, walking, and restoration after restart). Use the existing `run-local-baseline.py` harness to verify the next Rust slice beyond those checkpoints.
   `why:` `repo:notes/Research/Client Baseline.md:44` (World Ready, 2026-10-07) and `:97` (Rust gateway login, world entry, walking, restart restore); `repo:prototype/osfr-tools/README.md:5` (actual client reached World Ready against the Rust gateway and restored position after restart). The harness is `repo:prototype/osfr-tools/scripts/run-local-baseline.py`, cited in the README at line 48.

2. `old:` The first checkpoints are session negotiation, application login, completed zone initialization, movement observed by the server, and character restoration after restart.
   `new:` The first checkpoints (session negotiation, application login, completed zone initialization, movement observed by the server, and character restoration after restart) have been reached against the Rust gateway; see [[Research/Rust Gateway Milestone]].
   `why:` `repo:notes/Research/Client Baseline.md:97`; `repo:prototype/osfr-tools/README.md:5`. `repo:MODLOG.md:195` records seven real-UDP session checks.

3. `old:` `Gateway/Program.cs` selects `CGAPI_527`; `Login/Program.cs` selects `LoginUdp_6`.
   `new:` `src/Sanctuary.Gateway/Program.cs` selects `CGAPI_527` (line 83 of the pinned Sanctuary checkout); `src/Sanctuary.Login/Program.cs` selects `LoginUdp_6` (line 86).
   `why:` `refs:Sanctuary/src/Sanctuary.Gateway/Program.cs:83` and `refs:Sanctuary/src/Sanctuary.Login/Program.cs:86`. The protocol names are right, but the paths in the note are not the real ones.

**Checked and holding (no change):**
- The `um/scan.py` ASI-loader pattern is at line 344 (`("ASI loader", ("*.asi",))`), and line 669 applies the loader patterns to the index. `refs:universal-modder/um/scan.py:344,669`.
- The community pack check exists as described. It loads the DbgPack reader, audits names before extraction, runs `fl_pack.py unpack`, and refuses existing output and report paths (`output.mkdir(exist_ok=False)`, `open("x")`). `repo:scripts/check-community-pack.py:21-91`. The 6,074 entries and 45,765,884 bytes match `repo:MODLOG.md:174`.
- `Sanctuary.UdpLibrary.Tests/BasicTest.cs` contains unbounded loops (`while (true)` at line 57, plus polling loops at 50, 68, 71). `refs:Sanctuary/src/Sanctuary.UdpLibrary.Tests/BasicTest.cs`.
- `notes/Design/Rust Revival Roadmap.md` and `notes/Research/Free Realms Recovery.md` both exist.
- The `gfxcapture` check in the Windows prerequisites matches `refs:universal-modder/um/win.py:144-145`.

**Unsure:**
- The `1,762` client-file count and the `Miles/mssmp3.asi`, `mssogg.asi`, and `mssvoice.asi` files. The scan JSON (`lab/manifests/universal-modder-scan.json`) and the client files are not in the readable roots. A search of the client root found no `.asi` or proxy-DLL names, but that does not settle whether the files exist.
- The `lab/` artifacts cited for the pack run (`community-pack-check.json`, `tool.log`) are not in the readable roots. Their contents are only partly corroborated by `MODLOG.md:174` and `Community Asset Validation.md:7`.
- The external skill, GitHub, and archive claims (for example `um/scan.py` line 344 being the same revision as the pinned `baff1e5`) could not be checked against the pinned revision. The `refs` copy shows the same line, but I did not confirm its revision.
