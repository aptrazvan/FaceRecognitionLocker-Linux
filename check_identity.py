import face_recognition
import numpy as np
import socket
import sys
import os
import time


def check_photo_identity(identity_path, capture_path):
    try:
        picture_of_me = face_recognition.load_image_file(identity_path)
        my_face_encoding = face_recognition.face_encodings(picture_of_me)[0]

        unknown_picture = face_recognition.load_image_file(capture_path)
        unknown_face_encoding = face_recognition.face_encodings(unknown_picture)[0]
    except:
        return False

    results = face_recognition.compare_faces([my_face_encoding], unknown_face_encoding)

    return results[0]

#print(check_photo_identity('sample.bmp', 'Trust.bmp'))
# Create a UDP socket
s = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
# Bind the socket to the port
server_address = ('192.168.1.105', 50001)
s.bind(server_address)
send_data = "Passed"
index = 0

while True:
    while os.path.exists(str(index) + '.bmp') == False:
        pass

    if index % 5 == 0:
        result = False

    time.sleep(1)

    if result == False:
        result = check_photo_identity(str(index) + '.bmp', 'Trust.bmp')

    print(result)

    if result == True:
        s.sendto(send_data.encode('utf-8'), ('192.168.1.45', 8888))

    index += 1
