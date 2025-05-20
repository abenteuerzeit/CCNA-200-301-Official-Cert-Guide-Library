PRAGMA foreign_keys = ON;

CREATE TABLE volumes (
  id INTEGER PRIMARY KEY,
  name TEXT NOT NULL
);

CREATE TABLE chapters (
  id INTEGER PRIMARY KEY,
  volume_id INTEGER NOT NULL,
  number TEXT,
  title TEXT NOT NULL,
  FOREIGN KEY (volume_id) REFERENCES volumes(id)
);

CREATE TABLE tasks (
  id INTEGER PRIMARY KEY,
  name TEXT NOT NULL,
  description TEXT
);

CREATE TABLE study_items (
  id INTEGER PRIMARY KEY,
  chapter_id INTEGER NOT NULL,
  task_id INTEGER NOT NULL,
  goal_date TEXT,
  first_completion_date TEXT,
  second_completion_date TEXT,
  notes TEXT,
  FOREIGN KEY (chapter_id) REFERENCES chapters(id),
  FOREIGN KEY (task_id) REFERENCES tasks(id)
);

INSERT INTO volumes (id, name) VALUES (1, 'CCNA Volume 1');
INSERT INTO volumes (id, name) VALUES (2, 'CCNA Volume 2');

INSERT INTO tasks (id, name, description) VALUES (1, 'Read', 'Read Foundation Topics');
INSERT INTO tasks (id, name, description) VALUES (2, 'Review', 'Review Key Topics using the book or companion website');
INSERT INTO tasks (id, name, description) VALUES (3, 'Define', 'Define Key Terms using the book or companion website');
INSERT INTO tasks (id, name, description) VALUES (4, 'DIKTA', 'Repeat DIKTA questions using the book or PTP exam engine');
INSERT INTO tasks (id, name, description) VALUES (5, 'Memory Tables', 'Complete all memory tables using the companion website');
INSERT INTO tasks (id, name, description) VALUES (6, 'Practice Test', 'Take practice test in study mode');
INSERT INTO tasks (id, name, description) VALUES (7, 'Command Tables', 'Review command tables for this chapter');
INSERT INTO tasks (id, name, description) VALUES (8, 'Config Checklists', 'Complete config checklists');
INSERT INTO tasks (id, name, description) VALUES (9, 'Labs', 'Do labs listed for this chapter');
INSERT INTO tasks (id, name, description) VALUES (10, 'Videos', 'Watch chapter-associated videos');
INSERT INTO tasks (id, name, description) VALUES (11, 'Part Review', 'Complete all exercises in Part Review');
INSERT INTO tasks (id, name, description) VALUES (12, 'Final Review', 'Complete final review tasks');

INSERT INTO chapters (id, volume_id, number, title) VALUES (1, 1, 'Intro', 'Introduction');
INSERT INTO chapters (id, volume_id, number, title) VALUES (2, 1, 'Plan', 'Your Study Planner');
INSERT INTO chapters (id, volume_id, number, title) VALUES (3, 1, '1', 'Introduction to TCP/IP Networking');
INSERT INTO chapters (id, volume_id, number, title) VALUES (4, 1, '2', 'Fundamentals of Ethernet LANs');
INSERT INTO chapters (id, volume_id, number, title) VALUES (5, 1, '3', 'Fundamentals of WANs and IP Routing');
INSERT INTO chapters (id, volume_id, number, title) VALUES (6, 1, 'P1', 'Part I. Introduction to Networking');
INSERT INTO chapters (id, volume_id, number, title) VALUES (7, 1, '4', 'Using the Command-Line Interface');
INSERT INTO chapters (id, volume_id, number, title) VALUES (8, 1, '5', 'Analyzing Ethernet LAN Switching');
INSERT INTO chapters (id, volume_id, number, title) VALUES (9, 1, '6', 'Configuring Basic Switch Management');
INSERT INTO chapters (id, volume_id, number, title) VALUES (10, 1, '7', 'Configuring and Verifying Switch Interfaces');
INSERT INTO chapters (id, volume_id, number, title) VALUES (11, 1, 'P2', 'Part II. Implementing Ethernet LANs');
INSERT INTO chapters (id, volume_id, number, title) VALUES (12, 1, '8', 'Implementing Ethernet Virtual LANs');
INSERT INTO chapters (id, volume_id, number, title) VALUES (13, 1, '9', 'Spanning Tree Protocol Concepts');
INSERT INTO chapters (id, volume_id, number, title) VALUES (14, 1, '10', 'RSTP and EtherChannel Configuration');
INSERT INTO chapters (id, volume_id, number, title) VALUES (15, 1, 'P3', 'Part III. Implementing VLANs and STP');
INSERT INTO chapters (id, volume_id, number, title) VALUES (16, 1, '11', 'Perspectives on IPv4 Subnetting');
INSERT INTO chapters (id, volume_id, number, title) VALUES (17, 1, '12', 'Analyzing Classful IPv4 Networks');
INSERT INTO chapters (id, volume_id, number, title) VALUES (18, 1, '13', 'Analyzing Subnet Masks');
INSERT INTO chapters (id, volume_id, number, title) VALUES (19, 1, '14', 'Analyzing Existing Subnets');
INSERT INTO chapters (id, volume_id, number, title) VALUES (20, 1, '15', 'Subnet Design');
INSERT INTO chapters (id, volume_id, number, title) VALUES (21, 1, 'P4', 'Part IV. IPv4 Addressing');
INSERT INTO chapters (id, volume_id, number, title) VALUES (22, 1, '16', 'Operating Cisco Routers');
INSERT INTO chapters (id, volume_id, number, title) VALUES (23, 1, '17', 'Configuring IPv4 Addresses and Static Routes');
INSERT INTO chapters (id, volume_id, number, title) VALUES (24, 1, '18', 'IP Routing in the LAN');
INSERT INTO chapters (id, volume_id, number, title) VALUES (25, 1, '19', 'IP Addressing on Hosts');
INSERT INTO chapters (id, volume_id, number, title) VALUES (26, 1, '20', 'Troubleshooting IPv4 Routing');
INSERT INTO chapters (id, volume_id, number, title) VALUES (27, 1, 'P5', 'Part V. IPv4 Routing');
INSERT INTO chapters (id, volume_id, number, title) VALUES (28, 1, '21', 'Understanding OSPF Concepts');
INSERT INTO chapters (id, volume_id, number, title) VALUES (29, 1, '22', 'Implementing Basic OSPF Features');
INSERT INTO chapters (id, volume_id, number, title) VALUES (30, 1, '23', 'Implementing Optional OSPF Features');
INSERT INTO chapters (id, volume_id, number, title) VALUES (31, 1, '24', 'OSPF Neighbors and Route Selection');
INSERT INTO chapters (id, volume_id, number, title) VALUES (32, 1, 'P6', 'Part VI. OSPF');
INSERT INTO chapters (id, volume_id, number, title) VALUES (33, 1, '25', 'Fundamentals of IP Version 6');
INSERT INTO chapters (id, volume_id, number, title) VALUES (34, 1, '26', 'IPv6 Addressing and Subnetting');
INSERT INTO chapters (id, volume_id, number, title) VALUES (35, 1, '27', 'Implementing IPv6 Addressing on Routers');
INSERT INTO chapters (id, volume_id, number, title) VALUES (36, 1, '28', 'Implementing IPv6 Addressing on Hosts');
INSERT INTO chapters (id, volume_id, number, title) VALUES (37, 1, '29', 'Implementing IPv6 Routing');
INSERT INTO chapters (id, volume_id, number, title) VALUES (38, 1, 'P7', 'Part VII. IP Version 6');
INSERT INTO chapters (id, volume_id, number, title) VALUES (39, 1, 'FR', 'Final Review');

