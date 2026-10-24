<!-- fleet job=guide-refresh id=Network-User-Data-and-Storage status=done turns=10 usd=0.0073 tokens(read,write,in,out)=[111802, 26620, 22, 5752] model=claude-haiku-5-5 -->
# notes/Build Guides/Network/User Data and Storage.md

**Verdict:** minor drift. The per-function table rows, subsystem counts, shard counts, the 852 total and the `wire` count all match the current label data. Only the confidence tally in the generated header is stale.

**Corrections:**

- `old:` 852 accepted functions: 427 confirmed, 242 likely, 116 speculative, 67 unknown. Network-linked (`wire`): 0.
- `new:` 852 accepted functions: 414 confirmed, 254 likely, 116 speculative, 68 unknown. Network-linked (`wire`): 0.
- `why:` The `label` table, filtered to `net.uram*` and `net.userdata*` (all status `accepted`), gives confirmed 194+177+43 = 414, likely 179+55+20 = 254, speculative 63+25+28 = 116, unknown 37+4+27 = 68; total 852. The reviewer-confidence column gives different numbers again (456/303/92/1), so it does not explain the header either. The `wire` field is empty (`[]`) for all 852 rows, so "0" is right. The header's 427/242/116/67 matches neither source. Evidence: `repo:notes/Build Guides/Network/User Data and Storage.md:19`, label records such as `01528ab0` (likely, `net.userdata`), `01528b70` (confirmed).

**Checked and holding:**
- Subsystem line (`net.uram` 473, `net.userdata` 261, `net.userdata_command` 118) matches the label counts.
- Source-shard counts (S0450 45 … S0794 125) match the label counts per shard and sum to 852.
- Sampled table rows match the label confidence and names: `01528a80` speculative, `01527800` confirmed, `0151fcf0` likely, `00f88e50` unknown, `00f7b880` likely.
- The "How it works" section still reads "Not written yet", which is accurate.
- The `Command System` link target exists at `repo:notes/Build Guides/Network/Command System.md`.

**Unsure:**
- The note makes no claims about our server code. A search of `repo` for `UserData`/`userdata` finds only notes and an unrelated launcher screenshot call, so the server has no user-data handling. The note does not say otherwise, so nothing was corrected.
- I did not count the table rows one by one. The per-class counts are consistent with the 852 total in the spot checks.
