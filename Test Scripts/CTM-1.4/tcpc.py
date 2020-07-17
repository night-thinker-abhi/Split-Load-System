import socket
import sys
import os
import tqdm

SEPARATOR = "<SEPARATOR>"
BUFFER_SIZE = 4096
host = "192.168.43.78"
port = 5001
filename = "Dynamic Prog.pdf"
filesize = os.path.getsize(filename)
s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
print(f"[+] Connecting to {host}:{port}")
s.connect((host, port))
print("[+] Connected.")
s.sendall(f"{filename}{SEPARATOR}{filesize}".encode())
# progress = tqdm.tqdm(range(filesize), f'Sending {filename}', unit='B', unit_scale=True, unit_divisor=1024)
with open(filename, "rb") as f:
    while True:
        bytes_read = f.read(BUFFER_SIZE)
        if not bytes_read:
            # file transmitting is done
            print("File Sent.")
            exit(0)
        s.sendall(bytes_read)
        # progress.update(len(bytes_read))

s.close()