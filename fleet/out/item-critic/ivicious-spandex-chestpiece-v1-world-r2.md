<!-- fleet job=item-critic id=ivicious-spandex-chestpiece-v1-world-r2 status=no_submit turns=3 usd=0.0021 tokens(read,write,in,out)=[12512, 9470, 8, 1508] model=claude-haiku-5-5 -->
# Vicious Spandex Chestpiece

{"lens": "world", "pass": true, "wireable": true, "score": 4, "problems": [{"field": "evidence[1] / marketplace detail", "issue": "The answer dates the event start to January 21, 2014, which is the item-page date. The HeroRealms Month page says the event began January 14, 2014. The two dates don't contradict each other, since an item can appear a week into an event, but the answer doesn't note the difference.", "fix": "Keep the item's January 21, 2014 introduction date, cite it to the item page, and note that the event began January 14, 2014 per the HeroRealms Month page."}]}

Checks that passed:
- The HeroRealms Month page lists "[Vicious]: [Boots], [Gloves], [Mask], [Spandex] [Chestpiece], [Spandex] Leggings" under the Station Cash Marketplace HeroRealms gearsets, so the event-page source is real.
- The item name matches locale 5103115 and the Vicious Spandex Leggings and Chestpiece entries are in the client table.
- The two Station Cash sources (99 regular, 89 members) match the wiki's numbers. The 89 is a member discount, not a separate sale, so the second price is not a second source.
- No coin, vendor, quest or drop source appears anywhere in the pack or the wiki for this item, so the single SC marketplace source is not padded.
- The retired field is null and live is "unsure". The categories have no retired marker, so the honest unknown fits.
