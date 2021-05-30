import socket
import sys
import os

# cleans the previously stored files
def remove_files():
    index = 0

    while os.path.exists(str(index) + '.txt') == True:
        os.remove(str(index) + '.txt')
        os.remove(str(index) + '.bmp')
        index += 1

remove_files()

# create a UDP socket
s = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
# bind the socket to the port
server_address = ('192.168.1.105', 50000)
s.bind(server_address)
index = 0
data = bytearray()

while True:
    # receive chunks of 1280 bytes
    data += s.recvfrom(1280)[0]
    
    if len(data) == 76800:
        # write the image data to the file
        output_file = open(str(index) + '.txt', 'wb')
        output_file.write(data)
        data = bytearray()
        index += 1;
