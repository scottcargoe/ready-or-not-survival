# Next host probe

The next step must run against the user's installed Ready or Not build.

We need to capture only the reflected names needed for v0.1:
1. local player pawn/controller class;
2. player damage/health functions or properties;
3. interactable/searchable container classes;
4. mission start/end or map transition events for persistence;
5. AI pawn classes suitable for an infected archetype;
6. replicated player/session identifiers needed to keep survival state consistent in co-op.

Preferred method: use the UE4SS development build's custom Lua binding dump and Live Property Viewer while Ready or Not is running. Do not ship generated bindings or game-owned code/assets.
