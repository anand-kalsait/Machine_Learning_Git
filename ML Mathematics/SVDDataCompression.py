import numpy as np
from PIL import Image
import torch
import matplotlib.pyplot as plt
import warnings
warnings.filterwarnings('ignore')

yolo = Image.open('photo.jpg')
_=plt.imshow(yolo)
##plt.show()
b = yolo.convert('LA')
imgmat = np.array(list(b.getdata(band=0)))
imgmat.shape = (b.size[1], b.size[0])
imgmat = np.matrix(imgmat)
plt.imshow(imgmat, cmap='gray')
##plt.show()

print(np.shape(b))

##SVD
U, d, VT = np.linalg.svd(b)

Reconstruction = np.matrix(U[:, :2])* np.diag(d[:2]) * np.matrix(VT[:2,:])

plt.imshow(Reconstruction, cmap='gray')
plt.show()
