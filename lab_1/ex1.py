def recept(a):
    return print("Ingredienser för:",a,"personer" "\n"
        "Smör: ",(85/4)*a," g"  "\n"
        "Ströbröd: ", (0.75/4)*a, " dl" "\n"
        "Ägg: ", int((3/4)*a+0.5), " st" "\n"
        "Strösocker: ", (3/4)*a, " dl" "\n" 
        "Vaniljsocker: ", (2/4)*a, " tsk" "\n"
        "Bakpulver: ", (2/4)*a, " tsk" "\n"
        "Vetemjöl: ", (3/4)*a, " dl" "\n"
        "Vatten: ", (1/4)*a, " dl")

def tidblanda(a):
    f = 10
    return (a+f)

def tidgradda(a):
    f = 30
    r = 3 * a
    return (r+f)

def sockerkaka(a):
    recept(a)
    print(tidblanda(a) + tidgradda(a) , "minuter")

def main():
    sockerkaka(4)
    print("\n")
    sockerkaka(7)

if __name__ == "__main__":
    main()


