def is_prime3(n):
    if n <= 1:
        return False
    i = 2
    while i * i < n:
        if n % i == 0:
            return False
        i += 1
    return True


if __name__ == '__main__':
    count = 0
    for i in range(1, 1000000):
        if is_prime3(i):
            count += 1
    print(count)
