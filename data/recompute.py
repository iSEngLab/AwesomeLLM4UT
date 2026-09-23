"""Recompute descriptive distributions from studies.csv; Python 3, no dependencies."""
import csv, re
from pathlib import Path
from collections import defaultdict

ROOT=Path(__file__).resolve().parent
with (ROOT/'studies.csv').open(encoding='utf-8-sig',newline='') as f: studies=list(csv.DictReader(f))
assert len(studies)==len({r['study_id'] for r in studies})
def tokens(s):
    return {v.strip() for v in re.split(r'[;\uFF1B\n]',s or '') if v.strip()}
dimensions=[('year','publication_year',False),('venue','venue',False),('ccf','ccf_2026',False),('language','languages',True),('task','tasks',True),('study_type','study_types',True),('model','models',True),('strategy','strategies',True),('strategy_parent','strategy_parents',True),('integrated_technique','integrated_techniques',True),('generation_metric','generation_metrics',True),('code_availability','code_availability_group',False),('model_family','models',True)]
summary=[]; members=[]
for dim,field,multi in dimensions:
    population=[r for r in studies if dim!='generation_metric' or 'Test Generation' in tokens(r['tasks'])]
    groups=defaultdict(set)
    for r in population:
        labs=tokens(r[field]) if multi else {r[field].strip()} if r[field].strip() else set()
        if dim=='model_family': labs={f for f in ['Claude','Gemini','Phi','Gemma'] if any(v.lower().startswith(f.lower()) for v in labs)}
        for label in labs: groups[label].add(r['study_id'])
    total=sum(map(len,groups.values()))
    for label,ids in sorted(groups.items(),key=lambda kv:(-len(kv[1]),kv[0])):
        n=len(ids);summary.append([dim,label,n,len(population),n/len(population),total,n/total])
        members.extend([dim,label,i] for i in sorted(ids))
for name,header,data in [('statistics.csv',['dimension','category','study_count','study_denominator','study_fraction','label_assignment_denominator','assignment_fraction'],summary),('memberships.csv',['dimension','category','study_id'],members)]:
    with (ROOT/name).open('w',encoding='utf-8-sig',newline='') as f:
        writer=csv.writer(f);writer.writerow(header);writer.writerows(data)
print(f'Recomputed {len(summary)} category rows from {len(studies)} studies.')
