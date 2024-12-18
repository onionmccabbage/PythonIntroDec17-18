# the simplest possible Python class
class Useless:
    pass

# all classes ultimately inherit from Object
class MyObj():
    '''this is an object'''
    # everthing in Python is an object. 
    # variables, structures, classes, function, even modules

# we may choose to explicitly inherit
class OtherObj(object):
    pass

# ... but we may choose to inherit from something else
class MyList(list):
    '''we now have our own list object'''

# we can create our own exception class
class MyException(Exception):
    '''we may choose to add our own functionality to the Exception class'''