#! /usr/bin/python3.6

from ncclient import manager
from cisco_device import IOS_XR
import sys

try:
    with manager.connect(host=IOS_XR['address'],port=IOS_XR['port'],username=IOS_XR['username'],\
         password=IOS_XR['password'],hostkey_verify=False,device_params={'name': 'default'},allow_agent=False, look_for_keys=False) as m:
    	for capability in m.server_capabilities:
    		print(capability)
    m.close_session()

except Exception as e:
    print ("Encountered folloing error..")
    print (e)
    sys.exit()

#for capaibility in m.server_capabilities:
#    print(capability)

#m.close_session()

