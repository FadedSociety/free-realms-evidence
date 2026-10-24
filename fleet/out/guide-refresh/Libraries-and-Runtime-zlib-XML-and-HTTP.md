<!-- fleet job=guide-refresh id=Libraries-and-Runtime-zlib-XML-and-HTTP status=done turns=17 usd=0.0199 tokens(read,write,in,out)=[513193, 58452, 36, 15014] model=claude-haiku-5-5 -->
# notes/Build Guides/Libraries and Runtime/zlib, XML and HTTP.md

**Verdict:** minor drift. The generated counts are out of date for `lib.gparse`, and three function names have been refined by the W115 chunk audit. The sampled addresses, function bodies and the `wire` count check out.

**Corrections:**

1. `old:` 325 accepted functions: 84 confirmed, 126 likely, 65 speculative, 50 unknown.
   `new:` 390 accepted functions: 87 confirmed, 185 likely, 68 speculative, 50 unknown.
   `why:` client label table, status `accepted`, summed over the six `lib.*` subsystems this note covers (`lib.gparse` 98, `lib.pugixml` 82, `lib.zlib` 76, `lib.tinyhttp` 58, `lib.uploader` 50, `lib.tinyxml` 26). The note's total of 325 predates the current `lib.gparse` count.

2. `old:` `lib.gparse` (33), `lib.tinyxml` (26)
   `new:` `lib.gparse` (98), `lib.tinyxml` (26)
   `why:` client label table, `json_extract(record,'$.subsystem') = 'lib.gparse'`: 98 rows, all `pass` 1 and `status` accepted. The other five subsystem counts in the note match the table exactly.

3. `old:` (210 of 325)
   `new:` (272 of 390)
   `why:` confirmed + likely across the six subsystems is 87 + 185 = 272 in the label table (same source as correction 1).

4. `old:` `00f5a950` | ParseTextCrlfToLt |
   `new:` `00f5a950` | ParseTextCrlfToLt_Chunk |
   `why:` client label `00f5a950`: name `ParseTextCrlfToLt_Chunk`, `chunk_of` `00f5c010`. The audit (W115, by recheck B0024) refines it: it is a continuation/shared-tail chunk, and no direct call or vtable entry targets it. The `prior_name` was `ParseTextCrlfToLt`.

5. `old:` `00f5abc0` | ParseCrlfToDelimiter |
   `new:` `00f5abc0` | ParseEolToDelimiter_Chunk |
   `why:` client label `00f5abc0`: name `ParseEolToDelimiter_Chunk`, `chunk_of` `00f5c090`. The W115 audit classifies it as a jump-only chunk with no direct call or vtable pointer. The `prior_name` was `ParseCrlfToDelimiter`.

6. `old:` `010f1b50` | crc32_byfour |
   `new:` `010f1b50` | crc32_little_Chunk |
   `why:` client label `010f1b50`: name `crc32_little_Chunk`, `chunk_of` `010f22a0`. The W115 audit classifies it as a shared-tail chunk entered by `jmp` from `010f22b3`, not an independent function. The `prior_name` was `crc32_byfour`.

**Unsure:**

- The `lib.gparse` section lists only 16 rows, under a heading that says "only confirmed and likely functions are listed". The label table holds 78 confirmed + likely `lib.gparse` rows (3 confirmed, 75 likely). I could not tell whether the generator intended a partial listing or whether these rows were relabelled after the note was generated. The header statement "Network-linked (`wire`): 0" is correct: none of the six subsystems has a non-empty `wire` list.
- The narrative section ("How it works") is still a placeholder, so there are no behavioural claims to check there.
- I did not verify every row's `does` text against decompiled bytes. The sampled rows (e.g. `00f5c280`, `00d2f910`, `00f96090`, `00f733d0`, `00f5ea90`, `006f8280`, `00d30440`) match their names and descriptions.
