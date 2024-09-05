import cv2 as cv

img = cv.imread('/Users/abhinavsingh/Desktop/Opencv/photos/eyes.jpg')
cv.imshow('eyes', img)

cv.waitKey(0)

# Reading Videos
capture = cv.VideoCapture('/Users/abhinavsingh/Desktop/Opencv/Videos/10058358-hd_1080_1920_30fps.mp4')

while True:
    isTrue, frame = capture.read()
    
    # if cv.waitKey(20) & 0xFF==ord('d'):
    # This is the preferred way - if `isTrue` is false (the frame could 
    # not be read, or we're at the end of the video), we immediately
    # break from the loop. 
    if isTrue:    
        cv.imshow('Video', frame)
        if cv.waitKey(20) & 0xFF==ord('d'):
            break            
    else:
        break

capture.release()
cv.destroyAllWindows()
