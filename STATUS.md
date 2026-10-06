# Status

## Implemented locally
- Project Zomboid-style survival data model for hunger, thirst, health and infection.
- Item effects, infected archetypes and weighted scavenging tables.
- UE4SS Lua mod layout (`SurvivalZomboid/scripts/main.lua`).
- Generated Lua data modules from JSON sheets.
- Preflight checks for blank cells and unresolved sheet references.

## Not yet verified in Ready or Not
- Exact Ready or Not UObject/class/function names.
- Player tick/damage hooks.
- Container interaction hook.
- Infected actor spawning/AI replacement.
- HUD presentation.
- Persistence between actual missions.
- Solo/co-op replication behavior.

These are intentionally not guessed. They require inspection of the installed Ready or Not build and UE4SS bindings.
