#! string manipulation 
# !sting concatenation



string1 = " hello "
string2 = " Nima"

combined = string1 + string2
combined1 = "hi" + ""+ "there"
print('string Concatenation')
print(combined)
print(combined1)

# ! string interpolation
print('string Interpolation')
#! how do you print "john is 30 years of age"
name = "John"
age = 99
interolated: str = f"John is {age} years of age"
print(interolated)

#! string methods
print('string Methods')
## ! upper
print('string upper')
stringLower = 'hellow how are you?'
converted = stringLower.upper()
converted1 = "pure string".upper()

#! Lower
print('string lower')
lower = "HELLO".lower()
print(lower)

#! capitalize
print('string capitalize')
capitalize = "hello there".capitalize()
print(capitalize)