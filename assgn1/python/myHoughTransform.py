import numpy as np

def myHoughTransform(Im, rhoRes, thetaRes):
    # YOUR CODE HERE
    print("Imag_shape", Im.shape)
    print(rhoRes, thetaRes)
    thetaScale = np.arange(0, 2 * np.pi, thetaRes)
    M = np.sqrt(Im.shape[0]**2+Im.shape[1]**2)
    rhoScale = np.arange(0, M, rhoRes)

   # img_hough, rhoScale, thetaScale = [],[],[]
    img_hough = np.zeros((len(rhoScale), len(thetaScale)))
    # for i in range(Im.shape[0]):
    #     for j in range(Im.shape[1]):
    #         ps,ts += np.where(rhoRes = i*np.cos(thetaRes)+j*np.sin(thetaScale))
    #         print(ps,ts)
    
    for xi in range(Im.shape[0]):
        for yi in range(Im.shape[1]):
            if Im[xi, yi]> 0:
                for j in range(len(thetaScale)):
                    rho = xi*np.cos(thetaScale[j]) + yi*np.sin(thetaScale[j])
                    rho_index = np.argmin(np.abs(rhoScale - rho))
                    img_hough[rho_index, j] += 1
    
    print("Img hough",img_hough.shape)
    print("rho", rhoScale.shape)
    print("theta", thetaScale.shape)
    

            




    return img_hough, rhoScale, thetaScale 

