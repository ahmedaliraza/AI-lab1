s= input("input a string")
d=I=0
for c in s:
    if c.isdigit():
        d=d+1
    elif c.isalpha():
        I=I+1
else:
    pass
print("Letters", 1)
print("digits", d)