# filtering-borders.py

this one does exactly the same as pratica04 mean-flter.py does using the already existing function "cv.filter2D()" but it's all using for loops, including the convolution process itself, which is what actually happens inside cv.filter2D, you select a predefined or user defined mask and runs a certain *mask* by the original image and makes the convolution operation on it. there are some particularities including border management, you can supress the border (default), use zero padding (zero), or replicate the border pixels (replicate).
