import socket
import sys

def convert(data, index):
    header = bytearray(b'\x42\x4d\x00\x03\x84\x36\x00\x00\x00\x00\x36\x00\x00\x00\x28\x00\x00\x00\xf0\x00\x00\x00\x40\x01\x00\x00\x01\x00\x18\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00')

    output_file = open(str(index) + '.bmp', 'wb')
    output_file.write(header)

    image = []

    for x in range(320):
        image.append([])

    for y in range(240):
        for x in range(320):
            image[x].append(data[y * 240 + x])

    for line in image:
        for pixel in line:
            output_file.write(pixel)
            output_file.write(pixel)
            output_file.write(pixel)
    
    output_file.close()

# Create a UDP socket
s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
# Bind the socket to the port
server_address = ('192.168.1.105', 50000)
s.bind(server_address)
s.listen(5)
connection,address = s.accept()
index = 0
print("Do Ctrl+c to exit the program !!")

while True:
    print("####### Server is listening #######")
    data = connection.recv(5)

    if data == 'Ready':
        data = connection.recv(76800)
        convert(data)
        index += 1;
        print("\n\n 2. Server received: ", data, "\n\n")
