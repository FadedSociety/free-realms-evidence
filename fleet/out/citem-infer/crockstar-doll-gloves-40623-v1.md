<!-- fleet job=citem-infer id=crockstar-doll-gloves-40623-v1 status=done turns=7 usd=0.0054 tokens(read,write,in,out)=[76429, 22561, 16, 3703] model=claude-haiku-5-5 -->
# Rockstar Doll Gloves

{"item": {"name": "Rockstar Doll Gloves", "locale_id": 40623, "kind": "collection"},
 "sources": [
  {"type": "collection", "detail": "Entry in the [Rockstar] Pixie Doll collection (client 'Rockstar Pixie Doll', ucdt/ugdt 613346883; wiki List of Collections / Toys (Collections)). The collection's final reward is the Rockstar Pixie Doll; the glove is one of its 8 entries.", "where": "Central Wilds (collection area per data)", "price": null, "currency": null, "source": "repo:prototype/osfr-tools/data/content/collections.json:7465-7540 (wiki:4:117); locale:40623; locale:132311 ('This item can be added to the Rockstar Pixie Doll Collection')"},
  {"type": "collection", "detail": "Entry in the [Rockstar] Human Doll collection (client 'Rockstar Human Doll', ugdt 443120088; 8 entries including Rockstar Doll Gloves)", "where": "Northern Wilds (collection area per data)", "price": null, "currency": null, "source": "repo:prototype/osfr-tools/data/content/collections.json:7375-7460 (wiki:4:116); wiki List of Collections '[Rockstar] Human [Doll]'"},
  {"type": "drop", "detail": "Robgoblin spawns (the collection data lists spawn_type Robgoblin for both Rockstar doll collections, quality Common). The data does not say the glove itself drops; it gives the collection's enemy spawn type.", "where": "Central Wilds / Northern Wilds", "price": null, "currency": null, "source": "repo:prototype/osfr-tools/data/content/collections.json (spawn_type 'Robgoblin', wiki:4:116 and wiki:4:117)"}
 ],
 "retired": null,
 "live": "unsure",
 "evidence": [
  {"claim": "Client name 'Rockstar Doll Gloves' is locale 40623, two definitions (3407, 3455), slot 0, class 0, no model files, no coin store price.", "source": "locale:40623; client definition pack"},
  {"claim": "Client description says the item can be added to the Rockstar Pixie Doll Collection.", "source": "locale:132311"},
  {"claim": "Wiki list of collections and the Toys (Collections) page list Rockstar Doll Gloves as an entry of both the [Rockstar] Pixie Doll and [Rockstar] Human Doll collections.", "source": "lookup wiki 'Toys (Collections)' and 'List of Collections'; repo collections.json wiki:4:116 and wiki:4:117"},
  {"claim": "Collection data lists the Rockstar doll collections' spawn type as Robgoblin, quality Common, with a reward of 21 (coins) listed on the wiki line for the doll.", "source": "repo:prototype/osfr-tools/data/content/collections.json:7436-7447, 7522-7533"},
  {"claim": "The Rockstar doll set is tied to the Pear Jam missing-rockstar quest chain in Wugachug/the Wilds, but the glove is not named in those quest texts.", "source": "locale:774116531; locale:497711267; notes/Build Guides/Content/NPCs/NPCs - Wilds.md"}
 ],
 "confidence": 0.5,
 "open": [
  "The '21' on the collection lines is ambiguous: the wiki lists it as the reward for the doll, and it may be a coin value or sale price. Not confirmed as a price for the glove.",
  "No wiki page or video names the glove's own drop rate or the Robgoblin drop as a single-item source. The Robgoblin source is inferred from the collection's spawn type.",
  "Two client definitions (3407, 3455) exist, likely one per race variant. Not verified which applies to which collection.",
  "No coin vendor, Station Cash, prize wheel, or event source found. Confirm with the Robgoblin drop tables or a player source.",
  "Retired status not stated in any source. The wiki collection data is from 2013 (revision 31048). Live status is unsure."
 ]}
