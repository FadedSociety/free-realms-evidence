<!-- fleet job=guide-refresh id=World-Actors-and-NPCs status=done turns=20 usd=0.0231 tokens(read,write,in,out)=[729906, 62903, 42, 15959] model=claude-haiku-5-5 -->
# notes/Build Guides/World/Actors and NPCs.md

**Verdict:** minor drift. The per-section tables, the `wire` count, the shard-list shape and the spot-checked names and subsystems match the label table. The header totals miss one accepted row from shard S0801, so they are one short.

**Corrections:**

1. `old:` 198 accepted functions: 67 confirmed, 63 likely, 42 speculative, 26 unknown.
   `new:` 199 accepted functions: 68 confirmed, 63 likely, 42 speculative, 26 unknown.
   `why:` client_sql `label` where subsystem is `world.actor` or `world.transform`: 199 rows (199 distinct addresses), all `accepted`. Confirmed = 62 (actor) + 6 (transform) = 68. The extra row is `017230f0` (InitControllerCinematicActorHandler, shard S0801, confirmed), which this note does not list.

2. `old:` Subsystems: `world.actor` (154), `world.transform` (44)
   `new:` Subsystems: `world.actor` (155), `world.transform` (44)
   `why:` client_sql `label`: world.actor = 155 (62 confirmed, 48 likely, 26 speculative, 19 unknown); world.transform = 44. The note's own section tables sum to 154 for world.actor, so the one missing row is the S0801 entry in item 4.

3. `old:` [[S0588|S0588]] (14)
   `new:` [[S0588|S0588]] (14), [[S0801|S0801]] (1)
   `why:` client_sql `label`: shard `S0801` holds one `world.actor` row (`017230f0`). The shard list in this note otherwise sums to 198 and omits S0801.

4. `old:` **PlayerSphereTrackable** (4)
   `new:` **ControllerCinematicActorHandler** (1)

   | Address | Name | Confidence | What it does |
   |---|---|---|---|
   | `017230f0` | InitControllerCinematicActorHandler | confirmed | Writes the ControllerCinematicActorHandler vtable at 01b500cc, IString<char> vtable at 01b500d0, pointer 01be7034 at 01b500d4, and zeroes 01b500d8 and 01b500dc; registers 017471c0 with _atexit. |

   **PlayerSphereTrackable** (4)
   `why:` client_sql `label` addr `017230f0`: class ControllerCinematicActorHandler, kind init, subsystem world.actor, confirmed, shard S0801. The class has no section in this note; the new section keeps the alphabetical class order.

**Unsure:**
- The "Build Guides.md" index (`notes/Build Guides/Build Guides.md:43`) says "[[Actors and NPCs]] — 198 functions (67 confirmed, 63 likely)". It carries the same stale totals as this note's header, so it needs the same update. I did not edit it.
- I did not trace the individual prose claims (for example the `Actor::Update` hook at +0x368 or the `ProxiedObject` accessors) against the decompiled bytes. I spot-checked names, subsystems and confidence labels for about 40 addresses across the note's sections and they matched the label table. Every shard file the source list names was checked; the ones without an address suffix (S0162, S0164–S0167, S0170, S0173, S0175, S0179, S0396, S0581, S0588, S0801) are name-only links, a convention used across the vault, so they were not treated as broken.
- `Network-linked (wire): 0` holds: no `world.actor` or `world.transform` label has a non-empty `wire` array.
