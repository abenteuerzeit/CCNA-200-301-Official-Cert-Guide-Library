import random
import os
import time
import sys
from datetime import datetime

class CCNAStudyAssistant:
    def __init__(self):
        self.user_stats = {
            "flashcards_reviewed": 0,
            "quiz_questions_answered": 0,
            "correct_answers": 0,
            "study_sessions": 0,
            "last_session": None
        }
        
        # Chapter 1 key terms
        self.ch1_terms = {
            "adjacent-layer interaction": "When adjacent layers in a networking model, on the same computer, work together",
            "de-encapsulation": "The process of removing headers and trailers from a PDU",
            "encapsulation": "The process of putting headers (and sometimes trailers) around some data",
            "frame": "The data-link layer PDU that contains the header, trailer, and encapsulated data",
            "networking model": "A comprehensive set of documents that defines how networks should work",
            "packet": "The network layer PDU (Protocol Data Unit)",
            "same-layer interaction": "When a particular layer on one computer communicates with the same layer on another computer",
            "segment": "The transport layer PDU"
        }
        
        # Chapter 2 key terms
        self.ch2_terms = {
            "10BASE-T": "10 Mbps, baseband, twisted pair Ethernet standard",
            "100BASE-T": "100 Mbps, baseband, twisted pair Ethernet standard (Fast Ethernet)",
            "1000BASE-T": "1000 Mbps, baseband, twisted pair Ethernet standard (Gigabit Ethernet)",
            "auto-MDIX": "Feature that detects the cable pinout and automatically adjusts for incorrect cabling",
            "broadcast address": "An address that means 'all devices that reside on this LAN right now'",
            "Ethernet": "A family of LAN standards that together define the physical and data-link layers",
            "Ethernet frame": "The data-link PDU used in Ethernet networks",
            "MAC address": "Media Access Control address, a 48-bit (6-byte) binary number used to identify devices on Ethernet",
            "unicast address": "A term for a MAC address that represents a single LAN interface"
        }
        
        # Chapter 3 key terms
        self.ch3_terms = {
            "ARP": "Address Resolution Protocol, used to dynamically learn the MAC address of an IP host connected to a LAN",
            "default router": "The router to which a host sends packets when the destination is on a different subnet",
            "DNS": "Domain Name System, a service that resolves hostnames to IP addresses",
            "Ethernet WAN": "A WAN technology that uses Ethernet protocols but over long distances",
            "HDLC": "High-Level Data Link Control, a data-link protocol used on serial links",
            "IP address": "A 32-bit (IPv4) or 128-bit (IPv6) number assigned to hosts and routers",
            "IP network": "A group of IP addresses with the same numeric prefix",
            "IP subnet": "A subdivision of an IP network where all addresses share a common prefix",
            "leased line": "A WAN service offered by a service provider that provides a physical path between two sites",
            "routing protocol": "A protocol that routers use to learn and advertise routes",
            "wide-area network": "A network that spans a large geographical area"
        }
        
        # All terms combined
        self.all_terms = {**self.ch1_terms, **self.ch2_terms, **self.ch3_terms}
        
        # Quiz questions for Chapter 1
        self.ch1_questions = [
            {
                "question": "Which of the following protocols are examples of TCP/IP transport layer protocols?",
                "options": ["Ethernet", "HTTP", "IP", "UDP", "SMTP", "TCP"],
                "answer": ["UDP", "TCP"],
                "explanation": "UDP and TCP are transport layer protocols in the TCP/IP model."
            },
            {
                "question": "Which of the following protocols are examples of TCP/IP data-link layer protocols?",
                "options": ["Ethernet", "HTTP", "IP", "UDP", "SMTP", "TCP", "802.11"],
                "answer": ["Ethernet", "802.11"],
                "explanation": "Ethernet and 802.11 (Wi-Fi) are data-link layer protocols."
            },
            {
                "question": "The process of a web server adding a TCP header to the contents of a web page, followed by adding an IP header and then adding a data-link header and trailer, is an example of what?",
                "options": ["Data encapsulation", "Same-layer interaction", "TCP/IP model", "Adjacent-layer interaction"],
                "answer": ["Data encapsulation"],
                "explanation": "This describes the process of encapsulation, where data is wrapped with headers as it moves down the protocol stack."
            },
            {
                "question": "Which term is used specifically to identify the entity created when encapsulating data inside data-link layer headers and trailers?",
                "options": ["Data", "Chunk", "Segment", "Frame", "Packet"],
                "answer": ["Frame"],
                "explanation": "A frame is the PDU at the data-link layer, containing headers, trailers, and the encapsulated data."
            }
        ]
        
        # Quiz questions for Chapter 2
        self.ch2_questions = [
            {
                "question": "Which Ethernet standard defines Gigabit Ethernet over UTP cabling?",
                "options": ["10GBASE-T", "100BASE-T", "1000BASE-T", "1000BASE-LX"],
                "answer": ["1000BASE-T"],
                "explanation": "1000BASE-T defines Gigabit Ethernet over UTP (unshielded twisted pair) cabling."
            },
            {
                "question": "What is true about Ethernet crossover cables for Fast Ethernet?",
                "options": [
                    "Pins 1 and 2 are reversed on the other end of the cable",
                    "Pins 1 and 2 on one end connect to pins 3 and 6 on the other end",
                    "Pins 1 and 2 on one end connect to pins 3 and 4 on the other end",
                    "The cable can be up to 1000 meters long"
                ],
                "answer": ["Pins 1 and 2 on one end connect to pins 3 and 6 on the other end"],
                "explanation": "In a crossover cable for Fast Ethernet, pins 1 and 2 on one end connect to pins 3 and 6 on the other end."
            },
            {
                "question": "Which statement is true about the CSMA/CD algorithm?",
                "options": [
                    "The algorithm never allows collisions to occur",
                    "Collisions can happen, but the algorithm defines how computers should notice and recover",
                    "The algorithm works with only two devices on the same Ethernet",
                    "It's only used in fiber optic networks"
                ],
                "answer": ["Collisions can happen, but the algorithm defines how computers should notice and recover"],
                "explanation": "CSMA/CD allows for collision detection and recovery in half-duplex Ethernet environments."
            },
            {
                "question": "Which of the following terms describe Ethernet addresses that can be used to send one frame that is delivered to multiple devices on the LAN?",
                "options": ["Burned-in address", "Unicast address", "Broadcast address", "Multicast address"],
                "answer": ["Broadcast address", "Multicast address"],
                "explanation": "Broadcast addresses reach all devices on a LAN, while multicast addresses reach a subset of devices."
            }
        ]
        
        # Quiz questions for Chapter 3
        self.ch3_questions = [
            {
                "question": "Which of the following terms is not commonly used to describe a serial link?",
                "options": ["Private line", "Point-to-point link", "Leased circuit", "E-line"],
                "answer": ["E-line"],
                "explanation": "E-line refers to an Ethernet WAN service rather than a serial link."
            },
            {
                "question": "Which of the following does a router normally use when making a decision about routing TCP/IP packets?",
                "options": [
                    "Destination MAC address", 
                    "Source MAC address", 
                    "Destination IP address", 
                    "Source IP address",
                    "Destination MAC and IP addresses"
                ],
                "answer": ["Destination IP address"],
                "explanation": "Routers make forwarding decisions based on the destination IP address in the packet header."
            },
            {
                "question": "Which of the following are true about a LAN-connected TCP/IP host and its IP routing choices?",
                "options": [
                    "The host always sends packets to its default gateway",
                    "The host never sends packets to its default gateway",
                    "The host sends packets to its default gateway if the destination IP address is in a different subnet",
                    "The host sends packets to its default gateway if the destination IP address is in the same subnet"
                ],
                "answer": ["The host sends packets to its default gateway if the destination IP address is in a different subnet"],
                "explanation": "Hosts send packets to their default gateway only when the destination is in a different subnet."
            },
            {
                "question": "Which of the following are functions of a routing protocol?",
                "options": [
                    "Advertising known routes to neighboring routers",
                    "Learning routes to directly connected subnets",
                    "Learning routes as advertised by neighboring routers",
                    "Forwarding IP packets based on a packet's destination IP address"
                ],
                "answer": ["Advertising known routes to neighboring routers", "Learning routes as advertised by neighboring routers"],
                "explanation": "Routing protocols share route information between routers, but don't handle the actual forwarding of packets."
            }
        ]
        
        # Combined quiz questions
        self.all_questions = self.ch1_questions + self.ch2_questions + self.ch3_questions
        
        # Key topics summary
        self.key_topics = {
            "Chapter 1": [
                "IP routing: Routers examine destination IP addresses to forward packets toward their destination",
                "Data-link services: Provide the means to transfer data across a single network segment",
                "Encapsulation: The 5-step process of adding headers/trailers as data moves down the protocol stack",
                "Protocol Data Units: segment (transport), packet (network), frame (data link)",
                "OSI vs TCP/IP: The OSI 7-layer model compared to the TCP/IP 4-layer or 5-layer models"
            ],
            "Chapter 2": [
                "Ethernet LAN building blocks: Switches, NICs, cables, connectors",
                "Ethernet UTP cable types: Straight-through vs. crossover pinouts",
                "Multimode fiber: Transmits light using internal reflection across medium distances",
                "MAC addresses: 48-bit addresses with manufacturer OUI and device-specific portions",
                "Duplex: Half-duplex (CSMA/CD) vs. full-duplex operation"
            ],
            "Chapter 3": [
                "Router de-encapsulation and re-encapsulation: Process of removing and adding headers",
                "Ethernet WAN physical connections: How service providers connect customer sites",
                "IP routing process: The 4-step process routers use to forward packets",
                "IP address grouping: Rules for allocating addresses to networks/subnets",
                "Routing protocols: How routers learn and share route information",
                "DNS name resolution: How hostnames are translated to IP addresses",
                "ARP: How devices discover MAC addresses for known IP addresses"
            ]
        }

    def clear_screen(self):
        """Clear the terminal screen"""
        os.system('cls' if os.name == 'nt' else 'clear')
        
    def display_banner(self):
        """Display a program banner"""
        banner = """
  _____  _____  _   _          _____  _____ _    _ _______     __
 / ____|/ ____|| \ | |   /\   / ____|/ ____| |  | |  __ \ \   / /
| |    | |     |  \| |  /  \ | (___ | |    | |  | | |  | \ \_/ / 
| |    | |     | . ` | / /\ \ \___ \| |    | |  | | |  | |\   /  
| |____| |____ | |\  |/ ____ \____) | |____| |__| | |__| | | |   
 \_____|\_____||_| \_/_/    \_\_____/ \_____|\____/|_____/  |_|   
                                                               
 Part 1: Introduction to Networking - Study Assistant
 ===================================================
"""
        print(banner)
        
    def type_text(self, text, delay=0.01):
        """Type text with a slight delay for better UI"""
        for char in text:
            sys.stdout.write(char)
            sys.stdout.flush()
            time.sleep(delay)
        print()
        
    def main_menu(self):
        """Display main menu and get user choice"""
        self.clear_screen()
        self.display_banner()
        
        # Update study session stats
        self.user_stats["study_sessions"] += 1
        self.user_stats["last_session"] = datetime.now().strftime("%Y-%m-%d %H:%M")
        
        print("\n[1] Flashcards - Review Key Terms")
        print("[2] Quiz - Test Your Knowledge")
        print("[3] Key Topics Summary")
        print("[4] Study Statistics")
        print("[5] Exit Program")
        
        while True:
            try:
                choice = int(input("\nEnter your choice (1-5): "))
                if 1 <= choice <= 5:
                    return choice
                else:
                    print("Please enter a number between 1 and 5.")
            except ValueError:
                print("Please enter a valid number.")
                
    def select_chapter_menu(self, for_what="study"):
        """Menu to select which chapter to study"""
        print(f"\nWhich chapter would you like to {for_what}?")
        print("[1] Chapter 1: Introduction to TCP/IP Networking")
        print("[2] Chapter 2: Fundamentals of Ethernet LANs")
        print("[3] Chapter 3: Fundamentals of WANs and IP Routing")
        print("[4] All Chapters")
        
        while True:
            try:
                choice = int(input("\nEnter your choice (1-4): "))
                if 1 <= choice <= 4:
                    return choice
                else:
                    print("Please enter a number between 1 and 4.")
            except ValueError:
                print("Please enter a valid number.")
                
    def flashcards(self):
        """Flashcard study mode"""
        self.clear_screen()
        print("\n===== FLASHCARD MODE =====")
        
        chapter = self.select_chapter_menu(for_what="study with flashcards")
        
        if chapter == 1:
            terms = self.ch1_terms
            chapter_name = "Chapter 1: Introduction to TCP/IP Networking"
        elif chapter == 2:
            terms = self.ch2_terms
            chapter_name = "Chapter 2: Fundamentals of Ethernet LANs"
        elif chapter == 3:
            terms = self.ch3_terms
            chapter_name = "Chapter 3: Fundamentals of WANs and IP Routing"
        else:  # All chapters
            terms = self.all_terms
            chapter_name = "All Chapters"
            
        if not terms:
            print("No flashcards available for this selection.")
            input("\nPress Enter to return to the main menu...")
            return
            
        self.clear_screen()
        print(f"\n===== FLASHCARDS: {chapter_name} =====")
        print("\nInstructions:")
        print("- Press Enter to see the definition")
        print("- After seeing the definition, press:")
        print("  [1] Mark as known")
        print("  [2] Mark for review (will see again)")
        print("  [q] Quit to main menu")
        
        input("\nPress Enter to begin...")
        
        # Convert dictionary to list of tuples for easier shuffling
        cards = list(terms.items())
        random.shuffle(cards)
        
        review_pile = []
        cards_reviewed = 0
        
        while cards:
            self.clear_screen()
            print(f"\n===== FLASHCARDS: {chapter_name} =====")
            print(f"Cards remaining: {len(cards)} | For review: {len(review_pile)}")
            
            term, definition = cards.pop(0)
            
            # Show the term
            print("\n┌" + "─" * 60 + "┐")
            print("│" + term.center(60) + "│")
            print("└" + "─" * 60 + "┘")
            
            input("\nPress Enter to see definition...")
            
            # Show the definition
            print("\n┌" + "─" * 60 + "┐")
            for i in range(0, len(definition), 58):
                line = definition[i:i+58]
                print("│ " + line + " " * (58 - len(line)) + " │")
            print("└" + "─" * 60 + "┘")
            
            cards_reviewed += 1
            self.user_stats["flashcards_reviewed"] += 1
            
            while True:
                choice = input("\nEnter [1] Known, [2] Review again, or [q] Quit: ").lower()
                
                if choice == '1':
                    break  # Card is known, move to the next one
                elif choice == '2':
                    review_pile.append((term, definition))
                    break
                elif choice == 'q':
                    return
                else:
                    print("Invalid choice. Please try again.")
            
            # If we've gone through all cards, check if there are any for review
            if not cards and review_pile:
                print("\nReviewing marked cards...")
                cards = review_pile
                review_pile = []
                random.shuffle(cards)
                time.sleep(1)
                
        print("\nGreat job! You've completed all the flashcards.")
        input("\nPress Enter to return to the main menu...")
    
    def quiz(self):
        """Quiz mode"""
        self.clear_screen()
        print("\n===== QUIZ MODE =====")
        
        chapter = self.select_chapter_menu(for_what="be quizzed on")
        
        if chapter == 1:
            questions = self.ch1_questions
            chapter_name = "Chapter 1: Introduction to TCP/IP Networking"
        elif chapter == 2:
            questions = self.ch2_questions
            chapter_name = "Chapter 2: Fundamentals of Ethernet LANs"
        elif chapter == 3:
            questions = self.ch3_questions
            chapter_name = "Chapter 3: Fundamentals of WANs and IP Routing"
        else:  # All chapters
            questions = self.all_questions
            chapter_name = "All Chapters"
            
        if not questions:
            print("No quiz questions available for this selection.")
            input("\nPress Enter to return to the main menu...")
            return
            
        self.clear_screen()
        print(f"\n===== QUIZ: {chapter_name} =====")
        print("\nInstructions:")
        print("- Multiple choice questions will be presented")
        print("- Some questions may have multiple correct answers")
        print("- Enter the letter(s) of your answer(s) separated by commas")
        print("- For example: a,c,d")
        
        input("\nPress Enter to begin...")
        
        random.shuffle(questions)
        correct = 0
        total = len(questions)
        
        for i, q in enumerate(questions):
            self.clear_screen()
            print(f"\n===== QUIZ: {chapter_name} - Question {i+1}/{total} =====\n")
            
            print(q["question"])
            print()
            
            # Display options with letters
            options = q["options"]
            for j, option in enumerate(options):
                print(f"[{chr(97+j)}] {option}")
            
            # Get user's answer
            user_answer_input = input("\nYour answer (e.g., a,c,d): ").lower().strip()
            user_answers = [options[ord(c) - ord('a')] for c in user_answer_input.replace(',', '')]
            
            # Check if answer is correct (all correct options selected and no incorrect ones)
            is_correct = set(user_answers) == set(q["answer"])
            
            # Display result
            print("\n" + "=" * 40)
            if is_correct:
                print("\n✓ CORRECT!")
                correct += 1
                self.user_stats["correct_answers"] += 1
            else:
                print("\n✗ INCORRECT")
                
            # Display explanation
            print("\nCorrect answer(s):", ", ".join(q["answer"]))
            print("\nExplanation:", q["explanation"])
            
            self.user_stats["quiz_questions_answered"] += 1
            
            input("\nPress Enter to continue...")
        
        # Display final score
        self.clear_screen()
        print(f"\n===== QUIZ RESULTS: {chapter_name} =====\n")
        print(f"You scored {correct} out of {total} ({(correct/total)*100:.1f}%)")
        
        if (correct/total) >= 0.9:
            print("\nExcellent job! You have a strong understanding of this material.")
        elif (correct/total) >= 0.7:
            print("\nGood work! Review the questions you missed to strengthen your knowledge.")
        else:
            print("\nKeep studying! Consider reviewing the key topics and terms again.")
            
        input("\nPress Enter to return to the main menu...")
    
    def key_topics_summary(self):
        """Display key topics summary"""
        self.clear_screen()
        print("\n===== KEY TOPICS SUMMARY =====")
        
        chapter = self.select_chapter_menu(for_what="review")
        
        if chapter == 1:
            topics = {"Chapter 1": self.key_topics["Chapter 1"]}
        elif chapter == 2:
            topics = {"Chapter 2": self.key_topics["Chapter 2"]}
        elif chapter == 3:
            topics = {"Chapter 3": self.key_topics["Chapter 3"]}
        else:  # All chapters
            topics = self.key_topics
            
        self.clear_screen()
        print("\n===== KEY TOPICS SUMMARY =====\n")
        
        for ch, topic_list in topics.items():
            print(f"\n{ch}:")
            print("=" * len(ch) + "=")
            for i, topic in enumerate(topic_list):
                print(f"{i+1}. {topic}")
                
        input("\nPress Enter to return to the main menu...")
    
    def display_stats(self):
        """Display user study statistics"""
        self.clear_screen()
        print("\n===== YOUR STUDY STATISTICS =====\n")
        
        print(f"Total study sessions: {self.user_stats['study_sessions']}")
        print(f"Last session: {self.user_stats['last_session'] or 'N/A'}")
        print(f"Flashcards reviewed: {self.user_stats['flashcards_reviewed']}")
        print(f"Quiz questions answered: {self.user_stats['quiz_questions_answered']}")
        
        if self.user_stats['quiz_questions_answered'] > 0:
            accuracy = (self.user_stats['correct_answers'] / self.user_stats['quiz_questions_answered']) * 100
            print(f"Quiz accuracy: {accuracy:.1f}%")
        
        input("\nPress Enter to return to the main menu...")
    
    def run(self):
        """Main program loop"""
        while True:
            choice = self.main_menu()
            
            if choice == 1:
                self.flashcards()
            elif choice == 2:
                self.quiz()
            elif choice == 3:
                self.key_topics_summary()
            elif choice == 4:
                self.display_stats()
            elif choice == 5:
                self.clear_screen()
                self.display_banner()
                self.type_text("\nThank you for using the CCNA Study Assistant!")
                self.type_text("Keep studying and good luck with your certification!")
                break


# Run the program
if __name__ == "__main__":
    study_assistant = CCNAStudyAssistant()
    study_assistant.run()
