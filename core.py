#!/usr/bin/env python3
import argparse
from modules import whois, dns, geoip, http, scanner, social
from utils import banner

def main():
    parser = argparse.ArgumentParser(description="Atlas - Info Gathering Tool")
    parser.add_argument("-t", "--target", help="Target domain/IP/username", required=True)
    parser.add_argument("-m", "--module",
                        help="Module (whois, dns, geoip, http, scanner, social)",
                        required=True)
    parser.add_argument("--ports", help="Ports for scanner (comma separated)", default="22,80,443")
    args = parser.parse_args()

    banner.show_banner()

    mod = args.module.lower()
    tgt = args.target

    if mod == "whois":
        whois.lookup(tgt)
    elif mod == "dns":
        dns.lookup(tgt)
    elif mod == "geoip":
        geoip.lookup(tgt)
    elif mod == "http":
        http.headers(tgt)
    elif mod == "scanner":
        ports = [int(p.strip()) for p in args.ports.split(",") if p.strip().isdigit()]
        scanner.scan(tgt, ports)
    elif mod == "social":
        social.username_check(tgt)
    else:
        print("[!] Unknown module. Use: whois, dns, geoip, http, scanner, social")

if __name__ == "__main__":
    main()

