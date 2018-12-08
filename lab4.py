
g={}
g[1]=[3,4]
g[2]=[1,4]
g[3]=[]
g[4]=[3]

n=int(input('enter the node:'))

for k in g.keys():
    if n in g[k]:
        print(k)

ind=0
for k in g.keys():
  if n in g[k]:
     ind+=1
print(ind)
print(len(g[n]))

