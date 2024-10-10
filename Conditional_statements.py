#if statement
a = 33
b = 200
if b > a:
  print("b is greater than a")    #b is greater than a

#Elif
a = 33
b = 33
if b > a:
  print("b is greater than a")
elif a == b:
  print("a and b are equal")    #a and b are equal

#Else
a = 200
b = 33
if b > a:
  print("b is greater than a")
elif a == b:
  print("a and b are equal")
else:
  print("a is greater than b")    #a is greater than b


#Nested If
x = 41

if x > 10:
  print("Above ten,")
  if x > 20:
    print("and also above 20!")
  else:
    print("but not above 20.")      #Above ten,and also above 20!
