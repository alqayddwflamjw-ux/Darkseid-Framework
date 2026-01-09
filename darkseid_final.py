import os
import subprocess
import time

def banner():
    # شعار ASCII Art مخصص لـ Darkseid
    print("""\033[1;31m
    ██████╗  █████╗ ██████╗ ██╗  ██╗███████╗███████╗██╗██████╗ 
    ██╔══██╗██╔══██╗██╔══██╗██║ ██╔╝██╔════╝██╔════╝██║██╔══██╗
    ██║  ██║███████║██████╔╝█████╔╝ ███████╗█████╗  ██║██║  ██║
    ██║  ██║██╔══██║██╔══██╗██╔═██╗ ╚════██║██╔══╝  ██║██║  ██║
    ██████╔╝██║  ██║██║  ██║██║  ██╗███████║███████╗██║██████╔╝
    ╚═════╝ ╚═╝  ╚═╝╚═╝  ╚═╝╚═╝  ╚═╝╚══════╝╚══════╝╚═╝╚═════╝
           >> THE ULTIMATE STEALTH FRAMEWORK <<
    \033[0m""")

def check_stealth():
    """التأكد من أن نظام التخفي جاهز"""
    print("\033[1;34m[*] Verifying Darkseid Stealth Shield...\033[0m")
    # التحقق من وجود proxychains
    if subprocess.getstatusoutput("which proxychains4")[0] != 0:
        print("[!] Proxychains4 is missing! Installing...")
        os.system("pkg install proxychains-ng -y")
    
    # التحقق من عمل Tor
    status = subprocess.getoutput("pgrep -x tor")
    if not status:
        print("\033[1;33m[!] Tor Shield Offline. Activating...\033[0m")
        os.system("tor > /dev/null 2>&1 &")
        time.sleep(2) # انتظار التشغيل
        print("\033[1;32m[+] Tor Shield: ACTIVE\033[0m")
    else:
        print("\033[1;32m[+] Tor Shield: ONLINE\033[0m")

def run_cmd(cmd):
    check_stealth()
    # تشغيل الأمر عبر proxychains لتأمين الاتصال
    os.system(f"proxychains4 -q {cmd}")

def menu():
    banner()
    print(f"\033[1;37m[1] Nmap Vulnerability Scan (Stealth Mode)")
    print(f"[2] Impulse DoS Attack (Flood Target)")
    print(f"[3] Launch Metasploit (Dark Console)")
    print(f"[4] Exit Darkseid Framework\033[0m")

def main():
    while True:
        menu()
        choice = input("\n\033[1;31mDarkseid@Termux:~# \033[0m")
        
        if choice == '1':
            target = input("[+] Enter Target IP: ")
            run_cmd(f"nmap -sT -Pn -sV --script vuln {target}")
        elif choice == '2':
            target = input("[+] Enter Target IP:Port : ")
            threads = input("[+] Threads (default 500): ") or "500"
            run_cmd(f"python3 impulse.py --target {target} --method UDP --time 3600 --threads {threads}")
        elif choice == '3':
            run_cmd("msfconsole")
        elif choice == '4':
            print("\033[1;31mExiting... The Shadows remain.\033[0m")
            break
        else:
            print("[!] Invalid selection.")

if __name__ == "__main__":
    main()
  
