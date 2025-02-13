# Video Steganography Deployment  
A secure **video steganography tool** for embedding and extracting hidden messages in video files.

## 🔍 Features  
✅ **Securely hide text in video files**  
✅ **Extract hidden messages**  
✅ **Lossless encoding & decoding**  
✅ **Lightweight and fast Python implementation**  

## 🚀 How It Works  
1️⃣ **Embed a secret message into a video**  
2️⃣ **Send the video securely**  
3️⃣ **Extract the message using a key**  

## 🛠 Dependencies  
Install required libraries:  
```bash
pip install opencv-python numpy
```
## 🔹Usage
🔹 **Embed a Secret Message**
```
python scripts/embed_message.py -i sample_video.mp4 -m secret_message.txt -o steg_video.mp4
```
🔹 **Extract the Hidden Message**
```
python scripts/extract_message.py -i steg_video.mp4 -o extracted_message.txt
```
