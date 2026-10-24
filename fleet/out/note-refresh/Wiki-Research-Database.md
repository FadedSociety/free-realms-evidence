<!-- fleet job=note-refresh id=Wiki-Research-Database status=done turns=11 usd=0.0187 tokens(read,write,in,out)=[306571, 64246, 24, 15201] model=claude-haiku-5-5 -->
# notes/Research/Wiki Research Database.md

**Verdict:** Minor drift. The tooling, pins, commands and counts I could check match the tip. One sentence is stale because the client now settles the hammer-name question the note leaves open.

**Checked and holding (no change needed):**
- `scripts/wiki-research.py` and `scripts/wiki-requirements.txt` exist. The pins match the note: scrapling 0.4.15, sqlite-vec 0.1.9, onnxruntime 1.19.2 (`repo:scripts/wiki-requirements.txt:1-5`).
- Model `BAAI/bge-small-en-v1.5`, repository `Qdrant/bge-small-en-v1.5-onnx-Q`, revision `aa8f8b060edb00e03bfdd08813a2949946c8ba55`, 384 dimensions, cosine (`scripts/wiki-research.py:29-32`, `:86`).
- Crawl defaults: `--delay` 2.0, `--limit` 10000, namespaces `[0,112]`, so user, talk and forum namespaces are excluded (`scripts/wiki-research.py:372-374`). The client also enforces a 1 s minimum delay (`:96`).
- `Fetcher.get` with impersonation and stealth headers off, no bypass on non-200 (`:103-117`).
- Tables `pages`, `titles`, `requests`, `chunks`, `chunks_fts`, `chunk_vectors` (`:63-86`).
- Hybrid search uses reciprocal rank fusion with k=60 (`:357-365`). Search, status and verify open read-only (`:53-54`, `:283`, `:385`).
- Revision-changed handling stops rather than overwriting (`:155-158`).
- Writer stores exact bytes, which matches the LF/CRLF correction (`:161`).
- `verify` checks request and page SHA-256, chunk hashes, FTS and vector coverage, norms, and four sampled vectors (`:285-329`).
- Embedding resumes only missing vector rows (`:251`).
- Cross-links `[[Starting Area Content Audit]]`, `[[Starting Dungeon Audit]]` and `[[../Design/Opening Playthrough]]` resolve to files in `notes/`.
- Quest revisions 27815 (16 coins) and 28955 (18 coins, five wolves) match `scripts/prepare-opening-content.py:35-36`. The database SHA `b9d7b9f1…` and the 3,250 / 3,996 counts are used consistently by other notes, for example `notes/Research/Kart Racing Restoration.md:95`.

**Corrections:**

1. `old:` Dialogue inconsistently calls it Spunky Scrapper Hammer. Preserve the inconsistency until client data resolves it.
   `new:` Dialogue inconsistently calls it Spunky Scrapper Hammer. The client locale resolves it: every client string uses "Spunky" (for example locale 4420071 "Forge a Spunky Scrapper Hammer" and 5100135), and "Funky" appears nowhere in the locale. Use Spunky; the wiki's "Funky" is a community error.
   `why:` the client_sql locale lookup, `locale` ids 4419855, 4420071, 5100135 (no match for "Funky Scrapper"); `repo:scripts/prepare-opening-content.py:139` and `repo:notes/Build Guides/Content/NPCs/NPCs - Farnum Farmstead.md:195` already use Spunky.

**Unsure:**
- The counts (3,198 main pages, 341 redirects, one empty page, 24 missing seeds, 174 API requests, 2,909 newline corrections, 16,171,008 bytes) and the "five search checks pass" result are not in the repo. The lab database and reports are outside Git, so I could not confirm them. `repo:scripts/wiki-research.py:293` does compute the redirect and empty counts. `repo:scripts/wiki-research.py:124` is the seed list, which holds 45 entries. The 24 missing-seed figure cannot be recomputed from the code alone.
- The crafting probe (`lab/reports/opening-crafting-wiki-probe.json`) is not in the repo. `repo:notes/Build Guides/Content/Jobs/Adventurer.md:73` ("page absent from the corpus") is consistent with it.
- The absolute path `C:\Users\Bryce\...` cannot be checked from the repo. `notes/Research/original-quest-coverage.json:56` uses the same CartoonMMO root.
