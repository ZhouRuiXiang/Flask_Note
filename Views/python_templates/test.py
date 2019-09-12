def recurive(n, a, b, c):
    if n == 1:
        global count
        count = count + 1
        print(a + ' ->' + c)
        return
    recurive(n-1, a, c, b)
    recurive(1, a, b, c)
    recurive(n-1, b, a, c)


if __name__ == '__main__':
    count = 0
    recurive(3, 'a', 'b', 'c')
    print('最少移动次数：', count)



