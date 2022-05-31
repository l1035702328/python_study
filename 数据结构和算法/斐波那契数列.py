def fib(n):
    if n == 1:
        return [1]
    fibs = [1, 1]
    if n == 2:
        return fibs
    for i in range(2, n):
        fibs.append(fibs[-1]+fibs[-2])
    return fibs


if __name__ == '__main__':
    print(fib(10))


