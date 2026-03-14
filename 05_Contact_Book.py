contacts={}

while True:
    print("\n1. Add Contact")
    print("2. View Contacts")
    print("3. Search Contact")
    print("4. Exit")

    choice = int(input("Enter choice: "))

    if choice==1:
        name=input("enter name: ")
        phone=input("enter phone:")
        contacts[name]=phone

    elif choice == 2:
        for name in contacts:
            print(name, ":", contacts[name])

    elif choice == 3:
        search = input("Enter name to search: ")
        if search in contacts:
            print("Phone:", contacts[search])
        else:
            print("Contact not found")

    elif choice == 4:
        break