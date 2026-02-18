def listoperation():
    list = [1,2,3,4,5]
    
    while True:
        print("\n list operation new")
        print("1. append an element")
        print("2. insert a element at given position")
        print("3. remove an element")
        print("4. pop an element")
        print("5. display the list")
        print("6. sort the list")
        print("7. reverse the list")
        print("8. exit")

        choice = int(input("enter the choice"))

        if choice==1:
            val = int(input("enter the val"))
            list.append(val)
        elif choice == 2:
            val = int(input("enter val"))
            pos = int(input("enter pos"))
            list.insert(pos,val)
        elif choice == 3:
            print(list)
            val = int(input("enter which you want to remove"))
            list.remove(val)
        elif choice == 4:
            list.pop()
        elif choice==5:
            print(list)
        elif choice==6:
            list.sort()
        elif choice == 7:
            list.reverse()
        elif choice==8:
            return
        else:
            print("invalid choice")
listoperation()