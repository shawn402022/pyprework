#USING PYTHON AS A CALCULATOR
#THE INTEPRETER ACTS A S ASIMPLE CALCULATOR: YOU CAN TYPE AN EXPRESSION AT IT AND IT WIL WRITE THE VALE. EXPRESSION SYNTAX IS STRAIGHTFORWARD: 
# THE OPERATORS + - * AND / WORK JUST LIKE IN MOST OTHER LANGEAGES.

print(2+2)
4

print(50-5*6)
20

print((50-5*6)/4)
5.0

print(8/5) #division always returns a floating number 
1.6

#To do floor division and get an integer result you can use the // operator; to calculate the remainder you can use %

print(17/3) # classic division returns a float
5.66666666666667

print (17//3) # floor division discards the fractional part
5

print(17%3) # the % operator returns the remainder of the division
2

print(5*3+2) # result* divisor + remainder
17

# with python it is possible to use the ** operator to calculate powers

5**2 # 5 squared
25

2**7 # 2 to the power of 7
128

# The equal sign (=)  is used to assign a value to a variabvle.Afterwars, no result is displayed before the next interactive prompt: 
# There is full support for floating point; operators with mixed type operands convert the integer to operantd to floating point:

width = 20
height = 5*9
print(width*height)
900

print(4*3.75 - 1)
14.0
