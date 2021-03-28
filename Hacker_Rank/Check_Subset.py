for _ in range(int(input())):
    n, seta = input(), set(input().split())
    m, setb = input(), set(input().split())
    print(all([i in setb for i in seta])) 