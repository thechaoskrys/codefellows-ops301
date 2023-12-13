# Reading 13: Active Directory

## Assignment Questions

**1. What exactly is “Active Directory” and are the key services it provides?**
- It is an identity management service for Windows domain networks. The key services it provides are a schema, global catalog, query and index mechanism, and replication service.
       - A **schema** that defines the classes of objects and attributes contained in the directory.
       - A **global catalog** that contains detailed information about every object in the directory.
       - A **query and index mechanism** that allows users, administrators, and applications to efficiently find directory information.
       - A **replication service** that disseminates directory data across the network.


**2. What are the differences between a domain, forest, and tree in Active Directory?**
- A domain is a collection of objects (e.g. users, devices) that share the same Active Directory database. A domain is identified by a DNS name like company.com.
- A tree is a collection of one or more domains with a contiguous namespace (they have a common DNS root name like marketing.company.com, engineering.company.com, and sales.company.com).
- A forest is a collection of one or more trees that share a common schema, global catalog, and directory configuration—but aren’t part of a contiguous namespace. The forest typically serves as the security boundary for an enterprise network.

**3. How can objects (e.g. users, devices) within a domain be grouped?**
- Objects within a domain can be grouped into organizational units (OUs) to simplify administration and policy management. Administrators can create arbitrary organizational units to mirror functional, geographical, or business structures, and then apply group policies to OUs to simplify administration. OUs also make it easier to delegate control over resources to various administrators.

**4. Explain the benefits of Active Directory, as you would to a family member.**
- Active Directory helps all the users of the domain be able to sign in and access things easily, it is easier to find things, as everything has a determined spot that is easily navigated to, and it is easy to add new devices to track and manage through the Active Directory.

## Resources 
- [What is Active Directory?](https://www.cyberark.com/what-is/active-directory/)
- [DHCP Overview](https://www.professormesser.com/network-plus/n10-008/n10-008-video/dhcp-overview-n10-008/)
- [Configuring DHCP](https://www.professormesser.com/network-plus/n10-008/n10-008-video/configuring-dhcp-n10-008/)
