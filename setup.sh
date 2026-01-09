#!/bin/bash
pkg update && pkg upgrade -y
pkg install python nmap metasploit git -y
pip install -r requirements.txt
chmod +x darkseid.py
echo "Installation Complete. Run 'python darkseid.py'"
