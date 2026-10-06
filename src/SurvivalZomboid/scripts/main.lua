print("[SurvivalZomboid] v0.1 foundation loaded\n")

local Systems = require("generated.systems")
local Items = require("generated.items")
local Infection = require("generated.infection")
local Scavenge = require("generated.scavenge")
local Enemies = require("generated.enemies")
local Hooks = require("generated.hooks")
local State = require("state")

local Runtime = {
    state = State.new(Systems),
    systems = Systems,
    items = Items,
    infection = Infection,
    scavenge = Scavenge,
    enemies = Enemies,
    hooks = Hooks
}

-- Ready or Not-specific UObject bindings are intentionally not guessed here.
-- The adapter is attached only after inspecting the installed game's bindings.
_G.SurvivalZomboidRuntime = Runtime

print("[SurvivalZomboid] survival runtime initialized; waiting for Ready or Not adapter\n")
