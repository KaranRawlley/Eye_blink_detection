from scipy.spatial import distance as dist
import cv2
import imutils
from imutils import face_utils
import numpy as np
import dlib


def EAR(eye):
    # distance between 2 set if vertical landmarks (x,y)-coordinates
    A = dist.euclidean(eye[1], eye[5])
    B = dist.euclidean(eye[2], eye[4])
    # horizontal distance
    C = dist.euclidean(eye[0], eye[3])

    # computing EAR
    ear = (A+B)/(2.0*C)
    return ear


# defining 2 constants first as a Threshold EAR
# other for number of consecutive frames the eye must be beliow the threshold
EAR_thresh = 0.1899
EAR_consec_frames = 2

counter = 0
total = 0

# dlib's face detector
detector = dlib.get_frontal_face_detector()\
    # dlib's facial landmarks detector
predictor = dlib.shape_predictor("shape_predictor_68_face_landmarks.dat")


# geting the landmarks of lef and right eye resp.
(lStart, lEnd) = face_utils.FACIAL_LANDMARKS_IDXS['left_eye']
(rStart, rEnd) = face_utils.FACIAL_LANDMARKS_IDXS['right_eye']

cap = cv2.VideoCapture(0)
while True:
    check, frame = cap.read()
   # frame = imutils.resize(frame, width=400)
    gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
    rects = detector(gray, 0)

    for rect in rects:
        shape = predictor(gray, rect)
        shape = face_utils.shape_to_np(shape)

        # extract eye coordinates
        leftEye = shape[lStart:lEnd]
        rightEye = shape[rStart:rEnd]
        leftEAR = EAR(leftEye)
        rightEAR = EAR(rightEye)

        #average EAR
        ear = (leftEAR + rightEAR)/2.0
        #print(ear)

        leftEyeHull = cv2.convexHull(leftEye)
        rightEyeHull = cv2.convexHull(rightEye)
        cv2.drawContours(frame, [leftEyeHull], -1, (0, 255, 0), 1)
        cv2.drawContours(frame, [rightEyeHull], -1, (0, 255, 0), 1)

        if ear < EAR_thresh:
            counter += 1
        else:

            if counter >= EAR_consec_frames:
                total += 1
                print(total)
                counter = 0

    cv2.imshow('Capturing', frame)
    k = cv2.waitKey(1)
    if k == ord('q'):
        break
cap.release()
cv2.destroyAllWindows()
 