def menu():
    temp = []
    final = []

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
            for x,d in final:                                     
                if x == w:                                            
                    print(w+" Already exists")
                    break            
            else:                                                       
                d = input("Add a description to "+w+": ")
                temp.append(w)                                     
                temp.append(d)
                t = tuple(temp)                                
                final.append(t)                                
                del temp[:]

        elif ch == "2":
            l = input("Word to lookup: ")
            b = False
            for x,d in final: 
                if x == l:
                    print("Description for",l,"is: ",d)
                    b = True
            if b == False:
                print("Word not in dictionary!")

        elif ch == "3":
            d = input("Word to delete: ")
            b = False
            for x in final:
                if x[0] == d:
                    final.pop(0)
                    b = True
                    break
            if b == False:
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