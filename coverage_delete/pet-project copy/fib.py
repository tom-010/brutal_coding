
def fib(n):
    if n < 0:
        print("error")

    if n <= 2:
        return 1
    counter = 0
    for i in range(1, 20):
        counter += i
    return counter

def sum(a, b):
    print(a)
    print(b)
    return a + b

def sub(a, b):
    return a - b