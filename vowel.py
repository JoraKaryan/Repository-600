
#1.1

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
print(vowel("aec"))
print(vowel("america"))

