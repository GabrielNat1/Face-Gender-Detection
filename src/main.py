import cv2
import os
from deepface import Deepface

face_cascade = cv2.CascadeClassifier(cv2.data.haarcascades + 'haarcascade_frontalface_default.xml')

def detect_gender(image_path):
    img = cv2.imread(image_path)
    gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)

    faces = face_cascade.detectMultiScale(gray, 1.1, 4)
    
    for (x, y, w, h) in faces:
        face = img[y:y+h, x:x+w]
        result = DeepFace.analyze(face, actions=['gender'])
        gender = result[0]['gender']
        print(f'Image: {image_path} -> Detected gender: {gender}')
        cv2.rectangle(img, (x, y), (x+w, y+h), (0, 255, 0), 2)
        cv2.putText(img, f'Gender: {gender}', (x, y-10), cv2.FONT_HERSHEY_SIMPLEX, 0.9, (0, 255, 0), 2)

    cv2.imwrite(f'output_{os.path.basename(image_path)}', img)
    cv2.imshow('Image with Detected Gender', img)
    cv2.waitKey(0)
    cv2.destroyAllWindows()

def process_folder(folder_path):
    files = [f for f in os.listdir(folder_path) if f.lower().endswith(('.png', '.jpg', '.jpeg'))]

    for file in files:
        image_path = os.path.join(folder_path, file)
        detect_gender(image_path)

folder_path = '../imgs/'
process_folder(folder_path)
