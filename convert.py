import os

index = 0
width = 240
height = 320

# header bytes for the bmp files
header = bytearray(b'\x42\x4d\x00\x03\x84\x36\x00\x00\x00\x00\x36\x00\x00\x00\x28\x00\x00\x00\xf0\x00\x00\x00\x40\x01\x00\x00\x01\x00\x18\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00')

while True:
    # wait for the input file to be created
    while os.path.exists(str(index) + '.txt') == False:
        pass
    
    input_file = open(str(index) + '.txt', 'rb')
    output_file = open(str(index) + '.bmp', 'wb')
    output_file.write(header)

    image = []
    for x in range(height):
        image.append([])

    # transpose the image
    for y in range(width):
        for x in range(height):
            image[x].append(input_file.read(1))

    # write the rgb values for each pixel
    for line in image:
        for pixel in line:
            output_file.write(pixel)
            output_file.write(pixel)
            output_file.write(pixel)

    output_file.close()
    input_file.close()

    index += 1
