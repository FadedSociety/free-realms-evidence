<!-- fleet job=guide-refresh id=Client-Engine-Scaleform-and-Flash-UI status=done turns=14 usd=0.0133 tokens(read,write,in,out)=[309241, 40213, 30, 10387] model=claude-haiku-5-5 -->
# notes/Build Guides/Client Engine/Scaleform and Flash UI.md

**Verdict:** minor drift. The hand-checkable claims hold, but the generated count header is a stale snapshot of the native map. The note has no claims about our server code: the narrative is unwritten, and no `.rs` file in the repo mentions Scaleform or the GFx action layer.

**Corrections:**

1. `old:` 596 accepted functions: 142 confirmed, 286 likely, 138 speculative, 30 unknown. Network-linked (`wire`): 1.
   `new:` 1863 accepted functions: 427 confirmed, 1098 likely, 307 speculative, 31 unknown. Network-linked (`wire`): 1.
   `why:` `client_sql` on `label`, filtered to `subsystem` in (`ui.scaleform`, `lib.scaleform`, `ui.browser`): confidence counts are 427 / 1098 / 307 / 31 (sum 1863), and `wire` is set on 1 row (`ClientHousingPacketEnterRequest`). The note's own generator, `scripts/native_map/build_guides.py:190-191`, builds this line from `lab/native-map/run/map.sqlite`. The note's 596 equals the sum of its listed source shards, so it is internally consistent but predates shards S0117, S0074, S0832, S0834, S0836 and others that the DB now maps to these subsystems (see the `shard` counts in `client_sql`). The durable fix is to re-run the generator, not to hand-edit.

2. `old:` Subsystems: `ui.scaleform` (284), `lib.scaleform` (276), `ui.browser` (36)
   `new:` Subsystems: `ui.scaleform` (417), `lib.scaleform` (1321), `ui.browser` (125)
   `why:` same `client_sql` query on `label.subsystem` (417 + 1321 + 125 = 1863). Source: `scripts/native_map/build_guides.py:192`.

**Spot checks that hold (no change):**
- `repo:notes/.../Scaleform and Flash UI.md` line 709/718/727/761/771 frtwuihandlers.cc line numbers (257, 267, 247, 277, 234) match the client strings at `fn` 01248ae0, 01248c40, 01248980, 01248da0, 01249190.
- `00a89b90` (`FlashTimer:ResetTimer`, flag 8 at this+0xc), `009d2170` (`Main.wndSceneText.swfSceneText`), `00844420` (teardown clears `DAT_01be15ca`), `00843e90` (D3D device, present params, HWND arguments), `009d22d0` (one-argument wrapper), and `00ca8090`, `00d55a70` all match the decompiled pseudocode.
- The Source shards list sums to 596, matching the header.

**Unsure:**
- The index line `repo:notes/Build Guides/Build Guides.md:57` ("596 functions (142 confirmed, 286 likely)") carries the same stale count. It is outside this note, so I did not edit it, but it should change with correction 1.
- Whether `client_sql` and `lab/native-map/run/map.sqlite` are the same map. I assumed they are, since the shard counts match for the shards the note lists.
- The per-class counts in the table headers (for example `Scaleform::IScaleformActionHandler` (171)) were not recounted.
