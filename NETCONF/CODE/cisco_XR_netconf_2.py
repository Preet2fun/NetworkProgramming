#! /usr/bin/python3.6

from ncclient import manager
from cisco_device import IOS_XR
import sys
import xmltodict
import logging

logger = logging.basicConfig(level=logging.DEBUG,format='%(asctime)s %(levelname)s: %(message)s',stream=sys.stdout)


netconf_filter = open("ietf_fileter_interface.xml").read()
print (netconf_filter)


with manager.connect(host=IOS_XR['address'],port=IOS_XR['port'],username=IOS_XR['username'],\
         password=IOS_XR['password'],hostkey_verify=False,device_params={'name': 'default'},allow_agent=False, look_for_keys=False) as m:

	netconf_reply = m.get(netconf_filter)
        interface_dict = xmltodict.parse(netconf_reply)

	print(interface_dict) 


	m.close_session()

#except Exception as e:
#    print ("Encountered folloing error..")
#    print (e)
#    sys.exit()



