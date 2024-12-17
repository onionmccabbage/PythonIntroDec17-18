# JSON is a very common data interchange format
import json ' ...from teh Pyhton standard library'


j = '''{
  "albumId": 1,
  "id": 6,
  "title": "accusamus ea aliquid et amet sequi nemo",
  "url": "https://via.placeholder.com/600/56a8c2",
  "thumbnailUrl": "https://via.placeholder.com/150/56a8c2"
}'''

# we may convert the JSON to a Python data structure
s = json.loads(j) # this convetts the string of text into a Python dictionary
print(s, type(s))