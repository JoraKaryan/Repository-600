#ex-01

import json
def convert(dictionary):
    return json.dumps(dictionary, sort_keys = True, indent = 4)

print(convert({"llo":6,"kkk":5, "oo":"m"}))

#ex-02

sampleJson = """{ 
   "company":{ 
      "employee":{ 
         "name":"emma",
         "payble":{ 
            "salary":7000,
            "bonus":800
         }
      }
   }
}"""

def apply(file, key1, key2, key3, key4):
    return json.loads(file).get(key1).get(key2).get(key3).get(key4)

print(apply(sampleJson, "company", "employee", "payble", "salary"))

#ex-03

class Vehicle:
    def __init__(self, name, engine, price):
        self.name = name
        self.engine = engine
        self.price = price

vehicle = Vehicle("Toyota Rav4", "2.5L", 32000)

values = (vehicle.name, vehicle.engine, vehicle.price)
keys =("name", "engine", "price")

def collect(k, v):
    return json.dumps(dict.fromkeys(k, v))

print(collect(keys, values))

#ex-04
print("-------------------------------------------")
#ex-05
import xml.etree.ElementTree as ET
tree = ET.parse('movies.xml')
root = tree.getroot()

print(root.tag, root.attrib)

for i in root.iter():
    print(i.tag, i.attrib)
    
print("-------------------------------------------")

#ex-06
list_=[]
for i in root.iter():
    list_.append(i.tag)
print(list_)

print("-------------------------------------------")

#ex-07

for movie in root.iter('movie'):
    if movie.find('year').text == '1992':
        print(movie.attrib)

print("-------------------------------------------")

#ex-08

for movie in root.iter('movie'):
    for format in movie.iter('format'):
        if format.get('multiple') == 'Yes':
            print(movie.attrib)

print("-------------------------------------------")

#ex-09

for movie in root.iter('movie'):
    if movie.get('title') == "Back 2 the Future":
        movie.get('title') ==" Back to the Future"
        print (movie.get('title'))

print("-------------------------------------------")

#ex-10
for format_ in root.iter('format'):
    if format_.get('multiple') == 'False':
        format_.set('multiple', 'No')
    if format_.get('multiple') == 'True':
        format_.set('multiple', 'Yes')
    print(format_.get('multiple'))

print("-------------------------------------------")

#ex-11























            




















