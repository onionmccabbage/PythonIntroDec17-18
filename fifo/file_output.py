# There are a few ways to write text into a permanent file
# This is useful when we need to persist data after the Python program has ended

def printToFile():
    '''print some text to a persistent file'''
    # anything to do with files must use a file access object
    fout = open('my_log.txt', 'at') # 'at' will append text to the file
    # we can use 'print' to send text to a file
    print('Hello from Python', file=fout) # here we specify where the print should go

# exercise the code
printToFile() # here we call the function so it operates