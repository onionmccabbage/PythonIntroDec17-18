# Sometimes its handy to acess a sequence of values
f = range(0,11) # start at 0 stop-before 11 (i.e. stop at 10)
for i in f:
    print(i) #
g = range(-99, 1001, 5) # start, stop-before, step
for i in g:
    print(i)

# we may also use this concept for 'slicing'
# here is a tuple
t = ('a', False, 34, 7.33, 'ok')
print(t[0:4]) # [start:stop-before]
# we can convert a tuple to a list
l = list(t)
l.append(('a', 'b', 'c')) # put a tuple into the list
l.append({7,6,5,4,3})    # put a set into the list
print(l[2:6:2]) # [start:stop-before:step] slicing
# mini exercise: find a way to print the 
# slice of this string so we see 'Wallace'
s = 'Grommit and Wallace live in West Wallaby Lane'
print( s[12:19] ) # 'Wallace'

# a range object can also provide many calculated results
squares = [i*i for i in range(1,11)]
print(squares) # we get a list of square nubmers 1-10

# checking if the user entered a numeric value
# remember inout always returns a string (even if they type a number)
n = input('enter a number: ')
if n.isnumeric(): # check to see if the string contains only digits (not . or - etc)
    print(f'Thank you {n} is a number') # we may choose to format a string
    # we can safely convert the string to an integer
    num = int(n) # careful - this will throw an exception if it fails
    # NB single equals SETS a value. Double equals CHECKS a value
    # compare this number to expected values
    if num <10: # comparison operators: == < > also <= >= and != (not equal)
        print(f'{num} is less than ten')
    elif num >=10 and num<100: # we may choose to have several elif statements
        print(f'{num} is less than 100')
    else:
        print(f'{num} is 100 or more')
else:
    print(f'{n} is not a number') # {} let us inject values into a string