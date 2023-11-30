# Reading 4: Routing

## Assignment Questions
Which network mode in VirtualBox can be used to emulate unplugging the Ethernet cable from the network?
- The **not attached** mode resembles when the ethernet network cable is unplugged if there was a physical network adapter. 

Which network mode would be best if you wanted to run a server on a VM that could be fully accessible from your physical local area network?
- The **bridged adapter** mode is used for connecting the virtual network adapter of a VM to a physical network.
- This network mode can be used to run servers on VMs that must be fully accessible from a physical local area network. 

What are the three options of promiscuous mode and what does each do?
- **Allow all:** No restrictions. A VM adapter can see all incoming and outgoing traffic.
- **llow VMs:** Only the traffic transmitted to and from other VMs are visible. All other traffic is hidden.
- **Deny:** This default option hides all traffic that is not intended for the virtual network adapter.
- **Promiscious mode can be used in bridged network mode, NAT network, Internal Network, and Host-Only Adapter modes.

What is Port Forwarding?
- Port forwarding is the process of redirecting incoming traffic to the appropriate port or IP address.
- The incoming packets are intercepted by an application on the router, and gets sent to the appropriate place.
- [ChatGPT chat explaining port forwarding in simple terms. Eureka moment](https://chat.openai.com/share/855273a0-61e9-48e2-bce3-e1c6f318e59e)
  
## Resources
- [VirtualBox Network Settings Guide](https://www.nakivo.com/blog/virtualbox-network-setting-guide/)
- [Network Topologies](https://www.professormesser.com/network-plus/n10-008/n10-008-video/network-topologies-5/)
- [Routing Technologies](https://www.professormesser.com/network-plus/n10-008/n10-008-video/routing-technologies-n10-008/)
- [Dynamic Routing](https://www.professormesser.com/network-plus/n10-008/n10-008-video/n10-008-dynamic-routing/)
- [Network Switching Overview](https://www.professormesser.com/network-plus/n10-008/n10-008-video/network-switching-overview-n10-008/)
  
### Things I want to know more about 
