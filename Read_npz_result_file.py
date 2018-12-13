import numpy as np
import cv2
import glob

# Define the chess board rows and columns
b = np.load('D:/Images/calib.npz')
print('---------mtx camera matrix result is :----------\n')
print(b['mtx'])

print('---------dist distortion coefficients result is :------------\n')
print(b['dist'])

print('\n---------rvecs rotation vectors result is :----------\n')
print(b['rvecs'])

print('\n------tvecs translation vectors result is :-----------\n')
print(b['tvecs'])