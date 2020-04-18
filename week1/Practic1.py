#3

l = [False]

def quick_or(l):
    x=[False for i in range(len(l))]
    return x==l

print(quick_or(l))

#5

def last_digit(n):
    s=[x**2 for x in range(1,n+1)]
    d=0
    for i in s:
        d = d+i
    return d%10
print(last_digit(950))









