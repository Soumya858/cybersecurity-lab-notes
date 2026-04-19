 Nmap Notes

 What is Nmap?
Nmap is a network scanning tool used to discover hosts and services on a network.

Common Commands

Scan a target
nmap <target-ip>

Service version detection
nmap -sV <target-ip>

 OS detection
nmap -O <target-ip>

Full scan
nmap -A <target-ip>

Useful Commands (Intermediate)

SYN scan (stealth scan)
nmap -sS <target-ip>

Scan specific ports
nmap -p 80,443 <target-ip>

Scan all ports
nmap -p- <target-ip>

Faster scan
nmap -T4 <target-ip>

Disable host discovery (skip ping)
nmap -Pn <target-ip>

Run default scripts
nmap -sC <target-ip>

Save output to file
nmap -oN scan.txt <target-ip>

Key Learnings
- Identifying open ports
- Understanding running services
- Importance of enumeration in security testing


Example Workflow

1. Discover live hosts
2. Scan open ports
3. Identify services and versions
4. Run scripts for deeper analysis

## Example Workflow

1. Discover live hosts
2. Scan open ports
3. Identify services and versions
4. Run scripts for deeper analysis

Example:
nmap -sC -sV <target-ip>
