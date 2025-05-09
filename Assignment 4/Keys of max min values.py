d={'a':10,'b':20,'c':5}
vals=[]
for k in d:
 vals.append(d[k])
mx=max(vals)
mn=min(vals)
for k in d:
 if d[k]==mx:
  print("Key with max value:",k)
  break
for k in d:
 if d[k]==mn:
  print("Key with min value:",k)
  break
