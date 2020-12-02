def kostnad(P, r, a):
    k = P + (a+1)*(P*r/2)
    return print("Den totala kostnaden efter",a,"år är",int(k),"kr")

def main():
    kostnad(50000, 0.03, 10)

if __name__ == "__main__":
    main()
