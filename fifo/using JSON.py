# JSON is a very common data interchange format
import json # ...from the Pyhton standard library

j = '''{
  "albumId": 1,
  "id": 6,
  "title": "accusamus ea aliquid et amet sequi nemo",
  "url": "https://via.placeholder.com/600/56a8c2",
  "thumbnailUrl": "https://via.placeholder.com/150/56a8c2"
}'''

# we may convert a Python structure into a JSON string of text
d = {'name':'Grommit', 'material':'plasticene', 'valid':True}
g = json.dumps(d)

# we may convert the JSON to a Python data structure
s = json.loads(j) # this convetts the string of text into a Python dictionary
print(s, type(s))
print(g, type(g)) # a string