import whois
from utils import colors

def lookup(target):
    print(colors.cyan("[WHOIS]"))
    try:
        w = whois.whois(target)
        print(colors.green(f"Domain: {target}"))
        print(colors.yellow(f"Registrar: {w.registrar}"))
        print(colors.blue(f"Creation Date: {w.creation_date}"))
        print(colors.red(f"Expiration Date: {w.expiration_date}"))
    except Exception as e:
        print(colors.red(f"[!] WHOIS lookup failed: {e}"))
