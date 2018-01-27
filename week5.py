string = "abcdefdef"

print(" ".join(string)) #Joins space in between each letter of the string
#Output: a b c d e f d e f

print(" hello ".join(string)) #Joins space in between each letter of the string
#Output: a hello b hello c hello d hello e hello f hello d hello e hello f

print(string.replace("a","x")) 
#OUtput: xbcdefdef

print(string.replace("abc","x")) 
#OUtput: xdefdef

print(string.find("b")) #finds the first instance of b
#Output: 1

print(string.find("def")) #finds the FIRST instance of def
#Output: 3

print()

print("abc\ndef")
'''Output:
abc
def'''

print("abc\tdef")
'''Output:
abc      def'''

print()
for i in range(8):
	print(string[i:i+2])
'''Output:
ab
bc
cd
de
ef
fd
de
ef'''

print()
for i in range(9):
	print(string[i:i+4])
'''
abcd
bcde
cdef
defd
efde
fdef
def
ef
f
'''

