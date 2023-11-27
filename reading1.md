# Reading 1: Network Traffic Analysis with Wireshark

## Assignment Questions

**Layers of OSI Model**
1. What does “OSI” stand for?
- Open Systems Interconnection
  
2. List the 7 layers of the OSI model and what each one is responsible for.
- Physical: physical connection between devices
- Data Link: node to node deilvery of message
- Network: transmission of data from one host to another, located in different networks
- Transport: take servic from network layer and provide it to the application layer
- Session: establishes connection, maintenance, ensures authentication, and ensures security
- Presentation: data from the application layer is extracted and manipulated in the required format fro transmission
- Application: helps identifying the client and synchronizing communication

3. Distinguish which layers are the “hardware layers”, and which layers are the “software layers”. What does that even mean?
- 'Hardware layers' are the physical, data link, and network layers. They are considered the hardware layers due to handling the physcial connections between devices.
 
4. How can the OSI model be used in troubleshooting?
- The OSI model would be perfect for troubleshooting as it breaks down the different layers and the components they hold. When troubleshooting, it is easier to isolate issues to certain layers and focus on that. 

**What is Wireshark and How is it Used?**
1. What is Wireshark?
- Wireshark is an application that captures packets from a network connection.
  
2. What is a packet?
- Packet is the name given to a discrete unit of data in a a typical ethernet network.
  
3. What 3 high-level things does Wireshark accomplish? How could these be used for nefarious purposes? For benevolent purposes?
- Packet Capture: listens to netowkr connections in real time and grab entire streams of traffic
- Filtering: obtaining only the information needed from all the random live data.
- Visualization: allows user to dive into the middle of a network packet. the user can visualize entire conversations and network streams.

**Nefarious Uses**
- WireShark can be nefariously used to exploit vulnerabilities, and collecting sensitive information to use in a malicious way later on. 

**Benevolent Uses**
- Benevolent uses of WireShark may include troubleshooting network connectivity issues or simply monitoring the network. 

## Resources 
- [Layers of OSI Model](https://www.geeksforgeeks.org/open-systems-interconnection-model-osi/)
- [What Is Wireshark and How Is It Used?](https://www.comptia.org/content/articles/what-is-wireshark-and-how-to-use-it)

### Things I want to know more about

    
