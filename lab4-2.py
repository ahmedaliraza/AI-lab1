queue={}
def enqueue(q,e):
if e in s:return
s.insert(0,e)
return s

def dequeue(q):
if(len(q)==0):
 return null
else:
 return q.pop(0)

def empty(q):
 return len(q)==0

enqueue(Queue,1)

output=[]
while  empty(Queue)==False:
    e=dequeue(Queue)
    if e in output: continue
    output.append(e)
    for k in g[e]:
        enqueue(queue,k)
print(queue)