string=input("input a string")
vowels={'a,e,i,o,u'}
d={'a':0,'e':0,'i':0,'o':0,'u':0}

for i in string:
    if i in vowels:
        d[i]+=1
print(d)