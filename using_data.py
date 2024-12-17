# We can work with data in data structures such as tuple list dict, set
# a dictionary is a non-ordinal collection of mutable values
# we write key-value pairs
j = {'name':'Grommit', 'age':40, 'auth':False}
j['level']='user' # we can add members to the dictionary
j['auth'] = True # we can change members of the dictionary (mutable)
# we may iterate over a dict like this
for k,v in j.items():
    print(k,v)

# a Set is a mutable non-ordinal collection of unique values
k = {5, 2, -99, True, 2, 'coffee', '2', '1', '4', 'coffee', 1}
# be careful True evaluates to 1
# also False evaluates to zero
print(k, type(k))

# code blocks. Begin with : then indent lines
if True==1:
    print('of course True equals 1')
else:
    print('ummmmm')
# code block ends when the lines are no longer indented

# another code block - here we define a function
def fancyStuff():
    a = 4
    l = 3.2
    result = l**a
    return result
# all the above lines are indented, so they belong to the code block (function)
# we can invoke a function like this (i.e. call the function)
r = fancyStuff()
print(r)