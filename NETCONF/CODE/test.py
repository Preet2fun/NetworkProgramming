#! /usr/bin/python3.6

from ncclient import manager
from cisco_device import IOS_XR
import sys
import xmltodict
import logging

# NETCONF filter to use
netconf_filter = open("interfaces.xml").read()

if __name__ == '__main__':
    with manager.connect(host=IOS_XR["address"],
                         port=IOS_XR["port"],
                         username=IOS_XR["username"],
                         password=IOS_XR["password"],
                         hostkey_verify=False,device_params={'name': 'default'},allow_agent=False, look_for_keys=False) as m:

        # Get Configuration and State Info for Interface
        netconf_reply = m.get(netconf_filter)
	#logging.basicConfig(level=logging.DEBUG,format='%(asctime)s %(levelname)s: %(message)s',stream=sys.stdout)
	intf_details = xmltodict.parse(netconf_reply.xml)["rpc-reply"]["data"]
        intf_config = intf_details["interfaces"]["interface"]
        intf_info = intf_details["interfaces-state"]["interface"]

        print("")
        print("Interface Details:")
        print("  Name: {}".format(intf_config["name"]))
        print("  Description: {}".format(intf_config["description"]))
        print("  Type: {}".format(intf_config["type"]["#text"]))
        print("  MAC Address: {}".format(intf_info["phys-address"]))
        print("  Packets Input: {}".format(intf_info["statistics"]["in-unicast-pkts"]))
        print("  Packets Output: {}".format(intf_info["statistics"]["out-unicast-pkts"]))
