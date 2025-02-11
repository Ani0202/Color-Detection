#calculate the rgb values of the pixel which we double click
def draw_function(event, x, y, flags, param):
    if event == cv2.EVENT_LBUTTONDBLCLK:
        global b, g, r, xpos, ypos, clicked
        clicked = True
        xpos = x
        ypos = y
        b, g, r = img[y,x]
        b = int(b)
        g = int(g)
        r = int(r)

#return us the color name from RGB values
#d = abs(Red – ithRedColor) + (Green – ithGreenColor) + (Blue – ithBlueColor)
def getColorName (R, G, B):
    min = 10000
    for i in range(len(csv)):
        d = abs(R - int(csv.loc[i,"Red"])) + abs(G - int(csv.loc[i,"Green"])) + abs(B - int(csv.loc[i,"Blue"]))
        if (d <= min):
            min = d
            color_name = csv.loc[i, "color_name"]
    return color_name

#import neccessarry modules
import cv2
import pandas as pd
import numpy as np
import argparse

#argument parser to directly give an image path from the command prompt
ap = argparse.ArgumentParser()
ap.add_argument('-i', '--image', required=True, help="Path of Image")
args = vars(ap.parse_args())
img_path = args['image']

#Reading image with opencv
img = cv2.imread(img_path)

#read the CSV file with pandas
index=["color","color_name","hex","Red","Green","Blue"]
csv = pd.read_csv('colors.csv', names=index, header=None)

clicked = False
r = g = b = xpos = ypos = 0

#Set a mouse callback event on a window
cv2.namedWindow('image')
cv2.setMouseCallback('image',draw_function)

#Display image on the window
while(True):
    cv2.imshow("image",img)
    if (clicked):
        #draw rectangle to display text
        cv2.rectangle(img,(20,20), (750,60), (b,g,r), -1)

        #Creating text string to display ( Color name and RGB values )
        text = getColorName(r,g,b) + ' R='+ str(r) + ' G='+ str(g) + ' B='+ str(b)
        cv2.putText(img, text,(50,50),2,0.8,(255,255,255),2,cv2.LINE_AA)
  
        #For very light colours we will display text in black colour
        if(r+g+b>=600):
            cv2.putText(img, text,(50,50),2,0.8,(0,0,0),2,cv2.LINE_AA)

        clicked=False

    #Break the loop when user hits 'esc' key 
    if cv2.waitKey(20) & 0xFF ==27:
        break

cv2.destroyAllWindows()