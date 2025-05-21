#!/usr/bin/env python3
"""
CCNA Chapter 16 Study Assistant
A study tool to help review concepts from Chapter 16: Operating Cisco Routers
"""

import random
import os
import time
import sys

# Clear screen function - works on Windows and Unix-like systems
def clear_screen():
    os.system('cls' if os.name == 'nt' else 'clear')

# Quiz questions from the "Do I Know This Already?" quiz
quiz_questions = [
    {
        "question": "Which operating systems run on Cisco enterprise routers and use a CLI that works much like the CLI on Cisco LAN switches?",
        "options": [
            "A. CatOS",
            "B. IOS",
            "C. Windows",
            "D. IOS XE"
        ],
        "answer": ["B", "D"],
        "explanation": "Both IOS and IOS XE run on Cisco enterprise routers and use a similar CLI. IOS XE is a newer OS with improved software architecture, but maintains the familiar CLI."
    },
    {
        "question": "Which action would you expect to be true of a router CLI interaction that is not true when configuring a LAN switch that performs only Layer 2 switching functions?",
        "options": [
            "A. Moving from global to physical interface configuration mode",
            "B. Configuring an IP address in physical interface configuration mode",
            "C. Configuring a 10/100/1000 port's settings related to speed and autonegotiation",
            "D. Configuring a console password"
        ],
        "answer": ["B"],
        "explanation": "Configuring an IP address in physical interface configuration mode is something you would do on a router but not on a Layer 2 switch. Layer 2 switches don't assign IP addresses to each physical interface."
    },
    {
        "question": "Which answers list a task that could be helpful in making a router interface G0/0 ready to route packets?",
        "options": [
            "A. Configuring the ip address address mask command in G0/0 configuration mode",
            "B. Configuring the ip address address and ip mask mask commands in G0/0 configuration mode",
            "C. Configuring the no shutdown command in G0/0 configuration mode",
            "D. Setting the interface description in G0/0 configuration mode"
        ],
        "answer": ["A", "C"],
        "explanation": "To make a router interface ready to route packets, you need to configure an IP address using the 'ip address address mask' command (option A) and ensure the interface is up using the 'no shutdown' command (option C)."
    },
    {
        "question": "The output of the show ip interface brief command on R1 lists interface status codes of 'down' and 'down' for interface GigabitEthernet 0/0. The interface connects to a LAN switch with a UTP straight-through cable. Which of the following could be true?",
        "options": [
            "A. The shutdown command is currently configured for router interface G0/0.",
            "B. The shutdown command is currently configured for the switch interface on the other end of the cable.",
            "C. The router was never configured with an ip address command on the interface.",
            "D. The router was configured with the no ip address command."
        ],
        "answer": ["B"],
        "explanation": "If the status codes are 'down' and 'down', the physical layer has a problem. Since there is a cable attached, the most likely reason is that the switch interface on the other end is shut down."
    },
    {
        "question": "Which of the following commands list the IP address but not the subnet mask of an interface?",
        "options": [
            "A. show running-config",
            "B. show protocols type number",
            "C. show ip interface brief",
            "D. show interfaces"
        ],
        "answer": ["C"],
        "explanation": "The 'show ip interface brief' command lists the IP address but not the subnet mask of interfaces."
    },
    {
        "question": "Which of the following is different on the Cisco switch CLI for a Layer 2 switch as compared with the Cisco router CLI?",
        "options": [
            "A. The commands used to configure simple password checking for the console",
            "B. The number of IP addresses configured",
            "C. The configuration of the device's hostname",
            "D. The configuration of an interface description"
        ],
        "answer": ["B"],
        "explanation": "The number of IP addresses configured is different. A Layer 2 switch typically has only one IP address (for management), while a router has an IP address configured on each interface."
    }
]

