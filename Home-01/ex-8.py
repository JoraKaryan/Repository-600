#ex-8

mylist = [1,2,3,5,6,7,8]
def foo(l):
    for i in l:
        if l[i+1] != l[i]+1:
            return l[i]+1
        if l[i+1] == l[i]+1:
            return l[-1]+1
    if len(l) == 0:
        return 1
print(foo(mylist))
