import os
import socket
import time

print("HEY")
time.sleep(10)
msgFromClient = "Hello UDP Server"

bytesToSend = str.encode(msgFromClient)

serverAddressPort = (socket.gethostbyname(os.environ.get("HOST","127.0.0.1")), int(os.environ.get("PORT",12345)))

bufferSize = 1024

# Create a UDP socket at client side

print("Started")

UDPClientSocket = socket.socket(family=socket.AF_INET, type=socket.SOCK_DGRAM)

print("Socket created")
# Send to server using created UDP socket

UDPClientSocket.sendto(bytesToSend, serverAddressPort)

print("Message sent")

msgFromServer = UDPClientSocket.recvfrom(bufferSize)

msg = "Message from Server {}".format(msgFromServer[0])

print(msg)