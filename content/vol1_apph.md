# Appendix H


## Practice for Chapter 25: Fundamentals of IP Version 6

This appendix provides extra practice problems for two topics discussed in [Chapter 25](vol1_ch25.md#ch25), "[Fundamentals of IP Version 6](vol1_ch25.md#ch25)," of the book. The first problems let you convert from a full 32-digit IPv6 address to its abbreviated form, or to do the reverse. The second set of problems begins with IPv6 addresses and prefix lengths, asking you to determine the IPv6 prefix (subnet).

### Address Abbreviating and Expanding Problems

[Chapter 25](vol1_ch25.md#ch25) discusses some reasons why you may need to be able to mentally convert from the full 32-digit IPv6 address to the abbreviated form, or vice versa. The practice problems in this section simply provide more opportunities to practice.

[Table H-1](vol1_apph.md#apphtab01) lists some practice problems, with the full 32-digit IPv6 address on the left and the best abbreviation on the right. The table gives you either the expanded or abbreviated address, and you need to supply the opposite value. The answers sit at the end of the appendix, in the section "[Answers to Address Abbreviating and Expanding Problems](vol1_apph.md#apphlev1sec3)."

**Table H-1** IPv6 Address Abbreviation and Expansion Practice

|  | Full | Abbreviation |
| --- | --- | --- |
| 1 | 2987:BA11:B011:B00A:1000:0001:F001:F003 |  |
| 2 |  | 3100::1010:D00D:D000:D00B:B00D |
| 3 | FD00:0001:0001:0001:0200:00FF:FE00:0001 |  |
| 4 |  | FDDF:8080:880:1001:0:FF:FE01:507 |
| 5 | 32CC:0000:0000:000D:210F:0000:0000:0000 |  |
| 6 |  | 2100:E:E0::E00 |
| 7 | 3A11:CA00:0000:0000:0000:00FF:FECC:000C |  |
| 8 |  | 3799:9F9F:F000:0:FFFF::1 |
| 9 | 2A2A:0000:0000:0000:0000:0000:0000:2A2A |  |
| 10 |  | 3194::1:0:0:101 |
| 11 | 2001:0DB8:0000:0000:0001:0000:0002:0100 |  |
| 12 |  | 2001:DB8::10:A000 |
| 13 | 3330:0000:0000:0100:0000:0002:0000:0003 |  |
| 14 |  | FD00::1000:2000:0:1:20 |
| 15 | FD11:1000:0100:0010:0001:0000:1000:0100 |  |
| 16 |  | 2000::2 |

### Calculating the IPv6 Prefix Problems

Routers take the interface IPv6 address configuration and add a connected IPv6 route to the IPv6 routing table, for the IPv6 prefix (subnet) connected to that interface. This section provides some practice problems so that you can do the same math and predict the prefix value that the router will add to the routing table.

[Table H-2](vol1_apph.md#apphtab02) lists practice problems that all use the same prefix length (/64), which is the most common prefix length you see. [Table H-3](vol1_apph.md#apphtab03) that follows lists additional practice problems, with prefix lengths other than /64.

**Table H-2** Finding the IPv6 Prefix When Using a /64 Prefix Length

|  | Address (Assume a /64 Prefix Length) | Prefix (Subnet) |
| --- | --- | --- |
| 1 | 2987:BA11:B011:B00A:1000:0001:F001:F003 |  |
| 2 | 3100:0000:0000:1010:D00D:D000:D00B:B00D |  |
| 3 | FD00:0001:0001:0001:0200:00FF:FE00:0001 |  |
| 4 | FDDF:8080:0880:1001:0000:00FF:FE01:0507 |  |
| 5 | 32CC:0000:0000:000D:210F:0000:0000:0000 |  |
| 6 | 2100:000E:00E0:0000:0000:0000:0000:0E00 |  |
| 7 | 3A11:CA00:0000:0000:0000:00FF:FECC:000C |  |
| 8 | 3799:9F9F:F000:0000:FFFF:0000:0000:0001 |  |
| 9 | 2A2A:0000:0000:0000:0000:0000:0000:2A2A |  |
| 10 | 3194:0000:0000:0000:0001:0000:0000:0101 |  |
| 11 | 2001:0DB8:0000:0000:0001:0000:0002:0100 |  |
| 12 | 2001:0DB8:0000:0000:0000:0000:0010:A000 |  |
| 13 | 3330:0000:0000:0100:0000:0002:0000:0003 |  |
| 14 | FD00:0000:0000:1000:2000:0000:0001:0020 |  |
| 15 | FD11:1000:0100:0010:0001:0000:1000:0100 |  |
| 16 | 2000:0000:0000:0000:0000:0000:0000:0002 |  |




**Table H-3** Finding the IPv6 Prefix Using a Prefix Length Other Than /64

|  | Address | Prefix (Subnet) |
| --- | --- | --- |
| 1 | 2987:BA11:B011:B00A:1000:0001:F001:F003 /60 |  |
| 2 | 3100:0000:0000:1010:D00D:D000:D00B:B00D /56 |  |
| 3 | FD00:0001:0001:0001:0200:00FF:FE00:0001 /52 |  |
| 4 | FDDF:8080:0880:1001:0000:00FF:FE01:0507 /48 |  |
| 5 | 32CC:0000:0000:000D:210F:0000:0000:0000 /44 |  |
| 6 | 2100:000E:00E0:0000:0000:0000:0000:0E00 /60 |  |
| 7 | 3A11:CA00:0000:0000:0000:00FF:FECC:000C /56 |  |
| 8 | 3799:9F9F:F000:0000:FFFF:0000:0000:0001 /52 |  |
| 9 | 2A2A:0000:0000:0000:0000:0000:0000:2A2A /48 |  |
| 10 | 3194:0000:0000:0000:0001:0000:0000:0101 /44 |  |

### Answers to Address Abbreviating and Expanding Problems

[Table H-4](vol1_apph.md#apphtab04) lists the answers to the problems listed earlier in [Table H-1](vol1_apph.md#apphtab01).

**Table H-4** Answers: IPv6 Address Abbreviation and Expansion Practice

|  | Full | Abbreviation |
| --- | --- | --- |
| 1 | 2987:BA11:B011:B00A:1000:0001:F001:F003 | 2987:BA11:B011:B00A:1000:1:F001:F003 |
| 2 | 3100:0000:0000:1010:D00D:D000:D00B:B00D | 3100::1010:D00D:D000:D00B:B00D |
| 3 | FD00:0001:0001:0001:0200:00FF:FE00:0001 | FD00:1:1:1:200:FF:FE00:1 |
| 4 | FDDF:8080:0880:1001:0000:00FF:FE01:0507 | FDDF:8080:880:1001:0:FF:FE01:507 |
| 5 | 32CC:0000:0000:000D:210F:0000:0000:0000 | 32CC:0:0:D:210F:: |
| 6 | 2100:000E:00E0:0000:0000:0000:0000:0E00 | 2100:E:E0::E00 |
| 7 | 3A11:CA00:0000:0000:0000:00FF:FECC:000C | 3A11:CA00::FF:FECC:C |
| 8 | 3799:9F9F:F000:0000:FFFF:0000:0000:0001 | 3799:9F9F:F000:0:FFFF::1 |
| 9 | 2A2A:0000:0000:0000:0000:0000:0000:2A2A | 2A2A::2A2A |
| 10 | 3194:0000:0000:0000:0001:0000:0000:0101 | 3194::1:0:0:101 |
| 11 | 2001:0DB8:0000:0000:0001:0000:0002:0100 | 2001:DB8::1:0:2:100 |
| 12 | 2001:0DB8:0000:0000:0000:0000:0010:A000 | 2001:DB8::10:A000 |
| 13 | 3330:0000:0000:0100:0000:0002:0000:0003 | 3330::100:0:2:0:3 |
| 14 | FD00:0000:0000:1000:2000:0000:0001:0020 | FD00::1000:2000:0:1:20 |
| 15 | FD11:1000:0100:0010:0001:0000:1000:0100 | FD11:1000:100:10:1:0:1000:100 |
| 16 | 2000:0000:0000:0000:0000:0000:0000:0002 | 2000::2 |

### Answers to Calculating IPv6 Prefix Problems

[Tables H-5](vol1_apph.md#apphtab05) and [H-6](vol1_apph.md#apphtab06) list the answers to the problems listed earlier in [Tables H-2](vol1_apph.md#apphtab02) and [H-3](vol1_apph.md#apphtab03).

**Table H-5** Answers: Finding the IPv6 Prefix, with a /64 Prefix Length

|  | Address (Assume a /64 Prefix Length) | Prefix (Subnet) |
| --- | --- | --- |
| 1 | 2987:BA11:B011:B00A:1000:0001:F001:F003 | 2987:BA11:B011:B00A::/64 |
| 2 | 3100:0000:0000:1010:D00D:D000:D00B:B00D | 3100:0:0:1010::/64 |
| 3 | FD00:0001:0001:0001:0200:00FF:FE00:0001 | FD00:1:1:1::/64 |
| 4 | FDDF:8080:0880:1001:0000:00FF:FE01:0507 | FDDF:8080:880:1001::/64 |
| 5 | 32CC:0000:0000:000D:210F:0000:0000:0000 | 32CC:0:0:D::/64 |
| 6 | 2100:000E:00E0:0000:0000:0000:0000:0E00 | 2100:E:E0::/64 |
| 7 | 3A11:CA00:0000:0000:0000:00FF:FECC:000C | 3A11:CA00::/64 |
| 8 | 3799:9F9F:F000:0000:FFFF:0000:0000:0001 | 3799:9F9F:F000::/64 |
| 9 | 2A2A:0000:0000:0000:0000:0000:0000:2A2A | 2A2A::/64 |
| 10 | 3194:0000:0000:0000:0001:0000:0000:0101 | 3194::/64 |
| 11 | 2001:0DB8:0000:0000:0001:0000:0002:0100 | 2001:DB8::/64 |
| 12 | 2001:0DB8:0000:0000:0000:0000:0010:A000 | 2001:DB8::/64 |
| 13 | 3330:0000:0000:0100:0000:0002:0000:0003 | 3330:0:0:100::/64 |
| 14 | FD00:0000:0000:1000:2000:0000:0001:0020 | FD00:0:0:1000::/64 |
| 15 | FD11:1000:0100:0010:0001:0000:1000:0100 | FD11:1000:100:10::/64 |
| 16 | 2000:0000:0000:0000:0000:0000:0000:0002 | 2000::/64 |





**Table H-6** Answers: Finding the IPv6 Prefix, with Other Prefix Lengths

|  | Address | Prefix (Subnet) |
| --- | --- | --- |
| 1 | 2987:BA11:B011:B00A:1000:0001:F001:F003 /60 | 2987:BA11:B011:B000::/60 |
| 2 | 3100:0000:0000:1010:D00D:D000:D00B:B00D /56 | 3100:0:0:1000::/56 |
| 3 | FD00:0001:0001:0001:0200:00FF:FE00:0001 /52 | FD00:1:1::/52 |
| 4 | FDDF:8080:0880:1001:0000:00FF:FE01:0507 /48 | FDDF:8080:880::/48 |
| 5 | 32CC:0000:0000:000D:210F:0000:0000:0000 /44 | 32CC::/44 |
| 6 | 2100:000E:00E0:0000:0000:0000:0000:0E00 /60 | 2100:E:E0::/60 |
| 7 | 3A11:CA00:0000:0000:0000:00FF:FECC:000C /56 | 3A11:CA00::/56 |
| 8 | 3799:9F9F:F000:0000:FFFF:0000:0000:0001 /52 | 3799:9F9F:F000::/52 |
| 9 | 2A2A:0000:0000:0000:0000:0000:0000:2A2A /48 | 2A2A::/48 |
| 10 | 3194:0000:0000:0000:0001:0000:0000:0101 /44 | 3194::/44 |