# Part IV


# IPv4 Addressing

[**Chapter 11:** Perspectives on IPv4 Subnetting](vol1_ch11.xhtml#ch11)

[**Chapter 12:** Analyzing Classful IPv4 Networks](vol1_ch12.xhtml#ch12)

[**Chapter 13:** Analyzing Subnet Masks](vol1_ch13.xhtml#ch13)

[**Chapter 14:** Analyzing Existing Subnets](vol1_ch14.xhtml#ch14)

[**Chapter 15:** Subnet Design](vol1_ch15.xhtml#ch15)

[**Part IV Review**](vol1_part-p04.xhtml#part-p04)

The book makes a big transition at this point. [Part I](vol1_part01.xhtml#part01) gave you a broad introduction to networking, and [Parts II](vol1_part02.xhtml#part02) and [III](vol1_part03.xhtml#part03) went into some detail about the dominant LAN technology today: Ethernet. [Part IV](vol1_part04.xhtml#part04) transitions from Ethernet to the network layer details that sit above Ethernet and WAN technology, specifically IP version 4 (IPv4).

Thinking about the network layer requires engineers to shift how they think about addressing. Ethernet allows the luxury of using universal MAC addresses, assigned by the manufacturers, with no need to plan or configure addresses. Although the network engineer needs to understand MAC addresses, MAC already exists on each Ethernet NIC, and switches learn the Ethernet MAC addresses dynamically without even needing to be configured to do so. As a result, most people operating the network can ignore the specific MAC address values for most tasks.

Conversely, IP addressing gives you flexibility and allows choice; however, those features require planning, along with a much deeper understanding of the internal structure of the addresses. People operating the network must be more aware of the network layer addresses when doing many tasks. To better prepare you for these Layer 3 addressing details, this part breaks down the addressing details into five chapters, with an opportunity to learn more in preparation for the CCNP Enterprise certification.

[Part IV](vol1_part04.xhtml#part04) examines most of the basic details of IPv4 addressing and subnetting, mostly from the perspective of operating an IP network. [Chapter 11](vol1_ch11.xhtml#ch11) takes a grand tour of IPv4 addressing as implemented inside a typical enterprise network. [Chapters 12](vol1_ch12.xhtml#ch12) through [15](vol1_ch15.xhtml#ch15) look at some of the specific questions people must ask themselves when operating an IPv4 network.

This section includes all the details you need to learn for the CCNA 200-301 V1.1 blueprint's IPv4 addressing and subnetting exam topics. Many people have learned subnetting from these chapters over the years; however, some people have asked for video and more practice with subnetting—and understandably so. If that's you, consider these additional products as well, both of which can be found at [ciscopress.com](http://ciscopress.com):

IP Subnetting: From Beginning to Mastery (Video Course)

IP Subnetting Practice Question Kit (Practice Questions Product)

We mention these here before you begin [Part IV](vol1_part04.xhtml#part04) because, if you decide to use them, you might want to use them alongside the chapters in this part.