def master():
    a: int = int(input())
    b: list = list(map(int, input().split()))
    i1: int = 0
    i2: int = 0
    i1_v: int = 0
    i2_v: int = 0
    o: int = 1
    while len(b) != 0:
        if o == 1:
            if i1_v == 0:
                i1 += b[0] if b[0] > b[-1] else b[-1]
                b.pop(0 if b[0] > b[-1] else -1)
                i1_v = 1 if b[0] > b[-1] else 2
            elif i1_v == 1:
                i1 += b[-1]
                b.pop(-1)
                i1_v = 2
            elif i1_v == 2:
                i1 += b[0]
                b.pop(0)
                i1_v = 1
            o = 2

        else:
            if i2_v == 0:
                i2 += b[0] if b[0] > b[-1] else b[-1]
                b.pop(0 if b[0] > b[-1] else -1)
                i2_v = 1 if b[0] > b[-1] else 2

            elif i2_v == 1:
                i2 += b[-1]
                b.pop(-1)
                i2_v = 2

            elif i2_v == 2:
                i2 += b[0]
                b.pop(0)
                i2_v = 1
            o = 1

    print(i1, i2)
    if i1 == i2:
        print(0)
    elif i1 > i2:
        print(1)
    else:
        print(2)
    pass


if __name__ == '__main__':
    master()
