#QUESTION1 Write a function to print "hello_USERNAME!" 
# USERNAME is the input of the function. The first line od the code has been defined as:

from symbol import not_test


def hello_name(user_name):
    return "hello"

print(hello_name('Shawn'))

#QUESTION2, Write a python function, first_odds that prints 
# the odd numbers from 1-100 and returns nothing.

def first_odds():
    for value in range(1,100,2):
        print(value)

first_odds()

# QUESTION3, Please write a Python function,max_num_in_list 
# to return the max number of a given list.
# The first line of the code has been defined as below


def max_num_in_list(a_list):
    for num in a_list:
        max(a_list)
numlist = [1, 2, 3, 4, 5 ,6, 7, 8, 9]


 
#QUESTION4, Write to return if the given year is a leap year. A leap year is dvisible by 4, but not divisible by 100
#unless it is also divisible by 400. The return should be boolean Type (true/false)

question=("Is this year a leap year?")

def is_leap_year(a_year):
    leapYear = a_year
    return leapYear
    if question %4 == 0:  #I was working my way through the problem so i started with %4
        print("true") 
    else:
        print("false")

        




#QUESTION5 Write a function to check to see if all numbers in list are consecutive numbers, For examlpe [2,3,4,5,6,7] are consecutive numbers, but [1,2,3,4]
# are not consecutive numbers. The return should be boolean Type.

#NEED HELP WITH THIS ONE # WILL HAVE 1 ON 1 IN WEEK 2 WHEN WERE DOING PYTHON

#def is_consecutive(a_list)