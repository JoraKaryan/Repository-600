# PRACTIC-01

# N1

def vowel(x):
	collect = " "
	for i in x:
		if i in "aeiouAEIOU":
			collect += i
	mystring = " "
	for i in x:
		if i in "aeiouAEIOU":
			mystring += collect[-1]
			collect = collect[:-1]
		else:
			mystring += i
	return mystring
print(vowel("abc"))
print(vowel("aca"))
print(vowel("EAS"))


# N2 (arayjm chem stanum)

# N3

l = [101, 110, 11, 111]


def foo(n):
    n = list(str(n))
    l =[]
    for i in range(len(n)):
        if n[i] not in l:
            l.append(n[i])
    return l



ll = []
for i in range(len(l)):
    if len(foo(l[i])) == len(str(l[i])):
        ll.append(l[i])
if ll == []:
    print(-1)
else:
    print(ll[0])

    
# N4.1

num = int(input("type..."))


def factorial(n):
    fact = 1
    for i in range(1, n+1):
        fact = fact * i
    return fact
print(factorial(num))

# N4.2

num = int(input("type..."))


def factorial(n):
    if n == 0:
        return 1
    else:
        return n * factorial(n-1)
print(factorial(num))


# N5

def factorial(n):
    fact = 1
    for i in range(1, n+1):
        fact = fact * i
    return fact


def foo(num):
    l = []
    if num == 0:
        return 1
    for i in range(0, num):
        if (factorial(num - i)) < num:
            l.append(factorial(num - i + 1))
            return l[0]

print(foo(int(input("type..."))))

# N6

a = "abc"
b = "befca"     


def foo(a,b):
    l=[]
    for i in a:
        for j in b:
            if j in a:
                l.append(j * (a.count(j)))

    minimum=min(len(a),len(b))
    u=(l[ : minimum])

    s=""
    for i in range(len(u)):
        s= s + str(u[i])
    return s
print(foo(a,b))

# N7

a = [1, 2, 3]
b = [2, 3, 1]


def foo(a, b):
    for i in range(len(a)):
        if not a[i] in b:
            return False
    str_a = ""
    str_b = ""
    for i in a:
        str_a += str(i)
    for i in b:
        str_b += str(i)
    if str_a in 2 * str_b:
        return True
    return False
print (foo(a, b))

# N8

a = [5, 5, 5]


def max2(l):
    if len(l) > 1:
        l = sorted(l, reverse = True)
        for i in l:
           return l[1]
    return 0.5
print(max2(a))
