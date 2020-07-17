import socket
import sys
import os
import tqdm
SERVER_HOST = "0.0.0.0"
SERVER_PORT = 5001
BUFFER_SIZE = 4096
SEPARATOR = "<SEPARATOR>"
s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
s.bind((SERVER_HOST, SERVER_PORT))
s.listen(5)
print(f"[*] Listening as {SERVER_HOST}:{SERVER_PORT}")
client_socket, address = s.accept() 
print(f"[+] {address} is connected.")
received = client_socket.recv(BUFFER_SIZE).decode()
filename, filesize = received.split(SEPARATOR)
filename = os.path.basename(filename)
filesize = int(filesize)
progress = tqdm.tqdm(range(filesize), f'Receiving {filename}', unit='B', unit_scale=True, unit_divisor=1024)

with open(filename, "wb") as f:
	for _ in progress:
		bytes_read = client_socket.recv(BUFFER_SIZE)
		if not bytes_read:    
			exit()
		f.write(bytes_read)
		progress.update(len(bytes_read))

client_socket.close()
s.close()
# print('Waiting for connection')
# num=3
# abc = []
# bcd=[]
# while(num!=0):
# 	num = num-1
# 	connection, client_address = sock.accept()
# 	abc.append(connection)
# 	bcd.append(client_address)
# 	print(client_address,connection)

# print("abc")