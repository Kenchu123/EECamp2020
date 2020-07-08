import sys
import cv2

imgPath = sys.argv[1]
outputPath = sys.argv[2]

# Create haar cascade
face_cascade = cv2.CascadeClassifier('haarcascade_frontalface_default.xml')
eye_cascade = cv2.CascadeClassifier('haarcascade_eye.xml')
# Read Image
image = cv2.imread(imgPath)
# Convert the image to gray scale
gray = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)
# Detect face
faces = face_cascade.detectMultiScale(
    gray,                           # gray Image
    scaleFactor = 1.015,            # to compensate big/small face
    minNeighbors = 5,               # objects detected near the current one
    # minSize = (30, 30)            # size of each window of a image
    # flags = cv2.cv.CV_HAAR_SCALE_IMAGE
)

print("Found {0} faces!".format(len(faces)))

if len(faces) > 0:
    # Draw a rectangle around the faces
    for (x, y, w, h) in faces:
        cv2.rectangle(image, (x, y), (x+w, y+h), (0, 255, 0), 2)
        roi_gray = gray[y:y+h, x:x+w] 
        roi_color = image[y:y+h, x:x+w]
        eyes = eye_cascade.detectMultiScale(roi_gray) # detect eye in the face
        for (ex, ey, ew, eh) in eyes:
            cv2.rectangle(roi_color,(ex, ey),(ex+ew, ey+eh), (0, 255, 0), 2)

    # Show Image

    cv2.imshow("Faces found", image)
    cv2.waitKey(0)
    cv2.destroyAllWindows()

    # Save Image