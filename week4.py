###Introduction to variables

###
intvariable1 = 1
intvariable2 = -3

floatvariable1 = 1.0
floatvariable2 = 3.1415

print(intvariable1+intvariable2) #addition
#Output: -2
print(intvariable1-intvariable2) #subtraction
#Output: 4
print(intvariable1*intvariable2) #multiplication
#Output: -3
print(intvariable1/intvariable2) #division
#Output: -0.3333333333333333
print(intvariable1%intvariable2) #modulus (remainder)
#Output: -2


print()


print(floatvariable1+floatvariable2) #addition
#Output: 4.1415
print(floatvariable1-floatvariable2) #subtraction
#Output:-2.1415
print(floatvariable1*floatvariable2) #multiplication
#Output:3.1415
print(floatvariable1/floatvariable2) #division
#Output:0.31831927423205475
print(floatvariable1%floatvariable2) #modulus (remainder)
#Output:1.0


print()

print(floatvariable1+intvariable2) #addition
#Output: -2.0
print(floatvariable1-intvariable2) #subtraction
#Output: 4.0
print(floatvariable1*intvariable2) #multiplication
#Output: -3.0
print(floatvariable1/intvariable2) #division
#Output: -0.3333333333333333
print(floatvariable1%intvariable2) #modulus (remainder)
#Output: -2.0


print()

#Casting
print(int(2.6))
#Output: 2
#IMPORTANT: Chops off decimal place, it does not round the number
print(float(2))
#Output: 2.0


print()

###Strings

hello = "Hello"
world = "world"
goodbye = "goodbye"

concat = hello+world+goodbye
print(concat) #Output: Helloworldgoodbye

concat = hello + " " + world + "" + goodbye
print(concat) #Output: Hello worldgoodbye

newstr = hello*2+" "+world*3
print(newstr) #Output: HelloHello worldworldworld

newstr = (hello*2+" "+world*3).upper()
print(newstr) #Output: HELLOHELLO WORLDWORLDWORLD

newstr = (hello*2+" "+world*3).lower()
print(newstr) #Output: hellohello worldworldworld

#remember, the first index in a string starts with 0 not 1!
#This gets confusing, make sure you remember!

print()

string = "This is a very long string"
print(string)

newstr = string[0]
print(newstr) #Output: T


newstr = string[0:7]
print(newstr) #Output: This is

newstr = string[1:5]*2
print(newstr) #Output: his[space]his[space]

newstr = string[0:8:2] #same as for loop! Initial, final (not included), step
print(newstr) #Output: Ti s

newstr = string[-1]
print(newstr) #Output: g

newstr = string[-2]
print(newstr) #Output: n

newstr = string[:4] ###First 4 characters
print(newstr)

newstr = string[5:] ###From the 5th character onwards
print(newstr)

newstr = string[-5:] ###Last 5 characters
print(newstr)

newstr = string[::5] ##steps by 5 character
print(newstr)

newstr = string[::-1] #reverse
print(newstr)

newstr = string[:]
print(newstr)
