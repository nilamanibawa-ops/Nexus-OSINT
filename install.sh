#!/bin/bash
echo -e "\033[1;32m[+] Installing dependencies for Nexus-OSINT...\033[1;37m"
pkg update -y && pkg upgrade -y
pkg install python -y
chmod +x nexus.py
echo -e "\033[1;32m[+] Installation Complete! Run tool using: python3 nexus.py\033[1;37m"
