'''
This is a program that prints the numbers from 1 to 100.
But for multiples of three print "Fizz" instead of the number and for the multiples of five print "Buzz". 
For numbers which are multiples of both three and five print "FizzBuzz".
'''
print("Fizz-buzz, let's begin! ")
for i in range(1,101):
    if i % 3 == 0: # check whether i is divisible by 3
        
        if i % 5 == 0: # if i is divisible by 3, then check whether it is also divisible by 5
            print('fizz-buzz' , end = "  ") # if i is both divisible by 3 and 5, print 'fizz-buzz'

        else: # if i is not divisible by 5 but 3, print 'fizz' only
            print('fizz', end = "  ")

    elif i % 5 == 0: # check whether i is divisible by 5
        print('buzz', end = "  ") 
        
    else: # if i is neither divisible by 3 nor 5, then print the number 
        print(i, end = "  ")


# i have used the print function option end = '  ' to print a space instead of a new line 
# in order to displace and check the results more easily