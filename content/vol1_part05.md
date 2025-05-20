# Part V


# IPv4 Routing

[**Chapter 16:** Operating Cisco Routers](vol1_ch16.md#ch16)

[**Chapter 17:** Configuring IPv4 Addresses and Static Routes](vol1_ch17.md#ch17)

[**Chapter 18:** IP Routing in the LAN](vol1_ch18.md#ch18)

[**Chapter 19:** IP Addressing on Hosts](vol1_ch19.md#ch19)

[**Chapter 20:** Troubleshooting IPv4 Routing](vol1_ch20.md#ch20)

[**Part V Review**](vol1_part-p05.md#part-p05)

[Parts V](vol1_part05.md#part05) and [VI](vol1_part06.md#part06) work together to reveal the details of how to implement IPv4 routing in Cisco routers. To that end, [Part V](vol1_part05.md#part05) focuses on the most common features for Cisco routers, including IP address configuration, connected routes, and static routes. [Part VI](vol1_part06.md#part06) then goes into some detail about the one IP routing protocol discussed in this book: OSPF Version 2 (OSPFv2).

[Part V](vol1_part05.md#part05) follows a progression of topics. First, [Chapter 16](vol1_ch16.md#ch16) examines the fundamentals of routers--the physical components, how to access the router command-line interface (CLI), and the configuration process. [Chapter 16](vol1_ch16.md#ch16) makes a close comparison of the switch CLI and its basic administrative commands so that you need to learn only new commands that apply to routers but not to switches.

[Chapter 17](vol1_ch17.md#ch17) then moves on to discuss how to configure routers to route IPv4 packets in the most basic designs. Those designs require a simple IP address/mask configuration on each interface, with the addition of a static route command--a command that directly configures a route into the IP routing table--for each destination subnet.

[Chapter 18](vol1_ch18.md#ch18) continues the progression into more challenging but more realistic configurations related to routing between subnets in a LAN environment. Most LANs use many VLANs, with one subnet per VLAN. Cisco routers and switches can be configured to route packets between those subnets, with more than a few twists in the configuration.

[Chapter 19](vol1_ch19.md#ch19) moves the focus from routers to hosts. Hosts rely on a working internetwork of routers, but the hosts need IP settings as well, with an IP address, mask, default gateway, and DNS server list. This chapter examines how hosts can dynamically learn these IP settings using Dynamic Host Configuration Protocol (DHCP), and the role the routers play in that process. The chapter also shows how to display and understand IP settings on hosts.

Finally, [Part V](vol1_part05.md#part05) closes with a chapter about troubleshooting IPv4 routing. [Chapter 20](vol1_ch20.md#ch20) features the **ping** and **traceroute** commands, two commands that can help you discover not only whether a routing problem exists but also where the problem exists. The other chapters show how to confirm whether a route has been added to one router's routing table, while the commands discussed in [Chapter 20](vol1_ch20.md#ch20) teach you how to test the end-to-end routes from sending host to receiving host.