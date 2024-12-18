# we can make use of code from other modules
# NB the imported module will NOT run its own exercise code
from functional import controlAC 
from functional import findAverage

# using 'map' we can apply a function repeatedly
# This lets us apply a function to all the values
# in a collection
def useMap(data):
    '''Map the 'findAverage' function to every tuple within the data'''
    result = map(findAverage, data)
    return result

if __name__ == '__main__':
    # here we can exercise the code in THIS module
    print( controlAC(23) )
    # here is a load of data
    data = [(4,5,6),(-7,-3,-99,-2),(0,0,0,0),(3246,7644,2344,7647,5673,1236,7565)]
    # invoke our mapping function
    r = useMap(data)
    print(r) # we have a map object
    # we need to iterate over thsi map object
    for i in r:
        print(i)
