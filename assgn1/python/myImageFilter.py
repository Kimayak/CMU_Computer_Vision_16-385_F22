import numpy as np


# def myImageFilter(img0, h):
#     # YOUR CODE HERE
#     h_inv = np.flipud(np.fliplr(h))
#     padding = np.int((h.shape[0]-1)//2)
#     img_padded = np.zeros((img0.shape[0]+2*padding, img0.shape[1]+2*padding))
#     img_padded[padding:-padding, padding:-padding] = img0
#     conv = np.zeros(img0.shape)
#     for i in range(len(img0)):
#         for j in range(len(img0[0])):
#             conv[i,j] = h_inv*img_padded[i:i+len(h_inv),j:j+len(h_inv[0])].sum()

#     return conv
    

    
import numpy as np


def myImageFilter(img0, h):
    # YOUR CODE HERE
    h = np.array(h)
   # print(h.ndim)
    if (h.ndim == 2):
         h_inv = np.flipud(np.fliplr(h))
    h_inv = np.fliplr(h)
    padding1 = np.int((h.shape[0]-1)//2)
    padding2 = np.int((h.shape[1]-1)//2)
    img_padded = np.zeros((img0.shape[0]+2*padding1, img0.shape[1]+2*padding2))
    img_padded[padding1:-padding1, padding2:-padding2] = img0
    conv = np.zeros(img0.shape)
    temp =[]
    for i in range(len(img0)):
        for j in range(len(img0[0])):
            temp = h_inv*img_padded[i:i+len(h_inv),j:j+len(h_inv[0])]
            # print(temp.shape)
            # print(np.sum(temp).shape)
            conv[i,j] = np.sum(temp)

    return conv


    
