import subprocess
from utils import colors

def scan(target, ports):
    print(colors.cyan("[PORT SCAN - C++]"))
    port_str = ",".join(str(p) for p in ports)
    try:
        out = subprocess.check_output(
            ["./native/scanner", target, port_str],
            stderr=subprocess.STDOUT,
            timeout=10
        ).decode().strip()
        for line in out.splitlines():
            if "open" in line:
                print(colors.green(line))
            else:
                print(colors.red(line))
    except Exception as e:
        print(colors.red(f"[!] Scanner failed: {e}"))
        print(colors.yellow("[i] Did you build native/scanner? g++ -O2 -std=c++17 native/scanner.cpp -o native/scanner"))
