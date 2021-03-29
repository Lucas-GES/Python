cube = lambda x: x**3

def fibonacci(n):
    v0, v1 = 0, 1
    fibs = list()
    for _ in range(n):
        fibs.append(v0)
        v0, v1 = v1, v0+v1

    print(fibs)
    return fibs

if __name__ == '__main__':
    n = int(input())
    print(list(map(cube, fibonacci(n))))