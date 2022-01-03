import cv2
import numpy as np

# photo = np.zeros((450, 450, 3), dtype='uint8')
#
# # photo[100:150, 200:280] = 110, 240, 50
#
# cv2.rectangle(photo, (10, 70), (100, 100), (110, 240, 50), thickness=3)
#
# cv2.line(photo, (0, photo.shape[0] // 2), (photo.shape[1], photo.shape[0] // 2), (110, 240, 50), thickness=2)
#
# cv2.circle(photo, (photo.shape[1] // 2, photo.shape[0] // 2), 50, (110, 240, 50), thickness=2)
#
# cv2.putText(photo, 'Test_txt', (100, 150), cv2.FONT_HERSHEY_TRIPLEX, 1, (0, 0, 255), thickness=1)
#
# cv2.imshow('Photo', photo)
#
# cv2.waitKey(0)


# Работа с картинкой


photo = cv2.imread('..\images\Teser.jpg')



# img = np.zeros(photo.shape[:2], dtype='uint8')
#
# circle = cv2.circle(img.copy(), (395, 347), 160, 255, -1)
#
# square = cv2.rectangle(img.copy(), (25, 25), (250, 350), 255, -1)
#
# img = cv2.bitwise_and(photo, photo, mask=circle)
# img = cv2.bitwise_or(circle, square)
# img = cv2.bitwise_xor(circle, square)
# img = cv2.bitwise_not(circle)

# img = cv2.cvtColor(img, cv2.COLOR_, BGR2LAB)
# img =cv2.cvtColor(img, cv2.COLOR_LAB2BGR)
# img = cv2.cvtColor(img, cv2.COLOR_BGR2RGB)
# r, g, b = cv2.split(img)
# img = cv2.merge([g, g, r])



# new_img = np.zeros(img.shape, dtype='uint8')
#
# img = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
# img = cv2.GaussianBlur(img, (5, 5), 0)
#
# img = cv2.Canny(img, 100, 140)
#
# con, hir = cv2.findContours(img, cv2.RETR_LIST, cv2.CHAIN_APPROX_NONE)
#
# cv2.drawContours(new_img, con, -1, (230, 147, 25), 1)


# img = cv2.flip(img, -1)
#
# def rotate(img_param, angle):
#     height, width = img_param.shape[:2]
#     point = (width //2, height // 2)
#
#     mat = cv2.getRotationMatrix2D(point, angle, 1)
#     return  cv2.warpAffine(img_param, mat, (width, height))

# img = rotate(img, 90)

# def transform(img_param, x, y):
#     mat = np.float32([[1, 0, x], [0, 1, y]])
#     return  cv2.warpAffine(img_param, mat, (img_param.shape[1], img_param.shape[0]))
#
# img = transform(img, 30, 200)

# img = cv2.resize(img, (img.shape[1] // 2, img.shape[0] //2))
# img = cv2.GaussianBlur(img, (9, 9), 0 )
# img = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
#
# img = cv2.Canny(img, 200, 200)
#
# kernel = np.ones((5, 5), np.uint8)
# img = cv2.dilate(img, kernel, iterations=1)
#
# img = cv2.erode(img, kernel, iterations=1)
#
cv2.imshow('image', img)
#
#
# print(img.shape)
cv2.waitKey(0)


# cap = cv2.VideoCapture('../videos/water.mp4')
# while True:
#     success, img = cap.read()
#
#     # img = cv2.resize(img, (img.shape[1] // 2, img.shape[0] //2))
#     img = cv2.GaussianBlur(img, (9, 9), 0 )
#     img = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
#
#     img = cv2.Canny(img, 100, 100)
#
#     kernel = np.ones((5, 5), np.uint8)
#     img = cv2.dilate(img, kernel, iterations=1)
#
#     img = cv2.erode(img, kernel, iterations=1)
#
#
#     cv2.imshow('Result', img)
#
#     if cv2.waitKey(30) & 0xFF == ord('q'):
#         break


# webcam = cv2.VideoCapture(0)
# webcam.set(3, 900)
# webcam.set(4, 900)
# while True:
#     success, img = webcam.read()
#     cv2.imshow('Result', img)
#
#     if cv2.waitKey(30) & 0xFF == ord('q'):
#         break
