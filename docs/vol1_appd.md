# Appendix D


## Practice for Chapter 12: Analyzing Classful IPv4 Networks

### Practice Problems

The practice problems in this appendix require that you determine a few basic facts about a network, given an IP address and an assumption that subnetting is not used in that network. To do so, refer to the processes described in [Chapter 12](vol1_ch12.xhtml#ch12) of *CCNA 200-301 Official Cert Guide, Volume 1*.

Note

You may also elect to do this same set of practice problems using the "Practice Exercise: Analyzing Classful IPv4 Networks" application on the companion website.

In particular, for the upcoming list of IP addresses, you should identify the following information:

* Class of the address
* Number of octets in the network part of the address
* Number of octets in the host part of the address
* Network number
* Network broadcast address

Find all these facts for the following IP addresses:

1. 10.55.44.3
2. 128.77.6.7
3. 192.168.76.54
4. 190.190.190.190
5. 9.1.1.1
6. 200.1.1.1
7. 201.1.77.5
8. 101.1.77.5
9. 119.67.99.240
10. 219.240.66.98

### Answers

The process to answer these problems is relatively basic, so this section reviews the overall process and then lists the answers to problems 1–10.

The process starts by examining the first octet of the IP address:

* If the first octet of the IP address is a number between 1 and 126, inclusive, the address is a Class A address.
* If the first octet of the IP address is a number between 128 and 191, inclusive, the address is a Class B address.
* If the first octet of the IP address is a number between 192 and 223, inclusive, the address is a Class C address.

When no subnetting is used:

* Class A addresses have one octet in the network part of the address and three octets in the host part.
* Class B addresses have two octets each in the network and host part.
* Class C addresses have three octets in the network part and one octet in the host part.

After determining the class and the number of network octets, you can easily find the network number and network broadcast address. To find the network number, copy the network octets of the IP address and write down 0s for the host octets. To find the network broadcast address, copy the network octets of the IP address and write down 255s for the host octets.

[Table D-1](vol1_appd.xhtml#appdtab01) lists all ten problems and their respective answers.

**Table D-1** Answers to Problems

| IP Address | Class | Number of Network Octets | Number of Host Octets | Network Number | Network Broadcast Address |
| --- | --- | --- | --- | --- | --- |
| 10.55.44.3 | A | 1 | 3 | 10.0.0.0 | 10.255.255.255 |
| 128.77.6.7 | B | 2 | 2 | 128.77.0.0 | 128.77.255.255 |
| 192.168.76.54 | C | 3 | 1 | 192.168.76.0 | 192.168.76.255 |
| 190.190.190.190 | B | 2 | 2 | 190.190.0.0 | 190.190.255.255 |
| 9.1.1.1 | A | 1 | 3 | 9.0.0.0 | 9.255.255.255 |
| 200.1.1.1 | C | 3 | 1 | 200.1.1.0 | 200.1.1.255 |
| 201.1.77.55 | C | 3 | 1 | 201.1.77.0 | 201.1.77.255 |
| 101.1.77.55 | A | 1 | 3 | 101.0.0.0 | 101.255.255.255 |
| 119.67.99.240 | A | 1 | 3 | 119.0.0.0 | 119.255.255.255 |
| 219.240.66.98 | C | 3 | 1 | 219.240.66.0 | 219.240.66.255 |