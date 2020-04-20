#ex-1

def all_positive(*args):
    return sorted(args)[0]<0

print (all_positive(7,2,6,-3,10))

#ex-2

a = (1, 1, 1)
def xor_3(a):
    if a.count(1) == 2 or a.count(1) == 0:
        return False
    return True             #True --> 111, 100, 010, 001
print(xor_3(a))               #False -->> 101, 110, 000

#ex-3

a = "Hello"

def mirror_string(a):
    b = []
    B = []
    num = []
    for i in a:
        if i.isalpha() and i.islower():
            b.append(ord(i))
        if i.isalpha() and i.isupper():
            B.append(ord(i))
        if not i.isalpha():
            num.append(i)

                                       

    c = ""
    C = ""
    num1 = ""
    for i in b:
        c = c +(chr((122 - i)+ 97))
    for i in B:
        C = C+(chr((90-i)+ 65))
    for i in num:
        if not i.isalpha():
            num1 = num1 + i
    
   
        
    for i in a:
        if i.isupper():
            a = a.replace(i, "*")
        if i.islower():
            a = a.replace(i, "-")


    u = ""
    for i in a:
        for j in range(len(c)):
            if i == "-":
                u = u + (c[j])
        for k in range(len(C)):
            if i == "*":
                u = u + (C[k])
        for m in num1:
            if not i.isalpha():
                u = u + m

    return u[:(len(a))]

print(mirror_string(a))


#ex-4

mylist = [22, 21, 20, 255]


def bit_concat(l):
    if l == []:
        return ("Your list is empty, Try again! ")
    while len(l) < 4:
        l.append(0)
    l = [bin(l[i])[2:] for i in range(len(l))]
    a0 = ("{:0>8}".format(str(l[3])))
    b0= ("{:0>8}".format(str(l[2])))
    c0 = ("{:0>8}".format(str(l[1])))
    d0 = ("{:0>8}".format(str(l[0])))
    x = (a0[0:2] + b0[2:4] + c0[4:6] + d0[6:8])
    return int(x, 2)

print(bit_concat(mylist))


#ex-5

a = "1"
b = "10"

binary_sum = lambda n: int(str(n), 2)
print(binary_sum(a) + binary_sum(b))


#ex-6

a = ["Vlad", "Nairi", "", "", "Aram"]

def only_names(a):
    for i in a:
        if i == 0:
            return False
        else:
            return True
        
print(list(filter(only_names, a)))


#ex-7

discriminant = lambda a,b,c: (b**2)-4*a*c
print(discriminant(4,8,0))

#ex-8

a = ["Vlad", "Nairi"]
b = ["Poghosyan", "Hakobyan"]


full_name = lambda l1, l2: l1 + l2
print(list(map(full_name, a,b)))