# Key topics from Chapter 16
key_topics = [
    {
        "topic": "Router Installation Steps",
        "content": """
Steps required to install a router:
1. For Ethernet LAN interfaces, connect RJ-45 connector of appropriate Ethernet cable to the router and LAN switch.
2. For serial WAN ports:
   A. If using external CSU/DSU, connect router's serial interface to CSU/DSU and CSU/DSU to telco line.
   B. If using internal CSU/DSU, connect router's serial interface to telco line.
3. For Ethernet WAN ports:
   A. Confirm required Ethernet standard and SFP type, order SFPs.
   B. Install SFPs into routers, connect Ethernet cable for WAN link to SFP on each end.
4. Connect router's console port to PC as needed for configuration.
5. Connect power cable from outlet to router's power port.
6. Power on router using the on/off switch.
"""
    },
    {
        "topic": "Router and Switch CLI Similarities",
        "content": """
Router CLI features in common with switches:
• User and Privileged (enable) mode
• Entering/exiting configuration mode using configure terminal, end, exit commands and Ctrl+Z
• Configuration of console, Telnet (vty), and enable secret passwords
• Configuration of SSH encryption keys and username/password login credentials
• Configuration of hostname and interface description
• Configuration of interface shutdown/no shutdown
• Navigation through configuration mode contexts
• CLI help, command editing, and command recall features
• Management of startup-config, running-config, and external servers
"""
    },
    {
        "topic": "Router-Specific CLI Features",
        "content": """
Router-specific CLI features:
• Configuring interface IP addresses (ip address address mask)
• Configuring IP routing protocols (e.g., router ospf process-id)
• Verifying the IP routing table (show ip route)
• Configuring static IP routes (ip route subnet mask next-hop-address)
"""
    },
    {
        "topic": "Interface Status Codes",
        "content": """
Interface Status Codes and Their Meanings:
• Line status (first status code): Refers to Layer 1 status (cable installed, right/wrong cable, device on other end powered on)
• Protocol status (second status code): Refers to Layer 2 status, always down if line status is down
"""
    },
    {
        "topic": "Interface Status Code Combinations",
        "content": """
Combinations of Interface Status Codes:
• Administratively down/down: Interface has shutdown command configured
• Down/down: Interface not shutdown, but physical layer problem exists (no cable, switch powered off, etc.)
• Up/down: Usually data-link layer problems, often configuration issues
• Up/up: Both Layer 1 and Layer 2 functioning properly
"""
    },
    {
        "topic": "Interface Commands",
        "content": """
Commands to Display Interface Information:
• show ip interface brief: 1 line per interface, shows address and status
• show protocols [type number]: 1-2 lines per interface, shows address/mask and status
• show interfaces [type number]: Many lines per interface, shows address/mask and status
"""
    },
    {
        "topic": "Ethernet Autonegotiation",
        "content": """
Ethernet Autonegotiation Configuration:
• IOS routers: Use speed and duplex commands similar to switches
• IOS XE routers: Use negotiation auto command to enable/disable autonegotiation
• When manually configuring:
  - IOS: Configure both speed and duplex to specific settings
  - IOS XE: First use no negotiation auto, then set speed and duplex
"""
    }
]

# Command reference tables from Chapter 16
config_commands = [
    {"command": "interface type number", 
     "description": "Global command that moves the user into configuration mode of the named interface."},
    {"command": "ip address address mask", 
     "description": "Interface subcommand that sets the router's IPv4 address and mask."},
    {"command": "[no] shutdown", 
     "description": "Interface subcommand that enables (no shutdown) or disables (shutdown) the interface."},
    {"command": "duplex {full | half | auto}", 
     "description": "IOS (not XE) interface command that sets the duplex, or sets the use of IEEE autonegotiation, for router LAN interfaces that support multiple speeds."},
    {"command": "speed {10 | 100 | 1000 | auto}", 
     "description": "IOS (not XE) interface command for router Gigabit (10/100/1000) interfaces that sets the speed at which the router interface sends and receives data, or sets the use of IEEE autonegotiation."},
    {"command": "description text", 
     "description": "An interface subcommand with which you can type a string of text to document information about that particular interface."},
    {"command": "[no] negotiation auto", 
     "description": "IOS XE (not IOS) interface command that enables or disables the use of IEEE autonegotiation on the interface. There is no equivalent for routers that use IOS."},
    {"command": "duplex {full | half}", 
     "description": "IOS XE (not IOS) interface command that sets the duplex, allowed only if the interface is already configured with the no negotiation auto subcommand."},
    {"command": "speed {10 | 100 | 1000}", 
     "description": "IOS XE (not IOS) interface command that sets the speed, allowed only if the interface is already configured with the no negotiation auto subcommand."}
]

