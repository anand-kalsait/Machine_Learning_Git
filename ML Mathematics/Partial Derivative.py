import numpy as np
import matplotlib.pyplot as plt
import math
import torch
import warnings
warnings.filterwarnings('ignore')

def f(my_x,my_y):
    return my_x**2 - my_y**2

 x = torch.tensor(-2.).requires_grad_()
y = torch.tensor(- 3.).requires_grad_()

z = f(x, y)
z.backward()

print(x.grad)
print(y.grad)
