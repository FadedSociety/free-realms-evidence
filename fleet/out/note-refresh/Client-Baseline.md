<!-- fleet job=note-refresh id=Client-Baseline status=done turns=13 usd=0.0160 tokens(read,write,in,out)=[388581, 54322, 28, 10668] model=claude-haiku-5-5 -->
# notes/Research/Client Baseline.md

**Verdict:** minor drift. The run table, packet counts and the 46-message startup claims hold, and the lab-only figures can't be checked from the repo. The "Limits" section still describes Rust as it stood before the gateway milestone, and one source path has moved.

**Corrections:**

1. `old:` Rust currently provides tooling and transport components, not the running world service.
   `new:` Rust now runs a local gateway that logs in, enters the reference zone, walks, saves and restores position (see [[Rust Gateway Milestone]]). The wider game world is still partial; see the Build Ledger for each system's status.
   `why:` repo:notes/Research/Rust Gateway Milestone.md:3, 14-17; repo:notes/Design/Build Ledger.md:39 ("World entry (46 startup messages)" is Native-verified, built in `gateway.rs:1366-1403`); repo:prototype/osfr-tools/src/bin/osfr-gateway.rs exists.

2. `old:` `LibSOE/SOE.Core/SOEDataChannel.cs`
   `new:` `OpenSourceFreeRealms/ofrserver/Server/LibSOE/Core/SOEDataChannel.cs` (lines 89-93 hold the check)
   `why:` repo refs: the file is at `OpenSourceFreeRealms/ofrserver/Server/LibSOE/Core/SOEDataChannel.cs:89-93`; no `SOE.Core` directory exists. The claim itself holds: `previousFragmentSequenceNumber` is computed before `FragmentSequenceNumber` is overwritten, so the next incrementing fragment is rejected at line 93.

3. `old:` Save/restart/reload persistence remains unverified.
   `new:` Save/restart persistence was not verified in the original managed-emulator baseline; the later Rust gateway verified it (see Subsequent Rust acceptance).
   `why:` repo:notes/Research/Rust Gateway Milestone.md:14-17 (position saved, fresh Rust process and client restart, restored position matched); repo:notes/Research/Client Baseline.md:97 already says the later Rust run passed restart.

4. `old:` Packet loss, retransmission, duplicates, rollover and longer sessions require separate transport tests.
   `new:` The Rust transport now covers loss recovery, duplicates and sequence rollover (`prototype/osfr-tools/src/soe.rs:287-425`; `scripts/run-local-baseline.py:51`; a live dropped-sequence recovery is in repo:notes/Research/Rust Gateway Milestone.md:12). Longer sessions and the other limits remain untested.
   `why:` the code and milestone note above. The rest of the sentence is still open.

**Unsure:**
- "The legacy handler still ignores those fields." The supplied handler `OpenSourceFreeRealms/ofrserver/Gateway/Login/LoginManager.cs:46-58` never reads the message body, which agrees. I did not check the Sanctuary field-layout comparison.
- Lab-only figures (1,382 datagrams, 1,380 checked CRCs, 57/48/54 message counts, 12 position updates, 9.75-unit displacement, log lines `FreeRealms.log:319-320`) could not be verified from the repo. Their manifests are outside it.
- Adjacent note outside this task: `repo:notes/Research/Legacy Gateway Oracle.md:89` cites `LibSOE/SOE.Core/SOEDataChannel.cs:181`. It has the same path problem and should be checked too.
