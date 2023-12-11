from matplotlib import pyplot as plt
import cv2

a = cv2.imread("download.jpg")
a = cv2.cvtColor(a , cv2.COLOR_BGR2RGB)
b = cv2.CascadeClassifier("model.xml")
face = b.detectMultiScale(a)

x = face[0][0]
y = face[0][1]
an = face[0][2]
bn = face[0][3]

plt.imshow(a)
a = cv2.rectangle(a , (x,y) , (x+an,y+bn) , (0,255,0) , 2)     # ((x,y) , (x,y) , (color) , weight)

# a.shape        # size of pic

plt.imshow(a)