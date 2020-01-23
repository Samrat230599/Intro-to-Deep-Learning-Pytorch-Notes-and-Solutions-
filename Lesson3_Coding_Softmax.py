import numpy as np

# Write a function that takes as input a list of numbers, and returns
# the list of values given by the softmax function.
def softmax(L):
    den = 0
    for i in range(len(L)):
        den += np.exp(L[i])
    for i in range(len(L)):
        L[i] = np.exp(L[i]) / den
    return L
