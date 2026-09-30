import csv,collections,sys
from datetime import datetime,timezone
rows=sorted(csv.DictReader(open(sys.argv[1] if len(sys.argv)>1 else "th.csv")),key=lambda r:r['timestamp_utc'])
op={};res=collections.defaultdict(list)
for r in rows:
    k=(r['source_id'],r['symbol'])
    if r['side']=='buy': op[k]=float(r['value'])
    elif k in op: res[r['source_id']].append(float(r['value'])-op.pop(k))
dep={'5917':'2026-09-30T01:06+00:00','5918':'2026-09-30T01:07+00:00','5912':'2026-09-29T23:40+00:00','5913':'2026-09-29T23:42+00:00','5915':'2026-09-29T23:55+00:00','5926':'2026-09-30T04:20+00:00','5927':'2026-09-30T04:20+00:00','5928':'2026-09-30T04:20+00:00','5925':'2026-09-30T03:55+00:00'}
now=datetime.now(timezone.utc)
for sid,p in sorted(res.items()):
    if sid not in dep: continue
    h=(now-datetime.fromisoformat(dep[sid])).total_seconds()/3600
    print(sid,f"n={len(p)} WR={sum(x>0 for x in p)/len(p):.0%} pnl=${sum(p):.2f} {len(p)/h:.1f}/hr")
