# PYTHON STRING
# BESIDES NUMBERS, PYTHON CAN ALSO MANUPULATE STRINGS, WHICH CCAN BE EPRESSED IN SEVERAL WAYS. THEY CAN BE ENCLODES IN SINGLE QUOTES OR DOUBLE QUOTES WITH THE SAME RESULT
#\ CAN BE USED TO ESCAPE QUOTES

print('spam eggs') # single quotes 
#spam eggs

print('doesn\'t') # use \' to escape the single quote
#doesn't

print("doesn't") # or use double quotes instead
#doesn't

# IIF YOU WANT TO CONCATENATE VARIABLES OR A VARIABLE AND A LITER ,USE +

prefix = 'py'
print(prefix + 'thon123')

# STRINGS CAN BE INDEXED (SUBSCRIPTED), WITH THE FIRST CHARACTER HAVE INDEX 0. THERE IS NO SEPERATE CHARACTER TYPE; A CHARACTER IS SIMPLY A STRING OF SIZE ONE

word = 'python'
print(word[0]) # character in position 0
#p
print(word[5]) # character in position 5
#n

#INDICIES MAY ALSO BE NEFATIVE NUMBERS, TO START COUNTING FROM THE RIGHT 

print(word[-1]) # last character
#n
print(word[-2]) # second to last character
#o

# IN ADDITION TO INDEXING, SLICING IS ALSO SUPPORTED. WHILE INDEXING IS USED TO OBTAIN INDIVIDUAL CHARATERS, SLICING ALLOWS  YOU TO OBTAIN SUBSTRING

print(word[0:2]) # characters from position 0 (included) to 2 (excluded)
#py
print (word[2:5]) #characters fro position 2 (included) to 5 (exluded)
#tho

# SEE HOW THE START IS ALWAS INCLUDED AND THE END IS ALWAS EXCLUDED. THIS MAKES SURE THAT S[:I] + S[I:] IS ALWAYS EQUAL TO S

print(word[:2] + word[2:])
#python
print(word[:4] + word[4:])
#pyton

#SLICE INDICIES HAVE USEFUL DEFALUTS; AN OMITTED FIRST INDEX DEFAULTS TO ZERO, AN OMITTED SECOND INDEX DEFAULTS TO THE SIZE OF THE STRING BEING SLICED.

print(word[:2]) # character fro mthe befinnin to position 2 (excluded)
#py

print(word[4:]) # characters form position 4 (included) to the end
#on

print(word[-2:]) # characters form the second-last (inculded) to the end 
#on