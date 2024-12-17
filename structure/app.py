# we may choose to import stuff from other modules
import utility # we import the whole file
from calc import addThem
from calc import multThem

d = input('enter something: ')

r = utility.checkInt(d)

print(r)

# use the imported functions
a = addThem(3,4)
m = multThem(5,6)
print(a,m)