local State = {}

function State.new(systems)
    local s = { values = {}, inventory = {}, stash = {}, elapsed = 0 }
    for id, cfg in pairs(systems) do
        s.values[id] = cfg.start
    end
    return s
end

local function clamp(v, lo, hi)
    if v < lo then return lo end
    if v > hi then return hi end
    return v
end

function State.add(state, systems, id, amount)
    local cfg = systems[id]
    if not cfg then return false, "unknown system: " .. tostring(id) end
    state.values[id] = clamp((state.values[id] or cfg.start) + amount, cfg.min, cfg.max)
    return true
end

function State.tick(state, systems, infectionStages, dtSeconds)
    local minutes = dtSeconds / 60.0
    state.elapsed = state.elapsed + dtSeconds

    for id, cfg in pairs(systems) do
        if cfg.decay_per_min > 0 then
            State.add(state, systems, id, -cfg.decay_per_min * minutes)
        end
    end

    local starvationDamage = 0
    for _, id in ipairs({"hunger", "thirst"}) do
        local cfg = systems[id]
        if cfg and state.values[id] <= cfg.critical_threshold then
            starvationDamage = starvationDamage + cfg.health_damage_per_min * minutes
        end
    end

    local infection = state.values.infection or 0
    local infectionDamage = 0
    for _, stage in ipairs(infectionStages) do
        if infection >= stage.min_value and infection <= stage.max_value then
            infectionDamage = stage.health_drain_per_min * minutes
            break
        end
    end

    if starvationDamage + infectionDamage > 0 then
        State.add(state, systems, "health", -(starvationDamage + infectionDamage))
    end
end

return State
