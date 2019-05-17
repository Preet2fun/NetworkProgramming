#! /usr/bin/python3.6

from ncclient import manager
from cisco_device import IOS_XR
import sys
import xmltodict
import logging
from pprint import pprint


# NETCONF filter to use
netconf_filter = open("filter-ietf-interfaces.xml").read()


if __name__ == '__main__':
    with manager.connect(host=IOS_XR["address"],
                         port=IOS_XR["port"],
                         username=IOS_XR["username"],
                         password=IOS_XR["password"],
                         hostkey_verify=False) as m:

       print("Belwo is NETCONF capability")
       for capability in m.server_capabilities:
            print(capability)

       # Get Configuration and State Info for Interface
       netconf_reply = m.get(netconf_filter)
       #pprint(netconf_reply)

       intf_details = xmltodict.parse(netconf_reply.xml)['rpc-reply']['data']
       intf_config = intf_details["interfaces"]["interface"]
       intf_info = intf_details["interfaces-state"]["interface"]
       pprint(intf_details)
     
       print("")
       print("Interface Details:")
       print("  Name: {}".format(intf_config["name"]))
       print("  Type: {}".format(intf_config["type"]["#text"]))
       print("  MAC Address: {}".format(intf_info["phys-address"]))
       print("  Packets Input: {}".format(intf_info["statistics"]["in-unicast-pkts"]))
       print("  Packets Output: {}".format(intf_info["statistics"]["out-unicast-pkts"]))


















#logger = logging.basicConfig(level=logging.DEBUG,format='%(asctime)s %(levelname)s: %(message)s',stream=sys.stdout)


#netconf_filter = open("interface.xml").read()
#print (netconf_filter)


#with manager.connect(host=IOS_XR['address'],port=IOS_XR['port'],username=IOS_XR['username'],\
        # password=IOS_XR['password'],hostkey_verify=False,allow_agent=False, look_for_keys=False) as m:

	#netconf_reply = m.get(netconf_filter)

#print("recived reply ##############################################")
#print(netconf_reply)
#interface_dict = xmltodict.parse(netconf_reply)
#print(interface_dict) 

#m.close_session()

#except Exception as e:
#    print ("Encountered folloing error..")
#    print (e)
#    sys.exit()



