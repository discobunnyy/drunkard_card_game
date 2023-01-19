import cv2
import numpy as np
import os

path = 'cards'
orb = cv2.ORB_create(nfeatures = 1000)
images = []
classNames = []
myList = os.listdir(path)
print('Total Classes Detected', len(myList))
for cl in myList:
    imgCur = cv2.imread(f'{path}/{cl}',0)
    images.append(imgCur)
    classNames.append(os.path.splitext(cl)[0])
print(classNames)

def findDes(images):
    desList = []
    for img in images:
        kp, des = orb.detectAndCompute(img, None)
        desList.append(des)
    return desList

def findID(img, desList):
    kp2, des2 = orb.detectAndCompute(img, None)
    bf = cv2.BFMatcher()
    matchList = []
    finalVal = -1
    for des in desList:
        matches = bf.knnMatch(des, des2, k=2)
        good = []
        for m, n in matches:
            if m.distance < 0.75 * n.distance:
                good.append([m])
        matchList.append(len(good))
    print(matchList)


desList = findDes(images)
print(len(desList))


cap = cv2.VideoCapture(0)

while True:
    success, img2 = cap.read()
    imgOriginal = img2.copy()
    img2 = cv2.cvtColor(img2, cv2.COLOR_BGR2GRAY)
    findID(img2, desList)
    '''id = findID(img2, desList)
    if id != -1:
        cv2.putText (imgOriginal, classNames[id], (50,50), cv2.FONT_HERSHEY_COMPLEX, 1, (0,0,255), 2)
'''
    cv2.imshow('img2', imgOriginal)
    cv2.waitKey(1)


'''main_image = cv2.imread('card.png')
while True:
    gray_main_image = cv2.cvtColor(main_image, cv2.COLOR_BGR2GRAY)
    id = findID(gray_main_image, desList)
    if id != -1:
        cv2.putText(main_image, classNames[id], (50,50), cv2.FONT_HERSHEY_COMPLEX, 1, (0,0,255), 1)

    cv2.imshow('img2', main_image)'''
