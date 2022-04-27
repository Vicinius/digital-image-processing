# canny-harris-borders.py

first, it uses canny border detector (with opencv cv.Canny() method) for borders on pompeii.tif, then it uses harris corner detector (with opencv cv.cornerHarris() method) on OpenCV_Chessboard.png and plots the red dots on all the corners.