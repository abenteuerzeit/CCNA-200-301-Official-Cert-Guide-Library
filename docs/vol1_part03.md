# Part III


# Implementing VLANs and STP

[**Chapter 8:** Implementing Ethernet Virtual LANs](vol1_ch08.xhtml#ch08)

[**Chapter 9:** Spanning Tree Protocol Concepts](vol1_ch09.xhtml#ch09)

[**Chapter 10:** RSTP and EtherChannel Configuration](vol1_ch10.xhtml#ch10)

[**Part III Review**](vol1_part-p03.xhtml#part-p03)

[Part II](vol1_part02.xhtml#part02) of this book introduces the basics of Ethernet LANs, both in concept and in how to implement the features. However, the two primary features discussed in [Part III](vol1_part03.xhtml#part03) of this book—Virtual LANs (VLANs) and Spanning Tree Protocol (STP)—impact almost everything you have learned about Ethernet so far.

VLANs allow a network engineer to create separate Ethernet LANs through simple configuration choices. The ability to separate some switch ports into one VLAN and other switch ports into another VLAN gives network designers a powerful tool for creating networks. Once created, VLANs also have a huge impact on how a switch works, which then impacts how you verify and troubleshoot the operation of a campus LAN.

The two VLAN-related exam topics (2.1 and 2.2) use the verbs *configure* and *verify*. To support that depth, [Chapter 8](vol1_ch08.xhtml#ch08) opens this part with details about the concepts related to VLANs, VLAN trunks, and EtherChannels. It then shows a variety of configuration options, sprinkled with some troubleshooting topics.

STP acts to prevent frames from looping repeatedly around a LAN that has redundant links. Without STP, switches would forward broadcasts and some other frames around and around the LAN, eventually clogging the LAN so much as to make it unusable.

The CCNA 200-301 version 1.1 exam blueprint refers to STP using only topic 2.5. That topic uses the plural phrase *Spanning Tree Protocols*, in reference to the original Spanning Tree Protocol (STP) and its replacement Rapid STP (RSTP). That exam topic uses the verb *identify*, which places more importance on interpreting STP operations using **show** commands rather than every configuration option.

As for this part of the book, [Chapter 9](vol1_ch09.xhtml#ch09) focuses on STP concepts, with [Chapter 10](vol1_ch10.xhtml#ch10) focusing on configuration and verification—but with emphasis on interpreting STP behavior. It also discusses Layer 2 EtherChannel configuration.