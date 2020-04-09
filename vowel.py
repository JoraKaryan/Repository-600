
#1.1

def vowel(str1):
	collect = " "
	for i in str1:
		if i in "aeiouAEIOU":
			collect += i
	mystring = " "
	for i in str1:
		if i in "aeiouAEIOU":
			mystring += collect[-1]
			collect = collect[:-1]
		else:
			mystring += i
	return mystring
print(vowel("abc"))
print(vowel("aec"))
print(vowel("america"))

