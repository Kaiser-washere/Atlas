import subprocess
from utils import colors

def username_check(username):
    print(colors.cyan("[SOCIAL USERNAME CHECK - Ruby]"))
    try:
        out = subprocess.check_output(
            ["ruby", "./native/scraper.rb", username],
            stderr=subprocess.STDOUT,
            timeout=10
        ).decode().strip()
        for line in out.splitlines():
            # Example line: "github: found (200)"
            if "(" in line and ")" in line:
                code_str = line.split("(")[-1].strip(")")
                try:
                    code = int(code_str)
                except ValueError:
                    code = None
            else:
                code = None

            if code == 200:
                print(colors.green(line))
            elif code in [403, 404]:
                print(colors.red(line))
            else:
                print(colors.yellow(line))
    except Exception as e:
        print(colors.red(f"[!] Social check failed: {e}"))
