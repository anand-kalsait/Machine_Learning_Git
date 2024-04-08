import torch
import math
import warnings
warnings.filterwarnings('ignore')

P = torch.tensor([[25,2,-5],[3,-2,1],[-5,1,4.]])
##SVD
U,d,VT = torch.linalg.svd(P)
##print(U)
##print(VT)
##print(d)

D = torch.diag(d)
##print(D)

SVDP = torch.matmul(U, torch.matmul(D,VT))
print(SVDP)


L_complex, V_complex = torch.linalg.eig(P)
##print(L_complex,'\n', V_complex)

##EigenDecomposition
L = L_complex.float()
V = V_complex.float()

Vinv = torch.inverse(V)

Ldiag = torch.diag(L)
##print(Ldiag)


Pnew = torch.matmul(V,torch.matmul(Ldiag,Vinv))
print(Pnew)
print('-------------------------------------------------------------')

##relation between EigenDecomposition and SVD
L_complex, V_complex = torch.linalg.eig(torch.matmul(P,P.T))
##print(L_complex,'\n', V_complex)

##EigenDecomposition
LL = L_complex.float()
VL = V_complex.float()
print(U,'\n', VL)
print('-------------------------------------------------------------')

L_complex, V_complex = torch.linalg.eig(torch.matmul(P.T, P))
##print(L_complex,'\n', V_complex)

##EigenDecomposition
LR = L_complex.float()
VR = V_complex.float()
print(VT.T,'\n',VR )
print('-------------------------------------------------------------')

print(D, '\n', LL**1/2,'\n', LR**1/2 )
print('-------------------------------------------------------------')

