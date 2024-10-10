thislist = ["apple", "banana", "cherry"]
print(thislist)  #['apple', 'banana', 'cherry']


#Allow Duplicates
thislist = ["apple", "banana", "cherry", "apple", "cherry"]
print(thislist)  #["apple", "banana", "cherry", "apple", "cherry"]

#List Length
thislist = ["apple", "banana", "cherry"]
print(len(thislist))  #3

#Access
thislist = ["apple", "banana", "cherry"]
print(thislist[1])  #banana

#Append Items
thislist = ["apple", "banana", "cherry"]
thislist.append("orange")
print(thislist)    #['apple', 'banana', 'cherry', 'orange']


#Remove List Items
thislist = ["apple", "banana", "cherry"]
thislist.remove("banana")
print(thislist)  #['apple', 'cherry']


#Sort Lists
thislist = ["orange", "mango", "kiwi", "pineapple", "banana"]
thislist.sort()
print(thislist)  #['banana', 'kiwi', 'mango', 'orange', 'pineapple']

#Join Two Lists
list1 = ["a", "b", "c"]
list2 = [1, 2, 3]

list3 = list1 + list2
print(list3)  #['a', 'b', 'c', 1, 2, 3]