INSERT INTO chapters (id, volume_id, number, title) VALUES (40, 2, 'Intro', 'Introduction');
INSERT INTO chapters (id, volume_id, number, title) VALUES (41, 2, '1', 'Fundamentals of Wireless Networks');
INSERT INTO chapters (id, volume_id, number, title) VALUES (42, 2, '2', 'Analyzing Cisco Wireless Architectures');
INSERT INTO chapters (id, volume_id, number, title) VALUES (43, 2, '3', 'Securing Wireless Networks');
INSERT INTO chapters (id, volume_id, number, title) VALUES (44, 2, '4', 'Building a Wireless LAN');
INSERT INTO chapters (id, volume_id, number, title) VALUES (45, 2, 'P1', 'Part I. Wireless LANs');
INSERT INTO chapters (id, volume_id, number, title) VALUES (46, 2, '5', 'Introduction to TCP/IP Transport and Applications');
INSERT INTO chapters (id, volume_id, number, title) VALUES (47, 2, '6', 'Basic IPv4 Access Control Lists');
INSERT INTO chapters (id, volume_id, number, title) VALUES (48, 2, '7', 'Named and Extended IP ACLs');
INSERT INTO chapters (id, volume_id, number, title) VALUES (49, 2, '8', 'Applied IP ACLs');
INSERT INTO chapters (id, volume_id, number, title) VALUES (50, 2, 'P2', 'Part II. IP Access Control Lists');
INSERT INTO chapters (id, volume_id, number, title) VALUES (51, 2, '9', 'Security Architectures');
INSERT INTO chapters (id, volume_id, number, title) VALUES (52, 2, '10', 'Securing Network Devices');
INSERT INTO chapters (id, volume_id, number, title) VALUES (53, 2, '11', 'Implementing Switch Port Security');
INSERT INTO chapters (id, volume_id, number, title) VALUES (54, 2, '12', 'DHCP Snooping and ARP Inspection');
INSERT INTO chapters (id, volume_id, number, title) VALUES (55, 2, 'P3', 'Part III. Security Services');
INSERT INTO chapters (id, volume_id, number, title) VALUES (56, 2, '13', 'Device Management Protocols');
INSERT INTO chapters (id, volume_id, number, title) VALUES (57, 2, '14', 'Network Address Translation');
INSERT INTO chapters (id, volume_id, number, title) VALUES (58, 2, '15', 'Quality of Service (QoS)');
INSERT INTO chapters (id, volume_id, number, title) VALUES (59, 2, '16', 'First Hop Redundancy Protocols');
INSERT INTO chapters (id, volume_id, number, title) VALUES (60, 2, '17', 'SNMP, FTP, and TFTP');
INSERT INTO chapters (id, volume_id, number, title) VALUES (61, 2, 'P4', 'Part IV. IP Services');
INSERT INTO chapters (id, volume_id, number, title) VALUES (62, 2, '18', 'LAN Architecture');
INSERT INTO chapters (id, volume_id, number, title) VALUES (63, 2, '19', 'WAN Architecture');
INSERT INTO chapters (id, volume_id, number, title) VALUES (64, 2, '20', 'Cloud Architecture');
INSERT INTO chapters (id, volume_id, number, title) VALUES (65, 2, 'P5', 'Part V. Network Architecture');
INSERT INTO chapters (id, volume_id, number, title) VALUES (66, 2, '21', 'Introduction to Controller-Based Networking');
INSERT INTO chapters (id, volume_id, number, title) VALUES (67, 2, '22', 'Cisco Software-Defined Access (SDA)');
INSERT INTO chapters (id, volume_id, number, title) VALUES (68, 2, '23', 'Understanding REST and JSON');
INSERT INTO chapters (id, volume_id, number, title) VALUES (69, 2, '24', 'Understanding Ansible and Terraform');
INSERT INTO chapters (id, volume_id, number, title) VALUES (70, 2, 'P6', 'Part VI. Network Automation');
INSERT INTO chapters (id, volume_id, number, title) VALUES (71, 2, 'FR', 'Final Review');
INSERT INTO chapters (id, volume_id, number, title) VALUES (72, 2, 'CCNA-FR', 'CCNA Final Review');


INSERT INTO study_items (id, chapter_id, task_id) VALUES (1, 1, 1); -- Read Foundation Topics
INSERT INTO study_items (id, chapter_id, task_id) VALUES (2, 2, 1); -- Read Foundation Topics

-- Chapter 1: Introduction to TCP/IP Networking (Volume 1)
INSERT INTO study_items (id, chapter_id, task_id) VALUES (3, 3, 1); -- Read Foundation Topics
INSERT INTO study_items (id, chapter_id, task_id) VALUES (4, 3, 2); -- Review Key Topics
INSERT INTO study_items (id, chapter_id, task_id) VALUES (5, 3, 3); -- Define Key Terms
INSERT INTO study_items (id, chapter_id, task_id) VALUES (6, 3, 4); -- Repeat DIKTA questions
INSERT INTO study_items (id, chapter_id, task_id) VALUES (7, 3, 6); -- Practice Test

-- Chapter 2: Fundamentals of Ethernet LANs (Volume 1)
INSERT INTO study_items (id, chapter_id, task_id) VALUES (8, 4, 1); -- Read Foundation Topics
INSERT INTO study_items (id, chapter_id, task_id) VALUES (9, 4, 2); -- Review Key Topics
INSERT INTO study_items (id, chapter_id, task_id) VALUES (10, 4, 3); -- Define Key Terms
INSERT INTO study_items (id, chapter_id, task_id) VALUES (11, 4, 4); -- Repeat DIKTA questions
INSERT INTO study_items (id, chapter_id, task_id) VALUES (12, 4, 5); -- Memory Tables
INSERT INTO study_items (id, chapter_id, task_id) VALUES (13, 4, 6); -- Practice Test

-- Chapter 3: Fundamentals of WANs and IP Routing (Volume 1)
INSERT INTO study_items (id, chapter_id, task_id) VALUES (14, 5, 1); -- Read Foundation Topics
INSERT INTO study_items (id, chapter_id, task_id) VALUES (15, 5, 2); -- Review Key Topics
INSERT INTO study_items (id, chapter_id, task_id) VALUES (16, 5, 3); -- Define Key Terms
INSERT INTO study_items (id, chapter_id, task_id) VALUES (17, 5, 4); -- Repeat DIKTA questions
INSERT INTO study_items (id, chapter_id, task_id) VALUES (18, 5, 5); -- Memory Tables
INSERT INTO study_items (id, chapter_id, task_id) VALUES (19, 5, 6); -- Practice Test

-- Part I. Introduction to Networking (Volume 1)
INSERT INTO study_items (id, chapter_id, task_id) VALUES (20, 6, 11); -- Part Review
INSERT INTO study_items (id, chapter_id, task_id) VALUES (21, 6, 6); -- Practice Test

-- Chapter 4: Using the Command-Line Interface (Volume 1)
INSERT INTO study_items (id, chapter_id, task_id) VALUES (22, 7, 1); -- Read Foundation Topics
INSERT INTO study_items (id, chapter_id, task_id) VALUES (23, 7, 2); -- Review Key Topics
INSERT INTO study_items (id, chapter_id, task_id) VALUES (24, 7, 3); -- Define Key Terms
INSERT INTO study_items (id, chapter_id, task_id) VALUES (25, 7, 4); -- Repeat DIKTA questions
INSERT INTO study_items (id, chapter_id, task_id) VALUES (26, 7, 7); -- Command Tables
INSERT INTO study_items (id, chapter_id, task_id) VALUES (27, 7, 5); -- Memory Tables
INSERT INTO study_items (id, chapter_id, task_id) VALUES (28, 7, 6); -- Practice Test

-- Chapter 5: Analyzing Ethernet LAN Switching (Volume 1)
INSERT INTO study_items (id, chapter_id, task_id) VALUES (29, 8, 1); -- Read Foundation Topics
INSERT INTO study_items (id, chapter_id, task_id) VALUES (30, 8, 2); -- Review Key Topics
INSERT INTO study_items (id, chapter_id, task_id) VALUES (31, 8, 3); -- Define Key Terms
INSERT INTO study_items (id, chapter_id, task_id) VALUES (32, 8, 4); -- Repeat DIKTA questions
INSERT INTO study_items (id, chapter_id, task_id) VALUES (33, 8, 9); -- Labs
INSERT INTO study_items (id, chapter_id, task_id) VALUES (34, 8, 7); -- Command Tables
INSERT INTO study_items (id, chapter_id, task_id) VALUES (35, 8, 10); -- Videos
INSERT INTO study_items (id, chapter_id, task_id) VALUES (36, 8, 6); -- Practice Test

