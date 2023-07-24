import numpy as np
import cv2  # For cv2.dilate function

def myHoughLines(H, nLines):
    #rhos,thetas = [], []
    print(H.shape, nLines)
    rhos = np.zeros((nLines , 1))
    thetas = np.zeros((nLines , 1))
    kernel = np.ones((3, 3), np.uint8)
    nms_img= cv2.dilate(H, kernel)
    peaks = []
    for _ in range(nLines):
        # Find the maximum value in the Hough accumulator
        max_value = np.max(nms_img)

        # Find the indices of the maximum value in the Hough accumulator
        max_indices = np.argwhere(nms_img == max_value)
        max_index = tuple(max_indices[0])  # Take the first occurrence in case of ties

        # Convert the indices to (ρ, θ) coordinates
        rho, theta= max_index
        #theta = theta_index * (2 * np.pi / nms_img.shape[1])

        # Add the (ρ, θ) coordinate of the peak to the list
        peaks.append((rho, theta))

        # Suppress the neighborhood of the maximum value in the Hough accumulator
        nms_img[max_index] = 0

    # Convert the coordinates of the highest-scoring cells back to (ρ, θ) values
    rhos = np.array([peak[0] for peak in peaks])
    thetas = np.array([peak[1] for peak in peaks])

    print(rhos.shape, thetas.shape)
    return rhos,thetas
