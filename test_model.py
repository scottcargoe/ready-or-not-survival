import json, random
from pathlib import Path
R=Path(__file__).parent
systems={r['id']:r for r in json.loads((R/'sheets/systems.json').read_text())}
stages=json.loads((R/'sheets/infection.json').read_text())
items={r['id']:r for r in json.loads((R/'sheets/items.json').read_text())}
loot={r['id']:r for r in json.loads((R/'sheets/scavenge.json').read_text())}

def clamp(v,c): return max(c['min'], min(c['max'],v))
def tick(s, seconds):
    mins=seconds/60
    for id,c in systems.items(): s[id]=clamp(s[id]-c['decay_per_min']*mins,c)
    dmg=sum(c['health_damage_per_min']*mins for id,c in systems.items() if id in ('hunger','thirst') and s[id] <= c['critical_threshold'])
    inf=s['infection']
    for st in stages:
        if st['min_value'] <= inf <= st['max_value']: dmg += st['health_drain_per_min']*mins; break
    s['health']=clamp(s['health']-dmg, systems['health'])

def use(s,item):
    i=items[item]
    s[i['effect_system']]=clamp(s[i['effect_system']]+i['effect_amount'], systems[i['effect_system']])
    s[i['secondary_system']]=clamp(s[i['secondary_system']]+i['secondary_amount'], systems[i['secondary_system']])

def roll(table,seed=7):
    random.seed(seed); t=loot[table]; out=[]
    entries=t['entries']; weights=[e['weight'] for e in entries]
    for _ in range(random.randint(t['rolls_min'],t['rolls_max'])): out.append(random.choices(entries,weights)[0]['item'])
    return out
s={k:v['start'] for k,v in systems.items()}
tick(s, 60*60)
assert 81 < s['hunger'] < 83, s
assert 66 < s['thirst'] < 68, s
s['thirst']=5; h=s['health']; tick(s,600); assert s['health'] < h
s['thirst']=20; use(s,'water_bottle'); assert s['thirst']==55
s['infection']=85; h=s['health']; tick(s,600); assert s['health'] < h
x=roll('police_locker'); assert 2 <= len(x) <= 4 and all(i in items for i in x)
print('MODEL TESTS PASSED')
print('sample police locker:', ', '.join(x))
print('state after tests:', s)
