import numpy as np

def add(a, b):
    return a + b

def dif(a, b):
    return a - b

def dot(a, b):
    return np.dot(a, b)

def mag(a):
    return np.linalg.norm(a)

def transpose(A):
    return A.T

def questions():
    print(f"QUESTION 1 SUM = {add(np.array([1, 2, 3]), np.array([4, 5, 6]))}\n")
    print(f"QUESTION 1 DIF = {dif(np.array([1, 2, 3]), np.array([4, 5, 6]))}\n")
    print(f"QUESTION 2 SUM = {add(np.array([[1, 2], [3, 4]]), np.array([[5, 6], [7, 8]]))}\n")
    print(f"QUESTION 2 DIF = {dif(np.array([[1, 2], [3, 4]]), np.array([[5, 6], [7, 8]]))}\n")
    print(f"QUESTION 3 DOT = {dot(np.array([1, 2, 3]), np.array([4, 5, 6]))}\n")
    print(f"QUESTION 4 DOT = {dot(np.array([[1, 2, 3], [4, 5, 6]]) , np.array([[7, 8, 9, 10], [11, 12, 13, 14], [15, 16, 17, 18]]))}\n")
    print(f"QUESTION 5 MAGNITUDE = {mag(np.array([1, 1, 2]))}\n")
    print(f"QUESTION 6 ANSWER = {transpose(np.array([[1, 2], [3, 4]]))}\n")

questions()