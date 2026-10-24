<!-- fleet job=guide-refresh id=Libraries-and-Runtime-OpenSSL-and-Crypto status=nothing_found turns=19 usd=0.0210 tokens(read,write,in,out)=[599762, 56384, 40, 15941] model=claude-haiku-5-5 -->
# notes/Build Guides/Libraries and Runtime/OpenSSL and Crypto.md

**Verdict:** current. The note is a generated map of the client's OpenSSL/crypto functions, and every checkable claim I tested matches the label and fn data (`client_sql`). The note makes no claims about our server code beyond its links.

**Corrections:** none.

**What I checked:**
- **Totals and confidence split:** 359 functions = 10 confirmed + 178 likely + 102 speculative + 69 unknown. The label table gives the same split for the five source shards the note cites (S0041 3, S0540 1, S0634 151, S0636 195, S0791 9, total 359).
- **Subsystem counts:** all 19 match the same five-shard query, e.g. `lib.openssl.x509` 79, `lib.openssl.ec` 76, `lib.openssl` 45, `lib.crypto.sha1` 5.
- **"Network-linked (wire): 0":** true for this set. The 359 come from the five shards above, and none of them has a `wire` entry. Other OpenSSL labels do carry wire entries (32 in `lib.openssl`, e.g. SSL3 send/recv in shards S0629–S0631 and S0795), but those are outside the note's set.
- **Row names and addresses:** about 60 sampled rows (e.g. `011b71d0` CRYPTO_malloc, `011b5a00` sk_new, `011bf4b0` EVP_DigestFinal_ex, `011c2ea0` EC_KEY_new, `00f912f0` X509VerifyErrorString, `01519900` Sha1Init, `0151a7e0` Md5Final) match the label names and their stated confidence.
- **Per-section row counts:** the table rows in each section match the heading counts for x509 (39), ec (30), stack (17), evp (10), bn (23), crypto (18), lhash (8), bio (7) and the others.
- **Spot-checked details:** the MD5 pad table `01912020`, the SHA-1 `this+0x1c` buffer, and the source-line references (`ec_key.c line 0x49`, `lhash.c line 0x77`, `digest.c line 0x7f`, `eng_init.c line 0x7e`, `bss_mem.c,100`, `stack.c line 0x7d`, `bn_ctx.c line 0xd8`, `buffer.c line 0x43`) all appear in the label records.
- **Links:** `[[Gateway and Transport]]` resolves to `notes/Build Guides/Network/Gateway and Transport.md`, and `Build Guides.md` lists this note with the same 359 / 10 / 178 figures.

**Unsure:**
- The "How it works" narrative is still the placeholder "_Not written yet._" I did not judge whether that is a stale status, since it is a deliberate placeholder.
- I did not check the truncated descriptions in the table cells (cut at about 200 characters) against their full pseudocode, so wording inside those cells is unverified.
