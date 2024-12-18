# we can make use of code from other modules
# NB the imported module will NOT run its own exercise code
from functional import controlAC 


if __name__ == '__main__':
    # here we can exercise the code in THIS module
    print( controlAC(23) )