import math

def derivative(f,x,h):
    return 1.0 / (2 * h) * (f(x + h) - f(x - h))

def solve(f,x0,h):
    x = 0
    while True:
        x = x0 - (f(x0) / derivative(f, x0, h))
        if abs(x - x0) < h:
            return x
        x0 = x


def main():
    print(derivative(math.sin,math.pi,0.0001))
    

if __name__ == "__main__":
    main()