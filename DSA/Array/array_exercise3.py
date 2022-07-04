def odd_number(max):
    list = []
    for i in range(1,max+1):
        if i % 2 != 0:
            list.append(i)
    print (list)


if __name__ == '__main__':
    n = int(input())
    odd_number(n)
