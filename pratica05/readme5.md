# binary-thresholding.py

this one applies an binary thresholding inverse of 127 (from 0-255), on an already greyscale image

# skin-detector-hsv.py

skin detection from a webcam stream (if connected) using cv2.VideoCapture(0) method. this one uses hsv colorspace which is not ideal, for better results use skin-detector-ycrcb.py

# skin-detector-ycrcb.py

same as above, but with better results