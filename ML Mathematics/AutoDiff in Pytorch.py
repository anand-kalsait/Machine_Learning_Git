import torch
import warnings
warnings.filterwarnings('ignore')

x = torch.tensor(5.0)
print(x)

x.requires_grad_()
y = x**2
y.backward()

print(x.grad)
