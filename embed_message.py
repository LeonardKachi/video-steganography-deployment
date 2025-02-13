import cv2
import numpy as np

def embed_message(video_path, message_path, output_path):
    cap = cv2.VideoCapture(video_path)
    fourcc = cv2.VideoWriter_fourcc(*'XVID')
    out = cv2.VideoWriter(output_path, fourcc, 30, (int(cap.get(3)), int(cap.get(4))))
    
    with open(message_path, 'r') as f:
        message = f.read()
    
    binary_message = ''.join(format(ord(i), '08b') for i in message) + '1111111111111110'
    
    frame_idx = 0
    bit_idx = 0
    while cap.isOpened():
        ret, frame = cap.read()
        if not ret:
            break
        
        if bit_idx < len(binary_message):
            frame[0, 0, 0] = int(format(frame[0, 0, 0], '08b')[:-1] + binary_message[bit_idx], 2)
            bit_idx += 1
        
        out.write(frame)
        frame_idx += 1
    
    cap.release()
    out.release()
    print("Message embedded successfully in", output_path)

embed_message("sample_video.mp4", "secret_message.txt", "steg_video.mp4")

