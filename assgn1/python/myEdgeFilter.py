import numpy as np
from scipy import signal    # For signal.gaussian function

from myImageFilter import *

def myEdgeFilter(img0, sigma):
    # YOUR CODE HERE
    gauss_filt =signal.gaussian(2 * np.ceil(3 * sigma) + 1, sigma)

    denoise = myImageFilter(img0, gauss_filt)

    Sx = [[-1,0,1],[-2,0,2],[-1,0,1]]
    Sy = Sx.T

    Imgx = myImageFilter(denoise, Sx)
    Imgy = myImageFilter(denoise, Sy)
    thetas = np.arctan2(Imgy, Imgx) * 180 / np.pi

    gradm = np.sqrt(Imgx**2 +Imgy**2)

    qthetas = np.zeros_like(thetas, dtype=np.uint8)
    qthetas[np.where((thetas >= -22.5) & (thetas < 22.5))] = 0
    qthetas[np.where((thetas >= 22.5) & (thetas < 67.5))] = 45
    qthetas[np.where((thetas >= 67.5) & (thetas < 112.5))] = 90
    qthetas[np.where((thetas >= 112.5) & (thetas < 157.5))] = 135
    suppressed = np.copy(gradm)
    #height, width = gradm.shape
    for i in range(1, gradm.shape[0] - 1):
        for j in range(1, gradm.shape[1] - 1):
            a1 = qthetas[i, j]
            if a1 == 0:
                neighbors = [gradm[i, j-1], gradm[i, j+1]]
            elif a1 == 45:
                neighbors = [gradm[i-1, j+1], gradm[i+1, j-1]]
            elif a1 == 90:
                neighbors = [gradm[i-1, j], gradm[i+1, j]]
            else:
                neighbors = [gradm[i-1, j-1], gradm[i+1, j+1]]

            if gradm[i, j] <= max(neighbors):
                suppressed[i, j] = 0

    return Imgx, Imgy, suppressed



    

