 # creation of array

array1 = [1,2,3, "Thimphu", 2.5]

# retrieving
element1 = array1[0]
element2 = array1[4]

last_element = array1[-1]
print(last_element)

# modifying element
array1[0] = 10
print(array1)

# getting number of element in an array
no_of_element  = len(arrray1)

# slicing
elements = array1[0:2]
print(elements)

# print(elements)
arr1 = [1, 10]
arr2 = ['thimphu','sarpang' ]
number_to_check = '1'
result = number_to_check in arr1

arr3 = arr2 + arr1
print(arr3)

# append(adding)
arrVariable = [1,2,3]
arrVariable.append(4) #[1,2,3,4]


# insert
arrVariable.insert(1,10) # [1,10,3,4]
arrVariable.sort()
print(arrVariable)

stackVar = []
# adding to stack
stackVar.append(4)
stackVar.append(2)
stackVar.append(9)
stackVar.append(1) # 4, 2, 9, 1
print ('after appending', stackVar)
element = stackVar.pop()
print('After poping', stackVar)
print('removed element : ', element)
