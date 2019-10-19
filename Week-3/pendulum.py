# write a function that checks whether L and g are valid input values.
import math
def period(L,g):

    if isinstance(L,(float,int)) and isinstance(g,(float,int)): # check whether inputs are integers/ floats else raise Type Error
        
        if L > 0 and g > 0:# check whether inputs are of valid value
            T = 2 * math.pi * (L / g)**0.5 # compute period T
            return T # return T
        else:
            raise ValueError # use raise to raise an error instead of using return command to return a value /class ...
        
    else:
        raise TypeError
    
"""#Debug
print(period(1,1))
print(period(-1,1))
print(period(5,0))
print(period("Hi",1))
"""