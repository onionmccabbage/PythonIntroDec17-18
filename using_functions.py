# we know that a function can be defined like this:
import random # we can import from the Python standard library


def askUser(): # here is a docstring
    '''we often write documentation for a function within tripple quotes
    This lets us us new-lines within the quoted text'''
    r = input('What level random do we need: ') # this will be a string
    # check we have a number
    if r.isnumeric():
        rand = random.randint(0, int(r))
        return rand
    
# exercise the code
l = askUser()
print(f'The random integer is {l}')

