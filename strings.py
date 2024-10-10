print("It's alright")   #It's alright

a = "Hello"
print(a)   #Hello

#Multiline Strings
a = '''Lorem ipsum dolor sit amet,
consectetur adipiscing elit,
sed do eiusmod tempor incididunt
ut labore et dolore magna aliqua.'''
print(a)

#Strings are Arrays
a = "Hello, World!"
print(a[1])  #e

#String Length
a = "Hello, World!"
print(len(a))  #13

#Slicing Strings
b = "Hello, World!"
print(b[2:5])  #llo

#Slice From the Start
b = "Hello, World!"
print(b[:5])  #Hell

#Slice To the End
b = "Hello, World!"
print(b[2:])  #llo, World!


#Upper Case
#Lower Case
a = "Hello, World!"
print(a.upper())  #HELLO, WORLD!
print(a.lower())  #hello, world!

#Replace String
a = "Hello, World!"
print(a.replace("H", "J"))  #Jello, World!

#Split String
a = "Hello, World!"
print(a.split(",")) # returns ['Hello', ' World!']

#String Concatenation
a = "Hello"
b = "World"
c = a + b
print(c)  #HelloWorld

a = "Hello"
b = "World"
c = a + " " + b
print(c)  #Hello World