-- Chapter 6: Configuring Basic Switch Management (Volume 1)
INSERT INTO study_items (id, chapter_id, task_id) VALUES (37, 9, 1); -- Read Foundation Topics
INSERT INTO study_items (id, chapter_id, task_id) VALUES (38, 9, 2); -- Review Key Topics
INSERT INTO study_items (id, chapter_id, task_id) VALUES (39, 9, 3); -- Define Key Terms
INSERT INTO study_items (id, chapter_id, task_id) VALUES (40, 9, 4); -- Repeat DIKTA questions
INSERT INTO study_items (id, chapter_id, task_id) VALUES (41, 9, 8); -- Config Checklists
INSERT INTO study_items (id, chapter_id, task_id) VALUES (42, 9, 9); -- Labs
INSERT INTO study_items (id, chapter_id, task_id) VALUES (43, 9, 7); -- Command Tables
INSERT INTO study_items (id, chapter_id, task_id) VALUES (44, 9, 10); -- Videos
INSERT INTO study_items (id, chapter_id, task_id) VALUES (45, 9, 6); -- Practice Test

-- Chapter 7: Configuring and Verifying Switch Interfaces (Volume 1)
INSERT INTO study_items (id, chapter_id, task_id) VALUES (46, 10, 1); -- Read Foundation Topics
INSERT INTO study_items (id, chapter_id, task_id) VALUES (47, 10, 2); -- Review Key Topics
INSERT INTO study_items (id, chapter_id, task_id) VALUES (48, 10, 3); -- Define Key Terms
INSERT INTO study_items (id, chapter_id, task_id) VALUES (49, 10, 4); -- Repeat DIKTA questions
INSERT INTO study_items (id, chapter_id, task_id) VALUES (50, 10, 7); -- Command Tables
INSERT INTO study_items (id, chapter_id, task_id) VALUES (51, 10, 5); -- Memory Tables
INSERT INTO study_items (id, chapter_id, task_id) VALUES (52, 10, 9); -- Labs
INSERT INTO study_items (id, chapter_id, task_id) VALUES (53, 10, 6); -- Practice Test

-- Part II. Implementing Ethernet LANs (Volume 1)
INSERT INTO study_items (id, chapter_id, task_id) VALUES (54, 11, 11); -- Part Review
INSERT INTO study_items (id, chapter_id, task_id) VALUES (55, 11, 6); -- Practice Test

-- Chapter 8: Implementing Ethernet Virtual LANs (Volume 1)
INSERT INTO study_items (id, chapter_id, task_id) VALUES (56, 12, 1); -- Read Foundation Topics
INSERT INTO study_items (id, chapter_id, task_id) VALUES (57, 12, 2); -- Review Key Topics
INSERT INTO study_items (id, chapter_id, task_id) VALUES (58, 12, 3); -- Define Key Terms
INSERT INTO study_items (id, chapter_id, task_id) VALUES (59, 12, 4); -- Repeat DIKTA questions
INSERT INTO study_items (id, chapter_id, task_id) VALUES (60, 12, 8); -- Config Checklists
INSERT INTO study_items (id, chapter_id, task_id) VALUES (61, 12, 7); -- Command Tables
INSERT INTO study_items (id, chapter_id, task_id) VALUES (62, 12, 5); -- Memory Tables
INSERT INTO study_items (id, chapter_id, task_id) VALUES (63, 12, 9); -- Labs
INSERT INTO study_items (id, chapter_id, task_id) VALUES (64, 12, 10); -- Videos
INSERT INTO study_items (id, chapter_id, task_id) VALUES (65, 12, 6); -- Practice Test

-- Chapter 9: Spanning Tree Protocol Concepts (Volume 1)
INSERT INTO study_items (id, chapter_id, task_id) VALUES (66, 13, 1); -- Read Foundation Topics
INSERT INTO study_items (id, chapter_id, task_id) VALUES (67, 13, 2); -- Review Key Topics
INSERT INTO study_items (id, chapter_id, task_id) VALUES (68, 13, 3); -- Define Key Terms
INSERT INTO study_items (id, chapter_id, task_id) VALUES (69, 13, 4); -- Repeat DIKTA questions
INSERT INTO study_items (id, chapter_id, task_id) VALUES (70, 13, 5); -- Memory Tables
INSERT INTO study_items (id, chapter_id, task_id) VALUES (71, 13, 6); -- Practice Test

-- Chapter 10: RSTP and EtherChannel Configuration (Volume 1)
INSERT INTO study_items (id, chapter_id, task_id) VALUES (72, 14, 1); -- Read Foundation Topics
INSERT INTO study_items (id, chapter_id, task_id) VALUES (73, 14, 2); -- Review Key Topics
INSERT INTO study_items (id, chapter_id, task_id) VALUES (74, 14, 3); -- Define Key Terms
INSERT INTO study_items (id, chapter_id, task_id) VALUES (75, 14, 4); -- Repeat DIKTA questions
INSERT INTO study_items (id, chapter_id, task_id) VALUES (76, 14, 8); -- Config Checklists
INSERT INTO study_items (id, chapter_id, task_id) VALUES (77, 14, 7); -- Command Tables
INSERT INTO study_items (id, chapter_id, task_id) VALUES (78, 14, 5); -- Memory Tables
INSERT INTO study_items (id, chapter_id, task_id) VALUES (79, 14, 9); -- Labs
INSERT INTO study_items (id, chapter_id, task_id) VALUES (80, 14, 10); -- Videos
INSERT INTO study_items (id, chapter_id, task_id) VALUES (81, 14, 6); -- Practice Test

-- Part III. Implementing VLANs and STP (Volume 1)
INSERT INTO study_items (id, chapter_id, task_id) VALUES (82, 15, 11); -- Part Review
INSERT INTO study_items (id, chapter_id, task_id) VALUES (83, 15, 6); -- Practice Test

-- Chapter 11: Perspectives on IPv4 Subnetting (Volume 1)
INSERT INTO study_items (id, chapter_id, task_id) VALUES (84, 16, 1); -- Read Foundation Topics
INSERT INTO study_items (id, chapter_id, task_id) VALUES (85, 16, 2); -- Review Key Topics
INSERT INTO study_items (id, chapter_id, task_id) VALUES (86, 16, 3); -- Define Key Terms
INSERT INTO study_items (id, chapter_id, task_id) VALUES (87, 16, 4); -- Repeat DIKTA questions
INSERT INTO study_items (id, chapter_id, task_id) VALUES (88, 16, 5); -- Memory Tables
INSERT INTO study_items (id, chapter_id, task_id) VALUES (89, 16, 6); -- Practice Test

-- Chapter 12: Analyzing Classful IPv4 Networks (Volume 1)
INSERT INTO study_items (id, chapter_id, task_id) VALUES (90, 17, 1); -- Read Foundation Topics
INSERT INTO study_items (id, chapter_id, task_id) VALUES (91, 17, 2); -- Review Key Topics
INSERT INTO study_items (id, chapter_id, task_id) VALUES (92, 17, 3); -- Define Key Terms
INSERT INTO study_items (id, chapter_id, task_id) VALUES (93, 17, 4); -- Repeat DIKTA questions
INSERT INTO study_items (id, chapter_id, task_id) VALUES (94, 17, 5); -- Memory Tables
INSERT INTO study_items (id, chapter_id, task_id) VALUES (95, 17, 9); -- Practice analyzing classful IPv4 networks
INSERT INTO study_items (id, chapter_id, task_id) VALUES (96, 17, 10); -- Videos
INSERT INTO study_items (id, chapter_id, task_id) VALUES (97, 17, 6); -- Practice Test

-- Chapter 13: Analyzing Subnet Masks (Volume 1)
INSERT INTO study_items (id, chapter_id, task_id) VALUES (98, 18, 1); -- Read Foundation Topics
INSERT INTO study_items (id, chapter_id, task_id) VALUES (99, 18, 2); -- Review Key Topics
INSERT INTO study_items (id, chapter_id, task_id) VALUES (100, 18, 3); -- Define Key Terms
INSERT INTO study_items (id, chapter_id, task_id) VALUES (101, 18, 4); -- Repeat DIKTA questions
INSERT INTO study_items (id, chapter_id, task_id) VALUES (102, 18, 5); -- Memory Tables
INSERT INTO study_items (id, chapter_id, task_id) VALUES (103, 18, 9); -- Practice analyzing subnet masks
INSERT INTO study_items (id, chapter_id, task_id) VALUES (104, 18, 10); -- Videos
INSERT INTO study_items (id, chapter_id, task_id) VALUES (105, 18, 6); -- Practice Test

