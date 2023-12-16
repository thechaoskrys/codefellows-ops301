# Reading 14: Group policy 

## Assignment Questions
**1. What role does Group Policy play in Windows Active Directory?**
- Group Policy is a feature of Windows that facilitates a wide variety of advanced settings that network administrators can use to control the working environment of users and computer accounts in Active Directory.

**2. Name and describe different ways GPOs can benefit security.**
- GPOs can benefit security through password policies, systems management, and health checking. 
- **Password Policy:** GPOs can be used to establish password length, complexity and other requirements.
- **Systems Management:** GPOs can be used to save hours and hours of time configuring the environment of new users and computers joining the domain.
- **Health Checking:** GPOs can be used to deploy software updates and system patches to ensure your environment is healthy and up to date against the latest security threats.

**3. How can the acronym “LSDOU” help you figure out which policies are in effect?**
- **LSDOU:** local, site, domain, and organizational unit.
- The local computer policy is the first to be processed, followed by the site level to domain AD policies, then finally into organization units. If there happen to be conflicting policies in LSDOU, the last applied policies win out.

## Resources
- [What is Group Policy and What Role Does It Play in Data Security](What is Group Policy and What Role Does It Play in Data Security)
- [Wireless Standards](https://www.professormesser.com/network-plus/n10-008/n10-008-video/wireless-standards-n10-008/)
- [Wireless Technologies](https://www.professormesser.com/network-plus/n10-008/n10-008-video/wireless-standards-n10-008/)
- [Wireless Encryption](https://www.professormesser.com/network-plus/n10-008/n10-008-video/wireless-encryption-n10-008/)
