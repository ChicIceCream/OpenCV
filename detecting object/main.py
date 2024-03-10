import numpy as np
import cv2 as cv

img = cv.imread('detecting object\org.png', 0)
template = cv.imread('detecting object\image.png', 0)
h,w = template.shape
# print(img)

methods = [cv.TM_CCOEFF, cv.TM_CCOEFF_NORMED, cv.TM_CCORR,
            cv.TM_CCORR_NORMED, cv.TM_SQDIFF, cv.TM_SQDIFF_NORMED]

for method in methods:
    img2 = img.copy()
    
    result = cv.matchTemplate(img2, template, method)
    min_val, max_val, min_loc, max_loc = cv.minMaxLoc(result)
    if method in [cv.TM_SQDIFF, cv.TM_SQDIFF_NORMED]:
        location = min_loc
    else:
        location = max_loc
        
    bottom_right = (location[0] + w, location[1] + h)    
    cv.rectangle(img2, location, bottom_right, 0, 5)
    cv.imshow('Match', img2)
    cv.waitKey(0)