exec_commands = [
    {"command": "show interfaces [type number]", 
     "description": "Lists a large set of informational messages about each interface, or about the one specifically listed interface."},
    {"command": "show ip interface brief", 
     "description": "Lists a single line of information about each interface, including the IP address, line and protocol status, and the method with which the address was configured (manual or DHCP)."},
    {"command": "show protocols [type number]", 
     "description": "Lists information about the listed interface (or all interfaces if the interface is omitted), including the IP address, mask, and line/protocol status."},
    {"command": "show interfaces [type number] controller", 
     "description": "IOS XE (not IOS) command that lists detail about interface hardware and driver behavior, including detail about Ethernet autonegotiation processes and results."}
]

# Router simulator state
router_state = {
    "hostname": "Router",
    "interfaces": {
        "GigabitEthernet0/0": {
            "ip_address": None,
            "mask": None,
            "status": "administratively down",
            "protocol": "down",
            "description": ""
        },
        "GigabitEthernet0/1": {
            "ip_address": None,
            "mask": None,
            "status": "administratively down",
            "protocol": "down",
            "description": ""
        },
        "Serial0/0/0": {
            "ip_address": None,
            "mask": None,
            "status": "administratively down",
            "protocol": "down",
            "description": ""
        }
    },
    "current_mode": "user_exec",  # user_exec, privileged_exec, global_config, interface_config
    "current_interface": None,
    "enable_password": "cisco",
    "configured_password": False
}

# Quiz module
def run_quiz():
    clear_screen()
    print("\n===== CCNA Chapter 16 Quiz =====")
    print("Test your knowledge with questions from the chapter.\n")
    
    questions = quiz_questions.copy()
    random.shuffle(questions)
    correct_count = 0
    total_questions = len(questions)
    
    for i, q in enumerate(questions):
        print(f"Question {i+1} of {total_questions}:")
        print(q["question"])
        for option in q["options"]:
            print(option)
        
        if len(q["answer"]) == 1:
            print("\nSelect one answer (enter the letter): ")
        else:
            print(f"\nSelect {len(q['answer'])} answers (enter the letters with spaces between): ")
        
        user_answer = input("> ").upper().split()
        
        # Compare answers
        if sorted(user_answer) == sorted(q["answer"]):
            print("\n✅ Correct!")
            correct_count += 1
        else:
            print("\n❌ Incorrect.")
            print(f"The correct answer is: {', '.join(q['answer'])}")
        
        print(f"Explanation: {q['explanation']}")
        print("\nPress Enter to continue...")
        input()
        clear_screen()
    
    # Quiz summary
    print("\n===== Quiz Summary =====")
    print(f"You answered {correct_count} out of {total_questions} questions correctly.")
    percentage = (correct_count / total_questions) * 100
    print(f"Score: {percentage:.1f}%")
    
    if percentage >= 90:
        print("Excellent! You have mastered this chapter.")
    elif percentage >= 70:
        print("Good job! You have a solid understanding, but review a few concepts.")
    else:
        print("You should review this chapter more thoroughly.")
    
    print("\nPress Enter to return to the main menu...")
    input()

