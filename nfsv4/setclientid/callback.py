import socket
import time

reply1 = b'\x80\x00\x00\x18'
reply2 = b'\x00\x00\x00\x01\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00'

TCP_IP = '192.168.56.1'
TCP_PORT = 34393
BUFFER_SIZE = 1024  # Normally 1024, but we want fast response

s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
s.bind((TCP_IP, TCP_PORT))
s.listen(1)

while True:
    conn, addr = s.accept()
    print('Connection address:', addr)
    while True:
       data = conn.recv(BUFFER_SIZE)
       if not data: break
       print("received data:", data)
       time.sleep(0)
       conn.send(reply1 + data[4:8] + reply2)
    conn.close()