import numpy as np
import torch
import math
import warnings
warnings.filterwarnings('ignore')

A = torch.tensor([[-1,2],[3,-2],[5,7.]])
##print(A)

U, d, VT = torch.linalg.svd(A)

D = torch.diag(d)
Dinv = torch.inverse(D)
Dplus = torch.concatenate((Dinv, torch.tensor([[0,0]]).T),axis=1)

A_pinv = torch.matmul(VT.T, torch.matmul(Dplus,U.T))

print(A_pinv)
APINV = torch.pinverse(A)
print(APINV)



print(torch.trace(A))
print(torch.norm(A))
TR = torch.trace(torch.matmul(A,A.T))
print(math.sqrt(TR))
