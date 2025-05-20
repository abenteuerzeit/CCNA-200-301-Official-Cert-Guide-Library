# Appendix F


## Practice for Chapter 14: Analyzing Existing Subnets

### Practice Problems

This appendix lists practice problems related to [Chapter 14](vol1_ch14.md#ch14), "[Analyzing Existing Subnets](vol1_ch14.md#ch14)." Each problem asks you to find a variety of information about the subnet in which an IP address resides. Each problem supplies an IP address and a subnet mask, from which you should find the following information:

* Subnet number
* Subnet broadcast address
* Range of valid IP addresses in this network

To find these facts, you can use any of the processes explained in [Chapter 14](vol1_ch14.md#ch14).

In addition, these same problems can be used to review the concepts in [Chapter 13](vol1_ch13.md#ch13), "[Analyzing Subnet Masks](vol1_ch13.md#ch13)." To use these same problems for practice related to [Chapter 13](vol1_ch13.md#ch13), simply find the following information for each of the problems:

* Size of the network part of the address
* Size of the subnet part of the address
* Size of the host part of the address
* Number of hosts per subnet
* Number of subnets in this network

Feel free to either ignore or use the opportunity for more practice related to analyzing subnet masks.

Solve for the following problems:

1. 10.180.10.18, mask 255.192.0.0
2. 10.200.10.18, mask 255.224.0.0
3. 10.100.18.18, mask 255.240.0.0
4. 10.100.18.18, mask 255.248.0.0
5. 10.150.200.200, mask 255.252.0.0
6. 10.150.200.200, mask 255.254.0.0
7. 10.220.100.18, mask 255.255.0.0
8. 10.220.100.18, mask 255.255.128.0
9. 172.31.100.100, mask 255.255.192.0
10. 172.31.100.100, mask 255.255.224.0
11. 172.31.200.10, mask 255.255.240.0
12. 172.31.200.10, mask 255.255.248.0
13. 172.31.50.50, mask 255.255.252.0
14. 172.31.50.50, mask 255.255.254.0
15. 172.31.140.14, mask 255.255.255.0
16. 172.31.140.14, mask 255.255.255.128
17. 192.168.15.150, mask 255.255.255.192
18. 192.168.15.150, mask 255.255.255.224
19. 192.168.100.100, mask 255.255.255.240
20. 192.168.100.100, mask 255.255.255.248
21. 192.168.15.230, mask 255.255.255.252
22. 10.1.1.1, mask 255.248.0.0
23. 172.16.1.200, mask 255.255.240.0
24. 172.16.0.200, mask 255.255.255.192
25. 10.1.1.1, mask 255.0.0.0

### Answers

This section includes the answers to the 25 problems listed in this appendix. The answer section for each problem explains how to use the process outlined in [Chapter 14](vol1_ch14.md#ch14) to find the answers. Also, refer to [Chapter 13](vol1_ch13.md#ch13) for details on how to find information about analyzing the subnet mask.

#### Answer to Problem 1

The answers begin with the analysis of the three parts of the address, the number of hosts per subnet, and the number of subnets of this network using the stated mask, as outlined in [Table F-1](vol1_appf.md#appftab01). The binary math for subnet and broadcast address calculation follows. The answer finishes with the easier mental calculations for the range of IP addresses in the subnet.

**Table F-1** Question 1: Size of Network, Subnet, Host, Number of Subnets, and Number of Hosts

| Item | Example | Rules to Remember |
| --- | --- | --- |
| Address | 10.180.10.18 | -- |
| Mask | 255.192.0.0 | -- |
| Number of network bits | 8 | Always defined by Class A, B, C |
| Number of host bits | 22 | Always defined as number of binary 0s in mask |
| Number of subnet bits | 2 | 32 - (network size + host size) |
| Number of subnets | 22 = 4 | 2number-of-subnet-bits |
| Number of hosts | 222 - 2 = 4,194,302 | 2number-of-host-bits - 2 |

[Table F-2](vol1_appf.md#appftab02) contains the important binary calculations for finding the subnet number and subnet broadcast address. To calculate the subnet number, perform a Boolean AND on the address and mask. To find the broadcast address for this subnet, change all the host bits to binary 1s in the subnet number. The host bits are in **bold** print in the table.

**Table F-2** Question 1: Binary Calculation of Subnet and Broadcast Addresses

|  |  |  |
| --- | --- | --- |
| Address | 10.180.10.18 | `00001010 10110100 00001010 00010010` |
| Mask | 255.192.0.0 | `11111111 11000000 00000000 00000000` |
| AND result (subnet number) | 10.128.0.0 | `00001010 10000000 00000000 00000000` |
| Change host to 1s (broadcast address) | 10.191.255.255 | `00001010 10111111 11111111 11111111` |

To get the first valid IP address, just add 1 to the subnet number; to get the last valid IP address, just subtract 1 from the broadcast address. In this case:

10.128.0.1 through 10.191.255.254

10.128.0.0 + 1 = 10.128.0.1

10.191.255.255 - 1 = 10.191.255.254

Alternatively, you can use the processes that only use decimal math to find the subnet and broadcast address. The key parts of the process are as follows:

* The interesting octet is the octet for which the mask's value is not a decimal 0 or 255.
* The magic number is calculated as the value of the IP address's interesting octet, subtracted from 256.
* The subnet number can be found by copying the IP address octets to the left of the interesting octet, by writing down 0s for octets to the right of the interesting octet, and by finding the multiple of the magic number closest to, but not larger than, the IP address's value in that same octet.
* The broadcast address can be similarly found by copying the subnet number's octets to the left of the interesting octet, by writing 255s for octets to the right of the interesting octet, and by taking the subnet number's value in the interesting octet, adding the magic number, and subtracting 1.

[Table F-3](vol1_appf.md#appftab03) shows the work for this problem, with some explanation of the work following the table. Refer to [Chapter 14](vol1_ch14.md#ch14) for the detailed processes.




**Table F-3** Question 1: Subnet, Broadcast, and First and Last Addresses Calculated Using the Subnet Chart

|  | Octet 1 | Octet 2 | Octet 3 | Octet 4 | Comments |
| --- | --- | --- | --- | --- | --- |
| **Mask** | 255 | 192 | 0 | 0 |  |
| **Address** | 10 | 180 | 10 | 18 |  |
| **Subnet Number** | 10 | 128 | 0 | 0 | Magic number = 256 - 192 = 64 |
| **First Address** | 10 | 128 | 0 | 1 | Add 1 to last octet of subnet |
| **Last Address** | 10 | 191 | 255 | 254 | Subtract 1 from last octet of broadcast |
| **Broadcast** | 10 | 191 | 255 | 255 | 128 + 64 - 1 = 191 |

This subnetting scheme uses a difficult mask because one of the octets is not a 0 or a 255. The second octet is "interesting" in this case. The key part of the trick to get the right answers is to calculate the magic number, which is 256 - 192 = 64 in this case (256 - mask's value in the interesting octet). The subnet number's value in the interesting octet (inside the box) is the multiple of the magic number that is not higher than the original IP address's value in the interesting octet. In this case, 128 is the multiple of 64 that is closest to 180 but not higher than 180. So, the second octet of the subnet number is 128.

The second part of this process calculates the subnet broadcast address, with the tricky part, as usual, in the "interesting" octet. Take the subnet number's value in the interesting octet, add the magic number, and subtract 1. That is the broadcast address's value in the interesting octet. In this case, it is 128 + 64 - 1 = 191.

#### Answer to Problem 2

**Table F-4** Question 2: Size of Network, Subnet, Host, Number of Subnets, and Number of Hosts

| Item | Example | Rules to Remember |
| --- | --- | --- |
| Address | 10.200.10.18 | -- |
| Mask | 255.224.0.0 | -- |
| Number of network bits | 8 | Always defined by Class A, B, C |
| Number of host bits | 21 | Always defined as number of binary 0s in mask |
| Number of subnet bits | 3 | 32 - (network size + host size) |
| Number of subnets | 23 = 8 | 2number-of-subnet-bits |
| Number of hosts | 221 - 2 = 2,097,150 | 2number-of-host-bits - 2 |

[Table F-5](vol1_appf.md#appftab05) contains the important binary calculations for finding the subnet number and subnet broadcast address. To calculate the subnet number, perform a Boolean AND on the address and mask. To find the broadcast address for this subnet, change all the host bits to binary 1s in the subnet number. The host bits are in **bold** print in the table.




**Table F-5** Question 2: Binary Calculation of Subnet and Broadcast Addresses

|  |  |  |
| --- | --- | --- |
| Address | 10.200.10.18 | `00001010 11001000 00001010 00010010` |
| Mask | 255.224.0.0 | `11111111 11100000 00000000 00000000` |
| AND result (subnet number) | 10.192.0.0 | `00001010 11000000 00000000 00000000` |
| Change host to 1s (broadcast address) | 10.223.255.255 | `00001010 11011111 11111111 11111111` |

Just add 1 to the subnet number to get the first valid IP address; just subtract 1 from the broadcast address to get the last valid IP address. In this case:

10.192.0.1 through 10.223.255.254

Alternatively, you can use the processes that only use decimal math to find the subnet and broadcast address. [Table F-6](vol1_appf.md#appftab06) shows the work for this problem, with some explanation of the work following the table.

**Table F-6** Question 2: Subnet, Broadcast, and First and Last Addresses Calculated Using the Subnet Chart

|  | Octet 1 | Octet 2 | Octet 3 | Octet 4 | Comments |
| --- | --- | --- | --- | --- | --- |
| **Mask** | 255 | 224 | 0 | 0 |  |
| **Address** | 10 | 200 | 10 | 18 |  |
| **Subnet Number** | 10 | 192 | 0 | 0 | Magic number = 256 - 224 = 32 |
| **First Address** | 10 | 192 | 0 | 1 | Add 1 to last octet of subnet |
| **Last Address** | 10 | 223 | 255 | 254 | Subtract 1 from last octet of broadcast |
| **Broadcast** | 10 | 223 | 255 | 255 | 192 + 32 - 1 = 223 |

This subnetting scheme uses a difficult mask because one of the octets is not a 0 or a 255. The second octet is "interesting" in this case. The key part of the trick to get the right answers is to calculate the magic number, which is 256 - 224 = 32 in this case (256 - mask's value in the interesting octet). The subnet number's value in the interesting octet (inside the box) is the multiple of the magic number that is not higher than the original IP address's value in the interesting octet. In this case, 192 is the multiple of 32 that is closest to 200 but not higher than 200. So, the second octet of the subnet number is 192.

The second part of this process calculates the subnet broadcast address, with the tricky part, as usual, in the "interesting" octet. Take the subnet number's value in the interesting octet, add the magic number, and subtract 1. That is the broadcast address's value in the interesting octet. In this case, it is 192 + 32 - 1 = 223.

#### Answer to Problem 3

**Table F-7** Question 3: Size of Network, Subnet, Host, Number of Subnets, and Number of Hosts

| Item | Example | Rules to Remember |
| --- | --- | --- |
| Address | 10.100.18.18 | -- |
| Mask | 255.240.0.0 | -- |
| Number of network bits | 8 | Always defined by Class A, B, C |
| Number of host bits | 20 | Always defined as number of binary 0s in mask |
| Number of subnet bits | 4 | 32 - (network size + host size) |
| Number of subnets | 24 = 16 | 2number-of-subnet-bits |
| Number of hosts | 220 - 2 = 1,048,574 | 2number-of-host-bits - 2 |

[Table F-8](vol1_appf.md#appftab08) contains the important binary calculations for finding the subnet number and subnet broadcast address. To calculate the subnet number, perform a Boolean AND on the address and mask. To find the broadcast address for this subnet, change all the host bits to binary 1s in the subnet number. The host bits are in **bold** print in the table.

**Table F-8** Question 3: Binary Calculation of Subnet and Broadcast Addresses

|  |  |  |
| --- | --- | --- |
| Address | 10.100.18.18 | `00001010 01100100 00010010 00010010` |
| Mask | 255.240.0.0 | `11111111 11110000 00000000 00000000` |
| AND result (subnet number) | 10.96.0.0 | `00001010 01100000 00000000 00000000` |
| Change host to 1s (broadcast address) | 10.111.255.255 | `00001010 01101111 11111111 11111111` |

Just add 1 to the subnet number to get the first valid IP address; just subtract 1 from the broadcast address to get the last valid IP address. In this case:

10.96.0.1 through 10.111.255.254

Alternatively, you can use the processes that only use decimal math to find the subnet and broadcast address. [Table F-9](vol1_appf.md#appftab09) shows the work for this problem, with some explanation of the work following the table.

**Table F-9** Question 3: Subnet, Broadcast, and First and Last Addresses Calculated Using the Subnet Chart

|  | Octet 1 | Octet 2 | Octet 3 | Octet 4 | Comments |
| --- | --- | --- | --- | --- | --- |
| **Mask** | 255 | 240 | 0 | 0 | -- |
| **Address** | 10 | 100 | 18 | 18 | -- |
| **Subnet Number** | 10 | 96 | 0 | 0 | Magic number = 256 - 240 = 16 |
| **First Address** | 10 | 96 | 0 | 1 | Add 1 to last octet of subnet |
| **Last Address** | 10 | 111 | 255 | 254 | Subtract 1 from last octet of broadcast |
| **Broadcast** | 10 | 111 | 255 | 255 | 96 + 16 - 1 = 111 |

This subnetting scheme uses a difficult mask because one of the octets is not a 0 or a 255. The second octet is "interesting" in this case. The key part of the trick to get the right answers is to calculate the magic number, which is 256 - 240 = 16 in this case (256 - mask's value in the interesting octet). The subnet number's value in the interesting octet (inside the box) is the multiple of the magic number that is not higher than the original IP address's value in the interesting octet. In this case, 96 is the multiple of 16 that is closest to 100 but not higher than 100. So, the second octet of the subnet number is 96.

The second part of this process calculates the subnet broadcast address, with the tricky part, as usual, in the "interesting" octet. Take the subnet number's value in the interesting octet, add the magic number, and subtract 1. That is the broadcast address's value in the interesting octet. In this case, it is 96 + 16 - 1 = 111.

#### Answer to Problem 4

**Table F-10** Question 4: Size of Network, Subnet, Host, Number of Subnets, and Number of Hosts

| Item | Example | Rules to Remember |
| --- | --- | --- |
| Address | 10.100.18.18 | -- |
| Mask | 255.248.0.0 | -- |
| Number of network bits | 8 | Always defined by Class A, B, C |
| Number of host bits | 19 | Always defined as number of binary 0s in mask |
| Number of subnet bits | 5 | 32 - (network size + host size) |
| Number of subnets | 25 = 32 | 2number-of-subnet-bits |
| Number of hosts | 219 - 2 = 524,286 | 2number-of-host-bits - 2 |

[Table F-11](vol1_appf.md#appftab11) contains the important binary calculations for finding the subnet number and subnet broadcast address. To calculate the subnet number, perform a Boolean AND on the address and mask. To find the broadcast address for this subnet, change all the host bits to binary 1s in the subnet number. The host bits are in **bold** print in the table.

**Table F-11** Question 4: Binary Calculation of Subnet and Broadcast Addresses

|  |  |  |
| --- | --- | --- |
| Address | 10.100.18.18 | `00001010 01100100 00010010 00010010` |
| Mask | 255.248.0.0 | `11111111 11111000 00000000 00000000` |
| AND result (subnet number) | 10.96.0.0 | `00001010 01100000 00000000 00000000` |
| Change host to 1s (broadcast address) | 10.103.255.255 | `00001010 01100111 11111111 11111111` |

Just add 1 to the subnet number to get the first valid IP address; just subtract 1 from the broadcast address to get the last valid IP address. In this case:

10.96.0.1 through 10.103.255.254

Alternatively, you can use the processes that only use decimal math to find the subnet and broadcast address. [Table F-12](vol1_appf.md#appftab12) shows the work for this problem, with some explanation of the work following the table.




**Table F-12** Question 4: Subnet, Broadcast, and First and Last Addresses Calculated Using the Subnet Chart

|  | Octet 1 | Octet 2 | Octet 3 | Octet 4 | Comments |
| --- | --- | --- | --- | --- | --- |
| **Mask** | 255 | 248 | 0 | 0 | -- |
| **Address** | 10 | 100 | 18 | 18 | -- |
| **Subnet Number** | 10 | 96 | 0 | 0 | Magic number = 256 - 248 = 8 |
| **First Address** | 10 | 96 | 0 | 1 | Add 1 to last octet of subnet |
| **Last Address** | 10 | 103 | 255 | 254 | Subtract 1 from last octet of broadcast |
| **Broadcast** | 10 | 103 | 255 | 255 | 96 + 8 - 1 = 103 |

This subnetting scheme uses a difficult mask because one of the octets is not a 0 or a 255. The second octet is "interesting" in this case. The key part of the trick to get the right answers is to calculate the magic number, which is 256 - 248 = 8 in this case (256 - mask's value in the interesting octet). The subnet number's value in the interesting octet (inside the box) is the multiple of the magic number that is not higher than the original IP address's value in the interesting octet. In this case, 96 is the multiple of 8 that is closest to 100 but not higher than 100. So, the second octet of the subnet number is 96.

The second part of this process calculates the subnet broadcast address with the tricky part, as usual, in the "interesting" octet. Take the subnet number's value in the interesting octet, add the magic number, and subtract 1. That is the broadcast address's value in the interesting octet. In this case, it is 96 + 8 - 1 = 103.

#### Answer to Problem 5

**Table F-13** Question 5: Size of Network, Subnet, Host, Number of Subnets, and Number of Hosts

| Item | Example | Rules to Remember |
| --- | --- | --- |
| Address | 10.150.200.200 | -- |
| Mask | 255.252.0.0 | -- |
| Number of network bits | 8 | Always defined by Class A, B, C |
| Number of host bits | 18 | Always defined as number of binary 0s in mask |
| Number of subnet bits | 6 | 32 - (network size + host size) |
| Number of subnets | 26 = 64 | 2number-of-subnet-bits |
| Number of hosts | 218 - 2 = 262,142 | 2number-of-host-bits - 2 |

[Table F-14](vol1_appf.md#appftab14) contains the important binary calculations for finding the subnet number and subnet broadcast address. To calculate the subnet number, perform a Boolean AND on the address and mask. To find the broadcast address for this subnet, change all the host bits to binary 1s in the subnet number. The host bits are in **bold** print in the table.




**Table F-14** Question 5: Binary Calculation of Subnet and Broadcast Addresses

|  |  |  |
| --- | --- | --- |
| Address | 10.150.200.200 | `00001010 10010110 11001000 11001000` |
| Mask | 255.252.0.0 | `11111111 11111100 00000000 00000000` |
| AND result (subnet number) | 10.148.0.0 | `00001010 10010100 00000000 00000000` |
| Change host to 1s (broadcast address) | 10.151.255.255 | `00001010 10010111 11111111 11111111` |

Just add 1 to the subnet number to get the first valid IP address; just subtract 1 from the broadcast address to get the last valid IP address. In this case:

10.148.0.1 through 10.151.255.254

Alternatively, you can use the processes that only use decimal math to find the subnet and broadcast address. [Table F-15](vol1_appf.md#appftab15) shows the work for this problem, with some explanation of the work following the table.

**Table F-15** Question 5: Subnet, Broadcast, and First and Last Addresses Calculated Using the Subnet Chart

|  | Octet 1 | Octet 2 | Octet 3 | Octet 4 | Comments |
| --- | --- | --- | --- | --- | --- |
| **Mask** | 255 | 252 | 0 | 0 | -- |
| **Address** | 10 | 150 | 200 | 200 | -- |
| **Subnet Number** | 10 | 148 | 0 | 0 | Magic number = 256 - 252 = 4 |
| **First Address** | 10 | 148 | 0 | 1 | Add 1 to last octet of subnet |
| **Last Address** | 10 | 151 | 255 | 254 | Subtract 1 from last octet of broadcast |
| **Broadcast** | 10 | 151 | 255 | 255 | 148 + 4 - 1 = 151 |

This subnetting scheme uses a difficult mask because one of the octets is not a 0 or a 255. The second octet is "interesting" in this case. The key part of the trick to get the right answers is to calculate the magic number, which is 256 - 252 = 4 in this case (256 - mask's value in the interesting octet). The subnet number's value in the interesting octet (inside the box) is the multiple of the magic number that is not higher than the original IP address's value in the interesting octet. In this case, 148 is the multiple of 4 that is closest to 150 but not higher than 150. So, the second octet of the subnet number is 148.

The second part of this process calculates the subnet broadcast address with the tricky part, as usual, in the "interesting" octet. Take the subnet number's value in the interesting octet, add the magic number, and subtract 1. That is the broadcast address's value in the interesting octet. In this case, it is 148 + 4 - 1 = 151.

#### Answer to Problem 6

**Table F-16** Question 6: Size of Network, Subnet, Host, Number of Subnets, and Number of Hosts

| Item | Example | Rules to Remember |
| --- | --- | --- |
| Address | 10.150.200.200 | -- |
| Mask | 255.254.0.0 | -- |
| Number of network bits | 8 | Always defined by Class A, B, C |
| Number of host bits | 17 | Always defined as number of binary 0s in mask |
| Number of subnet bits | 7 | 32 - (network size + host size) |
| Number of subnets | 27 = 128 | 2number-of-subnet-bits |
| Number of hosts | 217 - 2 = 131,070 | 2number-of-host-bits - 2 |

[Table F-17](vol1_appf.md#appftab17) contains the important binary calculations for finding the subnet number and subnet broadcast address. To calculate the subnet number, perform a Boolean AND on the address and mask. To find the broadcast address for this subnet, change all the host bits to binary 1s in the subnet number. The host bits are in **bold** print in the table.

**Table F-17** Question 6: Binary Calculation of Subnet and Broadcast Addresses

|  |  |  |
| --- | --- | --- |
| Address | 10.150.200.200 | `00001010 10010110 11001000 11001000` |
| Mask | 255.254.0.0 | `11111111 11111110 00000000 00000000` |
| AND result (subnet number) | 10.150.0.0 | `00001010 10010110 00000000 00000000` |
| Change host to 1s (broadcast address) | 10.151.255.255 | `00001010 10010111 11111111 11111111` |

Just add 1 to the subnet number to get the first valid IP address; just subtract 1 from the broadcast address to get the last valid IP address. In this case:

10.150.0.1 through 10.151.255.254

Alternatively, you can use the processes that only use decimal math to find the subnet and broadcast address. [Table F-18](vol1_appf.md#appftab18) shows the work for this problem, with some explanation of the work following the table.

**Table F-18** Question 6: Subnet, Broadcast, and First and Last Addresses Calculated Using the Subnet Chart

|  | Octet 1 | Octet 2 | Octet 3 | Octet 4 |
| --- | --- | --- | --- | --- |
| **Mask** | 255 | 254 | 0 | 0 |
| **Address** | 10 | 150 | 200 | 200 |
| **Subnet Number** | 10 | 150 | 0 | 0 |
| **First Valid Address** | 10 | 150 | 0 | 1 |
| **Last Valid Address** | 10 | 151 | 255 | 254 |
| **Broadcast** | 10 | 151 | 255 | 255 |

This subnetting scheme uses a difficult mask because one of the octets is not a 0 or a 255. The second octet is "interesting" in this case. The key part of the trick to get the right answers is to calculate the magic number, which is 256 - 254 = 2 in this case (256 - mask's value in the interesting octet). The subnet number's value in the interesting octet (inside the box) is the multiple of the magic number that is not higher than the original IP address's value in the interesting octet. In this case, 150 is the multiple of 2 that is closest to 150 but not higher than 150. So, the second octet of the subnet number is 150.

The second part of this process calculates the subnet broadcast address with the tricky part, as usual, in the "interesting" octet. Take the subnet number's value in the interesting octet, add the magic number, and subtract 1. That is the broadcast address's value in the interesting octet. In this case, it is 150 + 2 - 1 = 151.

#### Answer to Problem 7

**Table F-19** Question 7: Size of Network, Subnet, Host, Number of Subnets, and Number of Hosts

| Item | Example | Rules to Remember |
| --- | --- | --- |
| Address | 10.220.100.18 | -- |
| Mask | 255.255.0.0 | -- |
| Number of network bits | 8 | Always defined by Class A, B, C |
| Number of host bits | 16 | Always defined as number of binary 0s in mask |
| Number of subnet bits | 8 | 32 - (network size + host size) |
| Number of subnets | 28 = 256 | 2number-of-subnet-bits |
| Number of hosts | 216 - 2 = 65,534 | 2number-of-host-bits - 2 |

[Table F-20](vol1_appf.md#appftab20) contains the important binary calculations for finding the subnet number and subnet broadcast address. To calculate the subnet number, perform a Boolean AND on the address and mask. To find the broadcast address for this subnet, change all the host bits to binary 1s in the subnet number. The host bits are in **bold** print in the table.

**Table F-20** Question 7: Binary Calculation of Subnet and Broadcast Addresses

|  |  |  |
| --- | --- | --- |
| Address | 10.220.100.18 | `00001010 11011100 01100100 00010010` |
| Mask | 255.255.0.0 | `11111111 11111111 00000000 00000000` |
| AND result (subnet number) | 10.220.0.0 | `00001010 11011100 00000000 00000000` |
| Change host to 1s (broadcast address) | 10.220.255.255 | `00001010 11011100 11111111 11111111` |

Just add 1 to the subnet number to get the first valid IP address; just subtract 1 from the broadcast address to get the last valid IP address. In this case:

10.220.0.1 through 10.220.255.254

Alternatively, you can use the processes that only use decimal math to find the subnet and broadcast address. [Table F-21](vol1_appf.md#appftab21) shows the work for this problem.




**Table F-21** Question 7: Subnet, Broadcast, and First and Last Addresses Calculated Using the Subnet Chart

|  | Octet 1 | Octet 2 | Octet 3 | Octet 4 |
| --- | --- | --- | --- | --- |
| **Mask** | 255 | 255 | 0 | 0 |
| **Address** | 10 | 220 | 100 | 18 |
| **Subnet Number** | 10 | 220 | 0 | 0 |
| **First Valid Address** | 10 | 220 | 0 | 1 |
| **Last Valid Address** | 10 | 220 | 255 | 254 |
| **Broadcast** | 10 | 220 | 255 | 255 |

This subnetting scheme uses an easy mask because all the octets are a 0 or a 255. No math tricks are needed.

#### Answer to Problem 8

**Table F-22** Question 8: Size of Network, Subnet, Host, Number of Subnets, and Number of Hosts

| Item | Example | Rules to Remember |
| --- | --- | --- |
| Address | 10.220.100.18 | -- |
| Mask | 255.255.128.0 | -- |
| Number of network bits | 8 | Always defined by Class A, B, C |
| Number of host bits | 15 | Always defined as number of binary 0s in mask |
| Number of subnet bits | 9 | 32 - (network size + host size) |
| Number of subnets | 29 = 512 | 2number-of-subnet-bits |
| Number of hosts | 215 - 2 = 32,766 | 2number-of-host-bits - 2 |

[Table F-23](vol1_appf.md#appftab23) contains the important binary calculations for finding the subnet number and subnet broadcast address. To calculate the subnet number, perform a Boolean AND on the address and mask. To find the broadcast address for this subnet, change all the host bits to binary 1s in the subnet number. The host bits are in **bold** print in the table.

**Table F-23** Question 8: Binary Calculation of Subnet and Broadcast Addresses

|  |  |  |
| --- | --- | --- |
| Address | 10.220.100.18 | `00001010 11011100 01100100 00010010` |
| Mask | 255.255.128.0 | `11111111 11111111 10000000 00000000` |
| AND result (subnet number) | 10.220.0.0 | `00001010 11011100 00000000 00000000` |
| Change host to 1s (broadcast address) | 10.220.127.255 | `00001010 11011100 01111111 11111111` |

Just add 1 to the subnet number to get the first valid IP address; just subtract 1 from the broadcast address to get the last valid IP address. In this case:

10.220.0.1 through 10.220.127.254

[Table F-24](vol1_appf.md#appftab24) shows the work for this problem, with some explanation of the work following the table. Refer to [Chapter 14](vol1_ch14.md#ch14) for the detailed processes.

**Table F-24** Question 8: Subnet, Broadcast, and First and Last Addresses Calculated Using the Subnet Chart

|  | Octet 1 | Octet 2 | Octet 3 | Octet 4 |
| --- | --- | --- | --- | --- |
| **Mask** | 255 | 255 | 128 | 0 |
| **Address** | 10 | 220 | 100 | 18 |
| **Subnet Number** | 10 | 220 | 0 | 0 |
| **First Address** | 10 | 220 | 0 | 1 |
| **Last Address** | 10 | 220 | 127 | 254 |
| **Broadcast** | 10 | 220 | 127 | 255 |

This subnetting scheme uses a difficult mask because one of the octets is not a 0 or a 255. The third octet is "interesting" in this case. The key part of the trick to get the right answers is to calculate the magic number, which is 256 - 128 = 128 in this case (256 - mask's value in the interesting octet). The subnet number's value in the interesting octet (inside the box) is the multiple of the magic number that is not higher than the original IP address's value in the interesting octet. In this case, 0 is the multiple of 128 that is closest to 100 but not higher than 100. So, the third octet of the subnet number is 0.

The second part of this process calculates the subnet broadcast address with the tricky part, as usual, in the "interesting" octet. Take the subnet number's value in the interesting octet, add the magic number, and subtract 1. That is the broadcast address's value in the interesting octet. In this case, it is 0 + 128 - 1 = 127.

This example tends to confuse people, because a mask with 128 in it gives you subnet numbers that just do not seem to look right. [Table F-25](vol1_appf.md#appftab25) gives you the answers for the first several subnets, just to make sure that you are clear about the subnets when using this mask with a Class A network.

**Table F-25** Question 8: First Four Subnets

|  | Zero Subnet | 2nd Subnet | 3rd Subnet | 4th Subnet |
| --- | --- | --- | --- | --- |
| **Subnet** | 10.0.0.0 | 10.0.128.0 | 10.1.0.0 | 10.1.128.0 |
| **First Address** | 10.0.0.1 | 10.0.128.1 | 10.1.0.1 | 10.1.128.1 |
| **Last Address** | 10.0.127.254 | 10.0.255.254 | 10.1.127.254 | 10.1.255.254 |
| **Broadcast** | 10.0.127.255 | 10.0.255.255 | 10.1.127.255 | 10.1.255.255 |

#### Answer to Problem 9

**Table F-26** Question 9: Size of Network, Subnet, Host, Number of Subnets, and Number of Hosts

| Item | Example | Rules to Remember |
| --- | --- | --- |
| Address | 172.31.100.100 | -- |
| Mask | 255.255.192.0 | -- |
| Number of network bits | 16 | Always defined by Class A, B, C |
| Number of host bits | 14 | Always defined as number of binary 0s in mask |
| Number of subnet bits | 2 | 32 - (network size + host size) |
| Number of subnets | 22 = 4 | 2number-of-subnet-bits |
| Number of hosts | 214 - 2 = 16,382 | 2number-of-host-bits - 2 |

[Table F-27](vol1_appf.md#appftab27) contains the important binary calculations for finding the subnet number and subnet broadcast address. To calculate the subnet number, perform a Boolean AND on the address and mask. To find the broadcast address for this subnet, change all the host bits to binary 1s in the subnet number. The host bits are in **bold** print in the table.

**Table F-27** Question 9: Binary Calculation of Subnet and Broadcast Addresses

|  |  |  |
| --- | --- | --- |
| Address | 172.31.100.100 | `10101100 00011111 01100100 01100100` |
| Mask | 255.255.192.0 | `11111111 11111111 11000000 00000000` |
| AND result (subnet number) | 172.31.64.0 | `10101100 00011111 01000000 00000000` |
| Change host to 1s (broadcast address) | 172.31.127.255 | `10101100 00011111 01111111 11111111` |

Just add 1 to the subnet number to get the first valid IP address; just subtract 1 from the broadcast address to get the last valid IP address. In this case:

172.31.64.1 through 172.31.127.254

Alternatively, you can use the processes that only use decimal math to find the subnet and broadcast address. [Table F-28](vol1_appf.md#appftab28) shows the work for this problem, with some explanation of the work following the table.

**Table F-28** Question 9: Subnet, Broadcast, and First and Last Addresses Calculated Using the Subnet Chart

|  | Octet 1 | Octet 2 | Octet 3 | Octet 4 |
| --- | --- | --- | --- | --- |
| **Mask** | 255 | 255 | 192 | 0 |
| **Address** | 172 | 31 | 100 | 100 |
| **Subnet Number** | 172 | 31 | 64 | 0 |
| **First Valid Address** | 172 | 31 | 64 | 1 |
| **Last Valid Address** | 172 | 31 | 127 | 254 |
| **Broadcast** | 172 | 31 | 127 | 255 |

This subnetting scheme uses a difficult mask because one of the octets is not a 0 or a 255. The third octet is "interesting" in this case. The key part of the trick to get the right answers is to calculate the magic number, which is 256 - 192 = 64 in this case (256 - mask's value in the interesting octet). The subnet number's value in the interesting octet (inside the box) is the multiple of the magic number that is not higher than the original IP address's value in the interesting octet. In this case, 64 is the multiple of 64 that is closest to 100 but not higher than 100. So, the third octet of the subnet number is 64.

The second part of this process calculates the subnet broadcast address with the tricky part, as usual, in the "interesting" octet. Take the subnet number's value in the interesting octet, add the magic number, and subtract 1. That is the broadcast address's value in the interesting octet. In this case, it is 64 + 64 - 1 = 127.

#### Answer to Problem 10

**Table F-29** Question 10: Size of Network, Subnet, Host, Number of Subnets, and Number of Hosts

| Item | Example | Rules to Remember |
| --- | --- | --- |
| Address | 172.31.100.100 | -- |
| Mask | 255.255.224.0 | -- |
| Number of network bits | 16 | Always defined by Class A, B, C |
| Number of host bits | 13 | Always defined as number of binary 0s in mask |
| Number of subnet bits | 3 | 32 - (network size + host size) |
| Number of subnets | 23 = 8 | 2number-of-subnet-bits |
| Number of hosts | 213 - 2 = 8190 | 2number-of-host-bits - 2 |

[Table F-30](vol1_appf.md#appftab30) contains the important binary calculations for finding the subnet number and subnet broadcast address. To calculate the subnet number, perform a Boolean AND on the address and mask. To find the broadcast address for this subnet, change all the host bits to binary 1s in the subnet number. The host bits are in **bold** print in the table.

**Table F-30** Question 10: Binary Calculation of Subnet and Broadcast Addresses

|  |  |  |
| --- | --- | --- |
| Address | 172.31.100.100 | `10101100 00011111 01100100 01100100` |
| Mask | 255.255.224.0 | `11111111 11111111 11100000 00000000` |
| AND result (subnet number) | 172.31.96.0 | `10101100 00011111 01100000 00000000` |
| Change host to 1s (broadcast address) | 172.31.127.255 | `10101100 00011111 01111111 11111111` |

Just add 1 to the subnet number to get the first valid IP address; just subtract 1 from the broadcast address to get the last valid IP address. In this case:

172.31.96.1 through 172.31.127.254

Alternatively, you can use the processes that only use decimal math to find the subnet and broadcast address. [Table F-31](vol1_appf.md#appftab31) shows the work for this problem, with some explanation of the work following the table.




**Table F-31** Question 10: Subnet, Broadcast, and First and Last Addresses Calculated Using the Subnet Chart

|  | Octet 1 | Octet 2 | Octet 3 | Octet 4 |
| --- | --- | --- | --- | --- |
| **Mask** | 255 | 255 | 224 | 0 |
| **Address** | 172 | 31 | 100 | 100 |
| **Subnet Number** | 172 | 31 | 96 | 0 |
| **First Valid Address** | 172 | 31 | 96 | 1 |
| **Last Valid Address** | 172 | 31 | 127 | 254 |
| **Broadcast** | 172 | 31 | 127 | 255 |

This subnetting scheme uses a difficult mask because one of the octets is not a 0 or a 255. The third octet is "interesting" in this case. The key part of the trick to get the right answers is to calculate the magic number, which is 256 - 224 = 32 in this case (256 - mask's value in the interesting octet). The subnet number's value in the interesting octet (inside the box) is the multiple of the magic number that is not higher than the original IP address's value in the interesting octet. In this case, 96 is the multiple of 32 that is closest to 100 but not higher than 100. So, the third octet of the subnet number is 96.

The second part of this process calculates the subnet broadcast address, with the tricky parts, as usual, in the "interesting" octet. Take the subnet number's value in the interesting octet, add the magic number, and subtract 1. That is the broadcast address's value in the interesting octet. In this case, it is 96 + 32 - 1 = 127.

#### Answer to Problem 11

**Table F-32** Question 11: Size of Network, Subnet, Host, Number of Subnets, and Number of Hosts

| Item | Example | Rules to Remember |
| --- | --- | --- |
| Address | 172.31.200.10 | -- |
| Mask | 255.255.240.0 | -- |
| Number of network bits | 16 | Always defined by Class A, B, C |
| Number of host bits | 12 | Always defined as number of binary 0s in mask |
| Number of subnet bits | 4 | 32 - (network size + host size) |
| Number of subnets | 24 = 16 | 2number-of-subnet-bits |
| Number of hosts | 212 - 2 = 4094 | 2number-of-host-bits - 2 |

[Table F-33](vol1_appf.md#appftab33) contains the important binary calculations for finding the subnet number and subnet broadcast address. To calculate the subnet number, perform a Boolean AND on the address and mask. To find the broadcast address for this subnet, change all the host bits to binary 1s in the subnet number. The host bits are in **bold** print in the table.




**Table F-33** Question 11: Binary Calculation of Subnet and Broadcast Addresses

|  |  |  |
| --- | --- | --- |
| Address | 172.31.200.10 | `10101100 00011111 11001000 00001010` |
| Mask | 255.255.240.0 | `11111111 11111111 11110000 00000000` |
| AND result (subnet number) | 172.31.192.0 | `10101100 00011111 11000000 00000000` |
| Change host to 1s (broadcast address) | 172.31.207.255 | `10101100 00011111 11001111 11111111` |

Just add 1 to the subnet number to get the first valid IP address; just subtract 1 from the broadcast address to get the last valid IP address. In this case:

172.31.192.1 through 172.31.207.254

Alternatively, you can use the processes that only use decimal math to find the subnet and broadcast address. [Table F-34](vol1_appf.md#appftab34) shows the work for this problem, with some explanation of the work following the table.

**Table F-34** Question 11: Subnet, Broadcast, and First and Last Addresses Calculated Using the Subnet Chart

|  | Octet 1 | Octet 2 | Octet 3 | Octet 4 |
| --- | --- | --- | --- | --- |
| **Mask** | 255 | 255 | 240 | 0 |
| **Address** | 172 | 31 | 200 | 10 |
| **Subnet Number** | 172 | 31 | 192 | 0 |
| **First Valid Address** | 172 | 31 | 192 | 1 |
| **Last Valid Address** | 172 | 31 | 207 | 254 |
| **Broadcast** | 172 | 31 | 207 | 255 |

This subnetting scheme uses a difficult mask because one of the octets is not a 0 or a 255. The third octet is "interesting" in this case. The key part of the trick to get the right answers is to calculate the magic number, which is 256 - 240 = 16 in this case (256 - mask's value in the interesting octet). The subnet number's value in the interesting octet (inside the box) is the multiple of the magic number that is not higher than the original IP address's value in the interesting octet. In this case, 192 is the multiple of 16 that is closest to 200 but not higher than 200. So, the third octet of the subnet number is 192.

The second part of this process calculates the subnet broadcast address with the tricky part, as usual, in the "interesting" octet. Take the subnet number's value in the interesting octet, add the magic number, and subtract 1. That is the broadcast address's value in the interesting octet. In this case, it is 192 + 16 - 1 = 207.

#### Answer to Problem 12

**Table F-35** Question 12: Size of Network, Subnet, Host, Number of Subnets, and Number of Hosts

| Item | Example | Rules to Remember |
| --- | --- | --- |
| Address | 172.31.200.10 | -- |
| Mask | 255.255.248.0 | -- |
| Number of network bits | 16 | Always defined by Class A, B, C |
| Number of host bits | 11 | Always defined as number of binary 0s in mask |
| Number of subnet bits | 5 | 32 - (network size + host size) |
| Number of subnets | 25 = 32 | 2number-of-subnet-bits |
| Number of hosts | 211 - 2 = 2046 | 2number-of-host-bits - 2 |

[Table F-36](vol1_appf.md#appftab36) contains the important binary calculations for finding the subnet number and subnet broadcast address. To calculate the subnet number, perform a Boolean AND on the address and mask. To find the broadcast address for this subnet, change all the host bits to binary 1s in the subnet number. The host bits are in **bold** print in the table.

**Table F-36** Question 12: Binary Calculation of Subnet and Broadcast Addresses

|  |  |  |
| --- | --- | --- |
| Address | 172.31.200.10 | `10101100 00011111 11001000 00001010` |
| Mask | 255.255.248.0 | `11111111 11111111 11111000 00000000` |
| AND result (subnet number) | 172.31.200.0 | `10101100 00011111 11001000 00000000` |
| Change host to 1s (broadcast address) | 172.31.207.255 | `10101100 00011111 11001111 11111111` |

Just add 1 to the subnet number to get the first valid IP address; just subtract 1 from the broadcast address to get the last valid IP address. In this case:

172.31.200.1 through 172.31.207.254

Alternatively, you can use the processes that only use decimal math to find the subnet and broadcast address. [Table F-37](vol1_appf.md#appftab37) shows the work for this problem, with some explanation of the work following the table.

**Table F-37** Question 12: Subnet, Broadcast, and First and Last Addresses Calculated Using the Subnet Chart

|  | Octet 1 | Octet 2 | Octet 3 | Octet 4 |
| --- | --- | --- | --- | --- |
| **Mask** | 255 | 255 | 248 | 0 |
| **Address** | 172 | 31 | 200 | 10 |
| **Subnet Number** | 172 | 31 | 200 | 0 |
| **First Valid Address** | 172 | 31 | 200 | 1 |
| **Last Valid Address** | 172 | 31 | 207 | 254 |
| **Broadcast** | 172 | 31 | 207 | 255 |

This subnetting scheme uses a difficult mask because one of the octets is not a 0 or a 255. The third octet is "interesting" in this case. The key part of the trick to get the right answers is to calculate the magic number, which is 256 - 248 = 8 in this case (256 - mask's value in the interesting octet). The subnet number's value in the interesting octet (inside the box) is the multiple of the magic number that is not higher than the original IP address's value in the interesting octet. In this case, 200 is the multiple of 8 that is closest to 200 but not higher than 200. So, the third octet of the subnet number is 200.

The second part of this process calculates the subnet broadcast address, with the tricky part, as usual, in the "interesting" octet. Take the subnet number's value in the interesting octet, add the magic number, and subtract 1. That is the broadcast address's value in the interesting octet. In this case, it is 200 + 8 - 1 = 207.

#### Answer to Problem 13

**Table F-38** Question 13: Size of Network, Subnet, Host, Number of Subnets, and Number of Hosts

| Item | Example | Rules to Remember |
| --- | --- | --- |
| Address | 172.31.50.50 | -- |
| Mask | 255.255.252.0 | -- |
| Number of network bits | 16 | Always defined by Class A, B, C |
| Number of host bits | 10 | Always defined as number of binary 0s in mask |
| Number of subnet bits | 6 | 32 - (network size + host size) |
| Number of subnets | 26 = 64 | 2number-of-subnet-bits |
| Number of hosts | 210 - 2 = 1022 | 2number-of-host-bits - 2 |

[Table F-39](vol1_appf.md#appftab39) contains the important binary calculations for finding the subnet number and subnet broadcast address. To calculate the subnet number, perform a Boolean AND on the address and mask. To find the broadcast address for this subnet, change all the host bits to binary 1s in the subnet number. The host bits are in **bold** print in the table.

**Table F-39** Question 13: Binary Calculation of Subnet and Broadcast Addresses

|  |  |  |
| --- | --- | --- |
| Address | 172.31.50.50 | `10101100 00011111 00110010 00110010` |
| Mask | 255.255.252.0 | `11111111 11111111 11111100 00000000` |
| AND result (subnet number) | 172.31.48.0 | `10101100 00011111 00110000 00000000` |
| Change host to 1s (broadcast address) | 172.31.51.255 | `10101100 00011111 00110011 11111111` |

Just add 1 to the subnet number to get the first valid IP address; just subtract 1 from the broadcast address to get the last valid IP address. In this case:

172.31.48.1 through 172.31.51.254

Alternatively, you can use the processes that only use decimal math to find the subnet and broadcast address. [Table F-40](vol1_appf.md#appftab40) shows the work for this problem, with some explanation of the work following the table.




**Table F-40** Question 13: Subnet, Broadcast, and First and Last Addresses Calculated Using the Subnet Chart

|  | Octet 1 | Octet 2 | Octet 3 | Octet 4 |
| --- | --- | --- | --- | --- |
| **Mask** | 255 | 255 | 252 | 0 |
| **Address** | 172 | 31 | 50 | 50 |
| **Subnet Number** | 172 | 31 | 48 | 0 |
| **First Valid Address** | 172 | 31 | 48 | 1 |
| **Last Valid Address** | 172 | 31 | 51 | 254 |
| **Broadcast** | 172 | 31 | 51 | 255 |

This subnetting scheme uses a difficult mask because one of the octets is not a 0 or a 255. The third octet is "interesting" in this case. The key part of the trick to get the right answers is to calculate the magic number, which is 256 - 252 = 4 in this case (256 - mask's value in the interesting octet). The subnet number's value in the interesting octet (inside the box) is the multiple of the magic number that is not higher than the original IP address's value in the interesting octet. In this case, 48 is the multiple of 4 that is closest to 50 but not higher than 50. So, the third octet of the subnet number is 48.

The second part of this process calculates the subnet broadcast address, with the tricky part, as usual, in the "interesting" octet. Take the subnet number's value in the interesting octet, add the magic number, and subtract 1. That is the broadcast address's value in the interesting octet. In this case, it is 48 + 4 - 1 = 51.

#### Answer to Problem 14

**Table F-41** Question 14: Size of Network, Subnet, Host, Number of Subnets, and Number of Hosts

| Item | Example | Rules to Remember |
| --- | --- | --- |
| Address | 172.31.50.50 | -- |
| Mask | 255.255.254.0 | -- |
| Number of network bits | 16 | Always defined by Class A, B, C |
| Number of host bits | 9 | Always defined as number of binary 0s in mask |
| Number of subnet bits | 7 | 32 - (network size + host size) |
| Number of subnets | 27 = 128 | 2number-of-subnet-bits |
| Number of hosts | 29 - 2 = 510 | 2number-of-host-bits - 2 |

[Table F-42](vol1_appf.md#appftab42) contains the important binary calculations for finding the subnet number and subnet broadcast address. To calculate the subnet number, perform a Boolean AND on the address and mask. To find the broadcast address for this subnet, change all the host bits to binary 1s in the subnet number. The host bits are in **bold** print in the table.




**Table F-42** Question 14: Binary Calculation of Subnet and Broadcast Addresses

|  |  |  |
| --- | --- | --- |
| Address | 172.31.50.50 | `10101100 00011111 00110010 00110010` |
| Mask | 255.255.254.0 | `11111111 11111111 11111110 00000000` |
| AND result (subnet number) | 172.31.50.0 | `10101100 00011111 00110010 00000000` |
| Change host to 1s (broadcast address) | 172.31.51.255 | `10101100 00011111 00110011 11111111` |

Just add 1 to the subnet number to get the first valid IP address; just subtract 1 from the broadcast address to get the last valid IP address. In this case:

172.31.50.1 through 172.31.51.254

Alternatively, you can use the processes that only use decimal math to find the subnet and broadcast address. [Table F-43](vol1_appf.md#appftab43) shows the work for this problem, with some explanation of the work following the table.

**Table F-43** Question 14: Subnet, Broadcast, and First and Last Addresses Calculated Using the Subnet Chart

|  | Octet 1 | Octet 2 | Octet 3 | Octet 4 |
| --- | --- | --- | --- | --- |
| **Mask** | 255 | 255 | 254 | 0 |
| **Address** | 172 | 31 | 50 | 50 |
| **Subnet Number** | 172 | 31 | 50 | 0 |
| **First Valid Address** | 172 | 31 | 50 | 1 |
| **Last Valid Address** | 172 | 31 | 51 | 254 |
| **Broadcast** | 172 | 31 | 51 | 255 |

This subnetting scheme uses a difficult mask because one of the octets is not a 0 or a 255. The third octet is "interesting" in this case. The key part of the trick to get the right answers is to calculate the magic number, which is 256 - 254 = 2 in this case (256 - mask's value in the interesting octet). The subnet number's value in the interesting octet (inside the box) is the multiple of the magic number that is not higher than the original IP address's value in the interesting octet. In this case, 50 is the multiple of 2 that is closest to 50 but not higher than 50. So, the third octet of the subnet number is 50.

The second part of this process calculates the subnet broadcast address with the tricky part, as usual, in the "interesting" octet. Take the subnet number's value in the interesting octet, add the magic number, and subtract 1. That is the broadcast address's value in the interesting octet. In this case, it is 50 + 2 - 1 = 51.

#### Answer to Problem 15

**Table F-44** Question 15: Size of Network, Subnet, Host, Number of Subnets, and Number of Hosts

| Item | Example | Rules to Remember |
| --- | --- | --- |
| Address | 172.31.140.14 | -- |
| Mask | 255.255.255.0 | -- |
| Number of network bits | 16 | Always defined by Class A, B, C |
| Number of host bits | 8 | Always defined as number of binary 0s in mask |
| Number of subnet bits | 8 | 32 - (network size + host size) |
| Number of subnets | 28 = 256 | 2number-of-subnet-bits |
| Number of hosts | 28 - 2 = 254 | 2number-of-host-bits - 2 |

[Table F-45](vol1_appf.md#appftab45) contains the important binary calculations for finding the subnet number and subnet broadcast address. To calculate the subnet number, perform a Boolean AND on the address and mask. To find the broadcast address for this subnet, change all the host bits to binary 1s in the subnet number. The host bits are in **bold** print in the table.

**Table F-45** Question 15: Binary Calculation of Subnet and Broadcast Addresses

|  |  |  |
| --- | --- | --- |
| Address | 172.31.140.14 | `10101100 00011111 10001100 00001110` |
| Mask | 255.255.255.0 | `11111111 11111111 11111111 00000000` |
| AND result (subnet number) | 172.31.140.0 | `10101100 00011111 10001100 00000000` |
| Change host to 1s (broadcast address) | 172.31.140.255 | `10101100 00011111 10001100 11111111` |

Just add 1 to the subnet number to get the first valid IP address; just subtract 1 from the broadcast address to get the last valid IP address. In this case:

172.31.140.1 through 172.31.140.254

Alternatively, you can use the processes that only use decimal math to find the subnet and broadcast address. [Table F-46](vol1_appf.md#appftab46) shows the work for this problem.

**Table F-46** Question 15: Subnet, Broadcast, and First and Last Addresses Calculated Using the Subnet Chart

|  | Octet 1 | Octet 2 | Octet 3 | Octet 4 |
| --- | --- | --- | --- | --- |
| **Mask** | 255 | 255 | 255 | 0 |
| **Address** | 172 | 31 | 140 | 14 |
| **Subnet Number** | 172 | 31 | 140 | 0 |
| **First Valid Address** | 172 | 31 | 140 | 1 |
| **Last Valid Address** | 172 | 31 | 140 | 254 |
| **Broadcast** | 172 | 31 | 140 | 255 |

This subnetting scheme uses an easy mask because all the octets are a 0 or a 255. No math tricks are needed.

#### Answer to Problem 16

**Table F-47** Question 16: Size of Network, Subnet, Host, Number of Subnets, and Number of Hosts

| Item | Example | Rules to Remember |
| --- | --- | --- |
| Address | 172.31.140.14 | -- |
| Mask | 255.255.255.128 | -- |
| Number of network bits | 16 | Always defined by Class A, B, C |
| Number of host bits | 7 | Always defined as number of binary 0s in mask |
| Number of subnet bits | 9 | 32 - (network size + host size) |
| Number of subnets | 29 = 512 | 2number-of-subnet-bits |
| Number of hosts | 27 - 2 = 126 | 2number-of-host-bits - 2 |

[Table F-48](vol1_appf.md#appftab48) contains the important binary calculations for finding the subnet number and subnet broadcast address. To calculate the subnet number, perform a Boolean AND on the address and mask. To find the broadcast address for this subnet, change all the host bits to binary 1s in the subnet number. The host bits are in **bold** print in the table.

**Table F-48** Question 16: Binary Calculation of Subnet and Broadcast Addresses

|  |  |  |
| --- | --- | --- |
| Address | 172.31.140.14 | `10101100 00011111 10001100 00001110` |
| Mask | 255.255.255.128 | `11111111 11111111 11111111 10000000` |
| AND result (subnet number) | 172.31.140.0 | `10101100 00011111 10001100 00000000` |
| Change host to 1s (broadcast address) | 172.31.140.127 | `10101100 00011111 10001100 01111111` |

Just add 1 to the subnet number to get the first valid IP address; just subtract 1 from the broadcast address to get the last valid IP address. In this case:

172.31.140.1 through 172.31.140.126

Alternatively, you can use the processes that only use decimal math to find the subnet and broadcast address. [Table F-49](vol1_appf.md#appftab49) shows the work for this problem, with some explanation of the work following the table.

**Table F-49** Question 16: Subnet, Broadcast, and First and Last Addresses Calculated Using the Subnet Chart

|  | Octet 1 | Octet 2 | Octet 3 | Octet 4 |
| --- | --- | --- | --- | --- |
| **Mask** | 255 | 255 | 255 | 128 |
| **Address** | 172 | 31 | 140 | 14 |
| **Subnet Number** | 172 | 31 | 140 | 0 |
| **First Valid Address** | 172 | 31 | 140 | 1 |
| **Last Valid Address** | 172 | 31 | 140 | 126 |
| **Broadcast** | 172 | 31 | 140 | 127 |

This subnetting scheme uses a difficult mask because one of the octets is not a 0 or a 255. The fourth octet is "interesting" in this case. The key part of the trick to get the right answers is to calculate the magic number, which is 256 - 128 = 128 in this case (256 - mask's value in the interesting octet). The subnet number's value in the interesting octet (inside the box) is the multiple of the magic number that is not higher than the original IP address's value in the interesting octet. In this case, 0 is the multiple of 128 that is closest to 14 but not higher than 14. So, the fourth octet of the subnet number is 0.

The second part of this process calculates the subnet broadcast address, with the tricky part, as usual, in the "interesting" octet. Take the subnet number's value in the interesting octet, add the magic number, and subtract 1. That is the broadcast address's value in the interesting octet. In this case, it is 0 + 128 - 1 = 127.

#### Answer to Problem 17

**Table F-50** Question 17: Size of Network, Subnet, Host, Number of Subnets, and Number of Hosts

| Item | Example | Rules to Remember |
| --- | --- | --- |
| Address | 192.168.15.150 | -- |
| Mask | 255.255.255.192 | -- |
| Number of network bits | 24 | Always defined by Class A, B, C |
| Number of host bits | 6 | Always defined as number of binary 0s in mask |
| Number of subnet bits | 2 | 32 - (network size + host size) |
| Number of subnets | 22 = 4 | 2number-of-subnet-bits |
| Number of hosts | 26 - 2 = 62 | 2number-of-host-bits - 2 |

[Table F-51](vol1_appf.md#appftab51) contains the important binary calculations for finding the subnet number and subnet broadcast address. To calculate the subnet number, perform a Boolean AND on the address and mask. To find the broadcast address for this subnet, change all the host bits to binary 1s in the subnet number. The host bits are in **bold** print in the table.

**Table F-51** Question 17: Binary Calculation of Subnet and Broadcast Addresses

|  |  |  |
| --- | --- | --- |
| Address | 192.168.15.150 | `11000000 10101000 00001111 10010110` |
| Mask | 255.255.255.192 | `11111111 11111111 11111111 11000000` |
| AND result (subnet number) | 192.168.15.128 | `11000000 10101000 00001111 10000000` |
| Change host to 1s (broadcast address) | 192.168.15.191 | `11000000 10101000 00001111 10111111` |

Just add 1 to the subnet number to get the first valid IP address; just subtract 1 from the broadcast address to get the last valid IP address. In this case:

192.168.15.129 through 192.168.15.190

Alternatively, you can use the processes that only use decimal math to find the subnet and broadcast address. [Table F-52](vol1_appf.md#appftab52) shows the work for this problem, with some explanation of the work following the table.




**Table F-52** Question 17: Subnet, Broadcast, and First and Last Addresses Calculated Using the Subnet Chart

|  | Octet 1 | Octet 2 | Octet 3 | Octet 4 |
| --- | --- | --- | --- | --- |
| **Mask** | 255 | 255 | 255 | 192 |
| **Address** | 192 | 168 | 15 | 150 |
| **Subnet Number** | 192 | 168 | 15 | 128 |
| **First Valid Address** | 192 | 168 | 15 | 129 |
| **Last Valid Address** | 192 | 168 | 15 | 190 |
| **Broadcast** | 192 | 168 | 15 | 191 |

This subnetting scheme uses a difficult mask because one of the octets is not a 0 or a 255. The fourth octet is "interesting" in this case. The key part of the trick to get the right answers is to calculate the magic number, which is 256 - 192 = 64 in this case (256 - mask's value in the interesting octet). The subnet number's value in the interesting octet (inside the box) is the multiple of the magic number that is not higher than the original IP address's value in the interesting octet. In this case, 128 is the multiple of 64 that is closest to 150 but not higher than 150. So, the fourth octet of the subnet number is 128.

The second part of this process calculates the subnet broadcast address, with the tricky part, as usual, in the "interesting" octet. Take the subnet number's value in the interesting octet, add the magic number, and subtract 1. That is the broadcast address's value in the interesting octet. In this case, it is 128 + 64 - 1 = 191.

#### Answer to Problem 18

**Table F-53** Question 18: Size of Network, Subnet, Host, Number of Subnets, and Number of Hosts

| Item | Example | Rules to Remember |
| --- | --- | --- |
| Address | 192.168.15.150 | -- |
| Mask | 255.255.255.224 | -- |
| Number of network bits | 24 | Always defined by Class A, B, C |
| Number of host bits | 5 | Always defined as number of binary 0s in mask |
| Number of subnet bits | 3 | 32 - (network size + host size) |
| Number of subnets | 23 = 8 | 2number-of-subnet-bits |
| Number of hosts | 25 - 2 = 30 | 2number-of-host-bits - 2 |

[Table F-54](vol1_appf.md#appftab54) contains the important binary calculations for finding the subnet number and subnet broadcast address. To calculate the subnet number, perform a Boolean AND on the address and mask. To find the broadcast address for this subnet, change all the host bits to binary 1s in the subnet number. The host bits are in **bold** print in the table.




**Table F-54** Question 18: Binary Calculation of Subnet and Broadcast Addresses

|  |  |  |
| --- | --- | --- |
| Address | 192.168.15.150 | `11000000 10101000 00001111 10010110` |
| Mask | 255.255.255.224 | `11111111 11111111 11111111 11100000` |
| AND result (subnet number) | 192.168.15.128 | `11000000 10101000 00001111 10000000` |
| Change host to 1s (broadcast address) | 192.168.15.159 | `11000000 10101000 00001111 10011111` |

Just add 1 to the subnet number to get the first valid IP address; just subtract 1 from the broadcast address to get the last valid IP address. In this case:

192.168.15.129 through 192.168.15.158

Alternatively, you can use the processes that only use decimal math to find the subnet and broadcast address. [Table F-55](vol1_appf.md#appftab55) shows the work for this problem, with some explanation of the work following the table.

**Table F-55** Question 18: Subnet, Broadcast, and First and Last Addresses Calculated Using the Subnet Chart

|  | Octet 1 | Octet 2 | Octet 3 | Octet 4 |
| --- | --- | --- | --- | --- |
| **Mask** | 255 | 255 | 255 | 224 |
| **Address** | 192 | 168 | 15 | 150 |
| **Subnet Number** | 192 | 168 | 15 | 128 |
| **First Valid Address** | 192 | 168 | 15 | 129 |
| **Last Valid Address** | 192 | 168 | 15 | 158 |
| **Broadcast** | 192 | 168 | 15 | 159 |

This subnetting scheme uses a difficult mask because one of the octets is not a 0 or a 255. The fourth octet is "interesting" in this case. The key part of the trick to get the right answers is to calculate the magic number, which is 256 - 224 = 32 in this case (256 - mask's value in the interesting octet). The subnet number's value in the interesting octet (inside the box) is the multiple of the magic number that is not higher than the original IP address's value in the interesting octet. In this case, 128 is the multiple of 32 that is closest to 150 but not higher than 150. So, the fourth octet of the subnet number is 128.

The second part of this process calculates the subnet broadcast address, with the tricky part, as usual, in the "interesting" octet. Take the subnet number's value in the interesting octet, add the magic number, and subtract 1. That is the broadcast address's value in the interesting octet. In this case, it is 128 + 32 - 1 = 159.

#### Answer to Problem 19

**Table F-56** Question 19: Size of Network, Subnet, Host, Number of Subnets, and Number of Hosts

| Item | Example | Rules to Remember |
| --- | --- | --- |
| Address | 192.168.100.100 | -- |
| Mask | 255.255.255.240 | -- |
| Number of network bits | 24 | Always defined by Class A, B, C |
| Number of host bits | 4 | Always defined as number of binary 0s in mask |
| Number of subnet bits | 4 | 32 - (network size + host size) |
| Number of subnets | 24 = 16 | 2number-of-subnet-bits |
| Number of hosts | 24 - 2 = 14 | 2number-of-host-bits - 2 |

[Table F-57](vol1_appf.md#appftab57) contains the important binary calculations for finding the subnet number and subnet broadcast address. To calculate the subnet number, perform a Boolean AND on the address and mask. To find the broadcast address for this subnet, change all the host bits to binary 1s in the subnet number. The host bits are in **bold** print in the table.

**Table F-57** Question 19: Binary Calculation of Subnet and Broadcast Addresses

|  |  |  |
| --- | --- | --- |
| Address | 192.168.100.100 | `11000000 10101000 01100100 01100100` |
| Mask | 255.255.255.240 | `11111111 11111111 11111111 11110000` |
| AND result (subnet number) | 192.168.100.96 | `11000000 10101000 01100100 01100000` |
| Change host to 1s (broadcast address) | 192.168.100.111 | `11000000 10101000 01100100 01101111` |

Just add 1 to the subnet number to get the first valid IP address; just subtract 1 from the broadcast address to get the last valid IP address. In this case:

192.168.100.97 through 192.168.100.110

Alternatively, you can use the processes that only use decimal math to find the subnet and broadcast address. [Table F-58](vol1_appf.md#appftab58) shows the work for this problem, with some explanation of the work following the table.

**Table F-58** Question 19: Subnet, Broadcast, and First and Last Addresses Calculated Using the Subnet Chart

|  | Octet 1 | Octet 2 | Octet 3 | Octet 4 |
| --- | --- | --- | --- | --- |
| **Mask** | 255 | 255 | 255 | 240 |
| **Address** | 192 | 168 | 100 | 100 |
| **Subnet Number** | 192 | 168 | 100 | 96 |
| **First Valid Address** | 192 | 168 | 100 | 97 |
| **Last Valid Address** | 192 | 168 | 100 | 110 |
| **Broadcast** | 192 | 168 | 100 | 111 |

This subnetting scheme uses a difficult mask because one of the octets is not a 0 or a 255. The fourth octet is "interesting" in this case. The key part of the trick to get the right answers is to calculate the magic number, which is 256 - 240 = 16 in this case (256 - mask's value in the interesting octet). The subnet number's value in the interesting octet (inside the box) is the multiple of the magic number that is not higher than the original IP address's value in the interesting octet. In this case, 96 is the multiple of 16 that is closest to 100 but not higher than 100. So, the fourth octet of the subnet number is 96.

The second part of this process calculates the subnet broadcast address, with the tricky part, as usual, in the "interesting" octet. Take the subnet number's value in the interesting octet, add the magic number, and subtract 1. That is the broadcast address's value in the interesting octet. In this case, it is 96 + 16 - 1 = 111.

#### Answer to Problem 20

**Table F-59** Question 20: Size of Network, Subnet, Host, Number of Subnets, and Number of Hosts

| Item | Example | Rules to Remember |
| --- | --- | --- |
| Address | 192.168.100.100 | -- |
| Mask | 255.255.255.248 | -- |
| Number of network bits | 24 | Always defined by Class A, B, C |
| Number of host bits | 3 | Always defined as number of binary 0s in mask |
| Number of subnet bits | 5 | 32 - (network size + host size) |
| Number of subnets | 25 = 32 | 2number-of-subnet-bits |
| Number of hosts | 23 - 2 = 6 | 2number-of-host-bits - 2 |

[Table F-60](vol1_appf.md#appftab60) contains the important binary calculations for finding the subnet number and subnet broadcast address. To calculate the subnet number, perform a Boolean AND on the address and mask. To find the broadcast address for this subnet, change all the host bits to binary 1s in the subnet number. The host bits are in **bold** print in the table.

**Table F-60** Question 20: Binary Calculation of Subnet and Broadcast Addresses

|  |  |  |
| --- | --- | --- |
| Address | 192.168.100.100 | `11000000 10101000 01100100 01100100` |
| Mask | 255.255.255.248 | `11111111 11111111 11111111 11111000` |
| AND result (subnet number) | 192.168.100.96 | `11000000 10101000 01100100 01100000` |
| Change host to 1s (broadcast address) | 192.168.100.103 | `11000000 10101000 01100100 01100111` |

Just add 1 to the subnet number to get the first valid IP address; just subtract 1 from the broadcast address to get the last valid IP address. In this case:

192.168.100.97 through 192.168.100.102

Alternatively, you can use the processes that only use decimal math to find the subnet and broadcast address. [Table F-61](vol1_appf.md#appftab61) shows the work for this problem, with some explanation of the work following the table.




**Table F-61** Question 20: Subnet, Broadcast, and First and Last Addresses Calculated Using the Subnet Chart

|  | Octet 1 | Octet 2 | Octet 3 | Octet 4 |
| --- | --- | --- | --- | --- |
| **Mask** | 255 | 255 | 255 | 248 |
| **Address** | 192 | 168 | 100 | 100 |
| **Subnet Number** | 192 | 168 | 100 | 96 |
| **First Valid Address** | 192 | 168 | 100 | 97 |
| **Last Valid Address** | 192 | 168 | 100 | 102 |
| **Broadcast** | 192 | 168 | 100 | 103 |

This subnetting scheme uses a difficult mask because one of the octets is not a 0 or a 255. The fourth octet is "interesting" in this case. The key part of the trick to get the right answers is to calculate the magic number, which is 256 - 248 = 8 in this case (256 - mask's value in the interesting octet). The subnet number's value in the interesting octet (inside the box) is the multiple of the magic number that is not higher than the original IP address's value in the interesting octet. In this case, 96 is the multiple of 8 that is closest to 100 but not higher than 100. So, the fourth octet of the subnet number is 96.

The second part of this process calculates the subnet broadcast address, with the tricky part, as usual, in the "interesting" octet. Take the subnet number's value in the interesting octet, add the magic number, and subtract 1. That is the broadcast address's value in the interesting octet. In this case, it is 96 + 8 - 1 = 103.

#### Answer to Problem 21

**Table F-62** Question 21: Size of Network, Subnet, Host, Number of Subnets, and Number of Hosts

| Item | Example | Rules to Remember |
| --- | --- | --- |
| Address | 192.168.15.230 | -- |
| Mask | 255.255.255.252 | -- |
| Number of network bits | 24 | Always defined by Class A, B, C |
| Number of host bits | 2 | Always defined as number of binary 0s in mask |
| Number of subnet bits | 6 | 32 - (network size + host size) |
| Number of subnets | 26 = 64 | 2number-of-subnet-bits |
| Number of hosts | 22 - 2 = 2 | 2number-of-host-bits - 2 |

[Table F-63](vol1_appf.md#appftab63) contains the important binary calculations for finding the subnet number and subnet broadcast address. To calculate the subnet number, perform a Boolean AND on the address and mask. To find the broadcast address for this subnet, change all the host bits to binary 1s in the subnet number. The host bits are in **bold** print in the table.




**Table F-63** Question 21: Binary Calculation of Subnet and Broadcast Addresses

|  |  |  |
| --- | --- | --- |
| Address | 192.168.15.230 | `11000000 10101000 00001111 11100110` |
| Mask | 255.255.255.252 | `11111111 11111111 11111111 11111100` |
| AND result (subnet number) | 192.168.15.228 | `11000000 10101000 00001111 11100100` |
| Change host to 1s (broadcast address) | 192.168.15.231 | `11000000 10101000 00001111 11100111` |

Just add 1 to the subnet number to get the first valid IP address; just subtract 1 from the broadcast address to get the last valid IP address. In this case:

192.168.15.229 through 192.168.15.230

Alternatively, you can use the processes that only use decimal math to find the subnet and broadcast address. [Table F-64](vol1_appf.md#appftab64) shows the work for this problem, with some explanation of the work following the table.

**Table F-64** Question 21: Subnet, Broadcast, and First and Last Addresses Calculated Using the Subnet Chart

|  | Octet 1 | Octet 2 | Octet 3 | Octet 4 |
| --- | --- | --- | --- | --- |
| **Mask** | 255 | 255 | 255 | 252 |
| **Address** | 192 | 168 | 15 | 230 |
| **Subnet Number** | 192 | 168 | 15 | 228 |
| **First Valid Address** | 192 | 168 | 15 | 229 |
| **Last Valid Address** | 192 | 168 | 15 | 230 |
| **Broadcast** | 192 | 168 | 15 | 231 |

This subnetting scheme uses a difficult mask because one of the octets is not a 0 or a 255. The fourth octet is "interesting" in this case. The key part of the trick to get the right answers is to calculate the magic number, which is 256 - 252 = 4 in this case (256 - mask's value in the interesting octet). The subnet number's value in the interesting octet (inside the box) is the multiple of the magic number that is not higher than the original IP address's value in the interesting octet. In this case, 228 is the multiple of 4 that is closest to 230 but not higher than 230. So, the fourth octet of the subnet number is 228.

The second part of this process calculates the subnet broadcast address, with the tricky part, as usual, in the "interesting" octet. Take the subnet number's value in the interesting octet, add the magic number, and subtract 1. That is the broadcast address's value in the interesting octet. In this case, it is 228 + 4 - 1 = 231.

#### Answer to Problem 22

**Table F-65** Question 22: Size of Network, Subnet, Host, Number of Subnets, and Number of Hosts

| Item | Example | Rules to Remember |
| --- | --- | --- |
| Address | 10.1.1.1 | -- |
| Mask | 255.248.0.0 | -- |
| Number of network bits | 8 | Always defined by Class A, B, C |
| Number of host bits | 19 | Always defined as number of binary 0s in mask |
| Number of subnet bits | 5 | 32 - (network size + host size) |
| Number of subnets | 25 = 32 | 2number-of-subnet-bits |
| Number of hosts | 219 - 2 = 524,286 | 2number-of-host-bits - 2 |

[Table F-66](vol1_appf.md#appftab66) contains the important binary calculations for finding the subnet number and subnet broadcast address. To calculate the subnet number, perform a Boolean AND on the address and mask. To find the broadcast address for this subnet, change all the host bits to binary 1s in the subnet number. The host bits are in **bold** print in the table.

**Table F-66** Question 22: Binary Calculation of Subnet and Broadcast Addresses

|  |  |  |
| --- | --- | --- |
| Address | 10.1.1.1 | `00001010 00000001 00000001 00000001` |
| Mask | 255.248.0.0 | `11111111 11111000 00000000 00000000` |
| AND result (subnet number) | 10.0.0.0 | `00001010 00000000 00000000 00000000` |
| Change host to 1s (broadcast address) | 10.7.255.255 | `00001010 00000111 11111111 11111111` |

Just add 1 to the subnet number to get the first valid IP address; just subtract 1 from the broadcast address to get the last valid IP address. In this case:

10.0.0.1 through 10.7.255.254

Take a closer look at the subnet part of the subnet address, as shown in bold here: 0000 1010 **0000 0**000 0000 0000 0000 0000. The subnet part of the address is all binary 0s, making this subnet a zero subnet.

Alternatively, you can use the processes that only use decimal math to find the subnet and broadcast address. [Table F-67](vol1_appf.md#appftab67) shows the work for this problem, with some explanation of the work following the table.




**Table F-67** Question 22: Subnet, Broadcast, and First and Last Addresses Calculated Using the Subnet Chart

|  | Octet 1 | Octet 2 | Octet 3 | Octet 4 |
| --- | --- | --- | --- | --- |
| **Mask** | 255 | 248 | 0 | 0 |
| **Address** | 10 | 1 | 1 | 1 |
| **Subnet Number** | 10 | 0 | 0 | 0 |
| **First Valid Address** | 10 | 0 | 0 | 1 |
| **Last Valid Address** | 10 | 7 | 255 | 254 |
| **Broadcast** | 10 | 7 | 255 | 255 |

This subnetting scheme uses a difficult mask because one of the octets is not a 0 or a 255. The second octet is "interesting" in this case. The key part of the trick to get the right answers is to calculate the magic number, which is 256 - 248 = 8 in this case (256 - mask's value in the interesting octet). The subnet number's value in the interesting octet (inside the box) is the multiple of the magic number that is not higher than the original IP address's value in the interesting octet. In this case, 0 is the multiple of 8 that is closest to 1 but not higher than 1. So, the second octet of the subnet number is 0.

The second part of this process calculates the subnet broadcast address, with the tricky part, as usual, in the "interesting" octet. Take the subnet number's value in the interesting octet, add the magic number, and subtract 1. That is the broadcast address's value in the interesting octet. In this case, it is 0 + 8 - 1 = 7.

#### Answer to Problem 23

**Table F-68** Question 23: Size of Network, Subnet, Host, Number of Subnets, and Number of Hosts

| Item | Example | Rules to Remember |
| --- | --- | --- |
| Address | 172.16.1.200 | -- |
| Mask | 255.255.240.0 | -- |
| Number of network bits | 16 | Always defined by Class A, B, C |
| Number of host bits | 12 | Always defined as number of binary 0s in mask |
| Number of subnet bits | 4 | 32 - (network size + host size) |
| Number of subnets | 24 = 16 | 2number-of-subnet-bits |
| Number of hosts | 212 - 2 = 4094 | 2number-of-host-bits - 2 |

[Table F-69](vol1_appf.md#appftab69) contains the important binary calculations for finding the subnet number and subnet broadcast address. To calculate the subnet number, perform a Boolean AND on the address and mask. To find the broadcast address for this subnet, change all the host bits to binary 1s in the subnet number. The host bits are in **bold** print in the table.




**Table F-69** Question 23: Binary Calculation of Subnet and Broadcast Addresses

|  |  |  |
| --- | --- | --- |
| Address | 172.16.1.200 | `10101100 00010000 00000001 11001000` |
| Mask | 255.255.240.0 | `11111111 11111111 11110000 00000000` |
| AND result (subnet number) | 172.16.0.0 | `10101100 00010000 00000000 00000000` |
| Change host to 1s (broadcast address) | 172.16.15.255 | `10101100 00010000 00001111 11111111` |

Just add 1 to the subnet number to get the first valid IP address; just subtract 1 from the broadcast address to get the last valid IP address. In this case:

172.16.0.1 through 172.16.15.254

Take a closer look at the subnet part of the subnet address, as shown in bold here: 1010 1100 0001 0000 **0000** 0000 0000 0000. The subnet part of the address is all binary 0s, making this subnet a zero subnet.

Alternatively, you can use the processes that only use decimal math to find the subnet and broadcast address. [Table F-70](vol1_appf.md#appftab70) shows the work for this problem, with some explanation of the work following the table.

**Table F-70** Question 23: Subnet, Broadcast, and First and Last Addresses Calculated Using the Subnet Chart

|  | Octet 1 | Octet 2 | Octet 3 | Octet 4 |
| --- | --- | --- | --- | --- |
| **Mask** | 255 | 255 | 240 | 0 |
| **Address** | 172 | 16 | 1 | 200 |
| **Subnet Number** | 172 | 16 | 0 | 0 |
| **First Valid Address** | 172 | 16 | 0 | 1 |
| **Last Valid Address** | 172 | 16 | 15 | 254 |
| **Broadcast** | 172 | 16 | 15 | 255 |

This subnetting scheme uses a difficult mask because one of the octets is not a 0 or a 255. The third octet is "interesting" in this case. The key part of the trick to get the right answers is to calculate the magic number, which is 256 - 240 = 16 in this case (256 - mask's value in the interesting octet). The subnet number's value in the interesting octet (inside the box) is the multiple of the magic number that is not higher than the original IP address's value in the interesting octet. In this case, 0 is the multiple of 16 that is closest to 1 but not higher than 1. So, the third octet of the subnet number is 0.

The second part of this process calculates the subnet broadcast address, with the tricky part, as usual, in the "interesting" octet. Take the subnet number's value in the interesting octet, add the magic number, and subtract 1. That is the broadcast address's value in the interesting octet. In this case, it is 0 + 16 - 1 = 15.

#### Answer to Problem 24

**Table F-71** Question 24: Size of Network, Subnet, Host, Number of Subnets, and Number of Hosts

| Item | Example | Rules to Remember |
| --- | --- | --- |
| Address | 172.16.0.200 | -- |
| Mask | 255.255.255.192 | -- |
| Number of network bits | 16 | Always defined by Class A, B, C |
| Number of host bits | 6 | Always defined as number of binary 0s in mask |
| Number of subnet bits | 10 | 32 - (network size + host size) |
| Number of subnets | 210 = 1024 | 2number-of-subnet-bits |
| Number of hosts | 26 - 2 = 62 | 2number-of-host-bits - 2 |

[Table F-72](vol1_appf.md#appftab72) contains the important binary calculations for finding the subnet number and subnet broadcast address. To calculate the subnet number, perform a Boolean AND on the address and mask. To find the broadcast address for this subnet, change all the host bits to binary 1s in the subnet number. The host bits are in **bold** print in the table.

**Table F-72** Question 24: Binary Calculation of Subnet and Broadcast Addresses

|  |  |  |
| --- | --- | --- |
| Address | 172.16.0.200 | `10101100 00010000 00000000 11001000` |
| Mask | 255.255.255.192 | `11111111 11111111 11111111 11000000` |
| AND result (subnet number) | 172.16.0.192 | `10101100 00010000 00000000 11000000` |
| Change host to 1s (broadcast address) | 172.16.0.255 | `10101100 00010000 00000000 11111111` |

Just add 1 to the subnet number to get the first valid IP address; just subtract 1 from the broadcast address to get the last valid IP address. In this case:

172.16.0.193 through 172.16.0.254

Alternatively, you can use the processes that only use decimal math to find the subnet and broadcast address. [Table F-73](vol1_appf.md#appftab73) shows the work for this problem, with some explanation of the work following the table.

**Table F-73** Question 24: Subnet, Broadcast, and First and Last Addresses Calculated Using the Subnet Chart

|  | Octet 1 | Octet 2 | Octet 3 | Octet 4 |
| --- | --- | --- | --- | --- |
| **Mask** | 255 | 255 | 255 | 192 |
| **Address** | 172 | 16 | 0 | 200 |
| **Subnet Number** | 172 | 16 | 0 | 192 |
| **First Valid Address** | 172 | 16 | 0 | 193 |
| **Last Valid Address** | 172 | 16 | 0 | 254 |
| **Broadcast** | 172 | 16 | 0 | 255 |

This subnetting scheme uses a difficult mask because one of the octets is not a 0 or a 255. The fourth octet is "interesting" in this case. The key part of the trick to get the right answers is to calculate the magic number, which is 256 - 192 = 64 in this case (256 - mask's value in the interesting octet). The subnet number's value in the interesting octet (inside the box) is the multiple of the magic number that is not higher than the original IP address's value in the interesting octet. In this case, 192 is the multiple of 64 that is closest to 200 but not higher than 200. So, the fourth octet of the subnet number is 192.

The second part of this process calculates the subnet broadcast address, with the tricky part, as usual, in the "interesting" octet. Take the subnet number's value in the interesting octet, add the magic number, and subtract 1. That is the broadcast address's value in the interesting octet. In this case, it is 192 + 64 - 1 = 255.

You can easily forget that the subnet part of this address, when using this mask, actually covers all the third octet as well as 2 bits of the fourth octet. For example, the valid subnet numbers in order are listed here:

172.16.0.0 (zero subnet)

172.16.0.64

172.16.0.128

172.16.0.192

172.16.1.0

172.16.1.64

172.16.1.128

172.16.1.192

172.16.2.0

172.16.2.64

172.16.2.128

172.16.2.192

172.16.3.0

172.16.3.64

172.16.3.128

172.16.3.192

And so on.

#### Answer to Problem 25

Congratulations! You made it through the extra practice in this appendix! Here is an easy one to complete your review--one with no subnetting at all.

**Table F-74** Question 25: Size of Network, Subnet, Host, Number of Subnets, and Number of Hosts

| Item | Example | Rules to Remember |
| --- | --- | --- |
| Address | 10.1.1.1 | -- |
| Mask | 255.0.0.0 | -- |
| Number of network bits | 8 | Always defined by Class A, B, C |
| Number of host bits | 24 | Always defined as number of binary 0s in mask |
| Number of subnet bits | 0 | 32 - (network size + host size) |
| Number of subnets | 0 | 2number-of-subnet-bits |
| Number of hosts | 224 - 2 = 16,777,214 | 2number-of-host-bits - 2 |

[Table F-75](vol1_appf.md#appftab75) contains the important binary calculations for finding the subnet number and subnet broadcast address. To calculate the subnet number, perform a Boolean AND on the address and mask. To find the broadcast address for this subnet, change all the host bits to binary 1s in the subnet number. The host bits are in **bold** print in the table.

**Table F-75** Question 25: Binary Calculation of Subnet and Broadcast Addresses

|  |  |  |
| --- | --- | --- |
| Address | 10.1.1.1 | `00001010 00000001 00000001 00000001` |
| Mask | 255.0.0.0 | `11111111 00000000 00000000 00000000` |
| AND result (subnet number) | 10.0.0.0 | `00001010 00000000 00000000 00000000` |
| Change host to 1s (broadcast address) | 10.255.255.255 | `00001010 11111111 11111111 11111111` |

Just add 1 to the subnet number to get the first valid IP address; just subtract 1 from the broadcast address to get the last valid IP address. In this case:

10.0.0.1 through 10.255.255.254

Alternatively, you can use the processes that only use decimal math to find the subnet and broadcast address. [Table F-76](vol1_appf.md#appftab76) shows the work for this problem.

**Table F-76** Question 25: Subnet, Broadcast, and First and Last Addresses Calculated Using the Subnet Chart

|  | Octet 1 | Octet 2 | Octet 3 | Octet 4 |
| --- | --- | --- | --- | --- |
| **Mask** | 255 | 0 | 0 | 0 |
| **Address** | 10 | 1 | 1 | 1 |
| **Network Number** | 10 | 0 | 0 | 0 |
| **First Valid Address** | 10 | 0 | 0 | 1 |
| **Last Valid Address** | 10 | 255 | 255 | 254 |
| **Broadcast** | 10 | 255 | 255 | 255 |