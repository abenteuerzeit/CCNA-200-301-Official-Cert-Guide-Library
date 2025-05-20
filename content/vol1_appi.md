# Appendix I


## Practice for Chapter 27: Implementing IPv6 Addressing on Routers

This appendix provides practice problems for two types of addresses: unicast addresses formed with the EUI-64 feature and solicited node multicast addresses. With EUI-64, you take the 64-bit (16 hex digit) prefix and a MAC address, manipulate the MAC address into a 64-bit value, and use those 64 bits as the interface ID. Solicited node multicast addresses are formed from a standard 26 hex digit prefix, combined with the same last 6 hex digits as the unicast address.

### EUI-64 and Solicited Node Multicast Problems

[Table I-1](vol1_appi.md#appitab01) lists some practice problems. Each problem lists a prefix and a MAC address. Then, in [Table I-2](vol1_appi.md#appitab02), record your answers for the unicast IPv6 address, assuming that EUI-64 rules are used. Also in [Table I-2](vol1_appi.md#appitab02), list the solicited node multicast address associated with your calculated unicast address.

**Table I-1** IPv6 EUI-64 Unicast and Solicited Node Multicast Problems

|  | Prefix | MAC Address |
| --- | --- | --- |
| 1 | 2987:BA11:B011:B00A::/64 | 0000.1234.5678 |
| 2 | 3100:0000:0000:1010::/64 | 1234.5678.9ABC |
| 3 | FD00:0001:0001:0001::/64 | 0400.AAAA.0001 |
| 4 | FDDF:8080:0880:1001::/64 | 0611.BABA.DADA |
| 5 | 32CC:0000:0000:000D::/64 | 0000.0000.0001 |
| 6 | 2100:000E:00E0:0000::/64 | 0505.0505.0707 |
| 7 | 3A11:CA00:0000:0000::/64 | 0A0A.B0B0.0C0C |
| 8 | 3799:9F9F:F000:0000::/64 | F00F.0005.0041 |
| 9 | 2A2A:0000:0000:0000::/64 | 0200.0101.0101 |
| 10 | 3194:0000:0000:0000::/64 | 0C0C.000C.00CC |




**Table I-2** Blank Answer Table for Problems in [Table I-1](vol1_appi.md#appitab01)

|  | Unicast Address Using EUI-64 | Solicited Node Multicast Address |
| --- | --- | --- |
| 1 |  |  |
| 2 |  |  |
| 3 |  |  |
| 4 |  |  |
| 5 |  |  |
| 6 |  |  |
| 7 |  |  |
| 8 |  |  |
| 9 |  |  |
| 10 |  |  |

For each answer, use the best abbreviation, instead of a full 32-digit address.

The answers sit at the end of the appendix, in [Table I-3](vol1_appi.md#appitab03).

### Answers to EUI-64 and Solicited Node Multicast Problems

[Table I-3](vol1_appi.md#appitab03) lists the answers to the problems listed earlier in [Table I-1](vol1_appi.md#appitab01).

**Table I-3** Answers to Problems in [Table I-1](vol1_appi.md#appitab01)

|  | Unicast Address Using EUI-64 | Solicited Node Multicast Address |
| --- | --- | --- |
| 1 | 2987:BA11:B011:B00A:200:12FF:FE34:5678 | FF02::01:FF34.5678 |
| 2 | 3100::1010:1034:56FF:FE78:9ABC | FF02::01:FF78.9ABC |
| 3 | FD00:1:1:1:600:AAFF:FEAA:1 | FF02::01:FFAA:1 |
| 4 | FDDF:8080:880:1001:411:BAFF:FEBA:DADA | FF02::01:FFBA:DADA |
| 5 | 32CC::D:200:FF:FE00:1 | FF02::01:FF00:1 |
| 6 | 2100:E:E0:0:705:5FF:FE05:707 | FF02::01:FF05:707 |
| 7 | 3A11:CA00::80A:B0FF:FEB0:C0C | FF02::01:FFB0:C0C |
| 8 | 3799:9F9F:F000:0:F20F:FF:FE05:41 | FF02::01:FF05:41 |
| 9 | 2A2A::1FF:FE01:101 | FF02::01:FF01:101 |
| 10 | 3194::E0C:FF:FE0C:CC | FF02::01:FF0C:CC |