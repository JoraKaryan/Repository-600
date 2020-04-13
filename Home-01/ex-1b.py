#ex-1b

l = [[2, 58, 9, 4, 6, 1, 2, 2, 1],[5, 6]]
n = [5, 6]
while n in l:
        x = [l.remove(i) for i in l if i == n]
print(l)
