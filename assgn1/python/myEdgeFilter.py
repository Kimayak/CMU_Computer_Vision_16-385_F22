import numpy as np
from scipy import signal    # For signal.gaussian function

from myImageFilter import myImageFilter 

def myEdgeFilter(img0, sigma):
    # YOUR CODE HERE
    gauss_filt =signal.gaussian(2 * np.ceil(3 * sigma) + 1, sigma)

    denoise = myImageFilter(img0, gauss_filt)

    Sx = [[-1,0,1],[-2,0,2],[-1,0,1]]
    Sy = Sx.T

    Imgx = myImageFilter(denoise, Sx)
    Imgy = myImageFilter(denoise, Sy)
    thetas = np.arctan2(Imgy, Imgx) * 180 / np.pi

    gradm = np.sqrt(Imgx**2 + Imgy**2)

    qthetas = np.zeros_like(thetas, dtype=np.uint8)
    for i in range(len(thetas)):
        thetas[i] = thetas[i]+180
    qthetas[np.where(((thetas >= 0) and (thetas < 22.5)) or (thetas>=337.5 and (thetas<=360)))] = 0
    qthetas[np.where(((thetas >= 22.5 ) and (thetas < 67.5)))] = 45
    qthetas[np.where(((thetas >= 67.5  ) and (thetas < 112.5)))] = 90
    qthetas[np.where(((thetas >= 22.5 ) and (thetas < 67.5)))] = 135
  



    #thetas = [item = item + 180 for item in thetas]
   # qthetas[np.where(((thetas >= -45/2) and (thetas < 45/2)) or (thetas>=135+(180-135)/2 or (thetas<=135+(180-135)/2) ))] = 0
    # qthetas[np.where((thetas >= -22.5) & (thetas < 22.5)  )] = 0
    # qthetas[np.where((thetas >= 22.5) & (thetas < 67.5))] = 45
    # qthetas[np.where((thetas >= 67.5) & (thetas < 112.5))] = 90
    # qthetas[np.where((thetas >= 112.5) & (thetas < 157.5))] = 135
    nms_out = np.copy(gradm)
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
                nms_out[i, j] = 0

    return Imgx, Imgy, nms_out



    

