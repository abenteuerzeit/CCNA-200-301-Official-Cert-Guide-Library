# Glossary


### Numerics

**2.4-GHz band** The frequency range between 2.400 and 2.4835 GHz that is used for wireless LAN communication.

**2.5GBase-T** One of two Ethernet physical layer standards called multigigabit Ethernet (the other being 5.0GBase-T), first defined in IEEE addendum 802.3bz, which defines a 2.5 Gbps data rate over Cat 5E UTP cabling at distances of 100 meters.

**3G/4G Internet** An Internet access technology that uses wireless radio signals to communicate through mobile phone towers, most often used by mobile phones, tablets, and some other mobile devices.

**5-GHz band** The frequency range between 5.150 and 5.825 GHz that is used for wireless LAN communication.

**5.0GBase-T** One of two Ethernet physical layer standards called multigigabit Ethernet (the other being 2.5GBase-T), first defined in IEEE addendum 802.3bz, which defines a 2.5 Gbps data rate over Cat 5E UTP cabling at distances of 100 meters.

**6-GHz band** The frequency range between 5.925 and 7.125 GHz that is used for wireless LAN communication.

**10BASE-T** An Ethernet physical layer standard, first defined directly in the 802.3 standard as the first UTP-based Ethernet physical layer standard. It uses two twisted-pair UTP cabling and supports 10 Mbps data rates.

**10GBASE-SR** An Ethernet physical layer standard that uses optical multimode (OM) cabling, first defined in IEEE addendum 802.3ae, which defines a 10 Gbps data rate.

**10GBase-T** An Ethernet physical layer standard, introduced as IEEE addendum 802.3an, supporting 10 Gbps data rates over four-pair UTP cabling.

**40GBase-T** An Ethernet physical layer standard, introduced in IEEE addendum 802.3ba, supporting 40 Gbps data rates over four-pair UTP cabling.

**100BASE-T** An Ethernet physical layer standard, introduced as IEEE addendum 802.3u, supporting 100 Mbps data rates over two-pair UTP cabling.

**1000BASE-SX** An Ethernet physical layer standard that uses optical multimode (OM) cabling, first defined in IEEE addendum 802.3z, which defines a 1 Gbps data rate.

**1000BASE-T** An Ethernet physical layer standard, introduced as IEEE addendum 802.3ab, supporting 1000 Mbps (1 Gbps) data rates over four-pair UTP cabling.

### A

**AAA** Authentication, authorization, and accounting. Authentication confirms the identity of the user or device. Authorization determines what the user or device is allowed to do. Accounting records information about access attempts, including inappropriate requests.

