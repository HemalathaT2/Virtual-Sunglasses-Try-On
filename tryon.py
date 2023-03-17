import os

import cvzone
import cv2
from cvzone.PoseModule import PoseDetector

cap = cv2.VideoCapture("Resources/Videos/1.mp4")
detector = PoseDetector()

shirtFolderPath = "Resources/Shirts"
listShirts = os.listdir(shirtFolderPath)
fixedRatio = 83 / 15
shirtRatioHeightWidth = 140/180
#print(listShirts)
while True:
    success, img = cap.read()
    img = detector.findPose(img)
    #img = cv2.flip(img,1)
    lmList, bboxInfo = detector.findPosition(img, bboxWithHands=False, draw=False)
    
    if lmList:
        #print(lmList[7][1:3])
        # center = bboxInfo["center"]
        lm11 = lmList[6][1:3]
        lm12 = lmList[4][1:3]
        widthOfShirt = int((lm12[0] - lm11[0]) * fixedRatio)
        imgShirt = cv2.imread(os.path.join(shirtFolderPath, listShirts[0]), cv2.IMREAD_UNCHANGED)
        
        print(widthOfShirt)
        imgShirt = cv2.resize(imgShirt, (widthOfShirt, int(widthOfShirt * shirtRatioHeightWidth)))
        try:
            img = cvzone.overlayPNG(img, imgShirt, lm11)
        except:
            pass


    cv2.imshow("Image", img)
    cv2.waitKey(1)
