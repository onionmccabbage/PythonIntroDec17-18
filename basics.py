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

# Once created, we CANNOT alter a tuple
# f[2] = 'oops' # this will fail

# Strings, lists amd tuples are all ordinal. We can iterate over them
for i in s:
    print(i) # notice this line is indented
for i in f:
    print(i)
for i in g:
    print(i)

# we can carry out maths operations
print( b/a, b+a, b*a, 10**2 ) # + - / * also ** means raise to the power