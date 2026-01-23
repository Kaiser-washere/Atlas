import dns.resolver
from utils import colors

def lookup(target):
    print(colors.cyan("[DNS RECORDS]"))
    for rtype in ["A", "AAAA", "MX", "TXT", "NS", "CNAME"]:
        try:
            answers = dns.resolver.resolve(target, rtype)
            for ans in answers:
                print(colors.green(f"{rtype}: {ans.to_text()}"))
        except Exception:
            print(colors.red(f"{rtype}: not found"))
