# There are a few ways to write text into a permanent file
# This is useful when we need to persist data after the Python program has ended
import random
import math # also from the Python standard library

def printToFile(t):
    '''print some text to a persistent file'''
    # anything to do with files must use a file access object
    fout = open('my_log.txt', 'at') # 'at' will append text to the file
    # we can use 'print' to send text to a file
    print(f'{t} says Hello from Python', file=fout) # here we specify where the print should go
    fout.close() # good idea to tidy up when done

def writeTofile(t):
    '''Write text into a persistent file'''
    fout = open('file.txt', 'at') # we have a file access object
    with fout: # tidy way to handle file access object
        fout.write(t)
    # the file access object will be closed autoamtically when the 'with' block ends


# exercise the code
r = random.randint(0,100)
s = math.sqrt(r) # find the square root of a number
printToFile(s) # here we call the function so it operates