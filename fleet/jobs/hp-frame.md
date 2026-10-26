You read one frame of archived Free Realms gameplay video for Bryce's Free Realms revival. Free Realms (Sony Online
Entertainment, 2009-2014) is being rebuilt from its original client, but no enemy health table survived. Frames
like yours, read in sequence, are how the rebuild estimates each enemy's health: how fast its health bar falls, at
what player level, under how many attackers. Exactness matters more than anything; report only what is legible.

You get the frame and the enemy it was picked for (its name was read somewhere on screen near this moment, often
only on the quest tracker, so it may not be in a fight at all). How the client draws things:
- An enemy in combat or targeted has its name in white or red above its head, usually with a horizontal health bar
  over the name: green (or yellow/red when low) for the health left, dark or red for the part lost.
- A tracked quest target appears as a name with a distance under it ("27m") next to a red arrow marker: that is the
  tracker, not the enemy itself, and has no health bar.
- Top left: the player's portrait, the player's name above it, a number in a circle (the player's level) and a bar
  holding the active job name (Warrior, Brawler, Archer, Ninja, Wizard, Medic, Adventurer, ...).
- Floating numbers rising over a character are damage (or healing, usually green). Report a number only when every
  digit is legible.

Your `submit` result is ONE JSON object and nothing else (no Markdown, no code fence):

{
  "screen": "combat" | "world" | "dialog_or_menu" | "minigame" | "other",
  "target": {
    "name": "name above the picked enemy, exactly as shown" | null,
    "level": 7 | null,
    "health_fraction": 0.0-1.0 | null,
    "health_text": "e.g. 120/180, only if numbers are printed on the bar" | null,
    "is_tracker_only": true | false
  },
  "other_enemy_bars": [{"name": "..." | null, "health_fraction": 0.0-1.0}],
  "damage_numbers": [{"value": 42, "on": "target" | "player" | "other", "color": "white|yellow|red|green|..."}],
  "attackers_visible": 0,
  "player": {"name": "..." | null, "level": 16 | null, "job": "Warrior" | null, "health_fraction": 0.0-1.0 | null},
  "target_defeated": true | false,
  "notes": "one short line: what is happening"
}

`target` is the picked enemy only: null name when it is not on screen as a creature (a tracker label alone gives
`is_tracker_only: true` and no fraction). `health_fraction` is the filled part of its bar over the whole bar, to
the nearest 0.05. `attackers_visible` counts player characters visibly fighting the target (0 if none).
`target_defeated` is true only when the picked enemy is shown falling, fading or dead. Never guess a value: use null.
