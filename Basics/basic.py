a = 2
b = " Hello, World, Go"


# print(b.replace('l', 'z'))

# split = b.split(',')
# print(len(split))

# age = 36
# txt = "My name is Jhon, I am {}" 
# print(txt.format(age))


myTuple = tuple(('apple', 'banana', 'orange', 'cherry'));

# for x in myTuple:
#     print(x)
# for i in range(len(myTuple)):
#     print(myTuple[i])

# Comprehention
# newList = []
# for x in myTuple:
#     if "a" in x:
#         newList.append(x)

# print(newList)

#object/set

newSet = [
    { 
        'name': "Mr Jhon",
        'age': 32,
        'natinality': "USA"
    },
    {
        'name': "Mr Smith",
        'age': 25,
        'natinality': "UK"
    },
   
]

for dic in newSet:
   print(dic.get('name'))








