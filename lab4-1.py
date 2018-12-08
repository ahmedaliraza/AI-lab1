Stack={}
def push(s,e):
if e in s:return
s.insert(0,e)
return s

def pop(s):
    if(len(s)==0):
        return null
    else:
        return s.pop(0)

    def empty(s):
        return len(s)==0
push(stack,1)


while  empty(stack)==False:
    e=pop(stack)
    print(e)
    for k in g[e]:
        push(stack,k)