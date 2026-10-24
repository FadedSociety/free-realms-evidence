<!-- fleet job=guide-refresh id=Client-Engine-Text-and-Localization status=nothing_found turns=18 usd=0.0167 tokens(read,write,in,out)=[486206, 46681, 38, 12089] model=claude-haiku-5-5 -->
# notes/Build Guides/Client Engine/Text and Localization.md

**Verdict:** current. The note is a generated map of client (decompiled executable) functions, not of our server code. I found no claim about our code or status that is now false. Its only server-side-facing lines are the header counts and the "Network-linked (`wire`): 0" line, and both still hold.

**Checks that held:**
- **Header counts:** 820 = 178 confirmed + 151 likely + 301 speculative + 190 unknown. The subsystem tally also sums to 820. Per-section totals match the note's own bold headers: `engine.string` 162 (2+2+15+1+5+6+1+2+128), `engine.locale` 10, `ui.locale` 40, `lib.t4` 97.
- **`wire`:** every label record for the note's subsystems has `wire: []`, so 0 network-linked is correct (client_sql on `label`).
- **Build Guides index** (`repo:notes/Build Guides/Build Guides.md:58`): "820 functions (178 confirmed, 151 likely)" agrees with this note.
- **Sampled function rows:** names, subsystems and confidence labels match the `label` table for 26 addresses (e.g. 008ece50, 00726060, 007a50b0, 00c34880, 012e0de0, 00d04b60, 00979fc0, 0097bca0, 0097be40, 00d04bf0, 00d04d70, 00d04db0, 00a852a0, 00a85860).
- **Behaviour claims:** these match the decompiled C: `LanguageIdToCode` (0..11 table), `LocaleNameForLanguageId` (1=zh_CN … 12=ru_RU), `IStringFixed8::AllocBuffer` (size ≤ 12 → capacity 12 and inline buffer), `LookupCodeStringWithArgs` (this+0x20 → table at +0x290, 256 buckets), `StringLookupByIdWithFallback` (vtable 0xcc, then 00e52260, then 0097bca0), `TableFind11ByString` (11 entries at 0x183d700), `TableFind234ByString` (0xea entries at 0x183d758), `LocalizationManagerBase::Init` (IsValid assert, `localizationmanagerbase.cc:0x2e`).

**Unsure:**
- `repo:notes/Build Guides/Client Engine/Text and Localization.md` rows `00ec7590` (T4MacroEs_EmitTodosForms, likely) and `00ec7540` (T4MacroEs_Forms_018689d0, speculative). Both say the wrapper "builds a four-pointer table … on the stack". The stored decompile for each is only a three-argument forward to `FUN_00ebe9f0`, with no table visible. The table may come from disassembly that the C does not show, so I could not confirm or refute it.
- The "How it works" narrative section is still "_Not written yet._". That is a gap, not a false claim, so I did not propose a correction.
- I did not check every one of the 820 rows, or the source-shard list, against the vault.
