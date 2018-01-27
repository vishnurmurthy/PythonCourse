####Nested for loops
for i in range(0,5):
	for j in range(0,5):
		print(i, j)

'''Output:
0 0
0 1
0 2
0 3
0 4
1 0
1 1
1 2
1 3
1 4
2 0
2 1
2 2
2 3
2 4
3 0
3 1
3 2
3 3
3 4
4 0
4 1
4 2
4 3
4 4'''

print()

for abc in range(1,4):
	for bcd in range(2,5):
		print(abc, bcd)

'''Output:
1 2
1 3
1 4
2 2
2 3
2 4
3 2
3 3
3 4'''

print()

for x in range(3,6):
	for y in range(4,6):
		print(x*y)

#What do you think the output for this is?

print()
#While loops

xyz = True
counter = 0

while (xyz==True): #while the variable xyz is true
	print(xyz) #print xyz
	counter+=1 #Increase counter by 1
	if counter==5: #If counter is 5
		xyz = False #Set xyz to False


print()

#### Functions
def func(variable1, variable2):
	return variable1*variable2

output = func(4,5)
print(output)

print()

for c in range(4,1,-1):
	for d in range(9,3,-2):
		output = func(c,d)
		print(output)

#What should this output be






