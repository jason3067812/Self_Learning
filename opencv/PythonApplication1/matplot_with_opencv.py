import numpy as np
import cv2
from matplotlib import pyplot as plt

img = cv2.imread('lena.jpg', 1) 

cv2.imshow('img', img) #BGR

img = cv2.cvtColor(img, cv2.COLOR_BGR2RGB)

plt.imshow(img) #RGB
plt.xticks([]), plt.yticks([]) #axis scale
plt.show()

cv2.waitKey(0)
cv2.destroyAllWindows()
