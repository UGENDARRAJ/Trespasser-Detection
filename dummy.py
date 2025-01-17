# program to capture single image from webcam in python
  
# importing OpenCV library
import cv2
  
# initialize the camera
# If you have multiple camera connected with 
# current device, assign a value in cam_port 
# variable according to that
#cam_port = 0
cam = cv2.VideoCapture(0)
  
# reading the input using the camera
result, image = cam.read()
  
# If image will detected without any error, 
# show result
while(True):
    if result:
    
        # showing result, it take frame name and image 
        # output
        cv2.imshow("Yadav", image)
    
        
    
        # If keyboard interrupt occurs, destroy image 
        # window
        #cv2.waitKey(0)
        k = cv2.waitKey(30) & 0xff
        if k == 27:
            # saving image in local storage
            cv2.imwrite("still.jpeg", image)
            cv2.destroyWindow("Yadav")
            break
        #cv2.destroyWindow("Yadav")
    
    # If captured image is corrupted, moving to else part
    else:
        print("No image detected. Please! try again")
        break