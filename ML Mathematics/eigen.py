import torch
import warnings
warnings.filterwarnings('ignore')

A = torch.tensor([[25,2,9],[5,26,-5],[3,7,-1.]])
print(A)

L_complex, V_complex = torch.linalg.eig(A)
##print(L_complex,'\n', V_complex)

L_pt = L_complex.float()
V_pt = V_complex.float()

print(L_pt,'\n', V_pt)

v1_pt = V_pt[:,0]
l1_pt = L_pt[0]
v2_pt = V_pt[:,1]
l2_pt = L_pt[1]
v3_pt = V_pt[:,2]
l3_pt = L_pt[2]


Av1_pt = torch.matmul(A,v1_pt)
print(Av1_pt)

l1v1_pt = l1_pt.float()*v1_pt.float()
print(l1v1_pt)

Av2_pt = torch.matmul(A,v2_pt)
print(Av2_pt)

l2v2_pt = l2_pt.float()*v2_pt.float()
print(l2v2_pt)

Av3_pt = torch.matmul(A,v3_pt)
print(Av3_pt)

l3v3_pt = l3_pt.float()*v3_pt.float()
print(l3v3_pt)
