import numpy as np

#ex-01
def all_replace(l):
    l[l % 2 ==1] =0
    return l
print(all_replace(np.array([1,2,-3,-4,5,6,7,8])))

#ex-02
def all_replace_where(l):
    return np.where(l % 2 == 0, 0, l)
print(all_replace_where(np.array([1,5,8,4,9,6])))

#ex-03
def arr_repeat(a):
    a = np.concatenate((a,a,a))
    b = np.array([])
    for i in a:
        b = np.append(b, i)
    b = np.sort(b)
    return b
print(arr_repeat(np.array([1,2,3])))

#ex-04
def arr_join(a):
    return np.concatenate((a,a,a))
print(arr_join([1,2,3]))

#ex-05
def arr_intersection(a,b):
    return np.intersect1d(a,b)
print(arr_intersection(np.array([1,1,2]),np.array([2,1,1])))

#ex-06
def arr_random(rows, cols):
    matrix = np.random.random((rows,cols))+5
    return matrix

print(arr_random(6,1))