-- Chapter 14: Analyzing Existing Subnets (Volume 1)
INSERT INTO study_items (id, chapter_id, task_id) VALUES (106, 19, 1); -- Read Foundation Topics
INSERT INTO study_items (id, chapter_id, task_id) VALUES (107, 19, 2); -- Review Key Topics
INSERT INTO study_items (id, chapter_id, task_id) VALUES (108, 19, 3); -- Define Key Terms
INSERT INTO study_items (id, chapter_id, task_id) VALUES (109, 19, 4); -- Repeat DIKTA questions
INSERT INTO study_items (id, chapter_id, task_id) VALUES (110, 19, 5); -- Memory Tables
INSERT INTO study_items (id, chapter_id, task_id) VALUES (111, 19, 9); -- Practice mask analysis
INSERT INTO study_items (id, chapter_id, task_id) VALUES (112, 19, 9); -- Practice analyzing existing subnets
INSERT INTO study_items (id, chapter_id, task_id) VALUES (113, 19, 10); -- Videos
INSERT INTO study_items (id, chapter_id, task_id) VALUES (114, 19, 6); -- Practice Test

-- Chapter 15: Subnet Design (Volume 1)
INSERT INTO study_items (id, chapter_id, task_id) VALUES (115, 20, 1); -- Read Foundation Topics
INSERT INTO study_items (id, chapter_id, task_id) VALUES (116, 20, 2); -- Review Key Topics
INSERT INTO study_items (id, chapter_id, task_id) VALUES (117, 20, 3); -- Define Key Terms
INSERT INTO study_items (id, chapter_id, task_id) VALUES (118, 20, 4); -- Repeat DIKTA questions
INSERT INTO study_items (id, chapter_id, task_id) VALUES (119, 20, 9); -- Practice subnet design
INSERT INTO study_items (id, chapter_id, task_id) VALUES (120, 20, 10); -- Videos
INSERT INTO study_items (id, chapter_id, task_id) VALUES (121, 20, 6); -- Practice Test

-- Part IV. IPv4 Addressing (Volume 1)
INSERT INTO study_items (id, chapter_id, task_id) VALUES (122, 21, 11); -- Part Review
INSERT INTO study_items (id, chapter_id, task_id) VALUES (123, 21, 6); -- Practice Test

-- Chapter 16: Operating Cisco Routers (Volume 1)
INSERT INTO study_items (id, chapter_id, task_id) VALUES (124, 22, 1); -- Read Foundation Topics
INSERT INTO study_items (id, chapter_id, task_id) VALUES (125, 22, 2); -- Review Key Topics
INSERT INTO study_items (id, chapter_id, task_id) VALUES (126, 22, 3); -- Define Key Terms
INSERT INTO study_items (id, chapter_id, task_id) VALUES (127, 22, 4); -- Repeat DIKTA questions
INSERT INTO study_items (id, chapter_id, task_id) VALUES (128, 22, 7); -- Command Tables
INSERT INTO study_items (id, chapter_id, task_id) VALUES (129, 22, 5); -- Memory Tables
INSERT INTO study_items (id, chapter_id, task_id) VALUES (130, 22, 9); -- Labs
INSERT INTO study_items (id, chapter_id, task_id) VALUES (131, 22, 10); -- Videos
INSERT INTO study_items (id, chapter_id, task_id) VALUES (132, 22, 6); -- Practice Test

-- Chapter 17: Configuring IPv4 Addresses and Static Routes (Volume 1)
INSERT INTO study_items (id, chapter_id, task_id) VALUES (133, 23, 1); -- Read Foundation Topics
INSERT INTO study_items (id, chapter_id, task_id) VALUES (134, 23, 2); -- Review Key Topics
INSERT INTO study_items (id, chapter_id, task_id) VALUES (135, 23, 3); -- Define Key Terms
INSERT INTO study_items (id, chapter_id, task_id) VALUES (136, 23, 4); -- Repeat DIKTA questions
INSERT INTO study_items (id, chapter_id, task_id) VALUES (137, 23, 7); -- Command Tables
INSERT INTO study_items (id, chapter_id, task_id) VALUES (138, 23, 9); -- Labs
INSERT INTO study_items (id, chapter_id, task_id) VALUES (139, 23, 10); -- Videos
INSERT INTO study_items (id, chapter_id, task_id) VALUES (140, 23, 6); -- Practice Test

-- Chapter 18: IP Routing in the LAN (Volume 1)
INSERT INTO study_items (id, chapter_id, task_id) VALUES (141, 24, 1); -- Read Foundation Topics
INSERT INTO study_items (id, chapter_id, task_id) VALUES (142, 24, 2); -- Review Key Topics
INSERT INTO study_items (id, chapter_id, task_id) VALUES (143, 24, 3); -- Define Key Terms
INSERT INTO study_items (id, chapter_id, task_id) VALUES (144, 24, 4); -- Repeat DIKTA questions
INSERT INTO study_items (id, chapter_id, task_id) VALUES (145, 24, 8); -- Config Checklists
INSERT INTO study_items (id, chapter_id, task_id) VALUES (146, 24, 7); -- Command Tables
INSERT INTO study_items (id, chapter_id, task_id) VALUES (147, 24, 9); -- Labs
INSERT INTO study_items (id, chapter_id, task_id) VALUES (148, 24, 10); -- Videos
INSERT INTO study_items (id, chapter_id, task_id) VALUES (149, 24, 6); -- Practice Test

-- Chapter 19: IP Addressing on Hosts (Volume 1)
INSERT INTO study_items (id, chapter_id, task_id) VALUES (150, 25, 1); -- Read Foundation Topics
INSERT INTO study_items (id, chapter_id, task_id) VALUES (151, 25, 2); -- Review Key Topics
INSERT INTO study_items (id, chapter_id, task_id) VALUES (152, 25, 3); -- Define Key Terms
INSERT INTO study_items (id, chapter_id, task_id) VALUES (153, 25, 4); -- Repeat DIKTA questions
INSERT INTO study_items (id, chapter_id, task_id) VALUES (154, 25, 7); -- Command Tables
INSERT INTO study_items (id, chapter_id, task_id) VALUES (155, 25, 10); -- Videos

-- Chapter 20: Troubleshooting IPv4 Routing (Volume 1)
INSERT INTO study_items (id, chapter_id, task_id) VALUES (156, 26, 1); -- Read Foundation Topics
INSERT INTO study_items (id, chapter_id, task_id) VALUES (157, 26, 2); -- Review Key Topics
INSERT INTO study_items (id, chapter_id, task_id) VALUES (158, 26, 3); -- Define Key Terms
INSERT INTO study_items (id, chapter_id, task_id) VALUES (159, 26, 6); -- Practice Test

-- Part V. IPv4 Routing (Volume 1)
INSERT INTO study_items (id, chapter_id, task_id) VALUES (160, 27, 11); -- Part Review
INSERT INTO study_items (id, chapter_id, task_id) VALUES (161, 27, 6); -- Practice Test

-- Chapter 21: Understanding OSPF Concepts (Volume 1)
INSERT INTO study_items (id, chapter_id, task_id) VALUES (162, 28, 1); -- Read Foundation Topics
INSERT INTO study_items (id, chapter_id, task_id) VALUES (163, 28, 2); -- Review Key Topics
INSERT INTO study_items (id, chapter_id, task_id) VALUES (164, 28, 3); -- Define Key Terms
INSERT INTO study_items (id, chapter_id, task_id) VALUES (165, 28, 4); -- Repeat DIKTA questions
INSERT INTO study_items (id, chapter_id, task_id) VALUES (166, 28, 5); -- Memory Tables
INSERT INTO study_items (id, chapter_id, task_id) VALUES (167, 28, 6); -- Practice Test

-- Chapter 22: Implementing Basic OSPF Features (Volume 1)
INSERT INTO study_items (id, chapter_id, task_id) VALUES (168, 29, 1); -- Read Foundation Topics
INSERT INTO study_items (id, chapter_id, task_id) VALUES (169, 29, 2); -- Review Key Topics
INSERT INTO study_items (id, chapter_id, task_id) VALUES (170, 29, 3); -- Define Key Terms
INSERT INTO study_items (id, chapter_id, task_id) VALUES (171, 29, 4); -- Repeat DIKTA questions
INSERT INTO study_items (id, chapter_id, task_id) VALUES (172, 29, 8); -- Config Checklists
INSERT INTO study_items (id, chapter_id, task_id) VALUES (173, 29, 7); -- Command Tables
INSERT INTO study_items (id, chapter_id, task_id) VALUES (174, 29, 9); -- Labs
INSERT INTO study_items (id, chapter_id, task_id) VALUES (175, 29, 10); -- Videos
INSERT INTO study_items (id, chapter_id, task_id) VALUES (176, 29, 6); -- Practice Test

