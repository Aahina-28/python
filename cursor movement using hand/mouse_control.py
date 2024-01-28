import cv2
import mediapipe
import pyautogui

capture_hands = mediapipe.solutions.hands.Hands()#mediapipe.solutions.hands: the solutions module contains pre-built solutions for specific tasks. 
                                                #The hands module, in turn, focuses on hand-related tasks, including hand tracking.
                                                #Hands():It creates an instance of the Hands class, that is present in the mediapipe, 
                                                #which is equipped with the necessary methods and functionalities 
                                                #to process images or video frames and extract information about hand landmarks

drawing_option = mediapipe.solutions.drawing_utils#module provides utility functions for drawing landmarks, connections, and other visual elements on images or frames.

screen_width , screen_height = pyautogui.size()#getting screen width and height
                                               #pyautogui.size():This function is used to obtain the screen resolution 
                                               #or size of the primary monitor

camera = cv2.VideoCapture(0) #video capture fuction is used to capture the vid through cam "0", that is the default cam
x1 = y1 = x2 = y2 = 0
while True: #this loop will execute till the vid cam is capturing video, camera 

    _,image = camera.read() #camera.read(): This method reads a single frame from the video capture device.
                            #It returns two values: a boolean value (_) indicating whether the frame was successfully read, 
                            #and the actual frame (image) as a NumPy array._: The underscore (_) is a common convention in Python
                            #to indicate that the returned value is not going to be used. 
                            #In this case, it is used to ignore the boolean return value indicating whether the frame was successfully read.
    
    image_height, image_width, _ = image.shape#getting only the height & width of the image, not depth
                                              #image.shape attribute is from the OpenCV library. In OpenCV, the shape attribute 
                                              #is used to obtain the dimensions of an image or an array. 
    
    image = cv2.flip(image,1)#cv2: Refers to the OpenCV library.
                            #flip: This is a function in OpenCV used to flip or mirror an image.
                            #image: This is the variable holding the current video frame or image.
                            #1: This parameter specifies the axis of flipping. When set to 1, it means flipping around the vertical axis,      
                            #which results in a horizontal flip.
                            #So, the purpose of this line is to create a mirrored version of the input image by flipping it horizontally.
    
    rgb_image = cv2.cvtColor(image ,cv2.COLOR_BGR2RGB)# to convert the image from bgr to rgb, cv uses bgr as a standard while 
                                                      #MediaPipe, use RGB as the standard color order.
    
    output_hands = capture_hands.process(rgb_image)#capture_hands: This is an instance of the Hands class from the MediaPipe library.   
                                                   #rgb_image: This is the input image in RGB format.    
                                                   #capture_hands.process(rgb_image): This method processes the input image (rgb_image) using the 
                                                   #hand tracking model provided by MediaPipe. It detects and analyzes the hand landmarks in the 
                                                   #image.output_hands: This variable holds the result of the hand tracking process. 
                                                   #It typically contains information such as the positions of hand landmarks, the presence of hands, and other relevant data.
    
    all_hands = output_hands.multi_hand_landmarks#output_hands: This variable holds the result of the hand tracking process
                                                 #output_hands.multi_hand_landmarks: This attribute (.multi_hand_landmarks) likely 
                                                 #contains a list of landmarks for all the detected hands 
                                                 #in the processed image. Each hand's landmarks are represented as a list of points.
                                                 #all_hands: This variable is assigned the value of output_hands.multi_hand_landmarks. 
                                                 #It represents the landmarks of all the detected hands in the image
    
    if all_hands:#if hand is detected
        for hand in all_hands:#then this must be applied to all the hands detected
            drawing_option.draw_landmarks(image,hand)#drawing_option is instance of drawing_utils from mediapipe, 
                                                     #for utility function to draw on images.
                                                     #draw_landmarks: This function is used to draw landmarks on an image.
            
            one_hand_landmarks = hand.landmark#hand: This is the variable representing a single detected hand.
                                              #landmark: This is likely an attribute or method of the hand object that 
                                              #provides information about the landmarks of the hand.
            
            for id, lm in enumerate(one_hand_landmarks):#id is a variable that represents the index or position 
                                                        #of the current landmark within the one_hand_landmarks
                                                        #lm is for landmarks 
                                                        #enumerate(one_hand_landmarks): This is a built-in Python function that adds a counter (id in this case) to 
                                                        #an iterable (one_hand_landmarks). 
                                                        #It allows you to loop over both the index and the value.
                 
                x = int(lm.x * image_width)#to convert decimal number to non decimal number
                y = int(lm.y * image_height)

                # print(x,y)
                if id == 8:#for index finger
                    mouse_x = int(screen_width / image_width * x)#This formula scales the hand landmark coordinates (x and y) to match 
                    mouse_y = int(screen_width / image_height * y)#the screen dimensions (screen_width and screen_height). 
                                                                 #The scaling ensures that the hand movements within the captured frame 
                                                                 #translate appropriately to the dimensions of the screen.
                    
                    cv2.circle(image,(x,y),10,(0,255,255))# drawing a circle on the img with center x,y with radius 10 
                                                          #and color yellow i.e. (0,255,255)
                    
                    pyautogui.moveTo(mouse_x,mouse_y)#to move the cursor to these specific coordinates
                    x1=x #index finger coordinates
                    y1=y
                if id == 4:#for thumb finger
                   cv2.circle(image,(x,y),10,(0,255,255))
                   x2 = x#thumb finger coordinates
                   y2 = y 
        dist = y2 - y1#to calculate the vertical distance
        print(dist)

        if(dist<20):# if the vertical distance becomes less than 20 the "click operation will take place"
            pyautogui.click()
            print("clicked")
    cv2.imshow("Hand movement video capture",image)#imshow: This function is used to display an image or a video frame in a window.
                                                   #(name of the window, whats being displayed)
    key = cv2.waitKey(100)
    if key == 27:#esc key ascii value to exit the loop
        break
camera.release()# to release the associated resources is vidcapture

cv2.destroyAllWindows() #When you call cv2.destroyAllWindows(), it closes all the GUI windows created by cv2.imshow()
