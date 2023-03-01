# Question 1:
# Write a function to print "hello_USERNAME!" USERNAME is the input of the function. The first line of the code has been defined as below.

def hello_name(Maggie):
    print("Hello" + Maggie + "!")
hello_name( 'Maggie' )

# Question 2:
#Write a python function, first_odds that prints the odd numbers from 1-100 and returns nothing
def first_odds():
    odds = [str(x) for x in range(100) if x%2 == 0]
    print(first_odds)

# Question 3
# Please write a Python function, max_num_in_list to return the max number of a given list. The first line of the code has been defined as below.

def max_num_in_list(a_list):
    max = list[ 0 ]
    for a in list:
        if a > max:
            max = a
        return max 
print(max_num_in_list([5, 17, 3490, -483818, 0]))

# Question 4
#Write a function to return if the given year is a leap year. A leap year is divisible by 4, but not divisible by 100, unless it is also divisible by 400. The return should be boolean Type (true/false).

def is_leap_year(a_year):
    leap = False
    # logic 
    if year % 400 == 0:
        leap = True
    elif year % 100 == 0:
        leap = False
    elif year % 4 == 0:
        leap = True
    
    year = int(raw_input())
    print(is_leap(year))

# Question 5 
# Write a function to check to see if all numbers in list are consecutive numbers. For example, [2,3,4,5,6,7] are consecutive numbers, but [1,2,4,5] are not consecutive numbers. The return should be boolean Type.

def is_consecutive(a_list):
    return sorted(1) == list(range(min(1), max(1)+1))

lst = [2, 5, 3, 4, 1]
print(is_consecutive(list))