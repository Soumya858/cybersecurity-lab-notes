Case Study: MariaDB Enumeration and Database Discovery
Objective

Perform service enumeration on a target machine to identify exposed services, investigate the database configuration, and enumerate accessible data.

Environment

Target IP: 10.129.72.199

Assessment Platform: Hack The Box (HTB)

Tools Used:

Nmap
MySQL Client
Linux Terminal
Phase 1: Network Reconnaissance

An Nmap service detection scan was conducted against the target host.

nmap -sC -sV 10.129.72.199
Findings

The scan identified:

Port	Service	Status
3306/TCP	MySQL/MariaDB	Open

The host was reachable and actively running a database service on port 3306.

Phase 2: Service Enumeration

Further analysis of the MySQL service revealed the following information:

Database Information
Protocol Version: 10
Version: 5.5.5-10.3.27-MariaDB-0+deb10u1
Version Analysis
Component	Meaning
5.5.5	MySQL compatibility marker
10.3.27	Actual MariaDB version
deb10u1	Debian 10 package build

Research indicated that MariaDB 10.3.x is an older release and may lack support for certain modern security features and SSL configurations.

Phase 3: Database Access

A connection attempt was made using the MySQL client.

mysql -h 10.129.72.199 -u root -p --skip-ssl
Parameter Explanation
Option	Description
-h	Target host
-u	Username
-p	Prompt for password
--skip-ssl	Disable SSL requirement

The connection to the MariaDB service was successfully established.

Phase 4: Privilege Verification

To determine the level of access obtained, the following commands were executed:

SELECT USER();
SELECT CURRENT_USER();
SHOW GRANTS;
Purpose
Identify authenticated user
Verify effective database account
Review assigned privileges
Phase 5: Database Enumeration

All available databases were listed using:

SHOW DATABASES;

Among the available databases, an interesting database named:

htb

was discovered.

The database was selected:

USE htb;
Phase 6: Table Enumeration

Tables within the selected database were identified.

SHOW TABLES;
Discovered Tables
config
users
Phase 7: Data Extraction

The contents of the configuration table were reviewed.

SELECT * FROM config;
Result

The table contained application configuration data and the target flag required for completing the challenge.

Key Skills Demonstrated
Network Reconnaissance
Service Enumeration
Database Enumeration
MariaDB Assessment
SQL Querying
Linux Command Line
Vulnerability Assessment Methodology
Information Gathering
Capture The Flag (CTF) Investigation
Conclusion

The assessment successfully identified an exposed MariaDB service running on TCP port 3306. Through systematic enumeration, database access was established, privileges were verified, and available databases and tables were explored. The investigation ultimately led to the discovery of sensitive information within the configuration table, demonstrating the importance of restricting database exposure and enforcing proper access controls.

This case study showcases practical experience in reconnaissance, service enumeration, and database investigation techniques commonly used during penetration testing and security assessments.
