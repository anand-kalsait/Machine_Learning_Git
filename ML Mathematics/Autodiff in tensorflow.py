import tensorflow as tf
import warnings
warnings.filterwarnings('ignore')

x = tf.Variable(5.0)
print(x)
with tf.GradientTape() as t:
    t.watch(x)
    y = x**2
print(t.gradient(y,x))
