# Reading 2: Network scanning with NMAP

## Assignment Questions
**What is a Port Scanner and How Does it Work?**
1. What is a port? Describe it with an analogy that would help a family member understand.
    - A port is a virtual location where networking communication starts and ends. It is how different devices are able to communicate with each other on the network.
    - A port can be compared to a door in a commercial building. A port is the desginated entry/exit point for data that is entering and leaving a machine. Each door leads to a different store that has a different purpose. 
    
2. What does a port scanner send to a port to check the current status?
    - A port scanner sends a network request to a specific TCp and UDP port on a computer and records the response of either open, closed, or filtered. 
    
3. When a port scanner sends a request to connect, what are the three possible responses? Describe them.
    - The possible responses are open, closed or filtered.
    - Open/Accepted: The computer will respond asking if there is anything that it can do for the user.
    - Closed/Not Listening: The computer will respond that the port is in use and not available at this time.
    - Filtered, Dropped, Blocked: The computer does not respond. 
    
4. What is the difference between TCP and UDP?
    - TCP and UDP are the most common protocols used for IP networks.
    - TCP sends each packet in order, complete with error checking, verification, and a 3-way handshake to ensure each packet is successful.
    - UDP is connectionless. It is typically used for online gaming as it tends to be faster. It does not have any error checking.

**Common Ports** 
- Telnet: 23
- SSH: 22
- DNS: 53
- SMTP: 587
- HTTP: 80
- HTTPS: 443
- RDP: 3389
- Ping: ICMP rather than ports

## Resources
- [What is a Port Scanner and How Does it Work?](https://www.varonis.com/blog/port-scanning-techniques)
- [Common Ports](https://www.professormesser.com/network-plus/n10-008/n10-008-video/common-ports-n10-008/)


### Things I want to know more about 
