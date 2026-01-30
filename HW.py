slam_book = []

def add_friends():
    name = input("Enter name: ")
    phone = input("Enter phone number:")
    fav_food = input("Enter favourite food:")

    friend = {
        "Name": name,
        "Phone": phone,
        "Favourite Food": fav_food
    }

    slam_book.append(friend)
    print("Friend added successfully! \n")

def view_friend():
    if not slam_book:
        print("Slam Book is empty. \n")
    else:
        for i, friend in enumerate(slam_book, start=1):
            print(f"\nFriend {i}")
            print("Name:",friend["Name"])
            print("Phone:", friend["Phone"])
            print("Fvourite Food:", friend["Favourite Food"])
        print()

while True:
    print("SLAM BOOK MENU")
    print("1. Add Friend")
    print("2. View Friends")
    print("3. Exit")

    choice = input("Enter your choice: ")

    if choice == "1":
        add_friends()
    elif choice == "2":
        view_friend()
    elif choice == "3":
        print("Exiting Slam Book. Bye!")
        break
    else:
        print("Invalid choice. Try again. \n")



