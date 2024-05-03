import numpy as np
from sklearn import datasets
# Generate a dataset and plot it
np.random.seed(0)
X, y = datasets.make_moons(200, noise=0.20)

# Neural network architecture
input_dim = 4
output_dim = 3
hidden_dim = 6 

# Weights and bias element for layer 1
W1 = np.random.randn(input_dim, hidden_dim)
b1 = np.zeros((1, hidden_dim))

# Weights and bias element for layer 2
W2 = np.random.randn(hidden_dim, hidden_dim)
b2 = np.zeros((1, hidden_dim))

# Weights and bias element for layer 2
W3 = np.random.randn(hidden_dim, output_dim)
b3 = np.zeros((1, output_dim))

# Forward propagation of input signals to 6 neurons in first hidden layer
# activation is calculated based tanh function
z1 = X.dot(W1) + b1
a1 = np.tanh(z1)

# Forward propagation of activation signals from first hidden layer to 6 neurons in second hidden layer
z2 = a1.dot(W2) + b2
a2 = np.tanh(z2)

# Forward propagation of activation signals from second hidden layer to 3 neurons in output layer
z3 = a2.dot(W3) + b3

# Probability is calculated as an output of softmax function
probs = np.exp(z3) / np.sum(np.exp(z3), axis=1, keepdims=True)
