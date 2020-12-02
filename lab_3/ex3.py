def menu():
    dictionary = {}

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
            if w not in dictionary:
                d = input("Add a description to "+w+": ")
                dictionary[w] = d
            else:
                print(w+" Already exists")

        elif ch == "2":
            l = input("Word to lookup: ")
            b = False
            for w, d in dictionary.items():
               if w == l:
                   print("Description for",w,"is:",d)
                   b = True
                   break
            if b == False:
                print("Word not in dictionary!")

        elif ch == "3":
            d = input("Word to delete: ")
            if d in dictionary:
                dictionary.pop(d)
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