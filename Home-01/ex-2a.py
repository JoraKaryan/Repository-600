#ex-2a

mylist = [44, [5, 6], 4, [2, 58, 1], [5, 6], [5, 6], 4, 4, 4, 6]

del_dupl = []

for i in range(len(mylist)):
        if mylist[i] not in del_dupl:
                del_dupl.append(mylist[i])
print(del_dupl)
