# why would we ever need a class?
# we often need to remember data within a program
age = 42 # we can just use numbers
username = 'student' # we may use strings
isAuthorised = True # boolean
# sometimes we gather related data together into a structure
details = (37, 'Ethel', False) # tuple
n = [age, username, isAuthorised] # a list
# the built-in data types have no means to validate the data
n[0] = -66 # we may mutate members of the list collection
print(f'User {n[1]} is {n[0]}') # use slicing to acess ordinal members of a collection

# it is a convention to use intitial capital letter for a class name
class User():
    '''this class will encapsulate user details
    Name will be a non-empty string'''
    def __init__(self, n):
        '''the __init__ function is called every time we use the class'''
        self.name = n
    # we may declare properties to validate parts of the class
    @property # we now have an accessor method (a getter)
    def name(self):
        return self.__name
    @name.setter # this is the mutator method (a setter)
    def name(self, new_name):
        '''valiate the name is a non-empty string'''
        if type(new_name)==str and new_name != '':
            self.__name = new_name
    def __str__(self): # NB every method in a class takes 'self' as an argument
        '''Everthing in Python has a __str__ method
        It is used whenever we use 'print' for output'''
        return f'This is {self.name}'

# Many things within Python have leading and trailing double underscore
# __name__, __main__, __init__ etc.
# These are known as 'dunder' (double underscore)
# Anything like this is a part of Python

if __name__ == '__main__':
    # exercise the code
    userA = User('Ethel') # we now have an instance of the class
    print( userA.name )
    userB = User('Oenid') # another instance of the class
    print(userB)