-- Chapter 23: Implementing Optional OSPF Features (Volume 1)
INSERT INTO study_items (id, chapter_id, task_id) VALUES (177, 30, 1); -- Read Foundation Topics
INSERT INTO study_items (id, chapter_id, task_id) VALUES (178, 30, 2); -- Review Key Topics
INSERT INTO study_items (id, chapter_id, task_id) VALUES (179, 30, 3); -- Define Key Terms
INSERT INTO study_items (id, chapter_id, task_id) VALUES (180, 30, 4); -- Repeat DIKTA questions
INSERT INTO study_items (id, chapter_id, task_id) VALUES (181, 30, 5); -- Memory Tables
INSERT INTO study_items (id, chapter_id, task_id) VALUES (182, 30, 8); -- Config Checklists
INSERT INTO study_items (id, chapter_id, task_id) VALUES (183, 30, 7); -- Command Tables
INSERT INTO study_items (id, chapter_id, task_id) VALUES (184, 30, 9); -- Labs
INSERT INTO study_items (id, chapter_id, task_id) VALUES (185, 30, 10); -- Videos
INSERT INTO study_items (id, chapter_id, task_id) VALUES (186, 30, 6); -- Practice Test

-- Chapter 24: OSPF Neighbors and Route Selection (Volume 1)
INSERT INTO study_items (id, chapter_id, task_id) VALUES (187, 31, 1); -- Read Foundation Topics
INSERT INTO study_items (id, chapter_id, task_id) VALUES (188, 31, 2); -- Review Key Topics
INSERT INTO study_items (id, chapter_id, task_id) VALUES (189, 31, 3); -- Define Key Terms
INSERT INTO study_items (id, chapter_id, task_id) VALUES (190, 31, 4); -- Repeat DIKTA questions
INSERT INTO study_items (id, chapter_id, task_id) VALUES (191, 31, 7); -- Command Tables
INSERT INTO study_items (id, chapter_id, task_id) VALUES (192, 31, 5); -- Memory Tables
INSERT INTO study_items (id, chapter_id, task_id) VALUES (193, 31, 10); -- Videos

-- Part VI. OSPF (Volume 1)
INSERT INTO study_items (id, chapter_id, task_id) VALUES (194, 32, 11); -- Part Review
INSERT INTO study_items (id, chapter_id, task_id) VALUES (195, 32, 6); -- Practice Test

-- Chapter 25: Fundamentals of IP Version 6 (Volume 1)
INSERT INTO study_items (id, chapter_id, task_id) VALUES (196, 33, 1); -- Read Foundation Topics
INSERT INTO study_items (id, chapter_id, task_id) VALUES (197, 33, 2); -- Review Key Topics
INSERT INTO study_items (id, chapter_id, task_id) VALUES (198, 33, 3); -- Define Key Terms
INSERT INTO study_items (id, chapter_id, task_id) VALUES (199, 33, 4); -- Repeat DIKTA questions
INSERT INTO study_items (id, chapter_id, task_id) VALUES (200, 33, 7); -- Command Tables
INSERT INTO study_items (id, chapter_id, task_id) VALUES (201, 33, 5); -- Memory Tables
INSERT INTO study_items (id, chapter_id, task_id) VALUES (202, 33, 9); -- Practice abbreviating and expanding addresses
INSERT INTO study_items (id, chapter_id, task_id) VALUES (203, 33, 9); -- Practice calculating the IPv6 subnet prefix
INSERT INTO study_items (id, chapter_id, task_id) VALUES (204, 33, 6); -- Practice Test

-- Chapter 26: IPv6 Addressing and Subnetting (Volume 1)
INSERT INTO study_items (id, chapter_id, task_id) VALUES (205, 34, 1); -- Read Foundation Topics
INSERT INTO study_items (id, chapter_id, task_id) VALUES (206, 34, 2); -- Review Key Topics
INSERT INTO study_items (id, chapter_id, task_id) VALUES (207, 34, 3); -- Define Key Terms
INSERT INTO study_items (id, chapter_id, task_id) VALUES (208, 34, 4); -- Repeat DIKTA questions
INSERT INTO study_items (id, chapter_id, task_id) VALUES (209, 34, 5); -- Memory Tables
INSERT INTO study_items (id, chapter_id, task_id) VALUES (210, 34, 10); -- Videos
INSERT INTO study_items (id, chapter_id, task_id) VALUES (211, 34, 6); -- Practice Test

-- Chapter 27: Implementing IPv6 Addressing on Routers (Volume 1)
INSERT INTO study_items (id, chapter_id, task_id) VALUES (212, 35, 1); -- Read Foundation Topics
INSERT INTO study_items (id, chapter_id, task_id) VALUES (213, 35, 2); -- Review Key Topics
INSERT INTO study_items (id, chapter_id, task_id) VALUES (214, 35, 3); -- Define Key Terms
INSERT INTO study_items (id, chapter_id, task_id) VALUES (215, 35, 4); -- Repeat DIKTA questions
INSERT INTO study_items (id, chapter_id, task_id) VALUES (216, 35, 7); -- Command Tables
INSERT INTO study_items (id, chapter_id, task_id) VALUES (217, 35, 5); -- Memory Tables
INSERT INTO study_items (id, chapter_id, task_id) VALUES (218, 35, 9); -- Practice EUI-64 and solicited node multicast problems
INSERT INTO study_items (id, chapter_id, task_id) VALUES (219, 35, 9); -- Labs
INSERT INTO study_items (id, chapter_id, task_id) VALUES (220, 35, 10); -- Videos
INSERT INTO study_items (id, chapter_id, task_id) VALUES (221, 35, 6); -- Practice Test

-- Chapter 28: Implementing IPv6 Addressing on Hosts (Volume 1)
INSERT INTO study_items (id, chapter_id, task_id) VALUES (222, 36, 1); -- Read Foundation Topics
INSERT INTO study_items (id, chapter_id, task_id) VALUES (223, 36, 2); -- Review Key Topics
INSERT INTO study_items (id, chapter_id, task_id) VALUES (224, 36, 3); -- Define Key Terms
INSERT INTO study_items (id, chapter_id, task_id) VALUES (225, 36, 4); -- Repeat DIKTA questions
INSERT INTO study_items (id, chapter_id, task_id) VALUES (226, 36, 5); -- Memory Tables
INSERT INTO study_items (id, chapter_id, task_id) VALUES (227, 36, 7); -- Command Tables
INSERT INTO study_items (id, chapter_id, task_id) VALUES (228, 36, 6); -- Practice Test

-- Chapter 29: Implementing IPv6 Routing (Volume 1)
INSERT INTO study_items (id, chapter_id, task_id) VALUES (229, 37, 1); -- Read Foundation Topics
INSERT INTO study_items (id, chapter_id, task_id) VALUES (230, 37, 2); -- Review Key Topics
INSERT INTO study_items (id, chapter_id, task_id) VALUES (231, 37, 3); -- Define Key Terms
INSERT INTO study_items (id, chapter_id, task_id) VALUES (232, 37, 4); -- Repeat DIKTA questions
INSERT INTO study_items (id, chapter_id, task_id) VALUES (233, 37, 7); -- Command Tables
INSERT INTO study_items (id, chapter_id, task_id) VALUES (234, 37, 5); -- Memory Tables
INSERT INTO study_items (id, chapter_id, task_id) VALUES (235, 37, 9); -- Labs
INSERT INTO study_items (id, chapter_id, task_id) VALUES (236, 37, 10); -- Videos
INSERT INTO study_items (id, chapter_id, task_id) VALUES (237, 37, 6); -- Practice Test

-- Part VII. IP Version 6 (Volume 1)
INSERT INTO study_items (id, chapter_id, task_id) VALUES (238, 38, 11); -- Part Review
INSERT INTO study_items (id, chapter_id, task_id) VALUES (239, 38, 6); -- Practice Test

