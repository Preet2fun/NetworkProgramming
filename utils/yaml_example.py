# Import the yamltodict library
import yaml

#Open the sample yaml file and read it into variable
with open("yaml_example.yaml") as f:
    yaml_example = f.read()

#Print the raw yaml data
print(yaml_example)

#Parse the yaml into a Python dictionary
yaml_dict = yaml.load(yaml_example)

#Pretty Print the Python Dictionary Object
from pprint import pprint
pprint(yaml_dict)

#Save the interface name into a variable
int_name = yaml_dict["interface"]["name"]

#Print the interface name
print(int_name)

#Change the IP address of the interface
yaml_dict["interface"]["ipv4"]["address"][0]["ip"] = "192.168.0.2"

#Check that the IP address has been changed in the dictionary
pprint(yaml_dict)

#Revert to the yaml string version of the dictionary
print(yaml.dump(yaml_dict, default_flow_style=False))
