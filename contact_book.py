user_input = ""
contacts = {}

# Open the file in read mode.
try:
    with open("contact_book.txt", "r") as file:
        for line in file:
            parts = line.split(":")
            name = parts[0]
            number = parts[1].strip()
            # When Python reads a line from a file, it includes \n at the end, and strip() removes it.
            contacts[name] = number

except FileNotFoundError:
    pass


def add_contact():
    contact_name = input("Enter name: ").strip()
    if contact_name == "":
        print("Contact cannot be empty")
    elif contact_name in contacts:
        print("Contact already exists")
    else:
        contact_number = input("Enter contact number: ").strip()
        if contact_number == "":
            print("Number cannot be empty")
        elif contact_number in contacts.values():
            print("Number already exists")
        else:
            contacts[contact_name] = contact_number
            print("Contact added successfully!")


def search_contact():
    print("""Search by:
1. Name
2. Number
  """)

    option = input("Choose an option: ")

    if option == "1":
        search_name = input("Enter contact name: ")
        if search_name in contacts:
            print(f"Name :{search_name} ")
            print(f"Number : {contacts[search_name]}")
        else:
            print("Contact not found.")

    elif option == "2":
        search_number = input("Enter contact number: ")
        for contact_name, contact_number in contacts.items():
            if search_number == contact_number:
                print(f"Name : {contact_name}")
                print(f"Number : {search_number}")
                break

        else:
            print("Contact not found.")

    else:
        print("Invalid option")


def update_contact():
    contact_name = input("Enter contact name: ")
    if contact_name in contacts:
        updated_number = input("Enter new number: ")
        if updated_number in contacts.values():
            print("Number already exists")
        else:
            contacts[contact_name] = updated_number
            print("Updated Successfully!")
    else:
        print("Contact doesn't exist")


def delete_contact():
    contact_name = input("Enter contact name: ")
    if contact_name in contacts:
        contacts.pop(contact_name)
        print("Deleted Successfully!")
    else:
        print("Contact doesn't exist")


def show_contact():
    print("Contacts: ")
    for contact_name in sorted(contacts):  # ~ for key in sorted(dictionary)
        print(f"{contact_name} : {contacts[contact_name]}")


while True:
    print("""========== CONTACT BOOK ==========

  1. Add Contact
  2. Search Contact
  3. Update Contact
  4. Delete Contact
  5. Show All Contacts
  6. Exit
""")
    user_input = input("Choose an option: ")

    if user_input == "1":
        add_contact()
    elif user_input == "2":
        search_contact()
    elif user_input == "3":
        update_contact()
    elif user_input == "4":
        delete_contact()
    elif user_input == "5":
        show_contact()
    elif user_input == "6":
        with open("contact_book.txt", "w") as file:
            for contact_name, contact_number in contacts.items():
                file.write(f"{contact_name}:{contact_number}\n")
        break
    else:
        print("Invalid option")
