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

if __name__ == '__main__':
    # exercise the code
    userA = User('Ethel') # we now have an instance of the class
    print( userA.name )