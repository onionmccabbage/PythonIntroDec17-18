# this is a comment - somewhere to explain whats going on
# All computer languages use variables - names for data
a = 3   # integer (whole number)
b = 5.4 # float (decimal point)
# All data has a data type. Simple types are int, float, boolean and None
s = 'welcome to python' # string of characters (we may use ' " or ''')
d = True # this is boolean (either True or False)

print( type(a), type(b), type(s))

# Python also has collection data types: Tuple and List
# List and Tuple allow any data types within themselves
f = (3,2,1) # this is a tuple: an ordinal collection of immutable members
#    0 1 2...
g = [3,2,1] # this is a list:  an ordinal collection of mutable members

# we can change members of a list like this
g[1] = 'altered'
g.append(None)
g.append(False)
print(g, type(g))