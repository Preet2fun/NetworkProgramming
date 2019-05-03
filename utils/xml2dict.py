# import required library for xml to dict conversation
import xmltodict

# Reading the XML file
with open('data.xml') as f:
	xmlfile = f.read()
#Print XML file data
print xmlfile

#converting XML file to dict
xml2dict = xmltodict.parse(xmlfile)
# print converted Dict 
print xml2dict


# print required interface 
element = ['active','interface-name']
element_int = ['address','netmask']

for ele in element:
	print xml2dict['interface-configuration'][ele]


for ele in element_int:
	print xml2dict['interface-configuration']['ipv4-network']['addresses']['primary'][ele]

#changing element in XML file by assigning its value
xml2dict['interface-configuration']['ipv4-network']['addresses']['primary']['address'] = '10.10.10.1'

# updating xml file using newly changed element using unparse method
new_xml_data = xmltodict.unparse(xml2dict)
print new_xml_data
