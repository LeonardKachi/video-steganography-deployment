import cv2

def extract_message(video_path, output_path):
    cap = cv2.VideoCapture(video_path)
    
    binary_message = ''
    while cap.isOpened():
        ret, frame = cap.read()
        if not ret:
            break
        
        binary_message += format(frame[0, 0, 0], '08b')[-1]
        
        if binary_message[-16:] == '1111111111111110':
            break
    
    cap.release()
    
    message = ''.join(chr(int(binary_message[i:i+8], 2)) for i in range(0, len(binary_message)-16, 8))
    
    with open(output_path, 'w') as f:
        f.write(message)
    
    print("Hidden message extracted successfully!")

extract_message("steg_video.mp4", "extracted_message.txt")




















