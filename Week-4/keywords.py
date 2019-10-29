'''
keywords.py

Create functions that use keyword arguments
with default values.
'''

# Create a function called welcome_message():
# if no input argument is provided
# it returns the string 'Hello and welcome'
# if a keyword argument called user_name is provided
# it returns 'Hello, <user_name>, and welcome'
# if a keyword argument called place is provided
# it returns 'Hello and welcome to <place>'
# if both user_name and place are provided
# it returns 'Hello, <user_name>, and welcome to <place>


def welcome_message(user_name='', place=''):
    """This function will print a welcome message depending on the input of parameters"""
    if user_name != '':
        if place != '':
            return 'Hello, ' + user_name + ', and welcome to ' + place
        return 'Hello, ' + user_name + ', and welcome'
    if place != '':
        return 'Hello and welcome to ' + place
    return 'Hello and welcome'

# Create a function called list_average()
# without using any libraries to do the maths for you
# (the point of this exercise is to practice interacting
# with lists)
# the first argument is a list of numbers
# the second optional keyword arguemt is called avg_type
# if nothing for avg_type provided, return the mean of the list
# if avg_type='mode', return the mode of the list
# (return list of all modes if there is a tie between multiple values)
# if avg_type='mean', return the mean of the list
# if avg_type='median', return the median of this list
def list_average(the_list, avg_type='mean'):
    """This function will perform math
    and return a type of average of the list
    specified by the argument ave_type"""
    #test whether the list is empty
    the_list.sort()
    n = len(the_list)
    # check keyword for mode
    if avg_type == 'mode':
        if the_list == []:
            return []
        the_list.sort()
        number = None
        mode_value = the_list[0]
        mode = [] # to store mode(s)
        for i in range(len(the_list)):
            # this iterates through the list
            a = the_list[i] # store the value of the next number from the reference number
            if a != number:
                # if true, a new value is found
                if the_list.count(a) > the_list.count(mode_value):
                    # if true, a new max mode is found
                    # then re-assign the value to the list of mode and the mode_value
                    mode = [a, ]
                    mode_value = a
                elif the_list.count(a) == the_list.count(mode_value):
                    # if true, a new mode is found and being added to the list of mode
                    mode.append(a)
                    mode_value = a
                number = a # change the reference number into a
        return mode
    #check keyword for median
    if avg_type == 'median':
        if the_list == []:
            return None
        if n % 2 == 0:
            median_1 = the_list[n//2]
            median_2 = the_list[n//2+1]
            return (median_1+median_2)/2
        return the_list[n//2]
    if the_list == []:
        return 0
    the_mean = sum(the_list) / n
    return the_mean

# improvement
"""
to improve --
keywords.py:46:4: C0103: Variable name "n" doesn't conform to snake_case naming style (invalid-name)
keywords.py:55:8: C0200: Consider using enumerate instead of iterating with range and len (consider-using-enumerate)
keywords.py:57:12: C0103: Variable name "a" doesn't conform to snake_case naming style (invalid-name)
keywords.py:40:0: R0911: Too many return statements (7/6) (too-many-return-statements)
"""