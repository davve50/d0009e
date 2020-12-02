def bounce(n):
    if n > 0:
        print(n, end=" ")
        bounce(n-1)
        print(n, end=" ")
        return
    else:
        print(n, end=" ")
    
def bounce2(n):
    m = n
    while(n > 0):
        print(n, end=" ")
        n = n - 1
    while(n != m):
        print(n, end=" ")
        n = n + 1
    else:
        print(n, end=" ")

def tvarsumman(n):
    if n > 0:
        return (n%10 + tvarsumman(int(n/10)))
    else:
        return 0
    


def tvarsumman2(n):
    m=0
    while n>0:
        m = m + int((n%10))
        n = n/10
    print(m)
    

def main():
    #bounce(5)
    #bounce2(5)
    print(tvarsumman(1235))
    #tvarsumman2(123)


if __name__ == "__main__":
    main()