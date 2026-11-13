#!/usr/bin/env python3
import sys
import time
import urllib.request
import json
import socket
import ipaddress

R = "\033[1;31m"
G = "\033[1;32m"
Y = "\033[1;33m"
B = "\033[1;34m"
C = "\033[1;36m"
W = "\033[1;37m"

def banner():
    print(f"""{C}
  _  _                 ___   ___ ___ _  _ _____ 
 | \| |___ ___ _  _   / _ \ / __/ __| \| |_   _|
 | .` / -_)_-< || | | (_) | (__\__ \ .` | | |  
 |_|\_\___/__/\_,_|  \___/ \___|___/_|\_| |_|  
    {W}[ Ultimate Non-Root Mobile OSINT Suite v2.5 ]{C}
    {Y}[+] Coded by: Raj (Raj Cyber Security){C}
    {Y}[+] GitHub: github.com/nilamanibawa-ops{W}
    """)

def username_checker():
    print(f"\n{Y}[*] Enter Target Username to Scan across Platforms:{W} ", end="")
    uname = input().strip()
    if not uname:
        print(f"{R}[!] Username cannot be empty!{W}")
        return

    platforms = {
        "Instagram": f"https://www.instagram.com/{uname}/",
        "GitHub": f"https://github.com/{uname}",
        "Twitter/X": f"https://twitter.com/{uname}",
        "Facebook": f"https://www.facebook.com/{uname}",
        "TikTok": f"https://www.tiktok.com/@{uname}",
        "Pinterest": f"https://www.pinterest.com/{uname}/",
        "Telegram": f"https://t.me/{uname}",
        "Reddit": f"https://www.reddit.com/user/{uname}",
        "Steam": f"https://steamcommunity.com/id/{uname}",
        "Twitch": f"https://www.twitch.tv/{uname}",
        "Medium": f"https://medium.com/@{uname}",
        "Spotify": f"https://open.spotify.com/user/{uname}",
        "LinkedIn": f"https://www.linkedin.com/in/{uname}"
    }

    print(f"\n{G}[+] Scanning digital footprints for: {B}{uname}{W}\n")
    headers = {'User-Agent': 'Mozilla/5.0 (Linux; Android 10)'}
    found_count = 0
    for platform, url in platforms.items():
        try:
            req = urllib.request.Request(url, headers=headers)
            with urllib.request.urlopen(req, timeout=4) as response:
                if response.status == 200:
                    print(f"  {G}[FOUND] {W}{platform:<15} ➔ {C}{url}{W}")
                    found_count += 1
        except Exception:
            pass
        time.sleep(0.2)
    print(f"\n{Y}[+] Scan completed! Found on {G}{found_count}{Y} platforms.{W}")

def domain_recon():
    print(f"\n{Y}[*] Enter Domain or IP (e.g., google.com or 8.8.8.8):{W} ", end="")
    target = input().strip()
    if not target:
        print(f"{R}[!] Target cannot be empty!{W}")
        return

    print(f"\n{G}[+] Gathering Network Intelligence for: {B}{target}{W}")
    try:
        ip_addr = socket.gethostbyname(target)
        print(f"  {G}[Resolved IP]  ➔ {W}{ip_addr}")
        
        if ipaddress.ip_address(ip_addr).is_private:
            print(f"  {Y}[Info]         ➔ This is a Private/Local or CGNAT IP. Public location is not applicable.{W}")
            return

        url = f"http://ip-api.com/json/{ip_addr}"
        req = urllib.request.Request(url, headers={'User-Agent': 'Mozilla/5.0'})
        with urllib.request.urlopen(req, timeout=5) as response:
            data = json.loads(response.read().decode())
            if data.get('status') == 'success':
                print(f"  {G}[ISP]          ➔ {W}{data.get('isp', 'N/A')}")
                print(f"  {G}[Country]      ➔ {W}{data.get('country', 'N/A')}")
                print(f"  {G}[Region]       ➔ {W}{data.get('regionName', 'N/A')}")
                print(f"  {G}[City]         ➔ {W}{data.get('city', 'N/A')}")
                print(f"  {G}[Timezone]     ➔ {W}{data.get('timezone', 'N/A')}")
            else:
                print(f"{R}[!] Failed to fetch location details via free API.{W}")
    except Exception as e:
        print(f"{R}[!] Error resolving target: {e}{W}")

def main_menu():
    while True:
        banner()
        print(f"{W}1. {C}Massive Username OSINT Scanner")
        print(f"2. {C}Advanced Domain & IP Geo-Intelligence")
        print(f"3. {R}Exit{W}")
        print(f"\n{Y}Select an option [1-3]:{W} ", end="")
        
        choice = input().strip()
        if choice == '1':
            username_checker()
            input(f"\n{Y}Press Enter to return to menu...{W}")
        elif choice == '2':
            domain_recon()
            input(f"\n{Y}Press Enter to return to menu...{W}")
        elif choice == '3':
            print(f"\n{G}[+] Thank you for using Nexus-OSINT by Raj. Goodbye!{W}\n")
            break
        else:
            print(f"{R}[!] Invalid option!{W}")
            time.sleep(1)

if __name__ == "__main__":
    try:
        main_menu()
    except KeyboardInterrupt:
        sys.exit(0)
