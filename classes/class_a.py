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


class User:
    pass