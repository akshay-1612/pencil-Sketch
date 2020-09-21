import cv2

#cv2.imread() method loads an image from the specified file
img = cv2.imread('pencil-Sketch/dhoni.jfif')


# cv2.imshow(window_name, image) method is used to display an image in a window 
# cv2.imshow('',img)

# cv2.cvtColor() method is used to convert an image from one color space to another
# grayscale gives us black & white pixels in the image which is used for creating a pencil sketch. 
img_gray = cv2.cvtColor(img,cv2.COLOR_BGR2GRAY)
# cv2.imshow('',img)

#bitwise not operation on the image
# bitwise_not function which is used to make brighter regions lighter and vice versa so that we can find the edges to create a pencil sketch
img_invert = cv2.bitwise_not(img_gray)
# cv2.imshow('',img_invert)

#Blur the image
img_smoothing = cv2.GaussianBlur(img_invert,(21,21),sigmaX=0,sigmaY=0)
# cv2.imshow('',img_smoothing)


def dodgeV2(x,y):
    # dividing the greyscale value of the image by the inverse of blurred image value which highlights the boldest edges
    return cv2.divide(x,255-y,scale=256)

final_img = dodgeV2(img_gray,img_smoothing)
cv2.imshow('',final_img)
cv2.imwrite('photo.png',final_img)

#waits for user to press any key  
#this is necessary to avoid Python kernel form crashing
cv2.waitKey(0)

