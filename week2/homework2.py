
#ex-01

def bisect_position(l,a):
    for i in range(len(l)):
        if l[i] >= a:
            return i
        if a > max(l):
            return len(l)

print(bisect_position([1,2,3,6],3))

#ex-02

def all_sums(n):
    l = list(range(1,n+1))
    left = l[:(n+1)//2]
    right = l[(n+1)//2:]
    right == right.reverse()
    my_list = []
    dictionary = dict(zip(left, right))

    return [(k, v) for k, v in dictionary.items()]
    
print(all_sums(7))

# ex-03

from collections import defaultdict

def duplicate_characdeters (string):
    my_set = set()
    d_d = defaultdict(int)
    for i in string:
        d_d[i] = d_d[i]+1
    for i in d_d:
        if d_d[i] > 1 and i!=" ":
            my_set == my_set.add(i)
    return my_set
print(duplicate_characdeters ("Here we have some duplicates"))



#ex-04  with merge_sorting

def merge(l1, l2):
    l = []
    i, j = 0, 0
    while i < len(l1) and j < len(l2):
        if l1[i] < l2[j]:
            l.append(l1[i])
            i += 1
        else:
            l.append(l2[j])
            j += 1
    l.extend(l1[i:])
    l.extend(l2[j:])
    return l

def merge_sort(l, start, end):
    if start == end-1:
        return [l[start]]
    mid = (start + end) // 2
    return merge(merge_sort(l, start, mid), merge_sort(l, mid, end))
  
def compare_lists(a,b):
    if merge_sort(a, 0, len(a)) == merge_sort(b, 0, len(b)):
        return True
    return False
print(compare_lists([1,1,5,2,6,5,2],[5,2,6,5,2,1,1]))


#ex-05

def heapq(l,a):
    for i in range(len(l)):
        if l[i] >= a:
            l.insert(i,a)
            return l
        if a > max(l):
            l.append(a)
            return l

print(heapq([1,3,5,7,9],2))


#ex-06   with bubble sorting

def sort_list(li, order):
    swapped = True
    while swapped:
        swapped = False
        for i in range(0, len(li)-1):
            if li[i] > li[i+1]:
                swapped = True
                li[i], li[i+1] = li[i+1], li[i]

    if order == 'ascending':
        return li

    if order == 'descending':
        return li[::-1]
    
print (sort_list([1,4,3,2],'descending'))











'''
















