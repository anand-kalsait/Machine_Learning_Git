from scipy.integrate import quad
import warnings
warnings.filterwarnings('ignore')

def f(x):
    return 2*x                           

print(quad(f, 3, 4))

