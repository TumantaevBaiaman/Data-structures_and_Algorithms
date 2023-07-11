def master():
    a, b = map(int, input().split())
    for i in range(a, b+1):
        f = 0
        g = []
        if a==b:
            print("Absent")
        else:
            for j in range(a, b+1):
                if f>=3:
                    print("Absent")
                    break
                elif i%j==0:
                    f += 1
                    g.append(j)
            print(g)


if __name__ == '__main__':
    master()
