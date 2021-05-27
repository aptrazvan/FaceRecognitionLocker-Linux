import os

def convert_files():
    index = 0

    while True:
        while os.path.exists(str(index) + '.txt') == False:
            pass

        
        input_file = open(str(index) + '.txt', 'rb')

        header = bytearray(b'\x42\x4d\x00\x03\x84\x36\x00\x00\x00\x00\x36\x00\x00\x00\x28\x00\x00\x00\xf0\x00\x00\x00\x40\x01\x00\x00\x01\x00\x18\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00')

        output_file = open(str(index) + '.bmp', 'wb')
        output_file.write(header)

        image = []

        for x in range(320):
            image.append([])

        for y in range(240):
            for x in range(320):
                image[x].append(input_file.read(1))

        for line in image:
            for pixel in line:
                output_file.write(pixel)
                output_file.write(pixel)
                output_file.write(pixel)
        output_file.close()
        input_file.close()

        index += 1
 
def convert():
    index = 0
    input_file = open('received.log', 'rb')
    while True:
        header = bytearray(b'\x42\x4d\x00\x03\x84\x36\x00\x00\x00\x00\x36\x00\x00\x00\x28\x00\x00\x00\xf0\x00\x00\x00\x40\x01\x00\x00\x01\x00\x18\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00')

        output_file = open(str(index) + '.bmp', 'wb')
        output_file.write(header)

        image = []

        for x in range(320):
            image.append([])

        for y in range(240):
            for x in range(320):
                image[x].append(input_file.read(1))

        for line in image:
            for pixel in line:
                output_file.write(pixel)
                output_file.write(pixel)
                output_file.write(pixel)
        output_file.close()

        index += 1


convert_files()

