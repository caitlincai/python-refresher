import numpy as np

def hello():
    return("Hello, world!")


def add(a: int | float, b: int | float):
    return a + b


def sub(a: int | float, b: int | float):
    return a - b


def mul(a: int | float, b: int | float):
    return a * b


def div(a: int | float, b: int | float):
    if b == 0:
        raise ValueError("Can't divide by zero!")
    return a / b


def sqrt(a: int | float):
    return np.sqrt(a)


def power(a: int | float, b: int | float):
    return np.power(a, b)


def log(a: int | float):
    return np.log(a)


def exp(a: int | float):
    return np.exp(a)


def sin(a: int | float):
    return np.sin(a)


def cos(a: int | float):
    return np.cos(a)


def tan(a: int | float):
    return np.tan(a)


def cot(a: int | float):
    return 1 / np.tan(a)


def __main__():
    hello()

if __name__ == "__main__":
    __main__()
