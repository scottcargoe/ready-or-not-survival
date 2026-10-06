import json, sys
from pathlib import Path
ROOT=Path(__file__).parent
S=ROOT/'sheets'
files=['systems','items','infection','enemies','scavenge','hooks']
data={n:json.loads((S/f'{n}.json').read_text()) for n in files}
errors=[]
for n, rows in data.items():
    for i,row in enumerate(rows):
        for k,v in row.items():
            if v is None or v=='': errors.append(f'{n}[{i}].{k}: blank')
        if 'id' not in row: errors.append(f'{n}[{i}]: missing id')
ids={n:{r['id'] for r in rows} for n,rows in data.items()}
# reference checks
for i,r in enumerate(data['items']):
    for k in ('effect_system','secondary_system'):
        if r[k] not in ids['systems']: errors.append(f'items[{i}].{k}: unresolved {r[k]}')
for i,r in enumerate(data['enemies']):
    if r['loot_table'] not in ids['scavenge']: errors.append(f'enemies[{i}].loot_table: unresolved {r["loot_table"]}')
for i,r in enumerate(data['scavenge']):
    for j,e in enumerate(r['entries']):
        if e.get('item') not in ids['items']: errors.append(f'scavenge[{i}].entries[{j}].item: unresolved {e.get("item")}')
        if not isinstance(e.get('weight'), (int,float)) or e['weight'] <= 0: errors.append(f'scavenge[{i}].entries[{j}].weight: invalid')
for i,r in enumerate(data['hooks']):
    if r['required'] and not r['implemented']: errors.append(f'hooks[{i}] required but not implemented')
# infection coverage and ordering
stages=sorted(data['infection'], key=lambda r:r['min_value'])
if stages[0]['min_value'] != 0 or stages[-1]['max_value'] != 100: errors.append('infection stages must cover 0..100')
for a,b in zip(stages, stages[1:]):
    if round(a['max_value']+0.01,2) != round(b['min_value'],2): errors.append(f'infection gap/overlap: {a["id"]}->{b["id"]}')
if errors:
    print('PREFLIGHT FAILED')
    for e in errors: print(' -',e)
    sys.exit(1)
print('PREFLIGHT CLEAN')
for n in files: print(f' - {n}: {len(data[n])} rows')
