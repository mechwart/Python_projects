import cv2
from random import randrange
# Load some pre-trained data on face frontals from opencv (haar cascade algorithm)
trained_face_data = cv2.CascadeClassifier('haarcascade_frontalface_default.xml')

# Choose an image to detect faces in
#img = cv2.imread('DRadcliffe.jpg')
# To capture video from webcam
webcam = cv2.VideoCapture(0)

# To detect faces from video
# webcam = cv2.VideoCapture('video.mp4')


# Iterate forever over frames
while True:
    #### Read the current frame
    successful_frame_read, frame = webcam.read()

    # Must convert to grayscale
    grayscaled_img = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)

    # Detect faces
    face_coordinates = trained_face_data.detectMultiScale(grayscaled_img)

    # Draw rectangles around the faces
    for (x, y, w, h) in face_coordinates:
        cv2.rectangle(frame, (x, y), (x + w, y + h), (randrange(256), randrange(256), randrange(256)), 2)

    # Display the image with the faces
    cv2.imshow('Richard Szilagyi Face Detector', frame)
    key = cv2.waitKey(1)
    ### Stop if you press Q or q break out from the loop
    if key == 81 or key == 113:
        break
### Release the VideoCapture object
webcam.release()

"""
This is for images

# Detect faces
face_coordinates = trained_face_data.detectMultiScale(grayscaled_img)

# Draw rectangles around the faces
for (x,y,w,h) in face_coordinates:
    cv2.rectangle(img,(x, y), (x+w, y+h), (randrange(256), randrange(256), randrange(256)), 2)

# Display the image with the faces
cv2.imshow('Richard Szilagyi Face Detector', img)
cv2.waitKey()
"""
print("Code Completed")
