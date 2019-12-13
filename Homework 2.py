name = "angela"
surname = "asatryan"

# Capitalize the string's 1st chars
print(name.capitalize(), end=" ")
print(surname.capitalize())

# move the string to the center of sepcified width string
print(surname.center(100))

# count the specific chars in string
print(name.count("a"))
funny_facts = "1. There is a technical name for the fear of long words-it's called hippopotomonstrosesquippedaliophobia.\n2. Cows moo with regional accents."

# Whether string ends with defined string
result1 = funny_facts.endswith('called')
print(result1)
result2 = funny_facts.endswith('hippopotomonstrosesquippedaliophobia.')
print(result2)

# Whether string starts with defined string
result3 = funny_facts.startswith('called')
print(result3)
result4 = funny_facts.startswith('There')
print(result4)

#Expand tabs betwwen stings
print(funny_facts.expandtabs(   ))

#find the substring in the strings by find
print(funny_facts.find('tec'))
print(funny_facts.find('aaaa'))

#find the substring in the strings by index
print(funny_facts.index('tec'))
#print(funny_facts.index('aaaa'))

#find out if all the characters in the string are alphanumeric
print(funny_facts.isalnum())
print(name.isalnum())

#find out if all the characters in the string are alphabetic
print(funny_facts.isalpha())
print(name.isalpha())

even_numbers10=("1" "3" "5" "7")
#find out if all the characters in the string are digits
print(even_numbers10.isdigit())
print(name.isdigit())

#find out if all the characters in the string are lowercase
print(funny_facts.islower())
print(name.islower())

#find out if the string is titelcased
print(funny_facts.istitle())
print(name.istitle())

#find out if the string is uppercased
print(funny_facts.isupper())

#concatenate strings
print(even_numbers10.join(even_numbers10))

#add characters of specified width to the left side of the string
print(surname.ljust(15, '0'))

#change uppercases in string to lowercases
print(funny_facts.lower())

#remove leading characters
print(surname.lstrip('a'))

#replace the substrings with new ones
print(funny_facts.replace('for', 'AAAAAA', 2))

#find the substring and return the highest index in the string for that substring
print(funny_facts.rfind('for'))

#find the substring and return the highest index in the string for that substring, value error if not found
#print(funny_facts.rindex('aaa'))

#add characters of specified width to the right side of the string
print(name.rjust(8, '*'))

#split the substrings of the string
print(funny_facts.rsplit())

#remove characters from right side of the string
print(surname.rstrip('an'))

#split the substrings of the string
print(funny_facts.split())

#split the lines of the string
print(funny_facts.splitlines())

#whether string starts with given prefix
print(funny_facts.startswith('1'))

#remove characters from strings
print(name.strip('an'))

#change the upppercases of string to lowercases and vice versa
print(funny_facts.swapcase())

#make the string titelcased
name_surname=name+" " +surname
print(name_surname.title())

#translation table to use
input="ast"
output="275"
transtable=name_surname.maketrans(input, output)
#translate the string uusing predefined translation table
print(name_surname.translate(transtable))

#make the string uppercased
print(name_surname.upper())

#Return the numeric string left filled with zeros in a string of length width.
print(even_numbers10.zfill(100))

