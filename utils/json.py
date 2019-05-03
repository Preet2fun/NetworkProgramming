#json.loads(json_data) ---> this method take json as string and convert it into python object either list or dict depands on json data
#json.dumps(object) ---> this method will convert python objcet back to JSON string format

import simplejson as json
from pprint import pprint

#Open the sample json file and read it into variable
with open("example_data.json") as f:
    json_example = f.read()

#Print the raw json data
print json_example

#Parse the json into a Python dictionary
json_dict = json.loads(json_example)

#Pretty Print the Python Dictionary Object
pprint(json_dict)

#Save the interface name into a variable
int_name =  json_dict['if-name']
print int_name

# Change the IP address of the interface
json_dict['ip-address']='1.1.1.1'

#Revert to the json string version of the dictionary
json_example = json.dumps(json_dict)

pprint(json_example)
