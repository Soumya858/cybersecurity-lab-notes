import argparse
import socket
import secrets
import string
import hashlib
import json
from concurrent.futures import ThreadPoolExecutor


def generate_password(length):
    chars = string.ascii_letters + string.digits + string.punctuation
    return ''.join(secrets.choice(chars) for _ in range(length))


def scan_port(target, port):
    try:
        s = socket.socket()
        s.settimeout(0.5)
        if s.connect_ex((target, port)) == 0:
            s.close()
            return port
        s.close()
    except:
        pass
    return None


def port_scanner(target):
    open_ports = []
    with ThreadPoolExecutor(max_workers=100) as executor:
        results = executor.map(lambda p: scan_port(target, p), range(1, 1025))
    for port in results:
        if port:
            open_ports.append(port)
    return open_ports


def hash_text(text):
    return {
        "MD5": hashlib.md5(text.encode()).hexdigest(),
        "SHA256": hashlib.sha256(text.encode()).hexdigest()
    }


def save_report(data):
    with open("report.json", "w") as f:
        json.dump(data, f, indent=4)


def main():
    parser = argparse.ArgumentParser(description="Cyber Toolkit Pro")
    parser.add_argument("--scan", help="Scan target (IP or domain)")
    parser.add_argument("--password", type=int, help="Generate password length")
    parser.add_argument("--hash", help="Generate hash for text")
    args = parser.parse_args()

    report = {}

    if args.scan:
        print(f"Scanning {args.scan}...")
        ports = port_scanner(args.scan)
        print("Open Ports:", ports)
        report["scan"] = {"target": args.scan, "open_ports": ports}

    if args.password:
        pwd = generate_password(args.password)
        print("Generated Password:", pwd)
        report["password"] = pwd

    if args.hash:
        hashes = hash_text(args.hash)
        print("Hashes:", hashes)
        report["hash"] = hashes

    if report:
        save_report(report)
        print("Report saved to report.json")


if __name__ == "__main__":
    main()
