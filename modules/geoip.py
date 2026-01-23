import requests, socket
from utils import colors

def lookup(target):
    print(colors.cyan("[GEOIP]"))
    try:
        ip = socket.gethostbyname(target)
        resp = requests.get(f"https://ipinfo.io/{ip}/json", timeout=5)
        data = resp.json()
        print(colors.green(f"IP: {ip}"))
        print(colors.yellow(f"Country: {data.get('country')}"))
        print(colors.blue(f"Region: {data.get('region')}"))
        print(colors.magenta(f"City: {data.get('city')}"))
        print(colors.red(f"Org/ASN: {data.get('org')}"))
    except Exception as e:
        print(colors.red(f"[!] GeoIP failed: {e}"))
