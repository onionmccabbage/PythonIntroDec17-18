# this utility module contains some useful functions

def checkInt(s):
    '''check to see if 's' is numeric. If it is, convert to an integer
    Otherwise retrun a default number'''
    if s.isnumeric():
        n = int(s) # convert the string to an integer
    else:
        n=1
    return n
