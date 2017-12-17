from collections import Counter


def rm_duplicate(n):
    counter = Counter(n)
    ret = []
    for i in n:
        if counter[i] == 1:
            ret.append(i)
        elif counter[i] == -1:
            continue
        else:
            ret.append(i)
            counter[i] = -1
    return ret


if __name__ == '__main__':
    print(rm_duplicate([1, 2, 4, 5, 7, 1, 1, 3, 4, 4, 7, 9, 7]))
