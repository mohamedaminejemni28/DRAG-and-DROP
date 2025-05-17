#importation 
import cv2
import cvzone
from cvzone.HandTrackingModule import HandDetector
import math


handdetector=HandDetector()

video=cv2.VideoCapture(0)
    
colorr=(288,0,0)

pt8x,pt8y=0,0
cx,cy,w,h=100,100,100,100
while True:
    
    ret,image=video.read()
    image=cv2.flip(image,1)
    resultat=handdetector.findHands(image,draw=True)
    if len(resultat[0])>0:

       #lmlist,_detector.findposition(image)
        
        landmarks=resultat[0][0]['lmList']
        pt8x,pt8y=landmarks[8][0],landmarks[8][1]
        pt12x,pt12y=landmarks[12][0],landmarks[12][1]

        length=math.hypot(pt12x-pt8x,pt12y-pt12y)

        #cv2.line(image,[pt12x,pt12y],[pt8x,pt8y],(255,0,0))

        
        for i in range(5):
           

         cv2.rectangle(image,(cx-w//2,cy-h),(cx+w//2,cy+h//2),colorr,cv2.FILLED)
       

        distance=handdetector.findDistance((pt8x,pt8y),(pt12x,pt12y))[0]
        print('distance=',distance)
        cursor=landmarks[8]
        if distance>30:


        
         if cx-w//2<cursor[0]<cx+w//2 and \
            cy-h//2<cursor[1]<cy+h//2:
            colorr=(255,255,0)
            cx,cy=landmarks[8][0],landmarks[8][1]
         else:

            colorr=(288,0,0)
        
        cv2.rectangle(image,(cx-w//2,cy-h),(cx+w//2,cy+h//2),colorr,cv2.FILLED)










    cv2.imshow('Video', image)
    if cv2.waitKey(50) == ord('a'):  # Quitter avec la touche 'a'
        break














    


# Load the video
video_path = 'input_video/test2.mp4'
cap = cv2.VideoCapture(video_path)

# Check if the video is loaded properly
if not cap.isOpened():
    print("Error: Unable to load the video.")
    exit()

# Set a frame skipping parameter
frame_skip = 2  # Process every 2nd frame (increase for faster playback)
frame_count = 0

while True:
    ret, frame = cap.read()
    if not ret:
        print("End of the video.")
        break

    frame_count += 1

    # Skip frames to increase playback speed
    if frame_count % frame_skip != 0:
        continue

    # Resize the frame to reduce processing time
    resized_frame = cv2.resize(frame, (640, 360))  # Lower resolution for speed

    # Perform predictions on the current frame
    results = model.predict(source=resized_frame, show=False)  # Disable built-in display

    # Annotate the frame with detection results
    annotated_frame = results[0].plot()  # Add detection boxes to the frame

    # Display the video with annotations
    cv2.imshow('Video', annotated_frame)

    # Reduce delay for faster playback
    if cv2.waitKey(1) == ord('a'):  # Use minimal delay (1 ms)
        break

# Release resources
cap.release()
cv2.destroyAllWindows()