-- Final Review (Volume 1)
INSERT INTO study_items (id, chapter_id, task_id) VALUES (240, 39, 6); -- Practice Test (all book questions)
INSERT INTO study_items (id, chapter_id, task_id) VALUES (241, 39, 2); -- Review all Key Topics
INSERT INTO study_items (id, chapter_id, task_id) VALUES (242, 39, 3); -- Review all Key Terms
INSERT INTO study_items (id, chapter_id, task_id) VALUES (243, 39, 5); -- Complete all memory tables
INSERT INTO study_items (id, chapter_id, task_id) VALUES (244, 39, 6); -- Practice Test (Exam Bank #1)
INSERT INTO study_items (id, chapter_id, task_id) VALUES (245, 39, 6); -- Practice Test (Exam Bank #2)

-- Introduction (Volume 2)
INSERT INTO study_items (id, chapter_id, task_id) VALUES (246, 40, 1); -- Read Introduction

-- Chapter 1: Fundamentals of Wireless Networks (Volume 2)
INSERT INTO study_items (id, chapter_id, task_id) VALUES (247, 41, 1); -- Read Foundation Topics
INSERT INTO study_items (id, chapter_id, task_id) VALUES (248, 41, 2); -- Review Key Topics
INSERT INTO study_items (id, chapter_id, task_id) VALUES (249, 41, 3); -- Define Key Terms
INSERT INTO study_items (id, chapter_id, task_id) VALUES (250, 41, 4); -- Repeat DIKTA questions
INSERT INTO study_items (id, chapter_id, task_id) VALUES (251, 41, 5); -- Memory Tables
INSERT INTO study_items (id, chapter_id, task_id) VALUES (252, 41, 6); -- Practice Test

-- Chapter 2: Analyzing Cisco Wireless Architectures (Volume 2)
INSERT INTO study_items (id, chapter_id, task_id) VALUES (253, 42, 1); -- Read Foundation Topics
INSERT INTO study_items (id, chapter_id, task_id) VALUES (254, 42, 2); -- Review Key Topics
INSERT INTO study_items (id, chapter_id, task_id) VALUES (255, 42, 3); -- Define Key Terms
INSERT INTO study_items (id, chapter_id, task_id) VALUES (256, 42, 4); -- Repeat DIKTA questions
INSERT INTO study_items (id, chapter_id, task_id) VALUES (257, 42, 5); -- Memory Tables
INSERT INTO study_items (id, chapter_id, task_id) VALUES (258, 42, 10); -- Videos
INSERT INTO study_items (id, chapter_id, task_id) VALUES (259, 42, 6); -- Practice Test

-- Chapter 3: Securing Wireless Networks (Volume 2)
INSERT INTO study_items (id, chapter_id, task_id) VALUES (260, 43, 1); -- Read Foundation Topics
INSERT INTO study_items (id, chapter_id, task_id) VALUES (261, 43, 2); -- Review Key Topics
INSERT INTO study_items (id, chapter_id, task_id) VALUES (262, 43, 3); -- Define Key Terms
INSERT INTO study_items (id, chapter_id, task_id) VALUES (263, 43, 4); -- Repeat DIKTA questions
INSERT INTO study_items (id, chapter_id, task_id) VALUES (264, 43, 5); -- Memory Tables
INSERT INTO study_items (id, chapter_id, task_id) VALUES (265, 43, 6); -- Practice Test

-- Chapter 4: Building a Wireless LAN (Volume 2)
INSERT INTO study_items (id, chapter_id, task_id) VALUES (266, 44, 1); -- Read Foundation Topics
INSERT INTO study_items (id, chapter_id, task_id) VALUES (267, 44, 2); -- Review Key Topics
INSERT INTO study_items (id, chapter_id, task_id) VALUES (268, 44, 3); -- Define Key Terms
INSERT INTO study_items (id, chapter_id, task_id) VALUES (269, 44, 4); -- Repeat DIKTA questions
INSERT INTO study_items (id, chapter_id, task_id) VALUES (270, 44, 5); -- Memory Tables
INSERT INTO study_items (id, chapter_id, task_id) VALUES (271, 44, 10); -- Videos
INSERT INTO study_items (id, chapter_id, task_id) VALUES (272, 44, 6); -- Practice Test

-- Part I. Wireless LANs (Volume 2)
INSERT INTO study_items (id, chapter_id, task_id) VALUES (273, 45, 11); -- Part Review
INSERT INTO study_items (id, chapter_id, task_id) VALUES (274, 45, 6); -- Practice Test

-- Chapter 5: Introduction to TCP/IP Transport and Applications (Volume 2)
INSERT INTO study_items (id, chapter_id, task_id) VALUES (275, 46, 1); -- Read Foundation Topics
INSERT INTO study_items (id, chapter_id, task_id) VALUES (276, 46, 2); -- Review Key Topics
INSERT INTO study_items (id, chapter_id, task_id) VALUES (277, 46, 3); -- Define Key Terms
INSERT INTO study_items (id, chapter_id, task_id) VALUES (278, 46, 4); -- Repeat DIKTA questions
INSERT INTO study_items (id, chapter_id, task_id) VALUES (279, 46, 5); -- Memory Tables
INSERT INTO study_items (id, chapter_id, task_id) VALUES (280, 46, 6); -- Practice Test

-- Chapter 6: Basic IPv4 Access Control Lists (Volume 2)
INSERT INTO study_items (id, chapter_id, task_id) VALUES (281, 47, 1); -- Read Foundation Topics
INSERT INTO study_items (id, chapter_id, task_id) VALUES (282, 47, 2); -- Review Key Topics
INSERT INTO study_items (id, chapter_id, task_id) VALUES (283, 47, 3); -- Define Key Terms
INSERT INTO study_items (id, chapter_id, task_id) VALUES (284, 47, 4); -- Repeat DIKTA questions
INSERT INTO study_items (id, chapter_id, task_id) VALUES (285, 47, 7); -- Command Tables
INSERT INTO study_items (id, chapter_id, task_id) VALUES (286, 47, 5); -- Memory Tables
INSERT INTO study_items (id, chapter_id, task_id) VALUES (287, 47, 9); -- Complete practice exercise: Create a one-line standard ACL
INSERT INTO study_items (id, chapter_id, task_id) VALUES (288, 47, 9); -- Complete practice exercise: Matching IP addresses
INSERT INTO study_items (id, chapter_id, task_id) VALUES (289, 47, 6); -- Practice Test

-- Chapter 7: Named and Extended IP ACLs (Volume 2)
INSERT INTO study_items (id, chapter_id, task_id) VALUES (290, 48, 1); -- Read Foundation Topics
INSERT INTO study_items (id, chapter_id, task_id) VALUES (291, 48, 2); -- Review Key Topics
INSERT INTO study_items (id, chapter_id, task_id) VALUES (292, 48, 3); -- Define Key Terms
INSERT INTO study_items (id, chapter_id, task_id) VALUES (293, 48, 4); -- Repeat DIKTA questions
INSERT INTO study_items (id, chapter_id, task_id) VALUES (294, 48, 7); -- Command Tables
INSERT INTO study_items (id, chapter_id, task_id) VALUES (295, 48, 5); -- Memory Tables
INSERT INTO study_items (id, chapter_id, task_id) VALUES (296, 48, 10); -- Videos
INSERT INTO study_items (id, chapter_id, task_id) VALUES (297, 48, 6); -- Practice Test

-- Chapter 8: Applied IP ACLs (Volume 2)
INSERT INTO study_items (id, chapter_id, task_id) VALUES (298, 49, 1); -- Read Foundation Topics
INSERT INTO study_items (id, chapter_id, task_id) VALUES (299, 49, 2); -- Review Key Topics
INSERT INTO study_items (id, chapter_id, task_id) VALUES (300, 49, 3); -- Define Key Terms
INSERT INTO study_items (id, chapter_id, task_id) VALUES (301, 49, 4); -- Repeat DIKTA questions
INSERT INTO study_items (id, chapter_id, task_id) VALUES (302, 49, 7); -- Command Tables
INSERT INTO study_items (id, chapter_id, task_id) VALUES (303, 49, 5); -- Memory Tables
INSERT INTO study_items (id, chapter_id, task_id) VALUES (304, 49, 10); -- Videos
INSERT INTO study_items (id, chapter_id, task_id) VALUES (305, 49, 6); -- Practice Test

-- Part II. IP Access Control Lists (Volume 2)
INSERT INTO study_items (id, chapter_id, task_id) VALUES (306, 50, 11); -- Part Review
INSERT INTO study_items (id, chapter_id, task_id) VALUES (307, 50, 6); -- Practice Test

-- Chapter 9: Security Architectures (Volume 2)
INSERT INTO study_items (id, chapter_id, task_id) VALUES (308, 51, 1); -- Read Foundation Topics
INSERT INTO study_items (id, chapter_id, task_id) VALUES (309, 51, 2); -- Review Key Topics
INSERT INTO study_items (id, chapter_id, task_id) VALUES (310, 51, 3); -- Define Key Terms
INSERT INTO study_items (id, chapter_id, task_id) VALUES (311, 51, 4); -- Repeat DIKTA questions
INSERT INTO study_items (id, chapter_id, task_id) VALUES (312, 51, 5); -- Memory Tables
INSERT INTO study_items (id, chapter_id, task_id) VALUES (313, 51, 10); -- Videos
INSERT INTO study_items (id, chapter_id, task_id) VALUES (314, 51, 6); -- Practice Test

-- Chapter 10: Securing Network Devices (Volume 2)
INSERT INTO study_items (id, chapter_id, task_id) VALUES (315, 52, 1); -- Read Foundation Topics
INSERT INTO study_items (id, chapter_id, task_id) VALUES (316, 52, 2); -- Review Key Topics
INSERT INTO study_items (id, chapter_id, task_id) VALUES (317, 52, 3); -- Define Key Terms
INSERT INTO study_items (id, chapter_id, task_id) VALUES (318, 52, 4); -- Repeat DIKTA questions
INSERT INTO study_items (id, chapter_id, task_id) VALUES (319, 52, 7); -- Command Tables
INSERT INTO study_items (id, chapter_id, task_id) VALUES (320, 52, 10); -- Videos
INSERT INTO study_items (id, chapter_id, task_id) VALUES (321, 52, 9); -- Labs
INSERT INTO study_items (id, chapter_id, task_id) VALUES (322, 52, 6); -- Practice Test

-- Chapter 11: Implementing Switch Port Security (Volume 2)
INSERT INTO study_items (id, chapter_id, task_id) VALUES (323, 53, 1); -- Read Foundation Topics
INSERT INTO study_items (id, chapter_id, task_id) VALUES (324, 53, 2); -- Review Key Topics
INSERT INTO study_items (id, chapter_id, task_id) VALUES (325, 53, 3); -- Define Key Terms
INSERT INTO study_items (id, chapter_id, task_id) VALUES (326, 53, 4); -- Repeat DIKTA questions
INSERT INTO study_items (id, chapter_id, task_id) VALUES (327, 53, 7); -- Command Tables
INSERT INTO study_items (id, chapter_id, task_id) VALUES (328, 53, 5); -- Memory Tables
INSERT INTO study_items (id, chapter_id, task_id) VALUES (329, 53, 8); -- Config Checklist
INSERT INTO study_items (id, chapter_id, task_id) VALUES (330, 53, 10); -- Videos
INSERT INTO study_items (id, chapter_id, task_id) VALUES (331, 53, 9); -- Labs
INSERT INTO study_items (id, chapter_id, task_id) VALUES (332, 53, 6); -- Practice Test

-- Chapter 12: DHCP Snooping and ARP Inspection (Volume 2)
INSERT INTO study_items (id, chapter_id, task_id) VALUES (333, 54, 1); -- Read Foundation Topics
INSERT INTO study_items (id, chapter_id, task_id) VALUES (334, 54, 2); -- Review Key Topics
INSERT INTO study_items (id, chapter_id, task_id) VALUES (335, 54, 3); -- Define Key Terms
INSERT INTO study_items (id, chapter_id, task_id) VALUES (336, 54, 4); -- Repeat DIKTA questions
INSERT INTO study_items (id, chapter_id, task_id) VALUES (337, 54, 7); -- Command Tables
INSERT INTO study_items (id, chapter_id, task_id) VALUES (338, 54, 8); -- Config Checklist: DHCP Snooping
INSERT INTO study_items (id, chapter_id, task_id) VALUES (339, 54, 8); -- Config Checklist: Dynamic IP ARP Inspection
INSERT INTO study_items (id, chapter_id, task_id) VALUES (340, 54, 10); -- Videos
INSERT INTO study_items (id, chapter_id, task_id) VALUES (341, 54, 6); -- Practice Test

-- Part III. Security Services (Volume 2)
INSERT INTO study_items (id, chapter_id, task_id) VALUES (342, 55, 11); -- Part Review
INSERT INTO study_items (id, chapter_id, task_id) VALUES (343, 55, 6); -- Practice Test

-- Chapter 13: Device Management Protocols (Volume 2)
INSERT INTO study_items (id, chapter_id, task_id) VALUES (344, 56, 1); -- Read Foundation Topics
INSERT INTO study_items (id, chapter_id, task_id) VALUES (345, 56, 2); -- Review Key Topics
INSERT INTO study_items (id, chapter_id, task_id) VALUES (346, 56, 3); -- Define Key Terms
INSERT INTO study_items (id, chapter_id, task_id) VALUES (347, 56, 4); -- Repeat DIKTA questions
INSERT INTO study_items (id, chapter_id, task_id) VALUES (348, 56, 7); -- Command Tables
INSERT INTO study_items (id, chapter_id, task_id) VALUES (349, 56, 5); -- Memory Tables
INSERT INTO study_items (id, chapter_id, task_id) VALUES (350, 56, 10); -- Videos
INSERT INTO study_items (id, chapter_id, task_id) VALUES (351, 56, 9); -- Labs
INSERT INTO study_items (id, chapter_id, task_id) VALUES (352, 56, 6); -- Practice Test

-- Chapter 14: Network Address Translation (Volume 2)
INSERT INTO study_items (id, chapter_id, task_id) VALUES (353, 57, 1); -- Read Foundation Topics
INSERT INTO study_items (id, chapter_id, task_id) VALUES (354, 57, 2); -- Review Key Topics
INSERT INTO study_items (id, chapter_id, task_id) VALUES (355, 57, 3); -- Define Key Terms
INSERT INTO study_items (id, chapter_id, task_id) VALUES (356, 57, 4); -- Repeat DIKTA questions
INSERT INTO study_items (id, chapter_id, task_id) VALUES (357, 57, 7); -- Command Tables
INSERT INTO study_items (id, chapter_id, task_id) VALUES (358, 57, 5); -- Memory Tables
INSERT INTO study_items (id, chapter_id, task_id) VALUES (359, 57, 8); -- Config Checklist: Static NAT
INSERT INTO study_items (id, chapter_id, task_id) VALUES (360, 57, 8); -- Config Checklist: Dynamic NAT
INSERT INTO study_items (id, chapter_id, task_id) VALUES (361, 57, 8); -- Config Checklist: Interface IP Address
INSERT INTO study_items (id, chapter_id, task_id) VALUES (362, 57, 10); -- Videos
INSERT INTO study_items (id, chapter_id, task_id) VALUES (363, 57, 9); -- Labs
INSERT INTO study_items (id, chapter_id, task_id) VALUES (364, 57, 6); -- Practice Test

-- Chapter 15: Quality of Service (QoS) (Volume 2)
INSERT INTO study_items (id, chapter_id, task_id) VALUES (365, 58, 1); -- Read Foundation Topics
INSERT INTO study_items (id, chapter_id, task_id) VALUES (366, 58, 2); -- Review Key Topics
INSERT INTO study_items (id, chapter_id, task_id) VALUES (367, 58, 3); -- Define Key Terms
INSERT INTO study_items (id, chapter_id, task_id) VALUES (368, 58, 4); -- Repeat DIKTA questions
INSERT INTO study_items (id, chapter_id, task_id) VALUES (369, 58, 5); -- Memory Tables
INSERT INTO study_items (id, chapter_id, task_id) VALUES (370, 58, 10); -- Videos
INSERT INTO study_items (id, chapter_id, task_id) VALUES (371, 58, 6); -- Practice Test

-- Chapter 16: First Hop Redundancy Protocols (Volume 2)
INSERT INTO study_items (id, chapter_id, task_id) VALUES (372, 59, 1); -- Read Foundation Topics
INSERT INTO study_items (id, chapter_id, task_id) VALUES (373, 59, 2); -- Review Key Topics
INSERT INTO study_items (id, chapter_id, task_id) VALUES (374, 59, 3); -- Define Key Terms
INSERT INTO study_items (id, chapter_id, task_id) VALUES (375, 59, 4); -- Repeat DIKTA questions
INSERT INTO study_items (id, chapter_id, task_id) VALUES (376, 59, 5); -- Memory Tables
INSERT INTO study_items (id, chapter_id, task_id) VALUES (377, 59, 6); -- Practice Test

-- Chapter 17: SNMP, FTP, and TFTP (Volume 2)
INSERT INTO study_items (id, chapter_id, task_id) VALUES (378, 60, 1); -- Read Foundation Topics
INSERT INTO study_items (id, chapter_id, task_id) VALUES (379, 60, 2); -- Review Key Topics
INSERT INTO study_items (id, chapter_id, task_id) VALUES (380, 60, 3); -- Define Key Terms
INSERT INTO study_items (id, chapter_id, task_id) VALUES (381, 60, 4); -- Repeat DIKTA questions
INSERT INTO study_items (id, chapter_id, task_id) VALUES (382, 60, 7); -- Command Tables
INSERT INTO study_items (id, chapter_id, task_id) VALUES (383, 60, 6); -- Practice Test

-- Part IV. IP Services (Volume 2)
INSERT INTO study_items (id, chapter_id, task_id) VALUES (384, 61, 11); -- Part Review
INSERT INTO study_items (id, chapter_id, task_id) VALUES (385, 61, 6); -- Practice Test

-- Chapter 18: LAN Architecture (Volume 2)
INSERT INTO study_items (id, chapter_id, task_id) VALUES (386, 62, 1); -- Read Foundation Topics
INSERT INTO study_items (id, chapter_id, task_id) VALUES (387, 62, 2); -- Review Key Topics
INSERT INTO study_items (id, chapter_id, task_id) VALUES (388, 62, 3); -- Define Key Terms
INSERT INTO study_items (id, chapter_id, task_id) VALUES (389, 62, 4); -- Repeat DIKTA questions
INSERT INTO study_items (id, chapter_id, task_id) VALUES (390, 62, 5); -- Memory Tables
INSERT INTO study_items (id, chapter_id, task_id) VALUES (391, 62, 6); -- Practice Test

-- Chapter 19: WAN Architecture (Volume 2)
INSERT INTO study_items (id, chapter_id, task_id) VALUES (392, 63, 1); -- Read Foundation Topics
INSERT INTO study_items (id, chapter_id, task_id) VALUES (393, 63, 2); -- Review Key Topics
INSERT INTO study_items (id, chapter_id, task_id) VALUES (394, 63, 3); -- Define Key Terms
INSERT INTO study_items (id, chapter_id, task_id) VALUES (395, 63, 4); -- Repeat DIKTA questions
INSERT INTO study_items (id, chapter_id, task_id) VALUES (396, 63, 5); -- Memory Tables
INSERT INTO study_items (id, chapter_id, task_id) VALUES (397, 63, 6); -- Practice Test

-- Chapter 20: Cloud Architecture (Volume 2)
INSERT INTO study_items (id, chapter_id, task_id) VALUES (398, 64, 1); -- Read Foundation Topics
INSERT INTO study_items (id, chapter_id, task_id) VALUES (399, 64, 2); -- Review Key Topics
INSERT INTO study_items (id, chapter_id, task_id) VALUES (400, 64, 3); -- Define Key Terms
INSERT INTO study_items (id, chapter_id, task_id) VALUES (401, 64, 4); -- Repeat DIKTA questions
INSERT INTO study_items (id, chapter_id, task_id) VALUES (402, 64, 5); -- Memory Tables
INSERT INTO study_items (id, chapter_id, task_id) VALUES (403, 64, 6); -- Practice Test

-- Part V. Network Architecture (Volume 2)
INSERT INTO study_items (id, chapter_id, task_id) VALUES (404, 65, 11); -- Part Review
INSERT INTO study_items (id, chapter_id, task_id) VALUES (405, 65, 6); -- Practice Test

-- Chapter 21: Introduction to Controller-Based Networking (Volume 2)
INSERT INTO study_items (id, chapter_id, task_id) VALUES (406, 66, 1); -- Read Foundation Topics
INSERT INTO study_items (id, chapter_id, task_id) VALUES (407, 66, 2); -- Review Key Topics
INSERT INTO study_items (id, chapter_id, task_id) VALUES (408, 66, 3); -- Define Key Terms
INSERT INTO study_items (id, chapter_id, task_id) VALUES (409, 66, 4); -- Repeat DIKTA questions
INSERT INTO study_items (id, chapter_id, task_id) VALUES (410, 66, 5); -- Memory Tables
INSERT INTO study_items (id, chapter_id, task_id) VALUES (411, 66, 6); -- Practice Test

-- Chapter 22: Cisco Software-Defined Access (SDA) (Volume 2)
INSERT INTO study_items (id, chapter_id, task_id) VALUES (412, 67, 1); -- Read Foundation Topics
INSERT INTO study_items (id, chapter_id, task_id) VALUES (413, 67, 2); -- Review Key Topics
INSERT INTO study_items (id, chapter_id, task_id) VALUES (414, 67, 3); -- Define Key Terms
INSERT INTO study_items (id, chapter_id, task_id) VALUES (415, 67, 4); -- Repeat DIKTA questions
INSERT INTO study_items (id, chapter_id, task_id) VALUES (416, 67, 10); -- Videos
INSERT INTO study_items (id, chapter_id, task_id) VALUES (417, 67, 6); -- Practice Test

-- Chapter 23: Understanding REST and JSON (Volume 2)
INSERT INTO study_items (id, chapter_id, task_id) VALUES (418, 68, 1); -- Read Foundation Topics
INSERT INTO study_items (id, chapter_id, task_id) VALUES (419, 68, 2); -- Review Key Topics
INSERT INTO study_items (id, chapter_id, task_id) VALUES (420, 68, 3); -- Define Key Terms
INSERT INTO study_items (id, chapter_id, task_id) VALUES (421, 68, 4); -- Repeat DIKTA questions
INSERT INTO study_items (id, chapter_id, task_id) VALUES (422, 68, 5); -- Memory Tables
INSERT INTO study_items (id, chapter_id, task_id) VALUES (423, 68, 10); -- Videos
INSERT INTO study_items (id, chapter_id, task_id) VALUES (424, 68, 6); -- Practice Test

-- Chapter 24: Understanding Ansible and Terraform (Volume 2)
INSERT INTO study_items (id, chapter_id, task_id) VALUES (425, 69, 1); -- Read Foundation Topics
INSERT INTO study_items (id, chapter_id, task_id) VALUES (426, 69, 2); -- Review Key Topics
INSERT INTO study_items (id, chapter_id, task_id) VALUES (427, 69, 3); -- Define Key Terms
INSERT INTO study_items (id, chapter_id, task_id) VALUES (428, 69, 4); -- Repeat DIKTA questions
INSERT INTO study_items (id, chapter_id, task_id) VALUES (429, 69, 5); -- Memory Tables
INSERT INTO study_items (id, chapter_id, task_id) VALUES (430, 69, 9); -- Labs
INSERT INTO study_items (id, chapter_id, task_id) VALUES (431, 69, 6); -- Practice Test

-- Part VI. Network Automation (Volume 2)
INSERT INTO study_items (id, chapter_id, task_id) VALUES (432, 70, 11); -- Part Review
INSERT INTO study_items (id, chapter_id, task_id) VALUES (433, 70, 6); -- Practice Test

-- Final Review (Volume 2)
INSERT INTO study_items (id, chapter_id, task_id) VALUES (434, 71, 6); -- Practice Test (all book questions)
INSERT INTO study_items (id, chapter_id, task_id) VALUES (435, 71, 2); -- Review all Key Topics
INSERT INTO study_items (id, chapter_id, task_id) VALUES (436, 71, 3); -- Review all Key Terms
INSERT INTO study_items (id, chapter_id, task_id) VALUES (437, 71, 5); -- Complete all memory tables
INSERT INTO study_items (id, chapter_id, task_id) VALUES (438, 71, 8); -- Complete all config checklists
INSERT INTO study_items (id, chapter_id, task_id) VALUES (439, 71, 9); -- Do all hands-on labs
INSERT INTO study_items (id, chapter_id, task_id) VALUES (440, 71, 6); -- Practice Test (Exam Bank #1)
INSERT INTO study_items (id, chapter_id, task_id) VALUES (441, 71, 6); -- Practice Test (Exam Bank #2)

-- CCNA Final Review (Volume 2)
INSERT INTO study_items (id, chapter_id, task_id) VALUES (442, 72, 1); -- Read Final Review Chapter
INSERT INTO study_items (id, chapter_id, task_id) VALUES (443, 72, 6); -- Take practice test (Full CCNA Exam Bank #1)
INSERT INTO study_items (id, chapter_id, task_id) VALUES (444, 72, 12); -- Identify areas of weakness
INSERT INTO study_items (id, chapter_id, task_id) VALUES (445, 72, 6); -- Take practice test (Full CCNA Exam Bank #2)