# Key Topics Review
def review_key_topics():
    clear_screen()
    print("\n===== Chapter 16 Key Topics =====")
    
    for i, topic in enumerate(key_topics):
        print(f"\n{i+1}. {topic['topic']}")
        print("=" * (len(topic['topic']) + 4))
        print(topic['content'])
        
        if i < len(key_topics) - 1:
            print("\nPress Enter to see the next topic, or type 'q' to quit...")
            if input("> ").lower() == 'q':
                break
    
    print("\nEnd of key topics. Press Enter to return to the main menu...")
    input()

# Command Reference
def command_reference():
    while True:
        clear_screen()
        print("\n===== Cisco Router Command Reference =====")
        print("1. View Configuration Commands")
        print("2. View EXEC Commands")
        print("3. Search Commands")
        print("4. Return to Main Menu")
        
        choice = input("\nEnter your choice (1-4): ")
        
        if choice == '1':
            clear_screen()
            print("\n===== Configuration Commands =====")
            for cmd in config_commands:
                print(f"\nCommand: {cmd['command']}")
                print(f"Description: {cmd['description']}")
            print("\nPress Enter to continue...")
            input()
            
        elif choice == '2':
            clear_screen()
            print("\n===== EXEC Commands =====")
            for cmd in exec_commands:
                print(f"\nCommand: {cmd['command']}")
                print(f"Description: {cmd['description']}")
            print("\nPress Enter to continue...")
            input()
            
        elif choice == '3':
            clear_screen()
            print("\n===== Search Commands =====")
            search_term = input("Enter search term: ").lower()
            
            found = False
            print("\nMatching Configuration Commands:")
            for cmd in config_commands:
                if search_term in cmd['command'].lower() or search_term in cmd['description'].lower():
                    print(f"\nCommand: {cmd['command']}")
                    print(f"Description: {cmd['description']}")
                    found = True
            
            print("\nMatching EXEC Commands:")
            for cmd in exec_commands:
                if search_term in cmd['command'].lower() or search_term in cmd['description'].lower():
                    print(f"\nCommand: {cmd['command']}")
                    print(f"Description: {cmd['description']}")
                    found = True
            
            if not found:
                print("No matching commands found.")
            
            print("\nPress Enter to continue...")
            input()
            
        elif choice == '4':
            return
        
        else:
            print("Invalid choice. Please try again.")
            time.sleep(1)

