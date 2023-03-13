import cv2
mic_on = cv2.imread('mic_on.png')
mic_on = cv2.resize(mic_on, (100,100))
mic_off = cv2.imread('mic_off.png')
mic_off = cv2.resize(mic_off, (100,100))
cv2.imwrite('mic_on.png', mic_on)
cv2.imwrite('mic_off.png', mic_off)