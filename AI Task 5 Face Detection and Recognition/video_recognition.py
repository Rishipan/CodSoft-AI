import cv2

# loding pre-trained face detection model
face_cascade = cv2.CascadeClassifier(cv2.data.haarcascades + 'haarcascade_frontalface_default.xml')

def recognize_face(face):
    print("Face recognized!")

# detect and recognize faces in a frame
def detect_and_recognize_faces(frame):
    gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
    faces = face_cascade.detectMultiScale(gray, scaleFactor=1.1, minNeighbors=5, minSize=(30, 30))
    
    for (x, y, w, h) in faces:
        face = frame[y:y+h, x:x+w]
        recognize_face(face)
        # draw rectangle around the face
        cv2.rectangle(frame, (x, y), (x+w, y+h), (255, 0, 0), 2)
    
    return frame

def process_video(video_path):
    # open the video file
    cap = cv2.VideoCapture(video_path)
    
    # check if the video opened successfully
    if not cap.isOpened():
        print("Error: Unable to open video.")
        return
    
    # read and process frames 
    while True:
        ret, frame = cap.read()
        
        if not ret:
            break
        
        # detect and recognize faces in the frame
        processed_frame = detect_and_recognize_faces(frame)
        
        # display the processed frame
        cv2.imshow('Face Detection', processed_frame)
        
        # press 'q' to exit
        if cv2.waitKey(1) & 0xFF == ord('q'):
            break
    
    cap.release()
    cv2.destroyAllWindows()

video_path = 'video.mp4'

process_video(video_path)
