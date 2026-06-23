import json

contacts = {}

try:
    with open("contacts.json", "r") as file:
        contacts = json.load(file)
except FileNotFoundError:
    contacts = {}

def save_contacts():
    with open("contacts.json", "w") as file:
        json.dump(contacts, file, indent=4)

def add_contact():
    name = input("Enter name: ")
    phone = input("Enter phone number: ")

    contacts[name] = phone
    save_contacts()
    print("Contact added.")


def view_contacts():
    if not contacts:
        print("No contacts found.")
        return

    print("\nContacts:")
    for name, phone in contacts.items():
        print(f"{name}: {phone}")


def update_contact():
    name = input("Enter contact name: ")

    if name in contacts:
        new_phone = input("Enter new phone number: ")
        contacts[name] = new_phone
        save_contacts()
        print("Contact updated.")
    else:
        print("Contact not found.")


def delete_contact():
    name = input("Enter contact name: ")

    if name in contacts:
        del contacts[name]
        save_contacts()
        print("Contact deleted.")
    else:
        print("Contact not found.")

def search_contact():
    search_name = input("Enter contact name: ").lower()

    for name, phone in contacts.items():
        if name.lower() == search_name:
            print(f"{name}: {phone}")
            return

    print("Contact not found.")


while True:
    print("\n===== Contact Book =====")
    print("1. Add Contact")
    print("2. View Contacts")
    print("3. Update Contact")
    print("4. Delete Contact")
    print("5. Search Contact")
    print("6. Exit")

    choice = input("Enter choice: ")
    print("")

    if choice == "1":
        add_contact()

    elif choice == "2":
        view_contacts()

    elif choice == "3":
        update_contact()

    elif choice == "4":
        delete_contact()

    elif choice == "5":
        search_contact()
    
    elif choice == "6":
        print("Goodbye!")
        break

    else:
        print("Invalid choice.")