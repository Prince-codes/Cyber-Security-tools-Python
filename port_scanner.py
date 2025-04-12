import socket
import threading

print("== Simple Port Scanner == \n By- Carnage Sentinels\n")

# Input target domain or IP
target = input("Enter target (e.g. example.com or 192.168.1.1): ")

# Port range
start_port = int(input("Start Port: "))
end_port = int(input("End Port: "))

# Try to resolve IP
try:
    target_ip = socket.gethostbyname(target)
    print(f"[+] Target IP: {target_ip}")
except socket.gaierror:
    print("[-] Could not resolve hostname.")
    exit()

print(f"[+] Scanning ports {start_port}-{end_port}...\n")

# Lock to prevent print overlap
print_lock = threading.Lock()

def scan_port(port):
    try:
        s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        s.settimeout(1)  # short timeout for quick scan
        result = s.connect_ex((target_ip, port))
        if result == 0:
            with print_lock:
                print(f"[OPEN] Port {port}")
        s.close()
    except Exception:
        pass

# Launch threads
for port in range(start_port, end_port + 1):
    t = threading.Thread(target=scan_port, args=(port,))
    t.start()
