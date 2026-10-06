import json
from pathlib import Path
ROOT=Path(__file__).parent
SRC=ROOT/'src'/'SurvivalZomboid'/'scripts'/'generated'
SRC.mkdir(parents=True, exist_ok=True)

def lua(v, indent=0):
    if v is None: return 'nil'
    if v is True: return 'true'
    if v is False: return 'false'
    if isinstance(v,(int,float)): return repr(v)
    if isinstance(v,str): return json.dumps(v)
    if isinstance(v,list):
        return '{' + ', '.join(lua(x, indent+1) for x in v) + '}'
    if isinstance(v,dict):
        parts=[]
        for k,val in v.items():
            key=k if k.isidentifier() else '['+json.dumps(k)+']'
            parts.append(f'{key} = {lua(val, indent+1)}')
        return '{' + ', '.join(parts) + '}'
    raise TypeError(v)

for name in ['systems','items','infection','enemies','scavenge','hooks']:
    rows=json.loads((ROOT/'sheets'/f'{name}.json').read_text())
    if name in ('systems','items','enemies','scavenge','hooks'):
        body='{\n' + ''.join(f'  [{json.dumps(r["id"])}] = {lua(r)},\n' for r in rows) + '}'
    else:
        body=lua(rows)
    (SRC/f'{name}.lua').write_text('return '+body+'\n')
    print('generated', SRC/f'{name}.lua')
