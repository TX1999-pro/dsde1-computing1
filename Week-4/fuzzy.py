'''
fuzzy.py

Lint this file using PyLint.
'''

# This function does some maths on three numbers.
def maths(input_a, input_b, input_c):
    """This function will multiply input_a by 3, followed by minusing input_b,
    and lastly add input_c and return the result"""
    result = input_a * 3 - input_b + input_c
    return result

# This function returns True or False.
def choices(question):
    """This function returns True or False"""
    return bool(question)


def main():
    """This is the main function and will call the maths function and choices function."""
    # first function takes three numbers
    answer = maths(3, 9, 2.3)
    print(answer)

    # second function takes a True or False
    new_answer = choices(True)
    print(new_answer)

if __name__ == '__main__':
    main()
