# importing cv2  
import cv2  
import numpy as np
    
HEIGHT, WIDTH = 500, 500

# Reading an image in default mode 
image = np.ones((HEIGHT, WIDTH, 3))
    
# Window name in which image is displayed 
window_name = 'Image'
   
# Center coordinates 
center_coordinates = (120, 50) 
  
# Radius of circle 
radius = 20
   
# Blue color in BGR 
color = (255, 0, 0) 
   
# Line thickness of 2 px 
thickness = 2
   
while True:
    image = cv2.circle(image, center_coordinates, radius, color, thickness) 
    cv2.imshow(window_name, image)
    if cv2.waitKey(1) == 'q':
        break