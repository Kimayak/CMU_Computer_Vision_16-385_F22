import numpy as np


def myImageFilter(img0, h):
    # YOUR CODE HERE
    h_inv = np.flipud(np.fliplr(h))
    padding = np.int((h.shape[0]-1)//2)
    img_padded = np.zeros((img0.shape[0]+2*padding, img0.shape[1]+2*padding))
    img_padded[padding:-padding, padding:-padding] = img0
    conv = np.zeros(img0.shape)
    for i in range(len(img0)):
        for j in range(len(img0[0])):
            conv[i,j] = h_inv*img_padded[i:i+len(h_inv),j:j+len(h_inv[0])].sum()

    return conv
    

    