**AAA server** *See* [authentication, authorization, and accounting (AAA) server](vol2_gloss.xhtml#gloss_047).

**access control entry (ACE)** One configuration line with a permit or deny action in an access control list (ACL).

**access interface** A LAN network design term that refers to a switch interface connected to end-user devices, configured so that it does not use VLAN trunking.

**access layer** In a campus LAN design, the switches that connect directly to endpoint devices (servers, user devices), and also connect into the distribution layer switches.

**access link** In campus LAN design, a link that connects an access switch to endpoint devices and wireless access points.

**access link (WAN)** A physical link between a service provider and its customer that provides access to the SP's network from that customer site.

**access point (AP)** A device that provides wireless service for clients within its coverage area or cell, with the AP connecting to both the wireless LAN and the wired Ethernet LAN.

**accounting** In security, the recording of access attempts. *See also* [AAA](vol2_gloss.xhtml#gloss_014).

**ACI** *See* [Application Centric Infrastructure (ACI)](vol2_gloss.xhtml#gloss_036).

**ACL** Access control list. A list configured on a router to control packet flow through the router, such as to prevent packets with a certain IP address from leaving a particular interface on the router.

**ACL persistence** A feature of IOS XE (but not IOS) by which a router initialization event (power off/on or reload) does not cause reassigning ACL sequence numbers. The feature can be enabled (default, meaning no resequencing) or disabled.

**ACL resequencing** The process of renumbering the sequence numbers of ACL commands, either for all ACLs at router initialization (power off/on or reload) or by using a command to renumber individual ACLs.

**ACL sequence number** A number assigned to each ACL ACE when configured, either automatically or as typed in the configuration command, which allows easier deletion of individual ACEs.

**ad hoc wireless network** *See* [independent basic service set (IBSS)](vol2_gloss.xhtml#gloss_170).

**administrative distance** In Cisco routers, a means for one router to choose between multiple routes to reach the same subnet when those routes are learned by different routing protocols. The lower the administrative distance, the more preferred the source of the routing information.

**agent-based architecture** With configuration management tools, an architecture that uses a software agent inside the device being managed as part of the functions to manage the configuration.

**agentless architecture** With configuration management tools, an architecture that does not need a software agent inside the device being managed as part of the functions to manage the configuration, instead using other mainstream methods like SSH and NETCONF.

**AI Ops** Artificial Intelligence for IT Operations. Refers to the application of artificial intelligence and machine learning techniques to automate and enhance various aspects of IT operations, including monitoring, troubleshooting, and incident management, to improve efficiency and reliability in managing complex IT environments.

**amplification attack** A reflection attack that leverages a service on the reflector to generate and reflect huge volumes of reply traffic to the victim.

**Ansible** A popular configuration management application, which can be used with or without a server, using a push model to move configurations into devices, with strong capabilities to manage network device configurations.

**APIC** *See* [Application Policy Infrastructure Controller](vol2_gloss.xhtml#gloss_037).

**Application Centric Infrastructure (ACI)** Cisco's data center SDN solution, the concepts of defining policies that the APIC controller then pushes to the switches in the network using the OpFlex protocol, with the partially distributed control plane in each switch building the forwarding table entries to support the policies learned from the controller. It also supports a GUI, a CLI, and APIs.

**Application Policy Infrastructure Controller (APIC)** The software that plays the role of controller, controlling the flows that the switches create to define where frames are forwarded, in a Cisco data center that uses the Application Centric Infrastructure (ACI) approach, switches, and software.

**application programming interface (API)** A software mechanism that enables software components to communicate with each other.

**application-specific integrated circuit (ASIC)** An integrated circuit (computer chip) designed for a specific purpose or application, often used to implement the functions of a networking device rather than running a software process as part of the device's OS that runs on a general-purpose processor.

**ARP reply** An ARP message used to supply information about the sending (origin) host's hardware (Ethernet) and IP addresses as listed in the origin hardware and origin IP address fields. Typically sent in reaction to receipt of an ARP request message.

**Artificial Intelligence (AI)** Refers to computer systems or software that can perform tasks typically requiring human intelligence, such as learning from data, making decisions, and solving problems.

**ASIC** *See* [application-specific integrated circuit](vol2_gloss.xhtml#gloss_039).

**association** A negotiated relationship between a wireless station and an access point.

**association request** An 802.11 frame that a wireless client sends to an AP to request an association with it.

**association response** An 802.11 frame that a wireless access point sends to a wireless client in reply to an association request.

**authentication** In security, the verification of the identity of a person or a process. *See also* [AAA](vol2_gloss.xhtml#gloss_014).

**authentication, authorization, and accounting (AAA) server** A server that holds security information and provides services related to user login, particularly authentication (is the user who he says he is), authorization (once authenticated, what do we allow the user to do), and accounting (tracking the user).

**authorization** In security, the determination of the rights allowed for a particular user or device. *See also* [AAA](vol2_gloss.xhtml#gloss_014).

**autonomous AP** A wireless AP operating in a standalone mode, such that it can provide a fully functional BSS and connect to the DS.

### B

**band** A contiguous range of frequencies.

**bandwidth** The speed at which bits can be sent and received over a link.

**basic service set (BSS)** Wireless service provided by one AP to one or more associated clients.

**basic service set identifier (BSSID)** A unique MAC address that is used to identify the AP that is providing a BSS.

**beacon** An 802.11 frame that an AP broadcasts at regular intervals to advertise the existence of an SSID. Separate beacons are transmitted for each SSID on each channel being used.

**brute-force attack** An attack where a malicious user runs software that tries every possible combination of letters, numbers, and special characters to guess a user's password. Attacks of this scale are usually run offline, where more computing resources and time are available.

**buffer overflow attack** An attack meant to exploit a vulnerability in processing inbound traffic such that the target system's buffers overflow; the target system can end up crashing or inadvertently running malicious code injected by the attacker.

### C

**cacheable** For resources that might be repeatedly requested over time, an attribute that means that the requesting host can keep in storage (cache) a copy of the resource for a specified amount of time.

**CAPWAP** A standards-based tunneling protocol that defines communication between a lightweight AP and a wireless LAN controller.

**CAT 5E** An unshielded twisted-pair (UTP) cable quality standard from the TIA and ANSI. It supports 1000BASE-T (and slower) UTP Ethernet at distances of 100 meters. It also supports multigig Ethernet standards at 100-meter distances.

**CAT 6A** An unshielded twisted-pair (UTP) cable quality standard from the TIA and ANSI. It is the lowest UTP cable category that formally supports 10GBase-T UTP Ethernet at distances of 100 meters.

**CDP** Cisco Discovery Protocol. A media- and protocol-independent device-discovery protocol that runs on most Cisco-manufactured equipment, including routers, access servers, and switches. Using CDP, a device can advertise its existence to other devices and receive information about other devices on the same LAN or on the remote side of a WAN.

**cell** The area of wireless coverage provided by an AP; also known as the basic service area.

**centralized control plane** An approach to architecting network protocols and products that places the control plane functions into a centralized function rather than distributing the function across the networking devices.

**centralized WLC deployment** A wireless network design that places a WLC centrally within a network topology.

**channel** An arbitrary index that points to a specific frequency within a band.

**Chat Ops** A collaboration model that integrates chat tools with automated workflows and tools, allowing teams to manage and execute tasks directly within chat interfaces, enhancing communication, visibility, and efficiency in operations and development workflows.

**CIDR** Classless interdomain routing. An RFC-standard tool for global IP address range assignment. CIDR reduces the size of Internet routers' IP routing tables, helping deal with the rapid growth of the Internet. The term *classless* refers to the fact that the summarized groups of networks represent a group of addresses that do not conform to IPv4 classful (Class A, B, and C) grouping rules.

**Cisco AnyConnect Secure Mobility Client** Cisco software product used as client software on user devices to create a client VPN. Commonly referred to as the Cisco VPN client.

**Cisco Catalyst 8000V** A virtual router platform designed for cloud and virtualized environments, offering high-performance, scalable, and secure routing capabilities with flexibility and agility.

**Cisco Catalyst Center** Cisco software, delivered by Cisco on a physical or virtual appliance, that acts as a network management application as well as being the control for Cisco's Software-Defined Access (Cisco SD-Access) offering.

**Cisco Prime Infrastructure (PI)** Graphical user interface (GUI) software that utilizes SNMP and can be used to manage your Cisco network devices. The term *Cisco Prime* is an umbrella term that encompasses many different individual software products.

**Cisco SD-Access** Cisco's intent-based networking (IBN) offering for enterprise networks.

**Cisco Secure Client (including AnyConnect)** Cisco software product used as client software on user devices to create a client VPN. Formerly called Cisco AnyConnect Secure Mobility Client, and sometimes referred to as the Cisco VPN client.

**Class of Service (CoS)** The informal term for the 3-bit field in the 802.IQ header intended for marking and classifying Ethernet frames for the purposes of applying QoS actions. Another term for Priority Code Point (PCP).

**classification** The process of examining various fields in networking messages in an effort to identify which messages fit into certain predetermined groups (classes).

**cloud-based AP** A wireless AP operating much like an autonomous AP, but having management and control functions present in the Internet cloud.

**cloud-based WLC deployment** A wireless network design that places a WLC centrally within a network topology, as a virtual machine in the private cloud portion of a data center.

**Cloud Management** Involves administering, monitoring, and optimizing cloud resources and services to ensure efficient utilization, performance, security, and compliance across cloud environments.

**cloud services catalog** A listing of the services available in a cloud computing service.

**code integrity** A software security term that refers to how likely that the software (code) being used is the software supplied by the vendor, unchanged, with no viruses or other changes made to the software.

**collapsed core design** A campus LAN design in which the design does not use a separate set of core switches in addition to the distribution switches—in effect collapsing the core into the distribution switches.

**Common ACL** A feature of IOS XE (but not IOS) that supports enabling two ACLs on a single interface and direction.

**configuration drift** A phenomenon that begins with the idea that devices with similar roles can and should have a similar standard configuration, so when one device's configuration is changed to be different, its configuration is considered to have moved away (drifted) from the standard configuration for a device in that role.

**configuration management** A component of network management focused on creating, changing, removing, and monitoring device configuration.

**configuration management tool** A class of application that manages data about the configuration of servers, network devices, and other computing nodes, providing consistent means of describing the configurations, moving the configurations into the devices, noticing unintended changes to the configurations, and troubleshooting by easily identifying changes to the configuration files over time.

**configuration monitoring** With configuration management tools like Ansible, a process of comparing over time a device's on-device configuration (running-config) versus the text file showing the ideal device configuration listed in the tool's centralized configuration repository. If different, the process can either change the device's configuration or report the issue.

**configuration provisioning** With configuration management tools like Ansible, the process of configuring a device to match the configuration as held in the configuration management tool.

**configuration template** With configuration management tools like Ansible, a file with variables, for the purpose of having the tool substitute different variable values to create the configuration for a device.

**connected mode** The operational mode used by a FlexConnect AP when the path back to its controller is up and working. In this mode, all wireless traffic flows over the CAPWAP tunnel to and from the controller.

**connection establishment** The process by which a connection-oriented protocol creates a connection. With TCP, a connection is established by a three-way transmission of TCP segments.

**container** One instance of a running application started from a container image and controlled by a container engine on a server.

**container image** One file that holds and embeds all files related to an application: all related executable files, required software libraries, and other files such as operating environment variables. Container virtualization systems then allow treating the application as a single file for movement, starting, stopping, and monitoring the container.

**control plane** Functions in networking devices and controllers that directly control how devices perform data plane forwarding, but excluding the data plane processes that work to forward each message in the network.

**controller-based networking** A style of building computer networks that use a controller that centralizes some features and provides application programming interfaces (APIs) that allow for software interactions between applications and the controller (northbound APIs) and between the controller and the network devices (southbound APIs).

**controller-less wireless deployment** A wireless design based on an embedded wireless controller (EWC), where the WLC function is co-located with an AP, rather than a discrete physical controller.

**core** In computer architecture, an individual processing unit that can execute instructions of a CPU; modern server processors typically have multiple cores, each capable of concurrent execution of instructions.

**core design** A campus LAN design that connects each access switch to distribution switches, and distribution switches into core switches, to provide a path between all LAN devices.

**core layer** In a campus LAN design, the switches that connect the distribution layer switches, and to each other, to provide connectivity between the various distribution layer switches.

**CRUD** In software development, an acronym that refers to the four most common actions taken by a program: Create, Read, Update, and Delete.

### D

**data plane** Functions in networking devices that are part of the process of receiving a message, processing the message, and forwarding the message.

**data serialization language** A language that includes syntax and rules that provides a means to describe the variables inside applications in a text format, for the purpose of sending that text between applications over a network or storing the data models in a file.

**Declarative Model** A method of describing IT automation that defines or declares the intended configuration, with the expectation that the automation software monitors the devices' configurations and changes them if they drift away from the intended (declared) configuration.

**declarative policy model** A term that describes the approach in an intent-based network (IBN) in which the engineer chooses settings that describe the intended network behavior (the declared policy) but does not command the network with specific configuration commands for each protocol (as would be the case with an imperative policy model).

**delay** In QoS, the amount of time it takes for a message to cross a network. Delay can refer to one-way delay (the time required for the message to be sent from the source host to the destination host) or two-way delay (the delay from the source to the destination host and then back again).

**denial-of-service (DoS) attack** An attack that tries to deplete a system resource so that systems and services crash or become unavailable.

**deny** An action taken with an ACL that implies that the packet is discarded.

**DevNet** Cisco's community and resource site for software developers, open to all, with many great learning resources; <https://developer.cisco.com>.

**DHCP attack** Any attack that takes advantage of DHCP protocol messages.

**DHCP Snooping** A switch security feature in which the switch examines incoming DHCP messages and chooses to filter messages that are abnormal and therefore might be part of a DHCP attack.

**DHCP Snooping binding table** When using DHCP Snooping, a table that the switch dynamically builds by analyzing the DHCP messages that flow through the switch. DHCP Snooping can use the table for part of its filtering logic, with other features, such as Dynamic ARP Inspection and IP Source Guard also using the table.

**dictionary attack** An attack where a malicious user runs software that attempts to guess a user's password by trying words from a dictionary or word list.

**dictionary variable** In applications, a single variable whose value is a list of other variables with values, known as key:value pairs.

**Differentiated Services (DiffServ)** An approach to QoS, originally defined in RFC 2475, that uses a model of applying QoS per classification, with planning of which applications and other traffic types are assigned to each class, with each class given different QoS per-hop behaviors at each networking device in the path.

**Differentiated Services Code Point (DSCP)** A field existing as the first 6 bits of the ToS byte, as defined by RFC 2474, which redefined the original IP RFC's definition for the IP header ToS byte. The field is used to mark a value in the header for the purpose of performing later QoS actions on the packet.

**distributed control plane** An approach to architecting network protocols and products that places some control plane functions into each networking device rather than centralizing the control plane functions in one or a few devices. An example is the use of routing protocols on each router which then work together so that each router learns Layer 3 routes.

**distributed denial-of-service (DDoS) attack** A DoS attack that is distributed across many hosts under centralized control of an attacker, all targeting the same victim.

**distributed WLC deployment** A wireless design based on distributing multiple controllers within the network. Each of the controllers commonly supports a relatively small number of users.

**distribution layer** In a campus LAN design, the switches that connect to access layer switches as the most efficient means to provide connectivity from the access layer into the other parts of the LAN.

**distribution link** In campus LAN design, a link that connects a distribution switch to an access switch.

**distribution system (DS)** The wired Ethernet that connects to an AP and transports traffic between a wired and wireless network.

**DNS** Domain Name System. An application layer protocol used throughout the Internet for translating hostnames into their associated IP addresses.

**DNS server** An application acting as a server for the purpose of providing name resolution services per the Domain Name System (DNS) protocol and worldwide system.

**domain-specific language** A generic term that refers to an attribute of different languages within computing, for languages created for a specific purpose (domain) rather than a general-purpose language like Python or JavaScript.

**Dynamic ARP Inspection (DAI)** A security feature in which a LAN switch filters a subset of incoming ARP messages on untrusted ports, based on a comparison of ARP, Ethernet, and IP header fields to data gathered in the IP DHCP Snooping binding table and found in any configured ARP ACLs.

### E

**egress tunnel router (ETR)** With LISP, a node at the end of a tunnel that receives an encapsulated message and then de-encapsulates the message.

**E-LAN** A specific carrier/Metro Ethernet service defined by MEF ([MEF.net](http://MEF.net)) that provides a service much like a LAN, with two or more customer sites connected to one E-LAN service in a full mesh so that each device in the E-LAN can send Ethernet frames directly to every other device.

**E-Line** A specific carrier/metro Ethernet service defined by MEF ([MEF.net](http://MEF.net)) that provides a point-to-point topology between two customer devices, much as if the two devices were connected using an Ethernet crossover cable.

**embedded wireless controller (EWC)** A WLC function that is co-located within an AP.

**embedded wireless controller (EWC) deployment** A wireless network design that places a WLC in the access layer, co-located with a LAN switch stack, near the APs it controls.

**enable secret** A reference to the password configured on the **enable secret** *pass-value* command, which defines the password required to reach enable (privileged) mode.

**error detection** The process of discovering whether a data-link level frame was changed during transmission. This process typically uses a Frame Check Sequence (FCS) field in the data-link trailer.

**error disabled (err-disable)** An interface state on LAN switches that can be the result of one of many security violations.

**error recovery** The process of noticing when some transmitted data was not successfully received and resending the data until it is successfully received.

**Ethernet access link** A WAN access link (a physical link between a service provider and its customer) that happens to use Ethernet.

**Ethernet WAN** A general and informal term for any WAN service that uses Ethernet links as the access link between the customer and the service provider.

**exploit** A means of taking advantage of a vulnerability to compromise something.

**extended access list** A list of IOS **access-list** global configuration commands that can match multiple parts of an IP packet, including the source and destination IP address and TCP/ UDP ports, for the purpose of deciding which packets to discard and which to allow through the router.

**extended service set (ESS)** Multiple APs that are connected by a common switched infrastructure.

**extended service set identifier (ESSID)** The SSID used consistently throughout an ESS.

### F

**fabric** In SDA, the combination of overlay and underlay that together provide all features to deliver data across the network with the desired features and attributes.

**fabric edge node** In SDA, a switch that connects to endpoint devices.

**fiber Internet** A general term for any Internet access technology that happens to use fiber-optic cabling. It often uses Ethernet protocols on the fiber link.

**firewall** A device that forwards packets between the less secure and more secure parts of the network, applying rules that determine which packets are allowed to pass and which are not.

**flash memory** A type of read/write permanent memory that retains its contents even with no power applied to the memory and that uses no moving parts, making the memory less likely to fail over time.

**FlexConnect mode** An AP mode tailored for remote sites. Wireless traffic flows to and from a controller if the AP's CAPWAP tunnel is up, or is locally switched if the tunnel is down.

**flow control** The process of regulating the amount of data sent by a sending computer toward a receiving computer. Several flow control mechanisms exist, including TCP flow control, which uses windowing.

**FTP** File Transfer Protocol. An application protocol, part of the TCP/IP protocol stack, used to transfer files between network nodes. FTP is defined in RFC 959.

**FTP control connection** A TCP connection initiated by an FTP client to an FTP server for the purpose of sending FTP commands that direct the activities of the connection.

**FTP data connection** A TCP connection created by an FTP client and server for the purpose of transferring data.

**FTPS** FTP Secure. Common term for FTP over TLS.

**full mesh** From a topology perspective, any topology that has two or more devices, with each device being able to send frames to every other device.

### G

**Generative AI** Also Strong AI; encompasses artificial intelligence systems capable of learning, reasoning, and making decisions similar to human cognition, often with the capability to create new content, ideas, or solutions beyond its initial training data.

**Git** An open-source version control application, widely popular for version control in software development and for other uses, like managing network device configurations.

**GitHub** A web-based platform for version control and collaboration, facilitating hosting, sharing, and managing of software projects using the Git version control system.

**GLBP active virtual forwarder (AVF)** A role implemented by all routers in a GLBP group, listening for frames sent to a unique virtual MAC address, so it can act as one of several active default routers in the group.

**GLBP active virtual gateway (AVG)** A role implemented by one router in a GLBP group, replying to ARP requests on behalf of the group's VIP, so that load balancing occurs.

**gratuitous ARP** An ARP Reply not sent as a reaction to an ARP request message, but rather as a general announcement informing other hosts of the values of the sending (origin) host's addresses.

### H

**host (context: DC)** In a virtualized server environment, the term used to refer to one physical server that is running a hypervisor to create multiple virtual machines.

**HSRP preemption** A configuration setting that dictates whether an HSRP router, when it initializes with HSRP, can immediately take over the HSRP active role (preemption) if it has a higher priority than the currently active router.

**HSRP priority** A configuration setting from 0 through 255 that impacts the choice of HSRP active state, with the highest priority router chosen as active.

**HTTP** Hypertext Transfer Protocol. The protocol used by web browsers and web servers to transfer files, such as text and graphic files.

**HTTP/1.0** A version of the HTTP protocol, published as an RFC in the mid 1990s. It uses TCP, expects URLs that begin with http, implying a default well-known server port of 80. It allows the use of secure HTTP as well.

**HTTP/1.1** A version of the HTTP protocol, published as an RFC in the mid 1990s. It uses TCP, expects URLs that begin with http, implying a default well-known server port of 80. It allows the use of secure HTTP as well.

**HTTP/2.0** A version of the HTTP protocol, published as an RFC in the mid 2010s. The protocol improved HTTP application processes to increase overall performance in the end-user experience. It supports using Secure HTTP (with TLS) or not.

**HTTP/3.0** A radically different HTTP version published as an RFC in 2022 and created by Google. It improved HTTP application processes plus changed the transport layer protocols, both to increase overall performance in the end-user experience. It uses the QUIC transport layer, which uses UDP (not TCP) and always includes TLS.

**hub and spoke** From a topology perspective, any topology that has a device that can send messages to all other devices (the hub), with one or more spoke devices that can send messages only to the hub. Also called point-to-multipoint.

**hypervisor** Software that runs on server hardware to create the foundations of a virtualized server environment primarily by allocating server hardware components like CPU core/threads, RAM, disk, and network to the VMs running on the server.

### I

**Imperative Model** A method of describing IT automation as a series of tasks, akin to a script or program, with the expectation that running the script will configure the devices to have the desired configuration.

**imperative policy model** A term that describes the approach in traditional networks in which the engineer chooses configuration settings for each control and data plane protocol (the imperative commands) that dictate specifically how the devices act. This model acts in contrast to the newer declarative policy model and intent-based networking (IBN).

**independent basic service set (IBSS)** An impromptu wireless network formed between two or more devices without an AP or a BSS; also known as an ad hoc network.

**Infrastructure as Code (IAC)** A practice that involves managing and provisioning computing infrastructure through machine-readable definition files, enabling automation, consistency, and scalability in infrastructure deployment and management processes.

**Infrastructure as a Service (laaS)** A cloud service in which the service consists of a virtual machine that has defined computing resources (CPUs, RAM, disk, and network) and may or may not be provided with an installed OS.

**infrastructure mode** The operating mode of an AP that is providing a BSS for wireless clients.

**inside global** For packets sent to and from a host that resides inside the trusted part of a network that uses NAT, a term referring to the IP address used in the headers of those packets when those packets traverse the global (public) Internet.

**inside local** For packets sent to and from a host that resides inside the trusted part of a network that uses NAT, a term referring to the IP address used in the headers of those packets when those packets traverse the enterprise (private) part of the network.

**intent-based networking (IBN)** An approach to networking in which the system gives the operator the means to express business intent, with the networking system then determining what should be done by the network, activating the appropriate configuration, and monitoring (assuring) the results.

**intrusion prevention system (IPS)** A security function that examines more complex traffic patterns against a list of both known attack signatures and general characteristics of how attacks can be carried out, rating each perceived threat, and reacting to prevent the more significant threats. *See also* [IPS](vol2_gloss.xhtml#gloss_181).

**IOS File System (IFS)** A file system created by a Cisco device that uses IOS.

**IOS image** A file that contains the IOS.

**IP Precedence (IPP)** In the original definition of the IP header's Type of Service (ToS) byte, the first 3 bits of the ToS byte, used for marking IP packets for the purpose of applying QoS actions.

**IPS** *See* [intrusion prevention system](vol2_gloss.xhtml#gloss_177).

**IPsec** The term referring to the IP Security protocols, which is an architecture for providing encryption and authentication services, usually when creating VPN services through an IP network.

**IPsec transport mode** The process of encrypting the data of the original IP packet when using IPsec, while using the original packet's IP header, plus VPN headers, to encapsulate the encrypted data. Typically used with remote access IPsec VPNs.

**IPsec tunnel mode** The process of encrypting the entire original IP packet when using IPsec, which requires a new IP header, plus VPN headers, to encapsulate the encrypted original packet. Typically used with site-to-site IPsec VPNs.

### J

**Jinja2** A text-based language used to define templates, with text plus variables; used by Ansible for templates.

**jitter** The variation in delay experienced by successive packets in a single application flow.

**JSON (JavaScript Object Notation)** A popular data serialization language, originally used with the JavaScript programming language, and popular for use with REST APIs.

**JSON array** A part of a set of JSON text that begins and ends with a matched set of square brackets that contain a list of values.

**JSON object** A part of a set of JSON text that begins and ends with a matched set of curly brackets that contain a set of key:value pairs.

### K–L

**key:value pair** In software, one variable name (key) and its value, separated by a colon in some languages and data serialization languages.

**Large Language Models (LLM)** Advanced artificial intelligence systems capable of understanding and generating human-like text based on extensive training on vast amounts of textual data.

**leaf** In an ACI network design, a switch that connects to spine switches and to endpoints, but not to other leaf switches, so that the leaf can forward frames from an endpoint to a spine, which then delivers the frame to some other leaf switch.

**LISP** Locator/ID Separation Protocol. A protocol, defined in RFC 6830, that separates the concepts and numbers used to identify an endpoint (the endpoint identifier) versus identifying the location of the endpoint (routing locator).

**list variable** In applications, a single variable whose value is a list of values, rather than a simple value.

**LLDP** Link Layer Discovery Protocol. An IEEE standard protocol (IEEE 802.1AB) that defines messages, encapsulated directly in Ethernet frames so they do not rely on a working IPv4 or IPv6 network, for the purpose of giving devices a means of announcing basic device information to other devices on the LAN. It is a standardized protocol similar to Cisco Discovery Protocol (CDP).

**LLDP-MED** A group of endpoint-focused LLDP TLVs, defined as a group TIA standard TIA-1057. It includes TLVs to communicate voice and data VLANs to phones and to manage power levels with PoE.

**local username** A username (with matching password), configured on a router or switch. It is considered local because it exists on the router or switch, and not on a remote server.

**log message** A message generated by any computer, but including Cisco routers and switches, for which the device OS wants to notify the owner or administrator of the device about some event.

**loss** A reference to packets in a network that are sent but do not reach the destination host.

### M

**malware** Malicious software.

**Management Information Base (MIB)** The data structures defined by SNMP to define a hierarchy (tree) structure with variables at the leaves of the tree, so that SNMP messages can reference the variables.

**management plane** Functions in networking devices and controllers that control the devices themselves but that do not impact the forwarding behavior of the devices like control plane protocols do.

**man-in-the-middle attack** An attack where an attacker manages to position a machine on the network such that it is able to intercept traffic passing between target hosts.

**marking** The process of changing one of a small set of fields in various network protocol headers, including the IP header's DSCP field, for the purpose of later classifying a message based on that marked value.

**MD5 hash** A specific mathematical algorithm intended for use in various security protocols. In the context of Cisco routers and switches, the devices store the MD5 hash of certain passwords, rather than the passwords themselves, in an effort to make the device more secure.

**Media Access Control (MAC) layer** The lower of the two sublayers of the data-link layer defined by the IEEE. Synonymous with IEEE 802.3 for Ethernet LANs.

**Meraki Dashboard** A centralized cloud-based management platform that provides intuitive control and monitoring of Meraki networking devices, offering streamlined configuration, real-time analytics, and seamless network administration.

**mesh network** A network of APs used to cover a large area without the need for wired Ethernet cabling; client traffic is bridged from AP to AP over a backhaul network.

**Metro Ethernet** The original term used for WAN service that used Ethernet links as the access link between the customer and the service provider.

**MIB** *See* [Management Information Base](vol2_gloss.xhtml#gloss_201).

**mitigation technique** A method to counteract or prevent threats and malicious activity.

**MPLS** *See* [Multiprotocol Label Switching](vol2_gloss.xhtml#gloss_218).

**MPLS VPN** A WAN service that uses MPLS technology, with many customers connecting to the same MPLS network, but with the VPN features keeping each customer's traffic separate from others.

**MTU** Maximum transmission unit. The maximum packet size, in bytes, that a particular interface can handle.

**multifactor authentication** A technique that uses more than one type of credential to authenticate users.

**Multigig Ethernet** The common name for the 2.5GBase-T and 5.0GBase-T Ethernet standards, which, when released simultaneously, represented an option for UTP Ethernet at speeds of multiple gigabits between the then-defined standard speeds of 1 Gbps and 10 Gbps.

**Multiprotocol BGP (MPBGP)** A particular set of BGP extensions that allows BGP to support multiple address families, which when used to create an MPLS VPN service gives the SP the method to advertise the IPv4 routes of many customers while keeping those route advertisements logically separated.

**Multiprotocol Label Switching (MPLS)** A WAN technology used to create an IP-based service for customers, with the service provider's internal network performing forwarding based on an MPLS label rather than the destination IP address.

### N

**named access list** An ACL that identifies the various statements in the ACL based on a name rather than a number.

**Narrow AI** Also Weak AI. Refers to artificial intelligence designed and trained for specific tasks or a limited range of activities, lacking broad cognitive capabilities and adaptability beyond its predefined scope.

**NAT** Network Address Translation. A mechanism for reducing the need for globally unique IP addresses. NAT allows an organization with addresses that are not globally unique to connect to the Internet, by translating those addresses into public addresses in the globally routable address space.

**NAT overload** Another term for Port Address Translation (PAT). One of several methods of configuring NAT, in this case translating TCP and UDP flows based on port numbers in addition to using one or only a few inside global addresses.

**NBI** *See* [northbound API](vol2_gloss.xhtml#gloss_230).

**Network Management System (NMS)** A software platform that enables centralized monitoring, configuration, and administration of network infrastructure and devices to ensure optimal performance, security, and reliability.

**Network Time Protocol (NTP)** A protocol used to synchronize time-of-day clocks so that multiple devices use the same time of day, which allows log messages to be more easily matched based on their timestamps.

**Next-generation firewall (NGFW)** A firewall device with advanced features, including the ability to run many related security features in the same firewall device (IPS, malware detection, VPN termination), along with deep packet inspection with Application Visibility and Control (AVC) and the ability to perform URL filtering versus data collected about the reliability and risk associated with every domain name.

**Next-generation IPS (NGIPS)** An IPS device with advanced features, including the capability to go beyond a comparison to known attack signatures to also look at contextual data, including the vulnerabilities in the current network, the capability to monitor for new zero-day threats, with frequent updates of signatures from the Cisco Talos security research group.

**NMS** *See* [Network Management System (NMS)](vol2_gloss.xhtml#gloss_224).

**nonoverlapping channels** Successive channel numbers in a band that each have a frequency range that is narrow enough to not overlap the next channel above or below.

**northbound API** In the area of SDN, a reference to the APIs that a controller supports that gives outside programs access to the services of the controller; for instance, to supply information about the network or to program flows into the network. Also called a northbound interface.

**northbound interface (NBI)** Another term for northbound API. *See also* [northbound API](vol2_gloss.xhtml#gloss_230).

**NTP client** Any device that attempts to use the Network Time Protocol (NTP) to synchronize its time by adjusting the local device's time based on NTP messages received from a server.

**NTP client/server mode** A mode of operation with the Network Time Protocol (NTP) in which the device acts as both an NTP client, synchronizing its time with some servers, and as an NTP server, supplying time information to clients.

**NTP server** Any device that uses Network Time Protocol (NTP) to help synchronize time-of-day clocks for other devices by telling other devices its current time.

**NTP synchronization** The process with the Network Time Protocol (NTP) by which different devices send messages, exchanging the devices' current time-of-day clock information and other data, so that some devices adjust their clocks to the point that the time-of-day clocks list the same time (often accurate to at least the same second).

### O

**on-demand self-service** One of the five key attributes of a cloud computing service as defined by NIST, referring to the fact that the consumer of the server can request the service, with the service being created without any significant delay and without waiting on human intervention.

**on-premises** An alternate term for private cloud. *See also* [private cloud](vol2_gloss.xhtml#gloss_267).

**OpenFlow** The open standard for Software-Defined Networking (SDN) as defined by the Open Networking Foundation (ONF), which defines the OpenFlow protocol as well as the concept of an abstracted OpenFlow virtual switch.

**Optical Multimode (OM)** The term used to refer to multimode fiber-optic cabling in various cabling standards.

**ordered data transfer** A networking function, included in TCP, in which the protocol defines how the sending host should number the data transmitted, defines how the receiving device should attempt to reorder the data if it arrives out of order, and specifies to discard the data if it cannot be delivered in order.

**outside global** With source NAT, the one address used by the host that resides outside the enterprise, which NAT does not change, so there is no need for a contrasting term.

**overlay** In SDA, the combination of VXLAN tunnels between fabric edge nodes as a data plane for forwarding frames, plus LISP for the control plane for the discovery and registration of endpoint identifiers.

### P

**partial mesh** A network topology in which more than two devices could physically communicate, but by choice, only a subset of the pairs of devices connected to the network is allowed to communicate directly.

**passive scanning** A technique used by a wireless client when it attempts to discover nearby APs by listening for their beacon frames.

**password guessing** An attack where a malicious user simply makes repeated attempts to guess a user's password.

**per-hop behavior (PHB)** The general term used to describe the set of QoS actions a device can apply to a message from the time it enters a networking device until the device forwards the message. PHBs include classification, marking, queuing, shaping, policing, and congestion avoidance.

**pharming** An attack that compromises name services to silently redirect users toward a malicious site.

**phishing** An attack technique that sends specially crafted emails to victims in the hope that the users will follow links to malicious websites.

**Platform as a Service (PaaS)** A cloud service intended for software developers as a development platform, with a variety of tools useful to developers already installed so that developers can focus on developing software rather than on creating a good development environment.

**PoE** Power over Ethernet. Both a generalized term for any of the standards that supply power over an Ethernet link, as well as a specific PoE standard as defined in the IEEE 802.3af amendment to the 802.3 standard.

**point of presence (PoP)** A term used for a service provider's (SP) perspective to refer to a service provider's installation that is purposefully located relatively near to customers, with several spread around major cities, so that the distance from each customer site to one of the SP's PoPs is short.

**point-to-point** From a topology perspective, any topology that has two and only two devices that can send messages directly to each other.

**point-to-point bridge** An AP configured to bridge a wired network to a companion bridge at the far end of a line-of-sight path.

**policing** A QoS tool that monitors the bit rate of the messages passing some point in the processing of a networking device, so that if the bit rate exceeds the policing rate for a period of time, the policer can discard excess packets to lower the rate.

**policing rate** The bit rate at which a policer compares the bit rate of packets passing through a policing function, for the purpose of taking a different action against packets that conform (are under) to the rate versus those that exceed (go over) the rate.

**port** (Multiple definitions) (1) In TCP and UDP, a number that is used to uniquely identify the application process that either sent (source port) or should receive (destination port) data. (2) In LAN switching, another term for switch interface.

**Port Address Translation (PAT)** A NAT feature in which one inside global IP address supports over 65,000 concurrent TCP and UDP connections.

**port number** A field in a TCP or UDP header that identifies the application that either sent (source port) or should receive (destination port) the data inside the data segment.

**port security** A Cisco switch feature in which the switch watches Ethernet frames that come in an interface (a port), tracks the source MAC addresses of all such frames, and takes a security action if the number of different such MAC addresses is exceeded.

**Power classification** With Power over Ethernet (PoE), the process by which a switch, once it detects a device wants power, discovers the amount of power as defined by a standardized set of power classes.

**Power detection** With Power over Ethernet (PoE), the process by which a switch discovers if the connected device wants to receive power over the link or not.

**Power over Ethernet (PoE)** Both a generalized term for any of the standards that supply power over an Ethernet link and a specific PoE standard as defined in the IEEE 802.3af amendment to the 802.3 standard.

**Power over Ethernet Plus (PoE+)** A specific PoE standard as defined in the IEEE 802.3at amendment to the 802.3 standard, which uses two wire pairs to supply power with a maximum of 30 watts as supplied by the PSE.

**power sourcing equipment (PSE)** With any Power over Ethernet standard, a term that refers to the device supplying the power over the cable, which is then used by the powered device (PD) on the other end of the cable.

**powered device (PD)** With any Power over Ethernet standard, a term that refers to the device that receives or draws its power over the Ethernet cable, with the power being supplied by the power sourcing equipment (PSE) on the other end of the cable.

**priority queue** In Cisco queuing systems, another term for a low latency queue (LLQ).

**private cloud** A cloud computing service in which a company provides its own IT services to internal customers inside the same company but by following the practices defined as cloud computing.

**private IP network** Any of the IPv4 Class A, B, or C networks as defined by RFC 1918, intended for use inside a company but not used as public IP networks.

**probe request** A technique used by a wireless client to discover nearby APs by actively requesting a response.

**provider** A plug-in that enables communication and interaction between Terraform and specific infrastructure platforms or services, facilitating the management and provisioning of resources within those environments through Terraform configuration files.

**provider edge (PE)** A term used by service providers, both generally and also specifically in MPLS VPN networks, to refer to the SP device in a point of presence (PoP) that connects to the customer's network and therefore sits at the edge of the SP's network.

**public cloud** A cloud computing service in which the cloud provider is a different company than the cloud consumer.

**pull model** With configuration management tools, a practice by which an agent representing the device requests configuration data from the centralized configuration management tool, in effect pulling the configuration to the device.

**push model** With configuration management tools, a practice by which the centralized configuration management tool software initiates the movement of configuration from that node to the device that will be configured, in effect pushing the configuration to the device.

### Q–R

**Quality of Service (QoS)** The performance of a message, or the messages sent by an application, in regard to the bandwidth, delay, jitter, or loss characteristics experienced by the message(s).

**queuing** The process by which networking devices hold packets in memory while waiting on some constrained resource; for example, when waiting for the outgoing interface to become available when too many packets arrive in a short period of time.

**QUIC** The name (not an acronym) for a transport layer protocol that improves overall performance of transferring objects over a network, in comparison to TCP. It uses UDP and integrates TLS into its connection setup tasks.

**RADIUS** A security protocol often used for user authentication, including being used as part of the IEEE 802.lx messages between an 802.lx authenticator (typically a LAN switch) and a AAA server.

**RAM** Random-access memory. A type of volatile memory that can be read and written by a microprocessor.

**rapid elasticity** One of the five key attributes of a cloud computing service as defined by NIST, referring to the fact that the cloud service reacts to requests for new services quickly, and it expands (is elastic) to the point of appearing to be a limitless resource.

**read-only community** An SNMP community (a value that acts as a password), defined on an SNMP agent, which then must be supplied by any SNMP manager that sends the agent any messages asking to learn the value of a variable (like SNMP Get and GetNext requests).

**read-write community** An SNMP community (a value that acts as a password), defined on an SNMP agent, which then must be supplied by any SNMP manager that sends the agent any messages asking to set the value of a variable (like SNMP Set requests).

**reassociation request** An 802.11 frame that a roaming wireless client sends to an AP to request that its existing association be moved to a new AP.

**reconnaissance attack** An attack crafted to discover as much information about a target organization as possible; the attack can involve domain discovery, ping sweeps, port scans, and so on.

**recursive DNS server** A DNS server that, when asked for information it does not have, performs a repetitive (recursive) process to ask other DNS servers in sequence, hoping to find the DNS server that knows the information.

**reflection attack** An attack that uses spoofed source addresses so that a destination machine will reflect return traffic to the attack's target; the destination machine is known as the reflector.

**remote access VPN** A VPN for which one endpoint is a user device, such as a phone, tablet, or PC, typically created dynamically, and often using TLS. Also called a client VPN.

**repeater** A device that repeats or retransmits signals it receives, effectively expanding the wireless coverage area.

**Representational State Transfer (REST)** A type of API that allows two programs that reside on separate computers to communicate, with a set of six primary API attributes as defined early in this century by its creator, Roy Fielding. The attributes include client/server architecture, stateless operation, cachability, uniform interfaces, layered, and code-on-demand.

**resource pooling** One of the five key attributes of a cloud computing service as defined by NIST, referring to the fact that the cloud provider treats its resources as a large group (pool) of resources that its cloud management systems then allocate dynamically based on self-service requests by its customers.

**REST** *See* [Representational State Transfer](vol2_gloss.xhtml#gloss_289).

**REST API** Any API that uses the rules of Representational State Transfer (REST).

**roaming** The process a wireless client uses to move from one AP to another as it changes location.

**round robin** A queue scheduling algorithm in which the scheduling algorithm services one queue, then the next, then the next, and so on, working through the queues in sequence.

### S

**SBI** *See* [Southbound API](vol2_gloss.xhtml#gloss_326).

**scalable group tag (SGT)** In SDA, a value assigned to the users in the same security group.

**Secure HTTP (HTTP over TLS)** The IETF standard that defines how to use TLS to add security features such as server authentication and message encryption to HTTP/2 and earlier versions of HTTP.

**segment** (Multiple definitions) (1) In TCP, a term used to describe a TCP header and its encapsulated data (also called an L4PDU). (2) Also in TCP, the set of bytes formed when TCP breaks a large chunk of data given to it by the application layer into smaller pieces that fit into TCP segments. (3) In Ethernet, either a single Ethernet cable or a single collision domain (no matter how many cables are used).

**sender hardware address** In both an ARP request and reply message, the field intended to be used to list the sender (origin) device's hardware address, typically an Ethernet LAN address.

**sender IP address** In both an ARP request and reply message, the field intended to be used to list the sender (origin) device's IP address.

**sender protocol address** In both an ARP request and a reply message, the formal term the field intended to be used to list the sender (origin) device's network layer address.

**service provider (SP)** A company that provides a service to multiple customers. Used most often to refer to providers of private WAN services and Internet services. *See also* Internet service provider.

**Service Set Identifier (SSID)** A text string that is used to identify a wireless network.

**shaping** A QoS tool that monitors the bit rate of the messages exiting networking devices, so that if the bit rate exceeds the shaping rate for a period of time, the shaper can queue the packets, effectively slowing down the sending rate to match the shaping rate.

**shaping rate** The bit rate at which a shaper compares the bit rate of packets passing through the shaping function, so that when the rate is exceeded, the shaper enables the queuing of packets, resulting in slowing the bit rate of the collective packets that pass through the shaper, so the rate of bits getting through the shaper does not exceed the shaping rate.

**shared key** A reference to a security key whose value is known (shared) by both the sender and receiver.

**Simple Network Management Protocol (SNMP)** An Internet standard protocol for managing devices on IP networks. It is used mostly in network management systems to monitor network-attached devices for conditions that warrant administrative attention.

**site-to-site VPN** The mechanism that allows all devices at two different sites to communicate securely over some unsecure network like the Internet, by having one device at each site perform encryption/decryption and forwarding for all the packets sent between the sites.

**sliding windows** For protocols such as TCP that allow the receiving device to dictate the amount of data the sender can send before receiving an acknowledgment—a concept called a *window*—a reference to the fact that the mechanism to grant future windows is typically just a number that grows upward slowly after each acknowledgment, sliding upward.

**SNMP** *See* [Simple Network Management Protocol](vol2_gloss.xhtml#gloss_307).

**SNMP agent** Software that resides on the managed device and processes the SNMP messages sent by the Network Management Station (NMS).

**SNMP community** A simple password mechanism in SNMP in which either the SNMP agent or manager defines a community string (password), and the other device must send that same password value in SNMP messages, or the messages are ignored. *See also* [read-only community](vol2_gloss.xhtml#gloss_281), [read-write community](vol2_gloss.xhtml#gloss_282), and notification community.

**SNMP Get** Message used by SNMP to read from variables in the MIB.

**SNMP Inform** An unsolicited SNMP message like a Trap message, except that the protocol requires that the Inform message needs to be acknowledged by the SNMP manager.

**SNMP manager** Typically a Network Management System (NMS), with this term specifically referring to the use of SNMP and the typical role of the manager, which retrieves status information with SNMP Get requests, sets variables with the SNMP Set requests, and receives unsolicited notifications from SNMP agents by listening for SNMP Trap and Notify messages.

**SNMP Set** SNMP message to set the value in variables of the MIB. These messages are the key to an administrator configuring the managed device using SNMP.

**SNMP Trap** An unsolicited SNMP message generated by the managed device, and sent to the SNMP manager, to give information to the manager about some event or because a measurement threshold has been passed.

**SNMPv2c** A variation of the second version of SNMP. SNMP Version 2 did not originally support communities; the term *SNMPv2c* refers to SNMP version 2 with support added for SNMP communities (which were part of SNMPvl).

**SNMPv3** The third version of SNMP, with the notable addition of several security features as compared to SNMPv2c, specifically message integrity, authentication, and encryption.

**social engineering** Attacks that leverage human trust and social behaviors to divulge sensitive information.

**Software as a Service (SaaS)** A cloud service in which the service consists of access to working software, without the need to be concerned about the details of installing and maintaining the software or the servers on which it runs.

**Software-Defined Access** Cisco's intent-based networking (IBN) offering for enterprise networks.

**Software-Defined Networking (SDN)** A branch of networking that emerged in the marketplace in the 2010s characterized by the use of a centralized software controller that takes over varying amounts of the control plane processing formerly done inside networking devices, with the controller directing the networking elements as to what forwarding table entries to put into their forwarding tables.

**SOHO** A classification of a business site with a relatively small number of devices, sometimes in an employee office in their home.

**Source NAT** The type of Network Address Translation (NAT) used most commonly in networks (as compared to destination NAT), in which the source IP address of packets entering an inside interface is translated.

**southbound API** In the area of SDN, a reference to the APIs used between a controller and the network elements for the purpose of learning information from the elements and for programming (controlling) the forwarding behavior of the elements. Also called a southbound interface.

**southbound interface** Another term for southbound API. *See also* [southbound API](vol2_gloss.xhtml#gloss_326).

**spear phishing** Phishing that begins with research about a related group of people so that the attack uses messaging that appears more legitimate by using those researched facts.

**spine** In an ACI network design for a single site, a switch that connects to leaf switches only, for the purpose of receiving frames from one leaf switch and then forwarding the frame to some other leaf switch.

**split-MAC architecture** A wireless AP strategy based around the idea that normal AP functions are split or divided between a wireless LAN controller and lightweight APs.

**spoofing attack** A type of attack in which parameters such as IP and MAC addresses are spoofed with fake values to disguise the sender.

**standalone mode** The operational mode used by a FlexConnect AP when the path back to its controller is down and not working. In this mode, all wireless traffic is switched locally, preserving local connectivity while the AP is isolated from its controller.

**standard access list** A list of IOS global configuration commands that can match only a packet's source IP address for the purpose of deciding which packets to discard and which to allow through the router.

**star topology** A network topology in which endpoints on a network are connected to a common central device by point-to-point links.

**stateless** A protocol or process that does not use information stored from previous transactions to perform the current transaction.

**station (STA)** An 802.11 client device that is associated with a BSS.

**syslog server** A server application that collects syslog messages from many devices over the network and provides a user interface so that IT administrators can view the log messages to troubleshoot problems.

### T

**TCAM** *See* [ternary content-addressable memory](vol2_gloss.xhtml#gloss_339).

**ternary content-addressable memory (TCAM)** A type of physical memory, either in a separate integrated circuit or built into an ASIC, that can store tables and then be searched against a key, such that the search time happens quickly and does not increase as the size of the table increases. TCAMs are used extensively in higher-performance networking devices as the means to store and search forwarding tables in Ethernet switches and higher-performance routers.

**Terraform** An open-source infrastructure as code tool used for provisioning and managing cloud, on-premises, and hybrid infrastructure resources through declarative configuration files.

**TFTP** Trivial File Transfer Protocol. An application protocol that allows files to be transferred from one computer to another over a network, but with only a few features, making the software require little storage space.

**threat** An actual potential to use an exploit to take advantage of a vulnerability.

**Transport Layer Security (TLS)** A security standard that replaced the older Secure Sockets Layer (SSL) protocol, providing functions such as authentication, confidentiality, and message integrity over reliable in-order data streams like TCP.

**trojan horse** Malware that is hidden and packaged inside other legitimate software.

**trusted port** With both the DHCP Snooping and Dynamic ARP Inspection (DAI) switch features, the concept and configuration setting that tells the switch to allow all incoming messages of that respective type, rather than to consider the incoming messages (DHCP and ARP, respectively) for filtering.

**two-tier design** *See* [collapsed core design](vol2_gloss.xhtml#gloss_081).

### U

**underlay** In SDA, the network devices and links that create basic IP connectivity to support the creation of VXLAN tunnels for the overlay.

**Unified Computing System (UCS)** The Cisco brand name for its server hardware products.

**Universal Power over Ethernet (UPoE)** A specific PoE standard as defined in the IEEE 802.3bt amendment to the 802.3 standard, which uses four wire pairs to supply power with a maximum of 60 watts as supplied by the PSE.

**Universal Power over Ethernet Plus (UPoE+)** A specific PoE standard as defined in the IEEE 802.3bt amendment to the 802.3 standard, which uses four wire pairs to supply power with a maximum of 100 watts as supplied by the PSE.

**untrusted port** With both the DHCP Snooping and Dynamic ARP Inspection (DAI) switch features, the concept and configuration setting that tells the switch to analyze each incoming message of that respective type (DHCP and ARP) and apply some rules to decide whether to discard the message.

**UPoE** *See* [Universal Power over Ethernet (UPoE)](vol2_gloss.xhtml#gloss_349).

**URI** Uniform Resource Identifier. The formal and correct term for the formatted text used to refer to objects in an IP network. This text is commonly called a URL or a web address. For example, <http://www.certskills.com/config-labs> is a URI that identifies the protocol (HTTP), hostname ([www.certskills.com](http://www.certskills.com)), and web page (config-labs).

**URI parameters** *See* [URI query (parameters)](vol2_gloss.xhtml#gloss_356).

**URI path (resource)** In a URI, the part that follows the first /, up to the query field (which begins with a ?), which identifies the resource in the context of a server.

**URI query (parameters)** In a URI, the part that follows the first ?, which provides a place to list variable names and values as parameters.

**URI resource** *See* [URI path (resource)](vol2_gloss.xhtml#gloss_355).

**username secret** A reference to the password configured on the **username** *name* **secret** *pass-value* command, which defines a username and an encoded password, used to build a local username/password list on the router or switch.

**UTP Cable Category** A set of standards from the TIA and ANSI that defines the electrical characteristics of UTP cabling under various tests. Ethernet standards then refer to these UTP cable categories to define the minimum category needed to support the Ethernet standard at stated distances.

### V

**violation mode** In port security, a configuration setting that defines the specific set of actions to take on a port when a port security violation occurs. The modes are shutdown, restrict, and protect.

**virtual CPU (vCPU)** In a virtualized server environment, a CPU (processor) core or thread allocated to a virtual machine (VM) by the hypervisor.

**Virtual IP address (VIP)** Used with first hop redundancy protocols, an address, referenced by hosts as their default router, that can move between multiple routers to support failover of the default router function from one router to another.

**virtual machine** An instance of an operating system, running on server hardware that uses a hypervisor to allocate a subset of the server hardware (CPU, RAM, disk, and network) to that VM.

**virtual NIC (vNIC)** In a virtualized server environment, a network interface card (NIC) used by a virtual machine, which then connects to some virtual switch (vSwitch) running on that same host, which in turn connects to a physical NIC on the host.

**virtual private network (VPN)** A set of security protocols that, when implemented by two devices on either side of an unsecure network such as the Internet, can allow the devices to send data securely. VPNs provide privacy, device authentication, anti-replay services, and data integrity services.

**Virtual routing and forwarding (VRF)** Virtual routing and forwarding instance. A feature of routers and Layer 3 switches that makes one router act as multiple routers by assigning interfaces and routing protocol neighbors to specific VRFs, with related routes landing in the associated VRF-unique routing table.

**virtual switch (vSwitch)** A software-only virtual switch inside one host (one hardware server), to provide switching features to the virtual machines running on that host.

**virus** Malware that injects itself into other applications and then propagates through user intervention.

**VPN** *See* [virtual private network](vol2_gloss.xhtml#gloss_365).

**VPN client** Software that resides on a PC, often a laptop, so that the host can implement the protocols required to be an endpoint of a VPN.

**vty ACL** An IP ACL enabled for inbound SSH and Telnet connections to a router or for outbound requests per the **ssh** and **telnet** commands issued by a user who is already connected to the router using SSH or Telnet.

**vulnerability** A weakness that can be used to compromise security.

**VXLAN** Virtual Extensible LAN. A flexible encapsulation protocol used for creating tunnels (overlays).

### W

**watering hole attack** An attack where a site frequently visited by a group of users is compromised; when the target users visit the site, they will be infected with malware, but other users will not.

**web server** Software, running on a computer, that stores web pages and sends those web pages to web clients (web browsers) that request the web pages.

**whaling** Spear phishing that targets high-profile individuals.

**wildcard mask** The mask used in Cisco IOS ACL commands and OSPF and EIGRP **network** commands.

**wireless LAN controller (WLC)** A device that cooperates with wireless lightweight access points (LWAP) to create a wireless LAN by performing some control functions for each LWAP and forwarding data between each LWAP and the wired LAN.

**workgroup bridge (WGB)** An AP that is configured to bridge between a wired device and a wireless network. The WGB acts as a wireless client.

**worm** Malware that propagates from one system to another, infecting as it goes, all autonomously.

**write community** *See* [read-write community](vol2_gloss.xhtml#gloss_282).

### X–Y–Z

**XML (eXtensible Markup Language)** A markup language that helps enable dynamic web pages; also useful as a data serialization language.

**YAML (YAML Ain't Markup Language)** A data serialization language that can be easily read by humans; used by Ansible.

**Zero Touch Provisioning (ZTP)** An automated deployment process that enables the remote configuration and setup of network devices without requiring manual intervention, allowing for seamless and efficient network deployment at scale.