# Router simulator
def router_simulator():
    clear_screen()
    print("\n===== Cisco Router Command Simulator =====")
    print("This is a simplified simulator to practice basic router commands.")
    print("Type 'help' for available commands or 'exit' to quit the simulator.\n")
    
    # Reset router state for a fresh start
    router_state["hostname"] = "Router"
    for interface in router_state["interfaces"]:
        router_state["interfaces"][interface]["ip_address"] = None
        router_state["interfaces"][interface]["mask"] = None
        router_state["interfaces"][interface]["status"] = "administratively down"
        router_state["interfaces"][interface]["protocol"] = "down"
        router_state["interfaces"][interface]["description"] = ""
    
    router_state["current_mode"] = "user_exec"
    router_state["current_interface"] = None
    
    while True:
        # Display prompt based on current mode
        if router_state["current_mode"] == "user_exec":
            prompt = f"{router_state['hostname']}> "
        elif router_state["current_mode"] == "privileged_exec":
            prompt = f"{router_state['hostname']}# "
        elif router_state["current_mode"] == "global_config":
            prompt = f"{router_state['hostname']}(config)# "
        elif router_state["current_mode"] == "interface_config":
            prompt = f"{router_state['hostname']}(config-if)# "
        
        # Get user input
        command = input(prompt).strip()
        
        # Process the command
        if command.lower() == "exit":
            if router_state["current_mode"] == "user_exec":
                return  # Exit the simulator
            elif router_state["current_mode"] == "privileged_exec":
                router_state["current_mode"] = "user_exec"
            elif router_state["current_mode"] == "global_config":
                router_state["current_mode"] = "privileged_exec"
            elif router_state["current_mode"] == "interface_config":
                router_state["current_mode"] = "global_config"
                router_state["current_interface"] = None
        
        elif command.lower() in ["end", "ctrl+z"]:
            router_state["current_mode"] = "privileged_exec"
            router_state["current_interface"] = None
        
        elif command.lower() == "help":
            print("\nAvailable commands depend on the current mode:")
            if router_state["current_mode"] == "user_exec":
                print("enable - Enter privileged EXEC mode")
                print("exit - Exit the simulator")
            elif router_state["current_mode"] == "privileged_exec":
                print("configure terminal - Enter global configuration mode")
                print("show running-config - Show current configuration")
                print("show interfaces - Show interfaces status")
                print("show ip interface brief - Show IP interface summary")
                print("exit - Return to user EXEC mode")
                print("end or ctrl+z - Return to privileged EXEC mode")
            elif router_state["current_mode"] == "global_config":
                print("interface <type/number> - Enter interface configuration mode")
                print("hostname <name> - Set router hostname")
                print("exit - Return to privileged EXEC mode")
                print("end or ctrl+z - Return to privileged EXEC mode")
            elif router_state["current_mode"] == "interface_config":
                print("ip address <address> <mask> - Set interface IP address")
                print("no shutdown - Enable the interface")
                print("shutdown - Disable the interface")
                print("description <text> - Set interface description")
                print("exit - Return to global configuration mode")
                print("end or ctrl+z - Return to privileged EXEC mode")
        
        elif command.lower() == "enable":
            if router_state["current_mode"] == "user_exec":
                if router_state["configured_password"]:
                    password = input("Password: ")
                    if password == router_state["enable_password"]:
                        router_state["current_mode"] = "privileged_exec"
                    else:
                        print("Invalid password")
                else:
                    router_state["current_mode"] = "privileged_exec"
        
        elif command.lower() == "configure terminal" or command.lower() == "conf t":
            if router_state["current_mode"] == "privileged_exec":
                router_state["current_mode"] = "global_config"
                print("Enter configuration commands, one per line. End with CNTL/Z.")
        
        elif command.lower().startswith("hostname "):
            if router_state["current_mode"] == "global_config":
                parts = command.split()
                if len(parts) > 1:
                    router_state["hostname"] = parts[1]
        
        elif command.lower().startswith("interface "):
            if router_state["current_mode"] == "global_config":
                parts = command.split()
                if len(parts) > 1:
                    interface_name = parts[1]
                    # For simplicity, accept any interface that starts with G or S
                    if interface_name.startswith(("G", "S")):
                        for intf in router_state["interfaces"]:
                            if intf.lower().startswith(interface_name.lower()):
                                router_state["current_mode"] = "interface_config"
                                router_state["current_interface"] = intf
                                break
                        if router_state["current_mode"] != "interface_config":
                            print(f"Interface {interface_name} not found")
        
        elif command.lower().startswith("ip address "):
            if router_state["current_mode"] == "interface_config" and router_state["current_interface"]:
                parts = command.split()
                if len(parts) > 2:
                    ip_address = parts[1]
                    mask = parts[2]
                    # Very basic validation
                    if ip_address.count('.') == 3 and mask.count('.') == 3:
                        router_state["interfaces"][router_state["current_interface"]]["ip_address"] = ip_address
                        router_state["interfaces"][router_state["current_interface"]]["mask"] = mask
                        print(f"IP address configured on {router_state['current_interface']}")
                    else:
                        print("Invalid IP address or mask format")
        
        elif command.lower() == "no shutdown" or command.lower() == "no shut":
            if router_state["current_mode"] == "interface_config" and router_state["current_interface"]:
                router_state["interfaces"][router_state["current_interface"]]["status"] = "up"
                router_state["interfaces"][router_state["current_interface"]]["protocol"] = "up"
                print(f"{router_state['current_interface']} is now up, line protocol is up")
        
        elif command.lower() == "shutdown" or command.lower() == "shut":
            if router_state["current_mode"] == "interface_config" and router_state["current_interface"]:
                router_state["interfaces"][router_state["current_interface"]]["status"] = "administratively down"
                router_state["interfaces"][router_state["current_interface"]]["protocol"] = "down"
                print(f"{router_state['current_interface']} is now administratively down, line protocol is down")
        
        elif command.lower().startswith("description "):
            if router_state["current_mode"] == "interface_config" and router_state["current_interface"]:
                description = command[12:]  # Remove "description " from the start
                router_state["interfaces"][router_state["current_interface"]]["description"] = description
                print(f"Description set for {router_state['current_interface']}")
        
        elif command.lower() == "show running-config" or command.lower() == "show run":
            if router_state["current_mode"] in ["privileged_exec", "global_config", "interface_config"]:
                print(f"hostname {router_state['hostname']}")
                for intf, details in router_state["interfaces"].items():
                    print(f"interface {intf}")
                    if details["description"]:
                        print(f" description {details['description']}")
                    if details["ip_address"] and details["mask"]:
                        print(f" ip address {details['ip_address']} {details['mask']}")
                    if details["status"] != "administratively down":
                        print(" no shutdown")
                    else:
                        print(" shutdown")
        
        elif command.lower() == "show interfaces" or command.lower() == "show int":
            if router_state["current_mode"] in ["privileged_exec", "global_config", "interface_config"]:
                for intf, details in router_state["interfaces"].items():
                    status = "administratively down" if details["status"] == "administratively down" else "up"
                    protocol = details["protocol"]
                    print(f"{intf} is {status}, line protocol is {protocol}")
                    if details["description"]:
                        print(f"  Description: {details['description']}")
                    if details["ip_address"] and details["mask"]:
                        print(f"  Internet address is {details['ip_address']}/{mask_to_cidr(details['mask'])}")
                    print("  MTU 1500 bytes, BW 1000000 Kbit/sec, DLY 10 usec")
                    print("  reliability 255/255, txload 1/255, rxload 1/255")
                    print("  Encapsulation ARPA, loopback not set")
                    print("  ARP type: ARPA, ARP Timeout 04:00:00")
                    print("")
        
        elif command.lower() == "show ip interface brief" or command.lower() == "show ip int brief":
            if router_state["current_mode"] in ["privileged_exec", "global_config", "interface_config"]:
                print("Interface                  IP-Address      OK? Method Status                Protocol")
                for intf, details in router_state["interfaces"].items():
                    ip = details["ip_address"] if details["ip_address"] else "unassigned"
                    status = details["status"]
                    protocol = details["protocol"]
                    method = "manual" if details["ip_address"] else "unset"
                    ok = "YES" if details["ip_address"] else "YES"
                    print(f"{intf:<25} {ip:<15} {ok:<3} {method:<6} {status:<20} {protocol}")
        
        else:
            print(f"% Invalid input detected at '^' marker.")

# Helper function to convert subnet mask to CIDR notation
def mask_to_cidr(mask):
    try:
        # Convert mask like "255.255.255.0" to "/24"
        return sum([bin(int(x)).count('1') for x in mask.split('.')])
    except:
        return "unknown"

# Main menu
def main_menu():
    while True:
        clear_screen()
        print("""
========================================
  CCNA Chapter 16 Study Assistant
========================================
  Chapter 16: Operating Cisco Routers
----------------------------------------
""")
        print("1. Take Chapter Quiz")
        print("2. Review Key Topics")
        print("3. Command Reference")
        print("4. Router Command Simulator")
        print("5. Exit Program")
        
        choice = input("\nEnter your choice (1-5): ")
        
        if choice == '1':
            run_quiz()
        elif choice == '2':
            review_key_topics()
        elif choice == '3':
            command_reference()
        elif choice == '4':
            router_simulator()
        elif choice == '5':
            clear_screen()
            print("\nThank you for using the CCNA Chapter 16 Study Assistant!")
            print("Good luck with your CCNA studies!")
            sys.exit(0)
        else:
            print("Invalid choice. Please try again.")
            time.sleep(1)

if __name__ == "__main__":
    main_menu()
