Enumeration Checklist

Network Enumeration
- Scan open ports using Nmap
- Identify services running on ports

Web Enumeration
- Check directories and hidden endpoints
- Analyze forms and input fields
- Perform directory brute-forcing using Gobuster

Gobuster Usage
- Used Gobuster to discover hidden directories and files on web servers
- Helps identify admin panels, login pages, and sensitive endpoints

Example:
gobuster dir -u http://example.com -w wordlist.txt

Key Learning
Enumeration is the most important step in penetration testing, as it helps uncover hidden attack surfaces.

Practiced using Gobuster on safe lab environments and authorized targets only.
