<!-- fleet job=guide-refresh id=Content-Dungeons-Bigfoot-Defender status=done turns=12 usd=0.0120 tokens(read,write,in,out)=[239320, 38697, 26, 9604] model=claude-haiku-5-5 -->
# notes/Build Guides/Content/Dungeons/Bigfoot Defender.md

**Verdict:** minor drift. Most client `loc` ids, quoted strings and prize-wheel item names check out at the tip. One "not found" claim is false: the client does carry a panel description for this battle, and the Gaps list repeats the gap.

**Corrections:**

1. `old:` Not found in the client. The wiki infobox gives none for this page. | gap
   `new:` "Those violent Camp Chatty counselors are trying to hurt Bigfoot, Camp Robbie's guardian. So what if he's scaring the wimps at Camp Chatty. A good scare every now and then keeps ya' on your toes." (`loc 1243160555`; the locale entry right after the name "Bigfoot Defender", id 6758). The wiki infobox gives none for this page. | [client]
   `why:` Locale `6758` is "Bigfoot Defender" and `6759` is that description text, mirroring Bigfoot's Lair's name and description pair at `6756`/`6757` (locale lookup by id; `client:locale/en_us_data.dat:32913`, hash `1243160555 ucdt`). The note already cites the same string as the Story hook, so the "Not found" cell contradicts itself.

2. `old:` - Panel description, goals panel count, any bonus goal.
   `new:` - Goals panel count, any bonus goal. (The panel description is in the client; see the Overview correction.)
   `why:` Same evidence as correction 1: `repo:notes/Build Guides/Content/Dungeons/Bigfoot Defender.md` cites `loc 1243160555` as client text, and the client locale at Global.Text 6759 holds the description.

**Checked and holding (no change):**
- Client names: `loc 2068880740` (ugdt "Bigfoot Defender") and `3712650989` (ucdt); `54624951` and `3740470622` for Bigfoot's Endangered (`client:locale/en_us_data.dat`).
- Goal names for the four counselors: `314220268`, `1141526814`, `1564263106`, `22760277`. "Don't let Bigfoot get knocked out" is `817448663`, and `repo:prototype/osfr-tools/data/content/dungeons/bigfoot_s_lair.json:285` assigns it to this battle, as the note does.
- Requirement strings: "Requires a level 5 combat job" (`2145075890`) and "...must have a combat job of at least level 5 to play this battle" (`3173661191`).
- Dialogue and story ids (`2404845728`, `3421589477`, `3316236307`, `1148190599`, `1515101801`, `820703868`, and the rest of the Related-quests set) exist with the quoted wording.
- Prize-wheel item names (Camp Chatty Flair Shard, Owl Totem, Treeble Treat, Man-Eating Plant Totem, and others) all exist in the locale.
- Code: `repo:prototype/osfr-tools/data/content/dungeons/bigfoot_defender.json` exists with the same name id, difficulty 3 and job level 5, and has no goals or rewards. The note makes no code-status claim, so nothing there needed correcting.

**Unsure:**
- Whether the 6759 description is this battle's *panel* text rather than some other display. The id pairing with the name at 6758 strongly suggests it, but I did not see the UI that shows it.
- The 990-coin figure and the shared prize table with Bigfoot's Lair: both pages cite only the wiki, and the item lists match exactly. I could not check the figure against the client.
- Whether "Bigfoot Thrash", "Bigfoot Rock Throw", "Bigfoot Bash" and "Bigfoot Rage Resist" are used in this fight. The note already marks this unproven, and I found no code or client link.
