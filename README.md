# SurvivalZomboid for Ready or Not

A first-person survival mashup concept: Project Zomboid-style hunger, thirst, persistent injuries, scavenging and infection layered onto Ready or Not's movement, combat and physics.

## v0.1 target
Start in a fortified police-station safehouse, choose scarce equipment, scavenge for supplies, fight infected, risk infection, and return supplies to a persistent stash. The same survival rules are intended for solo and co-op.

## Architecture
- `sheets/` is the source of truth.
- `preflight.py` rejects blank cells and broken references.
- `generate.py` converts every sheet row into a Lua data record.
- `src/SurvivalZomboid/` is the UE4SS Lua mod payload.

## Current state
The data/runtime foundation is locally generated and model-tested. It is **not yet a playable Ready or Not build** because the exact game UObject hooks have not been inspected against the user's installed game. See `docs/STATUS.md`.
