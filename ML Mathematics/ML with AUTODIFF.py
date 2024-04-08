import torch
import warnings
import matplotlib.pyplot as plt
from numpy import random

warnings.filterwarnings('ignore')

##x = torch.tensor(2.).requires_grad_()
##
##y = x**2+2*x+2
##
##y.backward()
##print(x.grad)

x = torch.tensor([0,1,2,3,4,5,6,7,8.])
y = torch.tensor(0.5*x + 2)
plt.scatter(x,y)
plt.show()
m = torch.tensor([0.9]).requires_grad_()
b = torch.tensor([0.5]).requires_grad_()
print(m,b)

def regression(my_x,my_m,my_b):
    return my_m*my_x + my_b
def regression_plot(my_x,my_y,my_m,my_b):
    plt.scatter(x,y)
    x_min, x_max = plt.xlim()
    print(x_min, x_max)
    y_min = regression(x_min,my_m,my_b).detach().item()
    y_max = regression(x_max,my_m,my_b).detach().item()

    plt.plot([x_min, x_max],[y_min, y_max])
    plt.show()
regression_plot(x,y,m,b)
def mseloss(my_yhat,my_y):
    sigma = torch.sum((my_yhat - my_y)**2)
    return sigma/9

##Step 01
yhat = regression(x,m,b)    

##Step 02
C = mseloss(yhat,y) 
print(C)
##Step 03
C.backward()
print(m.grad)
print(b.grad)
##Step 04
optimizer = torch.optim.SGD([m,b], lr = 0.5)
optimizer.step()
regression_plot(x,y,m,b)


##putting all 4 steps in action
epochs = 1000
for epoch in range(epochs):
    
    optimizer.zero_grad() # Reset gradients to zero; else they accumulate
    
    yhat = regression(x, m, b) # Step 1
    C = mseloss(yhat, y) # Step 2
    
    C.backward() # Step 3
    optimizer.step() # Step 4
    
    print('Epoch {}, cost {}, m grad {}, b grad {}'.format(epoch, '%.3g' % C.item(), '%.3g' % m.grad.item(), '%.3g' % b.grad.item()))
regression_plot(x,y,m,b)


