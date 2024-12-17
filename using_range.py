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