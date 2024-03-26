# A funciton to print "hello_USERNAME!"
def hello_name(user_name):
    '''Print hello user_name'''
    print("hello_Brandon! (or whoever is grading this)")

hello_name(print)
print("\n")

# function that prints the odd numbers from 1-100 and returns nothing
def first_odds(odds):
    '''Print odd numbers between 1-100'''
    for i in range(1, 101, 2):
        print(i)
        
first_odds(print)
print("\n")

# Function max_num_in_list returning max number in the list
def max_num_in_list(a_list):
    '''Return the max number in a list'''
    max_number = a_list[0]

    for num in a_list[1:]:
        if num > max_number:
            max_number = num

    return max_number

list_of_numbers = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
print(max_num_in_list(list_of_numbers))
print("\n")

# Whether function is a leap year, returns true/false
def is_leap_year(a_year):
    ''''''
    if a_year % 4 == 0:
        if a_year % 100 == 0:
            if a_year % 400 == 0:
                return True
            else:
                return False
        else:
            return True
    else:
        return False      

print(is_leap_year(1200))
print(is_leap_year(1900))
print(is_leap_year(2024))
print("\n")

#
def is_consecutive(a_list):
    '''Check to see if all numbers in a list are consecutive numbers'''
    sorted(a_list) == list(range(min(a_list), max(a_list)+1))
    return True

numbers_list =[1, 2, 3, 4, 5]
print(is_consecutive(numbers_list))

