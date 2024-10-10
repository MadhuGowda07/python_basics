thistuple = ("apple", "banana", "cherry")
print(thistuple)  #('apple', 'banana', 'cherry')

#Allow Duplicates
thistuple = ("apple", "banana", "cherry", "apple", "cherry")
print(thistuple)    #('apple', 'banana', 'cherry', 'apple', 'cherry')

#Tuple Length
thistuple = ("apple", "banana", "cherry")
print(len(thistuple))    #3

#Create Tuple With One Item
thistuple = ("apple",)
print(type(thistuple))    #<class 'tuple'>

#NOT a tuple
thistuple = ("apple")
print(type(thistuple))    #<class 'str'>

#A tuple can contain different data types
tuple1 = ("abc", 34, True, 40, "male")
