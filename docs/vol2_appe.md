# Appendix E


## Practice for Chapter 6: Basic IPv4 Access Control Lists

### Practice Problems

This appendix includes two sets of practice problems. The first question set lists requirements for a single-line access control list (ACL), with your task being to create a standard numbered ACL that meets the requirements. The second question set shows an existing **access-list** command, with your job being to determine the range of IP addresses matched by the ACL.

Note that you can find additional practice on the author's blog, which is linked from the author's website, [www.certskills.com](http://www.certskills.com).

#### Practice Building access-list Commands

[Table E-1](vol2_appe.xhtml#appetab01) lists the criteria for several practice problems. Your job: Create a one-line standard ACL that matches the packets. The answers are listed later in this appendix.

**Table E-1** Building One-Line Standard ACLs: Practice

| Problem | Criteria |
| --- | --- |
| 1 | Packets from 10.1.1.1 |
| 2 | Packets from hosts with 10.1.1 as the first 3 octets |
| 3 | Packets from hosts with 10.1 as the first 2 octets |
| 4 | Packets from any host |
| 5 | Packets from subnet 192.168.3.128/29 |
| 6 | Packets from subnet 192.168.3.192/28 |
| 7 | Packets from subnet 192.168.3.64/27 |
| 8 | Packets from subnet 172.20.192.192/26 |
| 9 | Packets from subnet 172.20.200.0/22 |
| 10 | Packets from subnet 172.20.203.0/25 |
| 11 | Packet from subnet 192.168.99.0/30 |
| 12 | Packet from subnet 192.168.99.0/28 |
| 13 | Packet from subnet 172.28.28.0/23 |
| 14 | Packet from subnet 172.28.28.0/22 |
| 15 | Packet from subnet 172.28.28.0/24 |

#### Reverse Engineering from ACL to Address Range

For this second question set, look at the existing **access-list** commands in [Table E-2](vol2_appe.xhtml#appetab02). In each case, make a notation about the exact IP address, or range of IP addresses, matched by the command.

**Table E-2** Finding IP Addresses/Ranges Matching by Existing ACLs

| Problem | Commands for Which to Predict the Source Address Range |
| --- | --- |
| 1 | **access-list 1 permit 192.168.4.5** |
| 2 | **access-list 2 permit 192.168.4.128 0.0.0.3** |
| 3 | **access-list 3 permit 192.168.4.128 0.0.0.127** |
| 4 | **access-list 4 permit 172.25.96.0 0.0.0.255** |
| 5 | **access-list 5 permit 192.168.4.128 0.0.0.31** |
| 6 | **access-list 6 permit 192.168.4.128 0.0.0.7** |
| 7 | **access-list 7 permit 172.25.96.0 0.0.7.255** |
| 8 | **access-list 8 permit 172.25.96.0 0.0.0.63** |
| 9 | **access-list 9 permit 10.10.16.0 0.0.7.255** |
| 10 | **access-list 10 permit 10.10.16.0 0.0.0.127** |
| 11 | **access-list 11 permit 192.168.17.112 0.0.0.7** |
| 12 | **access-list 12 permit 192.168.17.112 0.0.0.15** |
| 13 | **access-list 13 permit 172.19.200.0 0.0.0.63** |
| 14 | **access-list 14 permit 172.19.200.0 0.0.1.255** |
| 15 | **access-list 15 permit 10.1.0.0 0.0.255.255** |

Note

You can only rely on the method of adding these numbers together (as shown in [Chapter 6](vol2_ch06.xhtml#ch06), "[Basic IPv4 Access Control Lists](vol2_ch06.xhtml#ch06)") if you know that the **access-list** command comes from the router and specifically is not what someone simply wrote on a piece of paper. In this case, you can assume that the statements in [Table E-2](vol2_appe.xhtml#appetab02) came from a router.

### Answers to Earlier Practice Problems

This section contains the answers to the two sets of practice problems.

#### Answers: Practice Building access-list Commands

[Table E-3](vol2_appe.xhtml#appetab03) lists the answers to the problems listed in [Table E-1](vol2_appe.xhtml#appetab01).

**Table E-3** Building One-Line Standard ACLs: Answers

| Problem | Answer |
| --- | --- |
| 1 | **access-list 1 permit 10.1.1.1** |
| 2 | **access-list 2 permit 10.1.1.0 0.0.0.255** |
| 3 | **access-list 3 permit 10.1.0.0 0.0.255.255** |
| 4 | **access-list 4 permit any** |
| 5 | **access-list 5 permit 192.168.3.128 0.0.0.7** |
| 6 | **access-list 6 permit 192.168.3.192 0.0.0.15** |
| 7 | **access-list 7 permit 192.168.3.64 0.0.0.31** |
| 8 | **access-list 8 permit 172.20.192.192 0.0.0.63** |
| 9 | **access-list 9 permit 172.20.200.0 0.0.3.255** |
| 10 | **access-list 10 permit 172.20.203.0 0.0.0.127** |
| 11 | **access-list 11 permit 192.168.99.0 0.0.0.3** |
| 12 | **access-list 12 permit 192.168.99.0 0.0.0.15** |
| 13 | **access-list 13 permit 172.28.28.0 0.0.1.255** |
| 14 | **access-list 14 permit 172.28.28.0 0.0.3.255** |
| 15 | **access-list 15 permit 172.28.28.0 0.0.0.255** |

#### Answers: Reverse Engineering from ACL to Address Range

[Table E-4](vol2_appe.xhtml#appetab04) lists the answers to the problems listed in [Table E-2](vol2_appe.xhtml#appetab02).

**Table E-4** Address Ranges for Problems in [Table E-2](vol2_appe.xhtml#appetab02): Answers

| Problem | Address Range |
| --- | --- |
| 1 | One address: 192.168.4.5 |
| 2 | 192.168.4.128 – 192.168.4.131 |
| 3 | 192.168.4.128 – 192.168.4.255 |
| 4 | 172.25.96.0 – 172.25.96.255 |
| 5 | 192.168.4.128 – 192.168.4.159 |
| 6 | 192.168.4.128 – 192.168.4.135 |
| 7 | 172.25.96.0 – 172.25.103.255 |
| 8 | 172.25.96.0 – 172.25.96.63 |
| 9 | 10.10.16.0 – 10.10.23.255 |
| 10 | 10.10.16.0 – 10.10.16.127 |
| 11 | 192.168.17.112 – 192.168.17.119 |
| 12 | 192.168.17.112 – 192.168.17.127 |
| 13 | 172.19.200.0 – 172.19.200.63 |
| 14 | 172.19.200.0 – 172.19.201.255 |
| 15 | 10.1.0.0 – 10.1.255.255 |