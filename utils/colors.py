from colorama import Fore, Style, init
init(autoreset=True)

def green(text): return f"{Fore.GREEN}{text}{Style.RESET_ALL}"
def red(text): return f"{Fore.RED}{text}{Style.RESET_ALL}"
def yellow(text): return f"{Fore.YELLOW}{text}{Style.RESET_ALL}"
def blue(text): return f"{Fore.BLUE}{text}{Style.RESET_ALL}"
def cyan(text): return f"{Fore.CYAN}{text}{Style.RESET_ALL}"
def magenta(text): return f"{Fore.MAGENTA}{text}{Style.RESET_ALL}"
