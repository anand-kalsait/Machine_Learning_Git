import torch
import warnings
warnings.filterwarnings('ignore')

#for Unsymmetric 3D Matrix
P = torch.tensor([[25,2,-5],[3,-2,1],[-5,1,4.]])
print(P)

L_complex, V_complex = torch.linalg.eig(P)
##print(L_complex,'\n', V_complex)

L = L_complex.float()
V = V_complex.float()

Vinv = torch.inverse(V)

Ldiag = torch.diag(L)
##print(Ldiag)


Pnew = torch.matmul(V,torch.matmul(Ldiag,Vinv))
print(Pnew)
print()
print()


##For Symmetric Matrix
S = torch.tensor([[25,2,-5],[2,-2,1],[-5,1,4.]])
print(S)
L_cplx, Q_cplx = torch.linalg.eig(S)

Ls = L_cplx.float()
Qs = Q_cplx.float()

Qt = Qs.T
##print(Qt)
Lsdiag = torch.diag(Ls)

Snew = torch.matmul(Qs,torch.matmul(Lsdiag,Qt))
print(Snew)
