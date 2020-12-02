def menu():
    word = []
    desc = []

    while True:
        print("""
        1. Insert
        2. Lookup
        3. Delete
        4. Exit
        """)

        ch = input("> ")

        if ch == "1":
            w = input("Insert a word: ")
            if w not in word:
                word.append(w)
                d = input("Add a description to "+w+": ")
                desc.append(d)
            else:
                print(w+" Already exists")

        elif ch == "2":
            l = input("Word to lookup: ")
            if l in word:
                print("Description for",l,"is: ",desc[word.index(l)])
            else:
                print("Word not in dictionary!")

        elif ch == "3":
            d = input("Word to delete: ")
            if d in word:
                index = word.index(d)
                del word[index]
                del desc[index]
            else:
                print("Word not in dictionary!")
                
        elif ch == "4":
            print("Exiting program...")
            break

        else:
            print("Enter a vaild input!")

def main():
    menu()

if __name__ == "__main__":
    main()