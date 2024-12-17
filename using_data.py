# We can work with data in data structures such as tuple list dict, set
# a dictionary is a non-ordinal collection of mutable values
# we write key-value pairs
j = {'name':'Grommit', 'age':40, 'auth':False}
j['level']='user' # we can add members to the dictionary
j['auth'] = True # we can change members of the dictionary (mutable)
# we may iterate over a dict like this
for k,v in j.items():
    print(k,v)