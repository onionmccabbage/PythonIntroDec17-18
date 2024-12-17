# we know that a function can be defined like this:
import random # we can import from the Python standard library


def askUser(): # here is a docstring
    '''we often write documentation for a function within tripple quotes
    This lets us us new-lines within the quoted text'''
    while True: # this code block will run endlessly
        r = input('What level random do we need: ') # this will be a string
        # check we have a number
        if r.isnumeric():
            rand = random.randint(0, int(r))
            return rand
        else:
            print(f'{r} is not a number')

def odds(x, y): # if we wish we may pass in arguments like this
    '''return a tuple containing the odd numbers between x and y'''
    r = range(x, y, 2) # (start, stop-before, step)
    # we can use this range to populate a tuple
    return tuple(r) # we may need to return some value!!!

# exercise the code
l = askUser()
print(f'The random integer is {l}')

o = odds(1, 11) # here we invoke the function, passing in our own choice for x and y
print(o)

# we may pass any values for x and y
p = odds(5, 9999999999)
print(p)

