thislist = ["apple", "banana", "cherry"]
print(thislist)



thislist = ["apple", "banana", "cherry", "apple", "cherry"]
print(thislist)


thislist = ["apple", "banana", "cherry"]
print(len(thislist))


list1 = ["apple", "banana", "cherry"]
list2 = [1, 5, 7, 9, 3]
list3 = [True, False, False]
print(list1)
print(list2)
print(list3)


list1 = ["abc", 34, True, 40, "male"]
print(list1)

thislist = list(("apple", "banana", "cherry")) # note the double round-brackets
print(thislist)

thislist = ["apple", "banana", "cherry"]
print(thislist[1])

thislist = ["apple", "banana", "cherry"]
print(thislist[-1])

thislist = ["apple", "banana", "cherry", "orange", "kiwi", "melon", "mango"]
print(thislist[0:2])


#Binaray type data
shoaib = [1,2,3,4,5,6,7,8,9,121,255]
b = bytes(shoaib)
print(b)

#binary type data byteArray
Shoaib = [1,2,3,4,5,6,7,8,9,121,255]
b1 = bytearray(Shoaib)
b1[5] = 50
print(b1[5])


# none type data
x = None
print(type(x))

#list type data

list = ['shoaib','khalid','miskat','jesan']
print(list)
print(type(list))

#tuple type data

tup = (3,45,5,6,67,7)
print(tup)
print(type(tup))

#range type

ran = range(6)
for i in ran:
    print(i)



print("Compiler Error")

























