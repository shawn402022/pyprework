# PYTHON LIST
# PYTHON KNOWS A NUMBER OF COMPOUND DATA TYPES,. USED TO GROUP TOGETHER OTHER VALUES. THE MOST VERSATILE IS THE LIST, WHICH CAN BE WRITTEN AS A LIST OF COMMA-SEPERATED VALES(ITEMS)
# BETWEEN SQUARE BRAKETS. LISTS MIGHT CONTAIN ITEMS OF DIFFRENT TYPES, BUT USLALY THE ITEMS ALL HAVE THE SAME TYPES

squares = [1,2,3,4,5,]
print(squares)
# [1,2,3,4,5,]

# LIKE STRINGS (AND ALL TOHER BUILD-IN SEQUENCE TYPE), LISTS CAN BNE INDEXED AND SLICED

print(squares[0]) #indexing returns the item
#1
print(squares[-1])
#5
print(squares[-3:]) # slicing returns a new list
#[9,.16,25]

# LISTS ALSO SUPPORT OPERATIONS LIKE CONCATENATION

print(squares + [6,7,8])
#[1,2,3,4,5,6,7,8]

# UNLIKE STRINGS, WHICH ARE IMMUTABLE, LISTS ARE A MUTABLE TYPE i.e. IT IS POSSIBLE TO CHANGE THIER CONTENT

cubes = [1,8,27,65,125] # something is wrong here
print(4**3) #the cube of 4 is 54 not 65
#64

cubes[3] = 64 # replace the wrong value
print(cubes)
#[1,8,27,64,125]

#YOU CAN ALSO ADD NEW ITEMS AT THE END OF THE LIST, BY USING THE APPEND() METHOD ( WE SILL SEE MORE ABOUT METHODS LATER)

cubes.append(216) # add the cube of 6
cubes.append(7**3) # add the cube of 7
print(cubes)
#[1,8,27,64,125,216,343]

#ASSIGNMENT TO SLICES IS ALSO POSSIBLE, AND THIS CAN EVEN CHANGE THE SIZE OF THE LIST OR CLEAR IT ENTIRELY

letters = ['a', 'b', 'c', 'd', 'e', 'f', 'g']
print(letters)
# ['a', 'b', 'c', 'd', 'e', 'f', 'g']

letters[2:5] # replace some values
print(letters)
# ['a', 'b', 'c', 'd', 'e', 'f', 'g']

letters[2:5] = [] # remove vales
print(letters)
#['a', 'b', 'f', 'g']

letters [:] - [] # clear the list by replacing all the elements with an empty list
print(letters)
#[]

# THE BUILD IN FUNCTION LEN() ALSO APPLIES TO LISTS

letters = ['a', 'b', 'c', 'd']
print(len(letters))
#4