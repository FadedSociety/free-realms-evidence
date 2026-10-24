<!-- fleet job=note-refresh id=Legacy-Gateway-Oracle status=done turns=11 usd=0.0145 tokens(read,write,in,out)=[288825, 49991, 24, 10756] model=claude-haiku-5-5 -->
# notes/Research/Legacy Gateway Oracle.md

**Verdict:** minor drift. The collector script, the framing code and the Sanctuary comparison match the tip. The main staleness is the closing "next acceptance step", which a later supplied-client run has already completed. The CRC trailer is also described as the general framing when it is only the synthetic handshake's value.

**Corrections:**

1. `old:` The next acceptance step is an **actual supplied-client** connection to the copied walking emulator: observe its complete login fields, session/application encryption, packet bundling, ACK pattern, world-load completion, movement and disconnect behavior.
   `new:` The actual supplied-client connection has since been recorded in [[Client Baseline]]: login, world load and an approved walking check (runs 020205Z and 020419Z). Its remaining gaps are persistence, reliable-transport edge cases (loss, retransmission, rollover) and longer sessions. A real-client trace can still resolve the legacy/Sanctuary differences.
   `why:` notes/Research/Client Baseline.md:3, 10, 18–24, 79–83, 88–91; notes/Tasks.md:75 (marked [x]).

2. `old:` CRC low 16 bits u16 BE
   `new:` CRC trailer, low negotiated bytes, big-endian (2 bytes in this synthetic handshake; the real client negotiated 3)
   `why:` scripts/collect-legacy-oracle.py:190 (`"crc_length": 2`) and :218 (synthetic session); prototype/osfr-tools/src/soe.rs:138 and :156 (trailer length is the negotiated `crc_len`, not fixed); notes/Research/Client Baseline.md:24 ("three CRC bytes"; "the real negotiated length must drive decoding").

3. `old:` it is not an original-client login or gameplay test.
   `new:` it is not an original-client login or gameplay test; the separate supplied-client run is recorded in [[Client Baseline]].
   `why:` notes/Research/Client Baseline.md:3 and :24 (original-client login and world load were observed in the 020205Z run).

**Checked and holding:**
- `scripts/collect-legacy-oracle.py` exists at the cited path. Its behaviour matches the note: `--skip-ready` (:162), 20 s startup (:205), 12 s receive timeout and 1.5 s idle (:98–105), loopback-only send with a transient port (:178–198), copied Config.json with only the port changed (:181–183), CREATE_NO_WINDOW (:203), and terminate in `finally` (:242–251). The one ready request is `05 00 01 02 00 00 00 0d 00` (:232).
- Seed 1884358976 (`prototype/osfr-tools/tests/fixtures/transport-vectors.tsv`); opcodes 9, 13 and 21 (`soe.rs:16–19`); the body over 100 bytes compresses (`soe.rs:124`); CRC is over `seed.to_le_bytes() || wire` (`soe.rs:252–263`).
- Sanctuary `PacketLogin.cs` reads ticket, GUID u64, version and one more string, and requires full consumption (`refs:Sanctuary/src/Sanctuary.Packet/ClientGateway/PacketLogin.cs:25–37`).
- Counts agree with notes/Research/Client Baseline.md:69 (8 login + 38 ready) and notes/Research/Free Realms Recovery.md:70 (1,253 frames, 1,237 compressed, 46 messages, 627,566 bytes).

**Unsure:**
- The `lab/decompiled/server` citations (LoginManager.cs:49/65/371, PlayerCode.cs:83, SOEWriter.cs:219/278, SOEDataChannel.cs:181, SOEProtocol.cs:260), the capture manifest counts, PID 10244, and the legacy dispatcher handler list (time sync 52, teleport 90/122, etc.) live in the lab, outside the repo. I could not verify them. Client Baseline's seven time-sync messages are consistent with the handler list.
- Frame and sequence totals (1,259 frames, sequences 921–1250) and the table byte sums could not be checked without the lab manifest.
