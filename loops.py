# loop over an array
fruits = [ 'a', 'b', 'c']

# loop through each element
# at each stage, if the element is "c"
# print true
for i in fruits :
    if i == 'c':
        print('True')
    if i =='b':
        print('True from b')



# iterate over a string
greeting = "Hello"
for char in greeting :
    print(char)
    #check id the string contain vowel

# iterate over a range
for i in range(20):
   # print(i) # output; 0 1 2 3 4 
   print(10)
   print(11)
   print(12)


#! while loops
# Basic while loops
count = 0
while count < 5:
    #print (count)
    count = count + 1 # Output: 0 1 2 3 4

# user input string is unkmown
# print every char of the string
s = 'hey you'

counter = 0
length_s = len(s)
print('counter:', counter)
print('len s:', length_s)
 # 0, 1, 2, 3
print('going in loop')
while counter < length_s:
    print('counter:', counter)
    char = s[counter]
    print(char)
    counter = counter + 1
    print('------')