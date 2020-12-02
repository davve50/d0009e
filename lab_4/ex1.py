def main():
    temp = []
    book = []
    com = []

    while True:
        ch = input("Phonebook> ")
        com = ch.split()
        if "add" in com:
            add(com,book,temp)
        elif "lookup" in com:
            lookup(com,book)
        elif "alias" in com:
            alias(com,book)
        elif "change" in com:
            change(com,book)
        elif "quit" in com:
            print("Exiting program...")
            break
        elif "save" in com:
            save(com,book)
        elif "load" in com:
            load(com,book)
        else:
            print("Enter a valid command!")

def add(com,book,temp):
    for x in book:
        for y in x:
            if com[1] == y:
                print("User already exists!")
                break
            elif com[2] == y:
                print("Number already exists!")
                break
    else:
        temp = [com[1],com[2]]
        book.append(temp)
    
def lookup(com,book):
    if(exist(book,com[1])):
        for x in book:
            for y in x:
                if com[1] == y:
                    print(x[1])
                    break
    else:
        print("User not found!")

def alias(com,book):
    if(exist(book,com[1])):
        if(exist(book,com[2])):
            print("User already exists!")
        else:
            for x in book:
                for y in x:
                    if com[1] == y:
                        x.append(com[2])
                        break
    else:
        print("User not found!")       

def change(com,book):
    if(exist(book,com[1])):
        for x in book:
            for y in x:
                if com[1] == y:
                    x[1] = com[2]
                    break
    else:
        print("User not found!") 

def save(com,book):
    f = open(com[1], "w")
    for i in book:
        for x in i:
            line = x + ";"
            f.write(line)
        f.write("\n")
    print("Saving...")
    f.close()

def load(com,book):
    book.clear()
    f = open(com[1], "r")
    for line in f:  
        line = line.split(";")
        line = line[:-1]
        book.append(line)
    print("Loading...")
    f.close()

def exist(book,user):
    for i in book:
        for x in i:
            if user == x:
                return True
    else:
        return False
    
if __name__ == "__main__":
    main()