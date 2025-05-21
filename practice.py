import random
import ipaddress
import math
import os
from typing import List, Dict, Tuple, Any, Optional
from datetime import datetime

class NetworkExerciseGenerator:
    """Class to generate network exercises similar to those in CCNA certification guide appendices."""
    
    def __init__(self):
        self.class_ranges = {
            'A': (1, 126),
            'B': (128, 191),
            'C': (192, 223)
        }
        
        # Table of subnet mask values
        self.mask_values = [0, 128, 192, 224, 240, 248, 252, 254, 255]
        
        # Powers of 2 for reference
        self.powers_of_2 = {i: 2**i for i in range(1, 33)}

    def _get_random_ip_by_class(self, ip_class: str) -> str:
        """Generate a random IP address in the specified class."""
        if ip_class not in self.class_ranges:
            raise ValueError(f"Invalid IP class: {ip_class}")
            
        first_octet_range = self.class_ranges[ip_class]
        first_octet = random.randint(first_octet_range[0], first_octet_range[1])
        
        # Generate random values for remaining octets
        second_octet = random.randint(0, 255)
        third_octet = random.randint(0, 255)
        fourth_octet = random.randint(0, 255)
        
        return f"{first_octet}.{second_octet}.{third_octet}.{fourth_octet}"

    def _get_class_of_ip(self, ip: str) -> str:
        """Determine the class of an IP address."""
        first_octet = int(ip.split('.')[0])
        
        if 1 <= first_octet <= 126:
            return 'A'
        elif 128 <= first_octet <= 191:
            return 'B'
        elif 192 <= first_octet <= 223:
            return 'C'
        elif 224 <= first_octet <= 239:
            return 'D'  # Multicast
        elif 240 <= first_octet <= 255:
            return 'E'  # Reserved
        else:
            return 'Special'

    def _get_network_bits(self, ip_class: str) -> int:
        """Get the number of network bits for a given IP class."""
        if ip_class == 'A':
            return 8
        elif ip_class == 'B':
            return 16
        elif ip_class == 'C':
            return 24
        else:
            raise ValueError(f"Invalid or unsupported IP class: {ip_class}")

    def _prefix_to_subnet_mask(self, prefix_length: int) -> str:
        """Convert a prefix length to a subnet mask in dotted decimal notation."""
        mask_bits = '1' * prefix_length + '0' * (32 - prefix_length)
        mask_octets = [
            int(mask_bits[i:i+8], 2) for i in range(0, 32, 8)
        ]
        return '.'.join(str(octet) for octet in mask_octets)

    def _subnet_mask_to_prefix(self, subnet_mask: str) -> int:
        """Convert a subnet mask in dotted decimal notation to prefix length."""
        binary_mask = ''
        for octet in subnet_mask.split('.'):
            binary_mask += bin(int(octet))[2:].zfill(8)
        return binary_mask.count('1')

    def _generate_subnet_mask(self, min_prefix: int = 8, max_prefix: int = 30) -> Tuple[str, int]:
        """Generate a random subnet mask and its prefix length."""
        prefix_length = random.randint(min_prefix, max_prefix)
        subnet_mask = self._prefix_to_subnet_mask(prefix_length)
        return subnet_mask, prefix_length
    
    def _calculate_network_number(self, ip: str, subnet_mask: str) -> str:
        """Calculate the network number given an IP address and subnet mask."""
        ip_octets = [int(octet) for octet in ip.split('.')]
        mask_octets = [int(octet) for octet in subnet_mask.split('.')]
        
        network_octets = [ip_octets[i] & mask_octets[i] for i in range(4)]
        return '.'.join(str(octet) for octet in network_octets)
    
    def _calculate_broadcast_address(self, network: str, subnet_mask: str) -> str:
        """Calculate the broadcast address given a network number and subnet mask."""
        network_octets = [int(octet) for octet in network.split('.')]
        mask_octets = [int(octet) for octet in subnet_mask.split('.')]
        
        # Invert the mask to get the host bits
        inverted_mask = [255 - octet for octet in mask_octets]
        
        # OR the network with the inverted mask to get the broadcast
        broadcast_octets = [network_octets[i] | inverted_mask[i] for i in range(4)]
        return '.'.join(str(octet) for octet in broadcast_octets)
    
    def _get_valid_ip_range(self, network: str, broadcast: str) -> Tuple[str, str]:
        """Get the valid IP range (first and last valid IP) given network and broadcast."""
        network_octets = [int(octet) for octet in network.split('.')]
        broadcast_octets = [int(octet) for octet in broadcast.split('.')]
        
        # First valid IP is network + 1
        first_valid = network_octets.copy()
        first_valid[3] += 1
        if first_valid[3] > 255:
            first_valid[3] = 0
            first_valid[2] += 1
            if first_valid[2] > 255:
                first_valid[2] = 0
                first_valid[1] += 1
                if first_valid[1] > 255:
                    first_valid[1] = 0
                    first_valid[0] += 1
        
        # Last valid IP is broadcast - 1
        last_valid = broadcast_octets.copy()
        last_valid[3] -= 1
        if last_valid[3] < 0:
            last_valid[3] = 255
            last_valid[2] -= 1
            if last_valid[2] < 0:
                last_valid[2] = 255
                last_valid[1] -= 1
                if last_valid[1] < 0:
                    last_valid[1] = 255
                    last_valid[0] -= 1
        
        return (
            '.'.join(str(octet) for octet in first_valid),
            '.'.join(str(octet) for octet in last_valid)
        )
    
    def _calculate_bits_and_counts(self, ip: str, subnet_mask: str) -> Dict[str, Any]:
        """Calculate network, subnet, host bits, number of subnets and hosts."""
        ip_class = self._get_class_of_ip(ip)
        network_bits = self._get_network_bits(ip_class)
        prefix_length = self._subnet_mask_to_prefix(subnet_mask)
        
        host_bits = 32 - prefix_length
        subnet_bits = prefix_length - network_bits
        
        # Calculate number of subnets and hosts
        num_subnets = 2 ** subnet_bits if subnet_bits > 0 else 0
        num_hosts = (2 ** host_bits) - 2 if host_bits > 0 else 0
        
        return {
            'ip_class': ip_class,
            'network_bits': network_bits,
            'subnet_bits': subnet_bits,
            'host_bits': host_bits,
            'num_subnets': num_subnets,
            'num_hosts': num_hosts
        }
    
    def _find_magic_number(self, mask_octet: int) -> int:
        """Find the magic number for a given subnet mask octet."""
        return 256 - mask_octet
    
    def _find_interesting_octet(self, subnet_mask: str) -> int:
        """Find the 'interesting' octet index in a subnet mask."""
        mask_octets = [int(octet) for octet in subnet_mask.split('.')]
        for i, octet in enumerate(mask_octets):
            if octet not in [0, 255]:
                return i
        return 3  # Default to last octet if no interesting octet found
    
    def _generate_all_subnet_ids(self, network: str, subnet_mask: str) -> List[str]:
        """Generate all subnet IDs for a given network and subnet mask."""
        ip_class = self._get_class_of_ip(network)
        network_bits = self._get_network_bits(ip_class)
        prefix_length = self._subnet_mask_to_prefix(subnet_mask)
        subnet_bits = prefix_length - network_bits
        
        if subnet_bits <= 0:
            return [network]  # No subnetting
        
        # Get the network number with all subnet bits set to 0
        network_octets = [int(octet) for octet in network.split('.')]
        mask_octets = [int(octet) for octet in subnet_mask.split('.')]
        
        # Find the indexes where subnet bits are located
        full_binary_network = ''.join(bin(octet)[2:].zfill(8) for octet in network_octets)
        full_binary_mask = ''.join(bin(octet)[2:].zfill(8) for octet in mask_octets)
        
        # Reset subnet bits to zero
        binary_start = full_binary_network[:network_bits]
        binary_rest = '0' * subnet_bits + full_binary_network[network_bits+subnet_bits:]
        zero_subnet_binary = binary_start + binary_rest
        
        # Convert to octets
        zero_subnet_octets = [
            int(zero_subnet_binary[i:i+8], 2) for i in range(0, 32, 8)
        ]
        
        # Find interesting octet and magic number
        interesting_octet = self._find_interesting_octet(subnet_mask)
        magic_number = self._find_magic_number(mask_octets[interesting_octet])
        
        # For subnets that have subnet bits spanning multiple octets
        if subnet_bits <= 8:
            # Simple case: all subnet bits in one octet
            subnet_ids = []
            for i in range(2**subnet_bits):
                subnet_octets = zero_subnet_octets.copy()
                subnet_octets[interesting_octet] = (zero_subnet_octets[interesting_octet] + 
                                                   i * magic_number) % 256
                
                # Handle overflow to next octet
                for j in range(interesting_octet, 0, -1):
                    if subnet_octets[j] < zero_subnet_octets[j] and j > 0:
                        subnet_octets[j-1] += 1
                
                subnet_ids.append('.'.join(str(octet) for octet in subnet_octets))
            return subnet_ids
        else:
            # Complex case: subnet bits span multiple octets
            subnet_ids = []
            total_subnets = 2**subnet_bits
            
            # Find where subnet bits are distributed across octets
            subnet_octets_start = network_bits // 8
            subnet_octets_end = (network_bits + subnet_bits - 1) // 8
            
            # Create a function to generate a subnet address given a subnet index
            def generate_subnet(subnet_index):
                # Start with the zero subnet
                result_octets = zero_subnet_octets.copy()
                
                # Convert subnet index to binary with proper length
                subnet_binary = bin(subnet_index)[2:].zfill(subnet_bits)
                
                # Insert subnet bits into the appropriate positions
                binary_result = list(zero_subnet_binary)
                for i in range(subnet_bits):
                    pos = network_bits + i
                    binary_result[pos] = subnet_binary[i]
                
                # Convert back to octets
                for i in range(4):
                    octet_bits = ''.join(binary_result[i*8:(i+1)*8])
                    result_octets[i] = int(octet_bits, 2)
                
                return '.'.join(str(octet) for octet in result_octets)
            
            # Generate all subnets
            for i in range(total_subnets):
                subnet_ids.append(generate_subnet(i))
                
            return subnet_ids
    
    def generate_classful_analysis_problem(self) -> Dict[str, Any]:
        """Generate a classful IPv4 network analysis problem (Appendix D)."""
        # Randomly choose an IP class
        ip_class = random.choice(['A', 'B', 'C'])
        ip = self._get_random_ip_by_class(ip_class)
        
        # Calculate answers
        network_bits = self._get_network_bits(ip_class)
        host_bits = 32 - network_bits
        
        # Calculate network number and broadcast address
        ip_octets = [int(octet) for octet in ip.split('.')]
        network_octets = ip_octets.copy()
        broadcast_octets = ip_octets.copy()
        
        # Set host bits to 0 for network number and 1 for broadcast
        if ip_class == 'A':
            network_octets[1:] = [0, 0, 0]
            broadcast_octets[1:] = [255, 255, 255]
        elif ip_class == 'B':
            network_octets[2:] = [0, 0]
            broadcast_octets[2:] = [255, 255]
        elif ip_class == 'C':
            network_octets[3:] = [0]
            broadcast_octets[3:] = [255]
        
        network = '.'.join(str(octet) for octet in network_octets)
        broadcast = '.'.join(str(octet) for octet in broadcast_octets)
        
        return {
            'problem': f"Analyze the classful IPv4 address: {ip}",
            'ip': ip,
            'class': ip_class,
            'network_octets': network_bits // 8,
            'host_octets': host_bits // 8,
            'network_number': network,
            'broadcast_address': broadcast
        }
    
    def generate_mask_conversion_problem(self) -> Dict[str, Any]:
        """Generate a subnet mask conversion problem (Appendix E)."""
        # Randomly decide if converting from DDN to prefix or vice versa
        ddn_to_prefix = random.choice([True, False])
        
        if ddn_to_prefix:
            # Generate a valid subnet mask
            prefix = random.randint(8, 30)
            subnet_mask = self._prefix_to_subnet_mask(prefix)
            
            return {
                'problem': f"Convert the dotted-decimal subnet mask to prefix format: {subnet_mask}",
                'subnet_mask': subnet_mask,
                'prefix': f"/{prefix}",
                'direction': 'ddn_to_prefix'
            }
        else:
            # Generate a prefix notation
            prefix = random.randint(8, 30)
            subnet_mask = self._prefix_to_subnet_mask(prefix)
            
            return {
                'problem': f"Convert the prefix format subnet mask to dotted-decimal: /{prefix}",
                'prefix': f"/{prefix}",
                'subnet_mask': subnet_mask,
                'direction': 'prefix_to_ddn'
            }
    
    def generate_mask_analysis_problem(self) -> Dict[str, Any]:
        """Generate a subnet mask analysis problem (Appendix E)."""
        # Randomly choose an IP class
        ip_class = random.choice(['A', 'B', 'C'])
        ip = self._get_random_ip_by_class(ip_class)
        
        # Generate a subnet mask that works with the IP class
        network_bits = self._get_network_bits(ip_class)
        min_prefix = network_bits + 1  # At least 1 subnet bit
        max_prefix = 30  # Leave at least 2 host bits
        
        subnet_mask, prefix = self._generate_subnet_mask(min_prefix, max_prefix)
        
        # Calculate answers
        bits_and_counts = self._calculate_bits_and_counts(ip, subnet_mask)
        
        return {
            'problem': f"Analyze the subnet mask for the IP address and mask: {ip}, {subnet_mask}",
            'ip': ip,
            'subnet_mask': subnet_mask,
            'prefix': f"/{prefix}",
            'network_bits': bits_and_counts['network_bits'],
            'subnet_bits': bits_and_counts['subnet_bits'],
            'host_bits': bits_and_counts['host_bits'],
            'num_subnets': bits_and_counts['num_subnets'],
            'num_hosts': bits_and_counts['num_hosts']
        }
    
    def generate_existing_subnet_analysis_problem(self) -> Dict[str, Any]:
        """Generate an existing subnet analysis problem (Appendix F)."""
        # Randomly choose an IP class
        ip_class = random.choice(['A', 'B', 'C'])
        
        # Generate a subnet mask that works with the IP class
        network_bits = self._get_network_bits(ip_class)
        min_prefix = network_bits + 1  # At least 1 subnet bit
        max_prefix = 30  # Leave at least 2 host bits
        
        subnet_mask, prefix = self._generate_subnet_mask(min_prefix, max_prefix)
        
        # Calculate a valid network number for this subnet mask
        if ip_class == 'A':
            first_octet = random.randint(1, 126)
            base_network = f"{first_octet}.0.0.0"
        elif ip_class == 'B':
            first_octet = random.randint(128, 191)
            second_octet = random.randint(0, 255)
            base_network = f"{first_octet}.{second_octet}.0.0"
        else:  # Class C
            first_octet = random.randint(192, 223)
            second_octet = random.randint(0, 255)
            third_octet = random.randint(0, 255)
            base_network = f"{first_octet}.{second_octet}.{third_octet}.0"
        
        # Generate a random IP in one of the subnets
        network_number = self._calculate_network_number(base_network, subnet_mask)
        broadcast_address = self._calculate_broadcast_address(network_number, subnet_mask)
        first_valid, last_valid = self._get_valid_ip_range(network_number, broadcast_address)
        
        # Generate a random IP in this subnet
        ip_int = random.randint(int(ipaddress.IPv4Address(first_valid)), 
                                int(ipaddress.IPv4Address(last_valid)))
        ip = str(ipaddress.IPv4Address(ip_int))
        
        return {
            'problem': f"Analyze the existing subnet for the IP address and mask: {ip}, {subnet_mask}",
            'ip': ip,
            'subnet_mask': subnet_mask,
            'prefix': f"/{prefix}",
            'subnet_number': network_number,
            'broadcast_address': broadcast_address,
            'first_valid_host': first_valid,
            'last_valid_host': last_valid
        }
    
    def generate_subnet_design_problem(self) -> Dict[str, Any]:
        """Generate a subnet design problem (Appendix G)."""
        # Randomly choose a network
        ip_class = random.choice(['A', 'B', 'C'])
        if ip_class == 'A':
            first_octet = random.randint(1, 126)
            network = f"{first_octet}.0.0.0"
        elif ip_class == 'B':
            first_octet = random.randint(128, 191)
            second_octet = random.randint(0, 255)
            network = f"{first_octet}.{second_octet}.0.0"
        else:  # Class C
            first_octet = random.randint(192, 223)
            second_octet = random.randint(0, 255)
            third_octet = random.randint(0, 255)
            network = f"{first_octet}.{second_octet}.{third_octet}.0"
        
        # Generate requirements
        network_bits = self._get_network_bits(ip_class)
        max_subnet_bits = 30 - network_bits  # Leave at least 2 host bits
        
        # Random number of needed subnets (from 2 to a reasonable max)
        num_subnets = random.randint(2, 2**(max_subnet_bits // 2))
        
        # Random number of hosts per subnet (reasonable based on remaining bits)
        max_possible_hosts = 2**(30 - network_bits - math.ceil(math.log2(num_subnets)))
        num_hosts = random.randint(2, min(500, max_possible_hosts))
        
        # Calculate minimum subnet and host bits needed
        min_subnet_bits = math.ceil(math.log2(num_subnets))
        min_host_bits = math.ceil(math.log2(num_hosts + 2))  # +2 for network/broadcast
        
        # Find all valid masks
        valid_masks = []
        for subnet_bits in range(min_subnet_bits, 32 - network_bits - min_host_bits + 1):
            prefix_length = network_bits + subnet_bits
            if 8 <= prefix_length <= 30:  # Valid prefix range
                subnet_mask = self._prefix_to_subnet_mask(prefix_length)
                valid_masks.append((subnet_mask, prefix_length))
        
        # Choose masks that maximize subnets and hosts
        if valid_masks:
            max_subnets_mask = valid_masks[-1][0]  # Mask with most subnet bits
            max_hosts_mask = valid_masks[0][0]  # Mask with fewest subnet bits
        else:
            max_subnets_mask = "N/A"
            max_hosts_mask = "N/A"
        
        return {
            'problem': f"Design a subnet scheme for network {network}, needing {num_subnets} subnets and {num_hosts} hosts per subnet",
            'network': network,
            'num_subnets_needed': num_subnets,
            'num_hosts_needed': num_hosts,
            'min_subnet_bits': min_subnet_bits,
            'min_host_bits': min_host_bits,
            'valid_masks': [mask for mask, _ in valid_masks],
            'max_subnets_mask': max_subnets_mask,
            'max_hosts_mask': max_hosts_mask
        }
    
    def generate_find_subnet_ids_problem(self) -> Dict[str, Any]:
        """Generate a problem to find all subnet IDs (Appendix G)."""
        # Randomly choose an IP class
        ip_class = random.choice(['A', 'B', 'C'])
        
        # Generate a network
        if ip_class == 'A':
            first_octet = random.randint(1, 126)
            network = f"{first_octet}.0.0.0"
        elif ip_class == 'B':
            first_octet = random.randint(128, 191)
            second_octet = random.randint(0, 255)
            network = f"{first_octet}.{second_octet}.0.0"
        else:  # Class C
            first_octet = random.randint(192, 223)
            second_octet = random.randint(0, 255)
            third_octet = random.randint(0, 255)
            network = f"{first_octet}.{second_octet}.{third_octet}.0"
        
        # Choose a mask with reasonable number of subnets
        network_bits = self._get_network_bits(ip_class)
        
        # Calculate maximum available subnet bits
        max_subnet_bits = 30 - network_bits - 2  # Leave at least 2 host bits
        
        # Check if we can generate problems with > 8 subnet bits
        can_have_many_subnets = max_subnet_bits >= 9
        
        # Randomly decide if we want <= 8 subnet bits or > 8 subnet bits
        # But only if it's possible to have > 8 subnet bits
        if can_have_many_subnets:
            few_subnets = random.choice([True, False])
        else:
            few_subnets = True  # Force few subnets if we can't have many
        
        if few_subnets:
            subnet_bits = random.randint(1, min(8, max_subnet_bits))
        else:
            subnet_bits = random.randint(9, min(16, max_subnet_bits))
        
        prefix_length = network_bits + subnet_bits
        subnet_mask = self._prefix_to_subnet_mask(prefix_length)
        
        # Generate all subnet IDs (limit to prevent too many for display)
        all_subnet_ids = self._generate_all_subnet_ids(network, subnet_mask)
        
        # If too many subnets, just return a sample
        if len(all_subnet_ids) > 20:
            sample_size = min(10, len(all_subnet_ids))
            sample_subnet_ids = random.sample(all_subnet_ids, sample_size)
            # Always include first and last subnets
            if all_subnet_ids[0] not in sample_subnet_ids:
                sample_subnet_ids[0] = all_subnet_ids[0]
            if all_subnet_ids[-1] not in sample_subnet_ids:
                sample_subnet_ids[-1] = all_subnet_ids[-1]
            display_subnets = sample_subnet_ids
            truncated = True
        else:
            display_subnets = all_subnet_ids
            truncated = False
        
        return {
            'problem': f"Find all subnet IDs for network {network} with mask {subnet_mask}",
            'network': network,
            'subnet_mask': subnet_mask,
            'prefix': f"/{prefix_length}",
            'subnet_bits': subnet_bits,
            'few_subnets': few_subnets,
            'all_subnet_ids': all_subnet_ids,
            'display_subnets': display_subnets,
            'truncated': truncated,
            'zero_subnet': all_subnet_ids[0] if all_subnet_ids else "N/A",
            'broadcast_subnet': all_subnet_ids[-1] if all_subnet_ids else "N/A"
        }

class NetworkEducator:
    """Class to provide educational explanations for networking problems"""
    
    def __init__(self):
        self.generator = NetworkExerciseGenerator()
    
    def explain_classful_analysis(self, problem: Dict[str, Any]) -> str:
        """Provide detailed explanation for classful IPv4 network analysis."""
        explanation = f"""
==== EXPLANATION: Classful IPv4 Network Analysis ====

We need to analyze the IP address: {problem['ip']}

STEP 1: Determine the class of the IP address by examining the first octet:
  - Class A: 1-126
  - Class B: 128-191
  - Class C: 192-223
  - Class D: 224-239 (Multicast)
  - Class E: 240-255 (Reserved)

The first octet of {problem['ip']} is {problem['ip'].split('.')[0]}, which falls in the range for Class {problem['class']}.

STEP 2: Based on the class, determine the number of octets for network and host parts:
  - Class A: 1 octet for network, 3 octets for hosts
  - Class B: 2 octets for network, 2 octets for hosts
  - Class C: 3 octets for network, 1 octet for hosts

Since this is a Class {problem['class']} address, we have {problem['network_octets']} octet(s) for the network part and {problem['host_octets']} octet(s) for the host part.

STEP 3: Calculate the network number by setting all host octets to 0:
Original IP: {problem['ip']}
Network number: {problem['network_number']}

STEP 4: Calculate the broadcast address by setting all host octets to 255:
Original IP: {problem['ip']}
Broadcast address: {problem['broadcast_address']}

REMEMBER: All addresses between the network number and broadcast address (inclusive) belong to the same network. The network number and broadcast address cannot be assigned to hosts.

PRACTICE TIP: To quickly identify the network number of a Class A address, just keep the first octet and set the rest to zero. For Class B, keep the first two octets and set the rest to zero. For Class C, keep the first three octets and set the last to zero.

Now you can analyze any classful IPv4 address!
"""
        return explanation
    
    def explain_mask_conversion(self, problem: Dict[str, Any]) -> str:
        """Provide detailed explanation for subnet mask conversion."""
        if problem['direction'] == 'ddn_to_prefix':
            explanation = f"""
==== EXPLANATION: Converting Dotted-Decimal Mask to Prefix Format ====

We need to convert the dotted-decimal subnet mask {problem['subnet_mask']} to prefix format.

METHOD 1: Binary Counting
STEP 1: Convert each octet to binary:
  {problem['subnet_mask'].split('.')[0]} = {bin(int(problem['subnet_mask'].split('.')[0]))[2:].zfill(8)}
  {problem['subnet_mask'].split('.')[1]} = {bin(int(problem['subnet_mask'].split('.')[1]))[2:].zfill(8)}
  {problem['subnet_mask'].split('.')[2]} = {bin(int(problem['subnet_mask'].split('.')[2]))[2:].zfill(8)}
  {problem['subnet_mask'].split('.')[3]} = {bin(int(problem['subnet_mask'].split('.')[3]))[2:].zfill(8)}

STEP 2: Count the number of 1s in the binary representation:
  {bin(int(problem['subnet_mask'].split('.')[0]))[2:].zfill(8).count('1')} + {bin(int(problem['subnet_mask'].split('.')[1]))[2:].zfill(8).count('1')} + {bin(int(problem['subnet_mask'].split('.')[2]))[2:].zfill(8).count('1')} + {bin(int(problem['subnet_mask'].split('.')[3]))[2:].zfill(8).count('1')} = {bin(int(problem['subnet_mask'].split('.')[0]))[2:].zfill(8).count('1') + bin(int(problem['subnet_mask'].split('.')[1]))[2:].zfill(8).count('1') + bin(int(problem['subnet_mask'].split('.')[2]))[2:].zfill(8).count('1') + bin(int(problem['subnet_mask'].split('.')[3]))[2:].zfill(8).count('1')}

STEP 3: The prefix format is /{bin(int(problem['subnet_mask'].split('.')[0]))[2:].zfill(8).count('1') + bin(int(problem['subnet_mask'].split('.')[1]))[2:].zfill(8).count('1') + bin(int(problem['subnet_mask'].split('.')[2]))[2:].zfill(8).count('1') + bin(int(problem['subnet_mask'].split('.')[3]))[2:].zfill(8).count('1')}

METHOD 2: Memorized Values (faster for CCNA exams)
Each octet in the subnet mask can have only the following values:
  0 = 00000000 (0 ones)
  128 = 10000000 (1 one)
  192 = 11000000 (2 ones)
  224 = 11100000 (3 ones)
  240 = 11110000 (4 ones)
  248 = 11111000 (5 ones)
  252 = 11111100 (6 ones)
  254 = 11111110 (7 ones)
  255 = 11111111 (8 ones)

STEP 1: Count the ones in each octet:
  {problem['subnet_mask'].split('.')[0]} = {bin(int(problem['subnet_mask'].split('.')[0]))[2:].zfill(8).count('1')} ones
  {problem['subnet_mask'].split('.')[1]} = {bin(int(problem['subnet_mask'].split('.')[1]))[2:].zfill(8).count('1')} ones
  {problem['subnet_mask'].split('.')[2]} = {bin(int(problem['subnet_mask'].split('.')[2]))[2:].zfill(8).count('1')} ones
  {problem['subnet_mask'].split('.')[3]} = {bin(int(problem['subnet_mask'].split('.')[3]))[2:].zfill(8).count('1')} ones

STEP 2: Add up all the ones: {bin(int(problem['subnet_mask'].split('.')[0]))[2:].zfill(8).count('1')} + {bin(int(problem['subnet_mask'].split('.')[1]))[2:].zfill(8).count('1')} + {bin(int(problem['subnet_mask'].split('.')[2]))[2:].zfill(8).count('1')} + {bin(int(problem['subnet_mask'].split('.')[3]))[2:].zfill(8).count('1')} = {problem['prefix'][1:]}

STEP 3: The prefix format is {problem['prefix']}

PRACTICE TIP: Memorize the number of 1s for each possible mask octet value (0, 128, 192, 224, 240, 248, 252, 254, 255). This makes conversion much faster during the exam!
"""
        else:
            explanation = f"""
==== EXPLANATION: Converting Prefix Format to Dotted-Decimal Mask ====

We need to convert the prefix format {problem['prefix']} to a dotted-decimal subnet mask.

METHOD 1: Binary Construction
STEP 1: Write down {problem['prefix'][1:]} binary 1s followed by {32 - int(problem['prefix'][1:])} binary 0s:
  {'1' * int(problem['prefix'][1:]) + '0' * (32 - int(problem['prefix'][1:]))}

STEP 2: Split this 32-bit number into four 8-bit octets:
  {'1' * int(problem['prefix'][1:]) + '0' * (32 - int(problem['prefix'][1:]))[:8]} {'1' * int(problem['prefix'][1:]) + '0' * (32 - int(problem['prefix'][1:]))[8:16]} {'1' * int(problem['prefix'][1:]) + '0' * (32 - int(problem['prefix'][1:]))[16:24]} {'1' * int(problem['prefix'][1:]) + '0' * (32 - int(problem['prefix'][1:]))[24:32]}

STEP 3: Convert each 8-bit octet to decimal:
  Octet 1: {('1' * min(int(problem['prefix'][1:]), 8) + '0' * max(0, 8 - int(problem['prefix'][1:])))} = {int(('1' * min(int(problem['prefix'][1:]), 8) + '0' * max(0, 8 - int(problem['prefix'][1:]))), 2)}
  Octet 2: {('1' * min(max(0, int(problem['prefix'][1:]) - 8), 8) + '0' * max(0, 8 - max(0, int(problem['prefix'][1:]) - 8)))} = {int(('1' * min(max(0, int(problem['prefix'][1:]) - 8), 8) + '0' * max(0, 8 - max(0, int(problem['prefix'][1:]) - 8))), 2)}
  Octet 3: {('1' * min(max(0, int(problem['prefix'][1:]) - 16), 8) + '0' * max(0, 8 - max(0, int(problem['prefix'][1:]) - 16)))} = {int(('1' * min(max(0, int(problem['prefix'][1:]) - 16), 8) + '0' * max(0, 8 - max(0, int(problem['prefix'][1:]) - 16))), 2)}
  Octet 4: {('1' * min(max(0, int(problem['prefix'][1:]) - 24), 8) + '0' * max(0, 8 - max(0, int(problem['prefix'][1:]) - 24)))} = {int(('1' * min(max(0, int(problem['prefix'][1:]) - 24), 8) + '0' * max(0, 8 - max(0, int(problem['prefix'][1:]) - 24))), 2)}

STEP 4: The dotted-decimal subnet mask is {problem['subnet_mask']}

METHOD 2: Shortcut for Common Prefixes
You can memorize common prefix-to-mask conversions for faster calculations:
  /8 = 255.0.0.0
  /16 = 255.255.0.0
  /24 = 255.255.255.0
  /25 = 255.255.255.128
  /26 = 255.255.255.192
  /27 = 255.255.255.224
  /28 = 255.255.255.240
  /29 = 255.255.255.248
  /30 = 255.255.255.252

For our prefix {problem['prefix']}, the dotted-decimal subnet mask is {problem['subnet_mask']}

PRACTICE TIP: Remember that the prefix number simply tells you how many bits (from left to right) are set to 1 in the 32-bit subnet mask. The remaining bits are set to 0.
"""
        return explanation
    
    def explain_mask_analysis(self, problem: Dict[str, Any]) -> str:
        """Provide detailed explanation for subnet mask analysis."""
        explanation = f"""
==== EXPLANATION: Subnet Mask Analysis ====

We need to analyze the subnet mask {problem['subnet_mask']} for the IP address {problem['ip']}.

STEP 1: Determine the class of the IP address by examining the first octet:
  - Class A: 1-126
  - Class B: 128-191
  - Class C: 192-223

The first octet of {problem['ip']} is {problem['ip'].split('.')[0]}, which falls in the range for Class {self.generator._get_class_of_ip(problem['ip'])}.

STEP 2: Based on the class, determine the number of network bits:
  - Class A: 8 network bits
  - Class B: 16 network bits
  - Class C: 24 network bits

Since this is a Class {self.generator._get_class_of_ip(problem['ip'])} address, we have {problem['network_bits']} network bits.

STEP 3: Convert the subnet mask to prefix format to find the total number of network + subnet bits:
Subnet mask: {problem['subnet_mask']} = {problem['prefix']}

STEP 4: Calculate the number of host bits:
Total bits - Prefix length = 32 - {problem['prefix'][1:]} = {problem['host_bits']} host bits

STEP 5: Calculate the number of subnet bits:
Prefix length - Network bits = {problem['prefix'][1:]} - {problem['network_bits']} = {problem['subnet_bits']} subnet bits

STEP 6: Calculate the number of possible subnets:
2^(number of subnet bits) = 2^{problem['subnet_bits']} = {problem['num_subnets']} subnets

STEP 7: Calculate the number of hosts per subnet:
2^(number of host bits) - 2 = 2^{problem['host_bits']} - 2 = {problem['num_hosts']} hosts per subnet
(We subtract 2 because each subnet needs a network address and a broadcast address)

SUMMARY:
- Network bits: {problem['network_bits']}
- Subnet bits: {problem['subnet_bits']}
- Host bits: {problem['host_bits']}
- Number of subnets: {problem['num_subnets']}
- Number of hosts per subnet: {problem['num_hosts']}

PRACTICE TIP: Remember that the formula for calculating the number of hosts per subnet is always 2^(host bits) - 2, where we subtract 2 to account for the network address and broadcast address, which cannot be assigned to hosts.
"""
        return explanation
    
    def explain_subnet_analysis(self, problem: Dict[str, Any]) -> str:
        """Provide detailed explanation for existing subnet analysis."""
        
        # Determine the interesting octet based on the subnet mask
        mask_octets = [int(octet) for octet in problem['subnet_mask'].split('.')]
        interesting_octet = None
        for i, octet in enumerate(mask_octets):
            if octet not in [0, 255]:
                interesting_octet = i
                break
        
        # Calculate the magic number
        magic_number = 256 - mask_octets[interesting_octet] if interesting_octet is not None else "N/A"
        
        explanation = f"""
==== EXPLANATION: Analyzing Existing Subnets ====

We need to analyze the subnet for IP address {problem['ip']} with subnet mask {problem['subnet_mask']}.

METHOD 1: Boolean AND Operation

STEP 1: Find the subnet number by performing a bitwise AND operation between the IP address and subnet mask:

IP address: {problem['ip']}
   {bin(int(problem['ip'].split('.')[0]))[2:].zfill(8)} {bin(int(problem['ip'].split('.')[1]))[2:].zfill(8)} {bin(int(problem['ip'].split('.')[2]))[2:].zfill(8)} {bin(int(problem['ip'].split('.')[3]))[2:].zfill(8)}

Subnet mask: {problem['subnet_mask']}
   {bin(int(problem['subnet_mask'].split('.')[0]))[2:].zfill(8)} {bin(int(problem['subnet_mask'].split('.')[1]))[2:].zfill(8)} {bin(int(problem['subnet_mask'].split('.')[2]))[2:].zfill(8)} {bin(int(problem['subnet_mask'].split('.')[3]))[2:].zfill(8)}
   
Subnet number (AND result): {problem['subnet_number']}
   {bin(int(problem['subnet_number'].split('.')[0]))[2:].zfill(8)} {bin(int(problem['subnet_number'].split('.')[1]))[2:].zfill(8)} {bin(int(problem['subnet_number'].split('.')[2]))[2:].zfill(8)} {bin(int(problem['subnet_number'].split('.')[3]))[2:].zfill(8)}

STEP 2: Find the broadcast address by changing all host bits to 1s:
- Take the subnet number
- For each position where the subnet mask has a 0, change that bit to a 1

Subnet number: {problem['subnet_number']}
   {bin(int(problem['subnet_number'].split('.')[0]))[2:].zfill(8)} {bin(int(problem['subnet_number'].split('.')[1]))[2:].zfill(8)} {bin(int(problem['subnet_number'].split('.')[2]))[2:].zfill(8)} {bin(int(problem['subnet_number'].split('.')[3]))[2:].zfill(8)}

Inverted mask: {'.'.join(str(255 - int(octet)) for octet in problem['subnet_mask'].split('.'))}
   {bin(255 - int(problem['subnet_mask'].split('.')[0]))[2:].zfill(8)} {bin(255 - int(problem['subnet_mask'].split('.')[1]))[2:].zfill(8)} {bin(255 - int(problem['subnet_mask'].split('.')[2]))[2:].zfill(8)} {bin(255 - int(problem['subnet_mask'].split('.')[3]))[2:].zfill(8)}

Broadcast address (OR result): {problem['broadcast_address']}
   {bin(int(problem['broadcast_address'].split('.')[0]))[2:].zfill(8)} {bin(int(problem['broadcast_address'].split('.')[1]))[2:].zfill(8)} {bin(int(problem['broadcast_address'].split('.')[2]))[2:].zfill(8)} {bin(int(problem['broadcast_address'].split('.')[3]))[2:].zfill(8)}

STEP 3: Find the range of valid IP addresses:
- First valid IP: Subnet number + 1 = {problem['subnet_number']} + 1 = {problem['first_valid_host']}
- Last valid IP: Broadcast address - 1 = {problem['broadcast_address']} - 1 = {problem['last_valid_host']}

METHOD 2: The "Magic Number" Method (Faster for CCNA Exams)

STEP 1: Find the "interesting octet" - the octet where the subnet mask is neither 0 nor 255:
In our subnet mask {problem['subnet_mask']}, the interesting octet is #{interesting_octet + 1 if interesting_octet is not None else None} with value {mask_octets[interesting_octet] if interesting_octet is not None else "N/A"}.

STEP 2: Calculate the "magic number":
Magic number = 256 - mask value in the interesting octet = 256 - {mask_octets[interesting_octet] if interesting_octet is not None else "N/A"} = {magic_number}

STEP 3: Find the subnet number:
- For octets to the left of the interesting octet, copy the IP address
- For the interesting octet, find the multiple of the magic number that's not higher than the IP address value
- For octets to the right of the interesting octet, use 0

STEP 4: Find the broadcast address:
- Copy the subnet number
- For the interesting octet, add the magic number and subtract 1
- For octets to the right of the interesting octet, use 255

PRACTICE TIP: The magic number method is faster for exam calculations because it avoids binary math. Memorize the process for finding the interesting octet and calculating the magic number!
"""
        return explanation
    
    def explain_subnet_design(self, problem: Dict[str, Any]) -> str:
        """Provide detailed explanation for subnet design."""
        explanation = f"""
==== EXPLANATION: Subnet Design ====

We need to design a subnet scheme for network {problem['network']} that supports {problem['num_subnets_needed']} subnets and {problem['num_hosts_needed']} hosts per subnet.

STEP 1: Determine the class of the network:
The network {problem['network']} is a Class {self.generator._get_class_of_ip(problem['network'])} network.

STEP 2: Determine the number of network bits based on the class:
- Class A: 8 network bits
- Class B: 16 network bits
- Class C: 24 network bits

Since this is a Class {self.generator._get_class_of_ip(problem['network'])} network, we have {self.generator._get_network_bits(self.generator._get_class_of_ip(problem['network']))} network bits.

STEP 3: Calculate the minimum number of subnet bits needed:
To support {problem['num_subnets_needed']} subnets, we need enough subnet bits where:
2^(subnet bits) ≥ {problem['num_subnets_needed']}

Testing different values:
2^{problem['min_subnet_bits']-1} = {2**(problem['min_subnet_bits']-1)} (not enough)
2^{problem['min_subnet_bits']} = {2**problem['min_subnet_bits']} (sufficient)

Therefore, we need at least {problem['min_subnet_bits']} subnet bits.

STEP 4: Calculate the minimum number of host bits needed:
To support {problem['num_hosts_needed']} hosts per subnet, we need enough host bits where:
2^(host bits) - 2 ≥ {problem['num_hosts_needed']}
(We subtract 2 because each subnet needs a network address and a broadcast address)

Testing different values:
2^{problem['min_host_bits']-1} - 2 = {2**(problem['min_host_bits']-1) - 2} (not enough)
2^{problem['min_host_bits']} - 2 = {2**problem['min_host_bits'] - 2} (sufficient)

Therefore, we need at least {problem['min_host_bits']} host bits.

STEP 5: Verify that the total number of bits is valid:
Network bits + Subnet bits + Host bits = {self.generator._get_network_bits(self.generator._get_class_of_ip(problem['network']))} + {problem['min_subnet_bits']} + {problem['min_host_bits']} = {self.generator._get_network_bits(self.generator._get_class_of_ip(problem['network'])) + problem['min_subnet_bits'] + problem['min_host_bits']}

This must be ≤ 32 (the total number of bits in an IPv4 address).
{self.generator._get_network_bits(self.generator._get_class_of_ip(problem['network'])) + problem['min_subnet_bits'] + problem['min_host_bits']} {"≤" if self.generator._get_network_bits(self.generator._get_class_of_ip(problem['network'])) + problem['min_subnet_bits'] + problem['min_host_bits'] <= 32 else ">"} 32, so this design is {"valid" if self.generator._get_network_bits(self.generator._get_class_of_ip(problem['network'])) + problem['min_subnet_bits'] + problem['min_host_bits'] <= 32 else "not valid"}.

STEP 6: Determine the valid subnet masks:
- Minimum prefix length: Network bits + Minimum subnet bits = {self.generator._get_network_bits(self.generator._get_class_of_ip(problem['network']))} + {problem['min_subnet_bits']} = /{self.generator._get_network_bits(self.generator._get_class_of_ip(problem['network'])) + problem['min_subnet_bits']}
- Maximum prefix length: 32 - Minimum host bits = 32 - {problem['min_host_bits']} = /{32 - problem['min_host_bits']}

The valid subnet masks include:
{"None" if not problem['valid_masks'] else '\\n'.join(['- ' + mask for mask in problem['valid_masks']])}

STEP 7: Choose the optimal mask based on requirements:
- To maximize the number of subnets: {problem['max_subnets_mask']}
- To maximize the number of hosts per subnet: {problem['max_hosts_mask']}

PRACTICE TIP: Always calculate both the minimum subnet bits and minimum host bits first, then verify that they fit within the 32-bit IPv4 address space before determining the valid subnet masks.
"""
        return explanation
    
    def explain_find_subnet_ids(self, problem: Dict[str, Any]) -> str:
        """Provide detailed explanation for finding subnet IDs."""
        
        # Determine the interesting octet based on the subnet mask
        mask_octets = [int(octet) for octet in problem['subnet_mask'].split('.')]
        interesting_octet = None
        for i, octet in enumerate(mask_octets):
            if octet not in [0, 255]:
                interesting_octet = i
                break
        
        # Calculate the magic number
        magic_number = 256 - mask_octets[interesting_octet] if interesting_octet is not None else "N/A"
        
        # Get sample subnet IDs for demonstration
        sample_subnets = problem['all_subnet_ids'][:min(5, len(problem['all_subnet_ids']))]
        
        explanation = f"""
==== EXPLANATION: Finding All Subnet IDs ====

We need to find all subnet IDs for network {problem['network']} with mask {problem['subnet_mask']} ({problem['prefix']}).

STEP 1: Understand what we're looking for:
- A subnet ID is the network address of each subnet
- For a given network and mask, there are 2^(subnet bits) possible subnets
- In this case, we have {problem['subnet_bits']} subnet bits, so there are 2^{problem['subnet_bits']} = {2**problem['subnet_bits']} possible subnets

STEP 2: Determine the class and network bits:
The network {problem['network']} is a Class {self.generator._get_class_of_ip(problem['network'])} network with {self.generator._get_network_bits(self.generator._get_class_of_ip(problem['network']))} network bits.

STEP 3: Find the "interesting octet" and calculate the "magic number":
- Interesting octet: The octet where the subnet mask is neither 0 nor 255
- In our subnet mask {problem['subnet_mask']}, the interesting octet is #{interesting_octet + 1 if interesting_octet is not None else None} with value {mask_octets[interesting_octet] if interesting_octet is not None else "N/A"}
- Magic number = 256 - mask value in the interesting octet = 256 - {mask_octets[interesting_octet] if interesting_octet is not None else "N/A"} = {magic_number}

STEP 4: Find all subnet IDs:

{"This problem has 8 or fewer subnet bits:" if problem['few_subnets'] else "This problem has more than 8 subnet bits:"}

{"For problems with 8 or fewer subnet bits, we can use the following process:" if problem['few_subnets'] else "For problems with more than 8 subnet bits, the subnets span multiple octets and we need to use a different approach:"}

{
'''
- Start with the zero subnet (the original network number)
- For each subsequent subnet, add the magic number to the interesting octet
- Continue until adding the magic number would exceed 255 in the interesting octet

For example, the first few subnets are:
''' + '\\n'.join([f"- {subnet}" for subnet in sample_subnets]) if problem['few_subnets'] else 
'''
- We have subnet bits that span multiple octets
- We need to create "subnet blocks" by incrementing the "just left" octet
- Within each block, we increment by the magic number in the interesting octet

For example, the first few subnets are:
''' + '\\n'.join([f"- {subnet}" for subnet in sample_subnets])
}

{"In total, there are " + str(len(problem['all_subnet_ids'])) + " subnet IDs, ranging from " + problem['zero_subnet'] + " (zero subnet) to " + problem['broadcast_subnet'] + " (broadcast subnet)."}

PRACTICE TIP: For problems with many subnet IDs, calculate the first few and the last subnet to verify your understanding, rather than listing all of them.
"""
        return explanation

    def get_step_by_step_instructions(self, problem_type: str) -> str:
        """Provide step-by-step instructions for solving different types of problems."""
        if problem_type == 'classful_analysis':
            return """
==== STEP-BY-STEP INSTRUCTIONS: Classful IPv4 Network Analysis ====

1. EXAMINE THE FIRST OCTET to determine the IP class:
   - Class A: 1-126
   - Class B: 128-191
   - Class C: 192-223
   - Class D: 224-239 (Multicast)
   - Class E: 240-255 (Reserved)

2. DETERMINE NETWORK AND HOST PARTS based on the class:
   - Class A: 1 octet for network, 3 octets for hosts
   - Class B: 2 octets for network, 2 octets for hosts
   - Class C: 3 octets for network, 1 octet for hosts

3. CALCULATE THE NETWORK NUMBER:
   - Copy the network octets from the IP address
   - Set all host octets to 0

4. CALCULATE THE BROADCAST ADDRESS:
   - Copy the network octets from the IP address
   - Set all host octets to 255

EXAMPLE:
For IP 192.168.10.25:
- First octet is 192, so it's a Class C address
- Network part: 3 octets (192.168.10), Host part: 1 octet (.25)
- Network number: 192.168.10.0
- Broadcast address: 192.168.10.255
"""
        elif problem_type == 'mask_conversion':
            return """
==== STEP-BY-STEP INSTRUCTIONS: Subnet Mask Conversion ====

FROM DOTTED-DECIMAL TO PREFIX FORMAT:
1. CONVERT EACH OCTET TO BINARY:
   - 255 = 11111111
   - 254 = 11111110
   - 252 = 11111100
   - 248 = 11111000
   - 240 = 11110000
   - 224 = 11100000
   - 192 = 11000000
   - 128 = 10000000
   - 0 = 00000000

2. COUNT THE NUMBER OF 1s in the binary representation
   
3. THE PREFIX IS /n, where n is the total number of 1s

EXAMPLE:
For mask 255.255.240.0:
- 255 = 11111111 (8 ones)
- 255 = 11111111 (8 ones)
- 240 = 11110000 (4 ones)
- 0 = 00000000 (0 ones)
- Total: 8 + 8 + 4 + 0 = 20 ones
- Prefix format is /20

FROM PREFIX FORMAT TO DOTTED-DECIMAL:
1. WRITE n BINARY 1s followed by (32-n) BINARY 0s

2. SPLIT INTO FOUR 8-BIT OCTETS

3. CONVERT EACH OCTET TO DECIMAL:
   - 11111111 = 255
   - 11111110 = 254
   - 11111100 = 252
   - 11111000 = 248
   - 11110000 = 240
   - 11100000 = 224
   - 11000000 = 192
   - 10000000 = 128
   - 00000000 = 0

EXAMPLE:
For prefix /20:
- 20 ones, 12 zeros: 11111111 11111111 11110000 00000000
- Octets: 11111111, 11111111, 11110000, 00000000
- Decimal: 255.255.240.0
"""
        elif problem_type == 'mask_analysis':
            return """
==== STEP-BY-STEP INSTRUCTIONS: Subnet Mask Analysis ====

1. IDENTIFY THE CLASS of the IP address by examining the first octet:
   - Class A: 1-126
   - Class B: 128-191
   - Class C: 192-223

2. DETERMINE THE NUMBER OF NETWORK BITS based on the class:
   - Class A: 8 network bits
   - Class B: 16 network bits
   - Class C: 24 network bits

3. CONVERT THE SUBNET MASK TO PREFIX NOTATION:
   - Count the number of binary 1s in the subnet mask
   - This is the prefix length

4. CALCULATE THE NUMBER OF HOST BITS:
   - Host bits = 32 - prefix length

5. CALCULATE THE NUMBER OF SUBNET BITS:
   - Subnet bits = prefix length - network bits

6. CALCULATE THE NUMBER OF POSSIBLE SUBNETS:
   - Number of subnets = 2^(subnet bits)

7. CALCULATE THE NUMBER OF HOSTS PER SUBNET:
   - Number of hosts per subnet = 2^(host bits) - 2
   - We subtract 2 for the network address and broadcast address

EXAMPLE:
For IP 172.16.10.5 with mask 255.255.240.0:
- First octet is 172, so it's a Class B address
- Network bits = 16
- Mask 255.255.240.0 has 20 binary 1s, so prefix = /20
- Host bits = 32 - 20 = 12
- Subnet bits = 20 - 16 = 4
- Number of subnets = 2^4 = 16
- Number of hosts per subnet = 2^12 - 2 = 4,094
"""
        elif problem_type == 'subnet_analysis':
            return """
==== STEP-BY-STEP INSTRUCTIONS: Analyzing Existing Subnets ====

METHOD 1: BOOLEAN AND OPERATION
1. CONVERT THE IP ADDRESS AND SUBNET MASK TO BINARY

2. CALCULATE THE SUBNET NUMBER using a bitwise AND operation:
   - For each bit position, if both the IP address bit AND the subnet mask bit are 1, the result is 1
   - Otherwise, the result is 0

3. CALCULATE THE BROADCAST ADDRESS:
   - Take the subnet number
   - Change all host bits to 1s (where the subnet mask has 0s)

4. DETERMINE THE VALID IP RANGE:
   - First valid IP = subnet number + 1
   - Last valid IP = broadcast address - 1

METHOD 2: MAGIC NUMBER METHOD (faster for exams)
1. FIND THE "INTERESTING OCTET":
   - The octet in the subnet mask that is neither 0 nor 255

2. CALCULATE THE "MAGIC NUMBER":
   - Magic number = 256 - mask value in the interesting octet

3. CALCULATE THE SUBNET NUMBER:
   - For octets to the left of the interesting octet, copy from the IP address
   - For the interesting octet, find the largest multiple of the magic number that's not greater than the IP value
   - For octets to the right of the interesting octet, use 0

4. CALCULATE THE BROADCAST ADDRESS:
   - For octets to the left of the interesting octet, copy from the subnet number
   - For the interesting octet, add (magic number - 1) to the subnet number's value
   - For octets to the right of the interesting octet, use 255

5. DETERMINE THE VALID IP RANGE:
   - First valid IP = subnet number + 1
   - Last valid IP = broadcast address - 1

EXAMPLE:
For IP 192.168.10.25 with mask 255.255.255.192:
- Interesting octet: 4th octet (192)
- Magic number: 256 - 192 = 64
- Subnet number: 192.168.10.0 (largest multiple of 64 not exceeding 25 is 0)
- Broadcast: 192.168.10.63 (0 + 64 - 1 = 63)
- Valid IPs: 192.168.10.1 to 192.168.10.62
"""
        elif problem_type == 'subnet_design':
            return """
==== STEP-BY-STEP INSTRUCTIONS: Subnet Design ====

1. IDENTIFY THE CLASS OF THE NETWORK to determine the number of network bits:
   - Class A: 8 network bits
   - Class B: 16 network bits
   - Class C: 24 network bits

2. DETERMINE THE MINIMUM NUMBER OF SUBNET BITS NEEDED:
   - Find the smallest value of x where 2^x >= number of required subnets
   - This is the minimum number of subnet bits needed

3. DETERMINE THE MINIMUM NUMBER OF HOST BITS NEEDED:
   - Find the smallest value of y where 2^y - 2 >= number of required hosts per subnet
   - This is the minimum number of host bits needed

4. VERIFY THAT THE TOTAL BITS DO NOT EXCEED 32:
   - Network bits + subnet bits + host bits <= 32

5. DETERMINE THE VALID MASK(S):
   - Minimum prefix length = network bits + minimum subnet bits
   - Maximum prefix length = 32 - minimum host bits
   - All prefix lengths between these values are valid

6. CHOOSE THE OPTIMAL MASK BASED ON REQUIREMENTS:
   - To maximize hosts per subnet: Use the minimum prefix length
   - To maximize number of subnets: Use the maximum prefix length

EXAMPLE:
For network 172.16.0.0 (Class B) needing 100 subnets and 500 hosts per subnet:
- Network bits = 16
- Minimum subnet bits = 7 (2^7 = 128 > 100)
- Minimum host bits = 9 (2^9 - 2 = 510 > 500)
- Total bits = 16 + 7 + 9 = 32 (valid)
- Valid masks: /23 only (16 + 7)
- Since there's only one valid mask, use 255.255.254.0
"""
        elif problem_type == 'find_subnet_ids':
            return """
==== STEP-BY-STEP INSTRUCTIONS: Finding All Subnet IDs ====

FOR 8 OR FEWER SUBNET BITS:
1. IDENTIFY THE CLASS OF THE NETWORK and determine network bits

2. CALCULATE THE NUMBER OF SUBNETS:
   - Number of subnets = 2^(subnet bits)

3. FIND THE INTERESTING OCTET (where the subnet mask is neither 0 nor 255)

4. CALCULATE THE MAGIC NUMBER:
   - Magic number = 256 - mask value in the interesting octet

5. GENERATE ALL SUBNET IDS:
   - Start with the zero subnet (the original network number)
   - For each subsequent subnet, add the magic number to the interesting octet
   - Continue until you've generated all subnets

FOR MORE THAN 8 SUBNET BITS (spanning multiple octets):
1. IDENTIFY THE CLASS OF THE NETWORK and determine network bits

2. CALCULATE THE TOTAL SUBNET BITS:
   - Subnet bits = prefix length - network bits

3. IDENTIFY THE BOUNDARY BETWEEN SUBNET OCTETS:
   - Determine which octets contain subnet bits
   - The rightmost octet with subnet bits is the "interesting octet"
   - The octet(s) to the left with subnet bits is the "just left" octet

4. CALCULATE THE MAGIC NUMBER for the interesting octet

5. GENERATE ALL SUBNET IDS IN BLOCKS:
   - Start with a block where the "just left" octet is 0
   - Generate all subnets within this block by incrementing the interesting octet by the magic number
   - Create new blocks by incrementing the "just left" octet by 1
   - Repeat until all blocks are generated

EXAMPLE:
For network 192.168.0.0 with mask 255.255.255.224 (/27):
- Class C network with 24 network bits
- 3 subnet bits (27 - 24 = 3)
- 8 possible subnets (2^3 = 8)
- Interesting octet: 4th octet (224)
- Magic number: 256 - 224 = 32
- Subnet IDs: 192.168.0.0, 192.168.0.32, 192.168.0.64, 192.168.0.96, 192.168.0.128, 192.168.0.160, 192.168.0.192, 192.168.0.224
"""
        else:
            return "No instructions available for this problem type."

def generate_decimal_binary_table():
    """Generate Table A-1: Decimal-Binary Cross Reference for values 0-255"""
    result = "# Decimal-Binary Cross Reference Table\n\n"
    result += "| Decimal Value | Binary Value | Decimal Value | Binary Value | Decimal Value | Binary Value | Decimal Value | Binary Value |\n"
    result += "| --- | --- | --- | --- | --- | --- | --- | --- |\n"
    
    # Generate rows for values 0-127 (first 32 rows)
    for i in range(32):
        row = []
        for j in range(4):  # 4 columns
            decimal = i + j * 32  # Calculate decimal value
            binary = format(decimal, '08b')  # Convert to 8-bit binary
            decimal_str = str(decimal).rjust(3)
            row.extend([decimal_str, binary])
        
        result += f"| {row[0]} | {row[1]} | {row[2]} | {row[3]} | {row[4]} | {row[5]} | {row[6]} | {row[7]} |\n"
    
    # Generate rows for values 128-255 (next 32 rows)
    for i in range(32):
        row = []
        for j in range(4):  # 4 columns
            decimal = i + j * 32 + 128  # Calculate decimal value (starting from 128)
            binary = format(decimal, '08b')  # Convert to 8-bit binary
            decimal_str = str(decimal).rjust(3)
            row.extend([decimal_str, binary])
        
        result += f"| {row[0]} | {row[1]} | {row[2]} | {row[3]} | {row[4]} | {row[5]} | {row[6]} | {row[7]} |\n"
    
    return result

def generate_hex_binary_table():
    """Generate Table A-2: Hex-Binary Cross Reference"""
    result = "# Hex-Binary Cross Reference\n\n"
    
    result += "| Hex | 4-Bit Binary |\n"
    result += "| --- | --- |\n"
    
    hex_chars = "0123456789ABCDEF"
    for char in hex_chars:
        decimal = int(char, 16)  # Convert hex to decimal
        binary = format(decimal, '04b')  # Convert to 4-bit binary
        result += f"| {char} | {binary} |\n"
    
    return result

def generate_subnet_exercises_markdown(num_exercises=10, output_file="subnet_exercises.md"):
    """Generate subnet exercises and save them to a markdown file with an answer sheet."""
    generator = NetworkExerciseGenerator()
    
    # Create the markdown content
    markdown_content = f"""# CCNA Subnet Exercises
*Generated on {datetime.now().strftime('%Y-%m-%d at %H:%M')}*

## Practice Problems

This document contains {num_exercises} subnet ID finding problems to help you practice your subnetting skills.

"""
    
    # Generate problems
    problems = []
    for i in range(num_exercises):
        problem = generator.generate_find_subnet_ids_problem()
        problems.append(problem)
        
        markdown_content += f"### Problem {i+1}\n"
        markdown_content += f"Find all subnet IDs for network {problem['network']} with mask {problem['subnet_mask']} ({problem['prefix']}).\n\n"
    
    # Add answer sheet
    markdown_content += "\n\n## Answer Sheet\n\n"
    
    for i, problem in enumerate(problems):
        markdown_content += f"### Answer to Problem {i+1}\n"
        markdown_content += f"Network: {problem['network']}\n"
        markdown_content += f"Mask: {problem['subnet_mask']} ({problem['prefix']})\n"
        
        # Add explanation about the class and bits
        ip_class = generator._get_class_of_ip(problem['network'])
        network_bits = generator._get_network_bits(ip_class)
        host_bits = 32 - int(problem['prefix'][1:])
        subnet_bits = int(problem['prefix'][1:]) - network_bits
        
        markdown_content += f"\nClass {ip_class} network with:\n"
        markdown_content += f"- {network_bits} network bits\n"
        markdown_content += f"- {subnet_bits} subnet bits\n"
        markdown_content += f"- {host_bits} host bits\n"
        markdown_content += f"- {2**subnet_bits} total subnets\n"
        markdown_content += f"- {2**host_bits - 2} hosts per subnet\n\n"
        
        # Add subnet IDs
        markdown_content += "Subnet IDs:\n"
        
        if len(problem['all_subnet_ids']) <= 20:
            # Show all subnets if there aren't too many
            for subnet in problem['all_subnet_ids']:
                if subnet == problem['zero_subnet']:
                    markdown_content += f"- {subnet} (zero subnet)\n"
                elif subnet == problem['broadcast_subnet']:
                    markdown_content += f"- {subnet} (broadcast subnet)\n"
                else:
                    markdown_content += f"- {subnet}\n"
        else:
            # Show first few, last few, and total count for larger subnet lists
            markdown_content += "First 5 subnets:\n"
            for subnet in problem['all_subnet_ids'][:5]:
                suffix = " (zero subnet)" if subnet == problem['zero_subnet'] else ""
                markdown_content += f"- {subnet}{suffix}\n"
                
            markdown_content += f"\n... (omitting {len(problem['all_subnet_ids']) - 10} subnets) ...\n\n"
            
            markdown_content += "Last 5 subnets:\n"
            for subnet in problem['all_subnet_ids'][-5:]:
                suffix = " (broadcast subnet)" if subnet == problem['broadcast_subnet'] else ""
                markdown_content += f"- {subnet}{suffix}\n"
                
        markdown_content += "\n"
    
    # Add explanation of subnet calculation
    markdown_content += """
## How to Calculate Subnets

To find all subnet IDs for a given network and mask, follow these steps:

1. **Identify the class of the network address** to determine the number of network bits:
   - Class A (1-126 in first octet): 8 network bits
   - Class B (128-191 in first octet): 16 network bits
   - Class C (192-223 in first octet): 24 network bits

2. **Calculate the number of subnet bits**:
   - Subnet bits = (prefix length) - (network bits)
   - Example: For a Class C with /27, subnet bits = 27 - 24 = 3

3. **Find the "interesting octet"**:
   - The octet where the subnet mask is neither 0 nor 255
   - This is where you'll increment by the "magic number"

4. **Calculate the "magic number"**:
   - Magic number = 256 - (mask value in the interesting octet)
   - Example: For mask 255.255.255.224, magic number = 256 - 224 = 32

5. **Generate all subnet IDs**:
   - Start with the zero subnet (the original network number with all subnet bits set to 0)
   - For each subsequent subnet, add the magic number to the interesting octet
   - Continue until you've created 2^(subnet bits) subnets

6. **For networks with subnet bits spanning multiple octets**:
   - Create "subnet blocks" by incrementing the "just left" octet
   - Within each block, increment by the magic number in the interesting octet

Remember: The total number of subnets is always 2^(subnet bits).
"""
    
    # Write to file
    with open(output_file, 'w') as f:
        f.write(markdown_content)
    
    return output_file

def generate_mask_conversion_exercises_markdown(num_exercises=10, output_file="mask_conversion_exercises.md"):
    """Generate mask conversion exercises and save them to a markdown file with an answer sheet."""
    generator = NetworkExerciseGenerator()
    
    # Create the markdown content
    markdown_content = f"""# CCNA Mask Conversion Exercises
*Generated on {datetime.now().strftime('%Y-%m-%d at %H:%M')}*

## Practice Problems

This document contains {num_exercises} mask conversion problems to help you practice your subnetting skills.

"""
    
    # Generate problems
    problems = []
    for i in range(num_exercises):
        # Alternate between DDN to prefix and prefix to DDN
        if i % 2 == 0:
            problem = generator.generate_mask_conversion_problem()
        else:
            problem = generator.generate_mask_conversion_problem()
            # Ensure it's the opposite type from the previous problem
            if problem['direction'] == problems[-1]['direction']:
                if problem['direction'] == 'ddn_to_prefix':
                    # Change to prefix to DDN
                    problem['direction'] = 'prefix_to_ddn'
                    problem['problem'] = f"Convert the prefix format subnet mask to dotted-decimal: {problem['prefix']}"
                else:
                    # Change to DDN to prefix
                    problem['direction'] = 'ddn_to_prefix'
                    problem['problem'] = f"Convert the dotted-decimal subnet mask to prefix format: {problem['subnet_mask']}"
        
        problems.append(problem)
        markdown_content += f"### Problem {i+1}\n"
        markdown_content += f"{problem['problem']}\n\n"
    
    # Add answer sheet
    markdown_content += "\n\n## Answer Sheet\n\n"
    
    for i, problem in enumerate(problems):
        markdown_content += f"### Answer to Problem {i+1}\n"
        if problem['direction'] == 'ddn_to_prefix':
            markdown_content += f"Subnet mask: {problem['subnet_mask']}\n"
            markdown_content += f"Prefix format: {problem['prefix']}\n\n"
            
            # Add binary conversion explanation
            binary_octets = []
            ones_count = 0
            
            for octet in problem['subnet_mask'].split('.'):
                binary = bin(int(octet))[2:].zfill(8)
                binary_octets.append(binary)
                ones_count += binary.count('1')
            
            markdown_content += "#### Binary Conversion:\n"
            markdown_content += f"```\n{problem['subnet_mask']} = {' '.join(binary_octets)}\n```\n\n"
            markdown_content += f"Count the number of binary 1s: {ones_count}\n"
            markdown_content += f"Therefore, the prefix notation is /{ones_count}\n\n"
        else:  # prefix_to_ddn
            markdown_content += f"Prefix: {problem['prefix']}\n"
            markdown_content += f"Dotted decimal: {problem['subnet_mask']}\n\n"
            
            # Add binary conversion explanation
            prefix_length = int(problem['prefix'][1:])
            binary = '1' * prefix_length + '0' * (32 - prefix_length)
            binary_octets = [binary[i:i+8] for i in range(0, 32, 8)]
            decimal_octets = [str(int(octet, 2)) for octet in binary_octets]
            
            markdown_content += "#### Binary Conversion:\n"
            markdown_content += f"/{prefix_length} means {prefix_length} binary 1s followed by {32-prefix_length} binary 0s:\n"
            markdown_content += f"```\n{' '.join(binary_octets)}\n```\n\n"
            markdown_content += "Converting each octet to decimal:\n"
            markdown_content += f"```\n{binary_octets[0]} = {decimal_octets[0]}\n{binary_octets[1]} = {decimal_octets[1]}\n{binary_octets[2]} = {decimal_octets[2]}\n{binary_octets[3]} = {decimal_octets[3]}\n```\n\n"
            markdown_content += f"Therefore, the dotted decimal notation is {'.'.join(decimal_octets)}\n\n"
    
    # Add conversion reference table
    markdown_content += """
## Subnet Mask Conversion Reference

### Dotted Decimal to Binary Conversion

| Decimal | Binary | # of 1s |
|---------|--------|---------|
| 0       | 00000000 | 0     |
| 128     | 10000000 | 1     |
| 192     | 11000000 | 2     |
| 224     | 11100000 | 3     |
| 240     | 11110000 | 4     |
| 248     | 11111000 | 5     |
| 252     | 11111100 | 6     |
| 254     | 11111110 | 7     |
| 255     | 11111111 | 8     |

### Common Subnet Mask Conversions

| Prefix | Dotted Decimal    |
|--------|-------------------|
| /8     | 255.0.0.0         |
| /16    | 255.255.0.0       |
| /24    | 255.255.255.0     |
| /25    | 255.255.255.128   |
| /26    | 255.255.255.192   |
| /27    | 255.255.255.224   |
| /28    | 255.255.255.240   |
| /29    | 255.255.255.248   |
| /30    | 255.255.255.252   |
"""
    
    # Write to file
    with open(output_file, 'w') as f:
        f.write(markdown_content)
    
    return output_file

def generate_subnet_design_exercises_markdown(num_exercises=10, output_file="subnet_design_exercises.md"):
    """Generate subnet design exercises and save them to a markdown file with an answer sheet."""
    generator = NetworkExerciseGenerator()
    
    # Create the markdown content
    markdown_content = f"""# CCNA Subnet Design Exercises
*Generated on {datetime.now().strftime('%Y-%m-%d at %H:%M')}*

## Practice Problems

This document contains {num_exercises} subnet design problems to help you practice your subnetting skills.

"""
    
    # Generate problems
    problems = []
    for i in range(num_exercises):
        problem = generator.generate_subnet_design_problem()
        problems.append(problem)
        
        markdown_content += f"### Problem {i+1}\n"
        markdown_content += f"{problem['problem']}\n\n"
    
    # Add answer sheet
    markdown_content += "\n\n## Answer Sheet\n\n"
    
    for i, problem in enumerate(problems):
        markdown_content += f"### Answer to Problem {i+1}\n"
        markdown_content += f"Network: {problem['network']}\n"
        markdown_content += f"Required subnets: {problem['num_subnets_needed']}\n"
        markdown_content += f"Required hosts per subnet: {problem['num_hosts_needed']}\n\n"
        
        # Add explanation
        ip_class = generator._get_class_of_ip(problem['network'])
        network_bits = generator._get_network_bits(ip_class)
        
        markdown_content += f"#### Analysis:\n"
        markdown_content += f"- Class {ip_class} network with {network_bits} network bits\n"
        markdown_content += f"- Minimum subnet bits needed: {problem['min_subnet_bits']} (2^{problem['min_subnet_bits']} = {2**problem['min_subnet_bits']} subnets)\n"
        markdown_content += f"- Minimum host bits needed: {problem['min_host_bits']} (2^{problem['min_host_bits']} - 2 = {2**problem['min_host_bits'] - 2} hosts per subnet)\n\n"
        
        if problem['valid_masks']:
            markdown_content += "#### Valid subnet masks:\n"
            for mask in problem['valid_masks']:
                markdown_content += f"- {mask}\n"
            
            markdown_content += f"\n- Mask that maximizes subnets: {problem['max_subnets_mask']}\n"
            markdown_content += f"- Mask that maximizes hosts per subnet: {problem['max_hosts_mask']}\n\n"
        else:
            markdown_content += "No valid subnet masks found. The requirements cannot be met with the available bits.\n\n"
    
    # Add subnet design guidelines
    markdown_content += """
## Subnet Design Guidelines

To design an appropriate subnet scheme:

1. **Identify the network class and network bits**:
   - Class A: 8 network bits
   - Class B: 16 network bits
   - Class C: 24 network bits

2. **Calculate minimum subnet bits needed**:
   - Find the smallest value of x where 2^x ≥ number of required subnets
   - Example: For 100 subnets, you need 7 subnet bits (2^7 = 128 ≥ 100)

3. **Calculate minimum host bits needed**:
   - Find the smallest value of y where 2^y - 2 ≥ number of required hosts per subnet
   - Example: For 300 hosts, you need 9 host bits (2^9 - 2 = 510 - 2 = 508 ≥ 300)

4. **Verify that the total bits doesn't exceed 32**:
   - Network bits + subnet bits + host bits must be ≤ 32
   - If the total exceeds 32, the requirements cannot be met

5. **Determine valid subnet masks**:
   - Minimum prefix length = Network bits + minimum subnet bits
   - Maximum prefix length = 32 - minimum host bits
   - All prefix lengths between these values are valid masks

6. **Choose the optimal mask based on requirements**:
   - To maximize hosts per subnet: Use the mask with smallest subnet bits (minimum prefix)
   - To maximize subnets: Use the mask with largest subnet bits (maximum prefix)
"""
    
    # Write to file
    with open(output_file, 'w') as f:
        f.write(markdown_content)
    
    return output_file

def generate_existing_subnet_analysis_exercises_markdown(num_exercises=10, output_file="subnet_analysis_exercises.md"):
    """Generate subnet analysis exercises and save them to a markdown file with an answer sheet."""
    generator = NetworkExerciseGenerator()
    
    # Create the markdown content
    markdown_content = f"""# CCNA Subnet Analysis Exercises
*Generated on {datetime.now().strftime('%Y-%m-%d at %H:%M')}*

## Practice Problems

This document contains {num_exercises} subnet analysis problems to help you practice analyzing existing subnets.

"""
    
    # Generate problems
    problems = []
    for i in range(num_exercises):
        problem = generator.generate_existing_subnet_analysis_problem()
        problems.append(problem)
        
        markdown_content += f"### Problem {i+1}\n"
        markdown_content += f"{problem['problem']}\n\n"
    
    # Add answer sheet
    markdown_content += "\n\n## Answer Sheet\n\n"
    
    for i, problem in enumerate(problems):
        markdown_content += f"### Answer to Problem {i+1}\n"
        markdown_content += f"IP address: {problem['ip']}\n"
        markdown_content += f"Subnet mask: {problem['subnet_mask']} ({problem['prefix']})\n\n"
        
        # Add explanation
        ip_class = generator._get_class_of_ip(problem['ip'])
        network_bits = generator._get_network_bits(ip_class)
        host_bits = 32 - int(problem['prefix'][1:])
        subnet_bits = int(problem['prefix'][1:]) - network_bits
        
        markdown_content += f"#### Analysis:\n"
        markdown_content += f"- Class {ip_class} network with {network_bits} network bits\n"
        markdown_content += f"- {subnet_bits} subnet bits\n"
        markdown_content += f"- {host_bits} host bits\n\n"
        
        markdown_content += f"#### Results:\n"
        markdown_content += f"- Subnet number: {problem['subnet_number']}\n"
        markdown_content += f"- Broadcast address: {problem['broadcast_address']}\n"
        markdown_content += f"- Valid IP address range: {problem['first_valid_host']} through {problem['last_valid_host']}\n\n"
        
        # Add magic number calculation explanation
        mask_octets = [int(octet) for octet in problem['subnet_mask'].split('.')]
        interesting_octet = None
        for i, octet in enumerate(mask_octets):
            if octet not in [0, 255]:
                interesting_octet = i
                break
        
        if interesting_octet is not None:
            magic_number = 256 - mask_octets[interesting_octet]
            interesting_octet_names = ['first', 'second', 'third', 'fourth']
            
            markdown_content += f"#### Magic Number Method:\n"
            markdown_content += f"- Interesting octet: {interesting_octet_names[interesting_octet]} octet ({mask_octets[interesting_octet]})\n"
            markdown_content += f"- Magic number: 256 - {mask_octets[interesting_octet]} = {magic_number}\n"
            
            ip_octets = [int(octet) for octet in problem['ip'].split('.')]
            subnet_octets = [int(octet) for octet in problem['subnet_number'].split('.')]
            
            markdown_content += f"- To find subnet number: Find largest multiple of {magic_number} not exceeding {ip_octets[interesting_octet]} in the {interesting_octet_names[interesting_octet]} octet\n"
            markdown_content += f"  {ip_octets[interesting_octet]} ÷ {magic_number} = {ip_octets[interesting_octet] // magic_number} remainder {ip_octets[interesting_octet] % magic_number}\n"
            markdown_content += f"  {magic_number} × {ip_octets[interesting_octet] // magic_number} = {subnet_octets[interesting_octet]}\n\n"
    
    # Add subnet analysis technique explanation
    markdown_content += """
## Subnet Analysis Techniques

### Boolean AND Method

To analyze a subnet given an IP address and subnet mask:

1. **Calculate the subnet number** using a Boolean AND operation:
   - Perform a bitwise AND between the IP address and subnet mask
   - This zeros out all host bits while keeping network and subnet bits
   - Example: 192.168.10.25 AND 255.255.255.192 = 192.168.10.0

2. **Calculate the broadcast address**:
   - Copy the subnet number
   - Set all host bits to 1 (OR the subnet number with the inverted mask)
   - Example: 192.168.10.0 OR 0.0.0.63 = 192.168.10.63

3. **Determine the valid IP range**:
   - First valid IP = Subnet number + 1
   - Last valid IP = Broadcast address - 1

### Magic Number Method (Faster for Exams)

1. **Locate the "interesting octet"** - the octet where the subnet mask is neither 0 nor 255

2. **Calculate the "magic number"**: 
   - Magic number = 256 - (mask value in the interesting octet)
   - Example: For mask 255.255.255.192, Magic number = 256 - 192 = 64

3. **Calculate the subnet number**:
   - For octets to the left of the interesting octet, copy the IP address
   - For the interesting octet, find the multiple of the magic number not exceeding the IP value
   - For octets to the right of interesting octet, use 0

4. **Calculate the broadcast address**:
   - For octets to the left of the interesting octet, copy the subnet number
   - For the interesting octet, add the magic number and subtract 1
   - For octets to the right of the interesting octet, use 255
"""
    
    # Write to file
    with open(output_file, 'w') as f:
        f.write(markdown_content)
    
    return output_file

def generate_complete_practice_exam(output_file="ccna_practice_exam.md"):
    """Generate a complete CCNA practice exam with multiple types of problems."""
    generator = NetworkExerciseGenerator()
    
    # Create the markdown content
    markdown_content = f"""# CCNA Subnetting Practice Exam
*Generated on {datetime.now().strftime('%Y-%m-%d at %H:%M')}*

This practice exam contains various types of subnetting problems commonly found on the CCNA exam.

## Section 1: Classful Network Analysis

"""
    
    # Generate classful analysis problems
    classful_problems = []
    for i in range(5):
        problem = generator.generate_classful_analysis_problem()
        classful_problems.append(problem)
        
        markdown_content += f"### Problem {i+1}\n"
        markdown_content += f"{problem['problem']}\n\n"
    
    markdown_content += "\n## Section 2: Subnet Mask Conversion\n\n"
    
    # Generate mask conversion problems
    mask_problems = []
    for i in range(5):
        problem = generator.generate_mask_conversion_problem()
        mask_problems.append(problem)
        
        markdown_content += f"### Problem {i+6}\n"
        markdown_content += f"{problem['problem']}\n\n"
    
    markdown_content += "\n## Section 3: Subnet Mask Analysis\n\n"
    
    # Generate subnet mask analysis problems
    analysis_problems = []
    for i in range(5):
        problem = generator.generate_mask_analysis_problem()
        analysis_problems.append(problem)
        
        markdown_content += f"### Problem {i+11}\n"
        markdown_content += f"{problem['problem']}\n\n"
    
    markdown_content += "\n## Section 4: Existing Subnet Analysis\n\n"
    
    # Generate existing subnet analysis problems
    subnet_analysis_problems = []
    for i in range(5):
        problem = generator.generate_existing_subnet_analysis_problem()
        subnet_analysis_problems.append(problem)
        
        markdown_content += f"### Problem {i+16}\n"
        markdown_content += f"{problem['problem']}\n\n"
    
    markdown_content += "\n## Section 5: Subnet Design\n\n"
    
    # Generate subnet design problems
    design_problems = []
    for i in range(5):
        problem = generator.generate_subnet_design_problem()
        design_problems.append(problem)
        
        markdown_content += f"### Problem {i+21}\n"
        markdown_content += f"{problem['problem']}\n\n"
    
    markdown_content += "\n## Section 6: Finding Subnet IDs\n\n"
    
    # Generate finding subnet IDs problems
    subnet_ids_problems = []
    for i in range(5):
        problem = generator.generate_find_subnet_ids_problem()
        subnet_ids_problems.append(problem)
        
        markdown_content += f"### Problem {i+26}\n"
        markdown_content += f"{problem['problem']}\n\n"
    
    # Add answer key
    markdown_content += "\n\n# Answer Key\n\n"
    
    # Classful analysis answers
    markdown_content += "## Section 1: Classful Network Analysis\n\n"
    for i, problem in enumerate(classful_problems):
        markdown_content += f"### Answer to Problem {i+1}\n"
        markdown_content += f"IP address: {problem['ip']}\n"
        markdown_content += f"Class: {problem['class']}\n"
        markdown_content += f"Network octets: {problem['network_octets']}\n"
        markdown_content += f"Host octets: {problem['host_octets']}\n"
        markdown_content += f"Network number: {problem['network_number']}\n"
        markdown_content += f"Broadcast address: {problem['broadcast_address']}\n\n"
    
    # Mask conversion answers
    markdown_content += "## Section 2: Subnet Mask Conversion\n\n"
    for i, problem in enumerate(mask_problems):
        markdown_content += f"### Answer to Problem {i+6}\n"
        if problem['direction'] == 'ddn_to_prefix':
            markdown_content += f"Subnet mask: {problem['subnet_mask']}\n"
            markdown_content += f"Prefix format: {problem['prefix']}\n\n"
        else:
            markdown_content += f"Prefix: {problem['prefix']}\n"
            markdown_content += f"Dotted decimal: {problem['subnet_mask']}\n\n"
    
    # Subnet mask analysis answers
    markdown_content += "## Section 3: Subnet Mask Analysis\n\n"
    for i, problem in enumerate(analysis_problems):
        markdown_content += f"### Answer to Problem {i+11}\n"
        markdown_content += f"IP address: {problem['ip']}\n"
        markdown_content += f"Subnet mask: {problem['subnet_mask']} ({problem['prefix']})\n"
        markdown_content += f"Network bits: {problem['network_bits']}\n"
        markdown_content += f"Subnet bits: {problem['subnet_bits']}\n"
        markdown_content += f"Host bits: {problem['host_bits']}\n"
        markdown_content += f"Number of subnets: {problem['num_subnets']}\n"
        markdown_content += f"Number of hosts per subnet: {problem['num_hosts']}\n\n"
    
    # Existing subnet analysis answers
    markdown_content += "## Section 4: Existing Subnet Analysis\n\n"
    for i, problem in enumerate(subnet_analysis_problems):
        markdown_content += f"### Answer to Problem {i+16}\n"
        markdown_content += f"IP address: {problem['ip']}\n"
        markdown_content += f"Subnet mask: {problem['subnet_mask']} ({problem['prefix']})\n"
        markdown_content += f"Subnet number: {problem['subnet_number']}\n"
        markdown_content += f"Broadcast address: {problem['broadcast_address']}\n"
        markdown_content += f"Valid IP address range: {problem['first_valid_host']} through {problem['last_valid_host']}\n\n"
    
    # Subnet design answers
    markdown_content += "## Section 5: Subnet Design\n\n"
    for i, problem in enumerate(design_problems):
        markdown_content += f"### Answer to Problem {i+21}\n"
        markdown_content += f"Network: {problem['network']}\n"
        markdown_content += f"Required subnets: {problem['num_subnets_needed']}\n"
        markdown_content += f"Required hosts per subnet: {problem['num_hosts_needed']}\n"
        markdown_content += f"Minimum subnet bits: {problem['min_subnet_bits']}\n"
        markdown_content += f"Minimum host bits: {problem['min_host_bits']}\n"
        
        if problem['valid_masks']:
            markdown_content += "Valid subnet masks:\n"
            for mask in problem['valid_masks']:
                markdown_content += f"- {mask}\n"
            
            markdown_content += f"Mask to maximize subnets: {problem['max_subnets_mask']}\n"
            markdown_content += f"Mask to maximize hosts per subnet: {problem['max_hosts_mask']}\n\n"
        else:
            markdown_content += "No valid subnet masks found. The requirements cannot be met with the available bits.\n\n"
    
    # Finding subnet IDs answers
    markdown_content += "## Section 6: Finding Subnet IDs\n\n"
    for i, problem in enumerate(subnet_ids_problems):
        markdown_content += f"### Answer to Problem {i+26}\n"
        markdown_content += f"Network: {problem['network']}\n"
        markdown_content += f"Subnet mask: {problem['subnet_mask']} ({problem['prefix']})\n"
        
        # Add explanation about the class and bits
        ip_class = generator._get_class_of_ip(problem['network'])
        network_bits = generator._get_network_bits(ip_class)
        host_bits = 32 - int(problem['prefix'][1:])
        subnet_bits = int(problem['prefix'][1:]) - network_bits
        
        markdown_content += f"Class {ip_class} network with {network_bits} network bits, {subnet_bits} subnet bits, and {host_bits} host bits\n"
        markdown_content += f"Total subnets: 2^{subnet_bits} = {2**subnet_bits}\n\n"
        
        # Add subnet IDs
        if len(problem['all_subnet_ids']) <= 20:
            # Show all subnets if there aren't too many
            markdown_content += "Subnet IDs:\n"
            for subnet in problem['all_subnet_ids']:
                if subnet == problem['zero_subnet']:
                    markdown_content += f"- {subnet} (zero subnet)\n"
                elif subnet == problem['broadcast_subnet']:
                    markdown_content += f"- {subnet} (broadcast subnet)\n"
                else:
                    markdown_content += f"- {subnet}\n"
        else:
            # Show first few, last few, and total count for larger subnet lists
            markdown_content += "First few subnets:\n"
            for subnet in problem['all_subnet_ids'][:5]:
                suffix = " (zero subnet)" if subnet == problem['zero_subnet'] else ""
                markdown_content += f"- {subnet}{suffix}\n"
                
            markdown_content += f"\n... (omitting {len(problem['all_subnet_ids']) - 10} subnets) ...\n\n"
            
            markdown_content += "Last few subnets:\n"
            for subnet in problem['all_subnet_ids'][-5:]:
                suffix = " (broadcast subnet)" if subnet == problem['broadcast_subnet'] else ""
                markdown_content += f"- {subnet}{suffix}\n"
        
        markdown_content += "\n"
    
    # Add reference information
    markdown_content += """
# Reference Information

## IP Address Classes

| Class | First Octet Range | Default Mask | Network Bits | Host Bits | Networks | Hosts per Network |
|-------|-------------------|--------------|--------------|-----------|----------|-------------------|
| A     | 1-126             | 255.0.0.0    | 8            | 24        | 126      | 16,777,214        |
| B     | 128-191           | 255.255.0.0  | 16           | 16        | 16,384   | 65,534            |
| C     | 192-223           | 255.255.255.0| 24           | 8         | 2,097,152| 254               |

Note: 127.x.x.x is reserved for loopback. Class D (224-239) is for multicast, and Class E (240-255) is reserved.

## Subnet Mask Values

| Decimal | Binary    | Prefix | Hosts |
|---------|-----------|--------|-------|
| 0       | 00000000  | /0     | -     |
| 128     | 10000000  | /1     | -     |
| 192     | 11000000  | /2     | -     |
| 224     | 11100000  | /3     | -     |
| 240     | 11110000  | /4     | -     |
| 248     | 11111000  | /5     | -     |
| 252     | 11111100  | /6     | -     |
| 254     | 11111110  | /7     | -     |
| 255     | 11111111  | /8     | -     |

## Powers of 2 Reference

| Power of 2 | Value    | Power of 2 | Value      |
|------------|----------|------------|------------|
| 2^1        | 2        | 2^9        | 512        |
| 2^2        | 4        | 2^10       | 1,024      |
| 2^3        | 8        | 2^11       | 2,048      |
| 2^4        | 16       | 2^12       | 4,096      |
| 2^5        | 32       | 2^13       | 8,192      |
| 2^6        | 64       | 2^14       | 16,384     |
| 2^7        | 128      | 2^15       | 32,768     |
| 2^8        | 256      | 2^16       | 65,536     |
"""
    
    # Write to file
    with open(output_file, 'w') as f:
        f.write(markdown_content)
    
    return output_file

def main():
    """Main function to run the CCNA practice exercise generator."""
    print("\n===== CCNA PRACTICE EXERCISE GENERATOR =====")
    print("This program generates networking exercises similar to those found in CCNA certification guide appendices.")
    
    while True:
        print("\n----- MAIN MENU -----")
        print("Select an option:")
        print("1. Generate Single Exercise")
        print("2. Generate Subnet Exercises to Markdown File")
        print("3. Generate Binary Tables")
        print("4. Generate CCNA Practice Exam")
        print("5. Exit")
        
        choice = input("\nEnter your choice (1-5): ")
        
        if choice == '1':
            print("\n----- EXERCISE TYPES -----")
            print("1. Classful IPv4 Network Analysis")
            print("2. Subnet Mask Conversion")
            print("3. Subnet Mask Analysis")
            print("4. Existing Subnet Analysis")
            print("5. Subnet Design")
            print("6. Find All Subnet IDs")
            
            exercise_choice = input("\nEnter your choice (1-6): ")
            
            generator = NetworkExerciseGenerator()
            
            if exercise_choice == '1':
                problem = generator.generate_classful_analysis_problem()
                print(f"\nProblem: {problem['problem']}")
                input("\nPress Enter to see the answer...")
                print(f"\nClass: {problem['class']}")
                print(f"Network octets: {problem['network_octets']}")
                print(f"Host octets: {problem['host_octets']}")
                print(f"Network number: {problem['network_number']}")
                print(f"Broadcast address: {problem['broadcast_address']}")
                
            elif exercise_choice == '2':
                problem = generator.generate_mask_conversion_problem()
                print(f"\nProblem: {problem['problem']}")
                input("\nPress Enter to see the answer...")
                if problem['direction'] == 'ddn_to_prefix':
                    print(f"\nPrefix format: {problem['prefix']}")
                else:
                    print(f"\nDotted-decimal format: {problem['subnet_mask']}")
                    
            elif exercise_choice == '3':
                problem = generator.generate_mask_analysis_problem()
                print(f"\nProblem: {problem['problem']}")
                input("\nPress Enter to see the answer...")
                print(f"\nNetwork bits: {problem['network_bits']}")
                print(f"Subnet bits: {problem['subnet_bits']}")
                print(f"Host bits: {problem['host_bits']}")
                print(f"Number of subnets: {problem['num_subnets']}")
                print(f"Hosts per subnet: {problem['num_hosts']}")
                
            elif exercise_choice == '4':
                problem = generator.generate_existing_subnet_analysis_problem()
                print(f"\nProblem: {problem['problem']}")
                input("\nPress Enter to see the answer...")
                print(f"\nSubnet number: {problem['subnet_number']}")
                print(f"Broadcast address: {problem['broadcast_address']}")
                print(f"Valid IP range: {problem['first_valid_host']} - {problem['last_valid_host']}")
                
            elif exercise_choice == '5':
                problem = generator.generate_subnet_design_problem()
                print(f"\nProblem: {problem['problem']}")
                input("\nPress Enter to see the answer...")
                print(f"\nMinimum subnet bits needed: {problem['min_subnet_bits']}")
                print(f"Minimum host bits needed: {problem['min_host_bits']}")
                print("Valid masks:")
                for mask in problem['valid_masks']:
                    print(f"  {mask}")
                print(f"Mask to maximize subnets: {problem['max_subnets_mask']}")
                print(f"Mask to maximize hosts: {problem['max_hosts_mask']}")
                
            elif exercise_choice == '6':
                problem = generator.generate_find_subnet_ids_problem()
                print(f"\nProblem: {problem['problem']}")
                input("\nPress Enter to see the answer...")
                print("\nSubnet IDs:")
                for subnet in problem['display_subnets']:
                    suffix = ""
                    if subnet == problem['zero_subnet']:
                        suffix = " (zero subnet)"
                    elif subnet == problem['broadcast_subnet']:
                        suffix = " (broadcast subnet)"
                    print(f"  {subnet}{suffix}")
                    
                if problem['truncated']:
                    print(f"\n(Showing {len(problem['display_subnets'])} of {len(problem['all_subnet_ids'])} total subnets)")
                    
            else:
                print("\nInvalid choice. Please try again.")
        
        elif choice == '2':
            print("\n----- SUBNET EXERCISE FILES -----")
            print("1. Subnet ID Finding Problems")
            print("2. Subnet Mask Conversion Problems")
            print("3. Subnet Design Problems")
            print("4. Subnet Analysis Problems")
            
            file_choice = input("\nEnter your choice (1-4): ")
            
            num_exercises = input("\nHow many problems would you like to generate? (1-50): ")
            try:
                num_exercises = int(num_exercises)
                if num_exercises < 1 or num_exercises > 50:
                    raise ValueError
            except ValueError:
                print("Invalid input. Using 10 problems.")
                num_exercises = 10
            
            if file_choice == '1':
                output_file = input("\nEnter output filename (default: subnet_exercises.md): ")
                if not output_file:
                    output_file = "subnet_exercises.md"
                elif not output_file.endswith(".md"):
                    output_file += ".md"
                    
                print(f"\nGenerating {num_exercises} subnet problems to {output_file}...")
                file_path = generate_subnet_exercises_markdown(num_exercises, output_file)
                print(f"Exercise file generated: {os.path.abspath(file_path)}")
                
            elif file_choice == '2':
                output_file = input("\nEnter output filename (default: mask_conversion_exercises.md): ")
                if not output_file:
                    output_file = "mask_conversion_exercises.md"
                elif not output_file.endswith(".md"):
                    output_file += ".md"
                    
                print(f"\nGenerating {num_exercises} mask conversion problems to {output_file}...")
                file_path = generate_mask_conversion_exercises_markdown(num_exercises, output_file)
                print(f"Exercise file generated: {os.path.abspath(file_path)}")
                
            elif file_choice == '3':
                output_file = input("\nEnter output filename (default: subnet_design_exercises.md): ")
                if not output_file:
                    output_file = "subnet_design_exercises.md"
                elif not output_file.endswith(".md"):
                    output_file += ".md"
                    
                print(f"\nGenerating {num_exercises} subnet design problems to {output_file}...")
                file_path = generate_subnet_design_exercises_markdown(num_exercises, output_file)
                print(f"Exercise file generated: {os.path.abspath(file_path)}")
                
            elif file_choice == '4':
                output_file = input("\nEnter output filename (default: subnet_analysis_exercises.md): ")
                if not output_file:
                    output_file = "subnet_analysis_exercises.md"
                elif not output_file.endswith(".md"):
                    output_file += ".md"
                    
                print(f"\nGenerating {num_exercises} subnet analysis problems to {output_file}...")
                file_path = generate_existing_subnet_analysis_exercises_markdown(num_exercises, output_file)
                print(f"Exercise file generated: {os.path.abspath(file_path)}")
                
            else:
                print("\nInvalid choice. Please try again.")
        
        elif choice == '3':
            print("\n----- BINARY TABLES -----")
            print("1. Decimal-Binary Conversion Table")
            print("2. Hex-Binary Conversion Table")
            
            table_choice = input("\nEnter your choice (1-2): ")
            
            if table_choice == '1':
                output_file = input("\nEnter output filename (default: decimal_binary_table.md): ")
                if not output_file:
                    output_file = "decimal_binary_table.md"
                elif not output_file.endswith(".md"):
                    output_file += ".md"
                    
                print(f"\nGenerating decimal-binary table to {output_file}...")
                with open(output_file, 'w') as f:
                    f.write(generate_decimal_binary_table())
                print(f"Table file generated: {os.path.abspath(output_file)}")
                
            elif table_choice == '2':
                output_file = input("\nEnter output filename (default: hex_binary_table.md): ")
                if not output_file:
                    output_file = "hex_binary_table.md"
                elif not output_file.endswith(".md"):
                    output_file += ".md"
                    
                print(f"\nGenerating hex-binary table to {output_file}...")
                with open(output_file, 'w') as f:
                    f.write(generate_hex_binary_table())
                print(f"Table file generated: {os.path.abspath(output_file)}")
                
            else:
                print("\nInvalid choice. Please try again.")
        
        elif choice == '4':
            output_file = input("\nEnter output filename (default: ccna_practice_exam.md): ")
            if not output_file:
                output_file = "ccna_practice_exam.md"
            elif not output_file.endswith(".md"):
                output_file += ".md"
                
            print(f"\nGenerating complete CCNA practice exam to {output_file}...")
            file_path = generate_complete_practice_exam(output_file)
            print(f"Exam file generated: {os.path.abspath(file_path)}")
        
        elif choice == '5':
            print("\nExiting program. Happy studying for your CCNA certification!")
            break
            
        else:
            print("\nInvalid choice. Please try again.")
        
        input("\nPress Enter to return to the main menu...")

if __name__ == "__main__":
    main()