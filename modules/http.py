import requests
from utils import colors

def headers(target):
    print(colors.cyan("[HTTP HEADERS]"))
    url = target if target.startswith("http") else f"http://{target}"
    try:
        resp = requests.get(url, timeout=7)
        code = resp.status_code
        if code == 200:
            print(colors.green(f"Status: {code}"))
        elif 300 <= code < 400:
            print(colors.yellow(f"Status: {code}"))
        elif 400 <= code < 500:
            print(colors.red(f"Status: {code}"))
        elif 500 <= code < 600:
            print(colors.magenta(f"Status: {code}"))
        else:
            print(colors.blue(f"Status: {code}"))

        for k, v in resp.headers.items():
            print(colors.yellow(f"{k}: {v}"))
    except Exception as e:
        print(colors.red(f"[!] HTTP request failed: {e}"))
