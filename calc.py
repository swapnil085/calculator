import logging


def sum(a,b):
    return a+b

def diff(a,b):
    return a-b

def multiply(a,b):
    return a*b

def divide(a,b):
    return a//b

if __name__ == "__main__":
    x = sum(4,2)
    y = diff(4,2)
    z = multiply(4,2)
    print("sum: ",x)
    print("diff: ",y)
    print("multiply: ",z)
    logging.basicConfig(filename='calculation.log',level=logging.DEBUG)
    logging.info(x)
    logging.info(y)
    logging.info(z)
