class Contact:
    def __init__(self, name: str, phone: str, email: str, address: str):
        self.name = name
        self.phone = phone
        self.email = email
        self.address = address

    def __str__(self):
        return f"{self.name} - {self.phone} | {self.email} | {self.address}"


class ContactBook:
    def __init__(self):
        self.contacts = []

    def add_contact(self, name, phone, email, address):
        if not name.strip():
            print("Name cannot be empty. Contact not added.")
            return
        contact = Contact(name.strip(), phone.strip(), email.strip(), address.strip())
        self.contacts.append(contact)
        print(f"Contact '{contact.name}' added successfully.")

    def view_contacts(self):
        if not self.contacts:
            print("No contacts available.")
            return
        print("\nContact List:")
        for i, contact in enumerate(self.contacts, 1):
            print(f"{i}. {contact}")

    def search_contact(self, query):
        query = query.strip().lower()
        results = [c for c in self.contacts if query in c.name.lower() or query in c.phone.lower()]
        if not results:
            print("No matching contacts found.")
            return
        print("\nSearch Results:")
        for i, contact in enumerate(results, 1):
            print(f"{i}. {contact}")

    def update_contact(self, name):
        name = name.strip().lower()
        for contact in self.contacts:
            if contact.name.lower() == name:
                new_name = input(f"Enter new name (current: {contact.name}): ").strip()
                new_phone = input(f"Enter new phone number (leave blank to keep '{contact.phone}'): ").strip()
                new_email = input(f"Enter new email (leave blank to keep '{contact.email}'): ").strip()
                new_address = input(f"Enter new address (leave blank to keep '{contact.address}'): ").strip()

                if new_name:
                    contact.name = new_name
                if new_phone:
                    contact.phone = new_phone
                if new_email:
                    contact.email = new_email
                if new_address:
                    contact.address = new_address

                print("Contact updated successfully.")
                return
        print("Contact not found.")

    def delete_contact(self, name):
        name = name.strip().lower()
        for contact in list(self.contacts):  # iterate over a copy
            if contact.name.lower() == name:
                self.contacts.remove(contact)
                print("Contact deleted successfully.")
                return
        print("Contact not found.")

    def display_menu(self):
        while True:
            print("\nContact Book Menu:")
            print("1. Add Contact")
            print("2. View Contacts")
            print("3. Search Contact")
            print("4. Update Contact")
            print("5. Delete Contact")
            print("6. Exit")
            choice = input("Enter your choice: ").strip()

            if choice == '1':
                name = input("Enter name: ")
                phone = input("Enter phone: ")
                email = input("Enter email: ")
                address = input("Enter address: ")
                self.add_contact(name, phone, email, address)
            elif choice == '2':
                self.view_contacts()
            elif choice == '3':
                query = input("Enter name or phone to search: ")
                self.search_contact(query)
            elif choice == '4':
                name = input("Enter the name of the contact to update: ")
                self.update_contact(name)
            elif choice == '5':
                name = input("Enter the name of the contact to delete: ")
                self.delete_contact(name)
            elif choice == '6':
                print("Exiting Contact Book.")
                break
            else:
                print("Invalid choice. Try again.")


def main():
    contact_book = ContactBook()
    contact_book.display_menu()


if __name__ == "__main__":
    main()