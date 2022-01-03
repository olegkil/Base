import cv2

img = cv2.imread('../images/photo_4.jpg')
img = cv2.resize(img, (img.shape[1] // 5, img.shape[0] // 5 ))

gray =cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)

faces = cv2.CascadeClassifier('../faces.xml')

results = faces.detectMultiScale(gray, scaleFactor=1.3, minNeighbors=4)

for (x, y, w, h) in results:
    cv2.rectangle(img, (x, y), (x+w, y+h), (0, 0, 255), thickness=3)

cv2.imshow('Present', img)

cv2.waitKey(0)