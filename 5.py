def contact_book():
    contacts = {}

    while True:
        print("\n--- Contact Book ---")
        print("1. Add Contact")
        print("2. View Contact List")
        print("3. Search Contact")
        print("4. Update Contact")
        print("5. Delete Contact")
        print("6. Exit")
        
        choice = input("Enter your choice (1-6): ")
        
        if choice == '1':
            name = input("Enter name: ").strip()
            phone = input("Enter phone number: ").strip()
            email = input("Enter email: ").strip()
            address = input("Enter address: ").strip()
            
            contacts[name] = {'phone': phone, 'email': email, 'address': address}
            print(f"Contact '{name}' added successfully.")
            
        elif choice == '2':
            if not contacts:
                print("No contacts found.")
            else:
                for name, info in contacts.items():
                    print(f"Name: {name} | Phone: {info['phone']}")
                    
        elif choice == '3':
            query = input("Enter name or phone number to search: ").strip()
            found = False
            for name, info in contacts.items():
                if query.lower() in name.lower() or query == info['phone']:
                    print(f"\nFound - Name: {name}")
                    print(f"Phone: {info['phone']}, Email: {info['email']}, Address: {info['address']}")
                    found = True
            if not found:
                print("Contact not found.")
                
        elif choice == '4':
            name = input("Enter the exact name of the contact to update: ").strip()
            if name in contacts:
                print("Leave field blank to keep current value.")
                phone = input(f"Enter new phone ({contacts[name]['phone']}): ") or contacts[name]['phone']
                email = input(f"Enter new email ({contacts[name]['email']}): ") or contacts[name]['email']
                address = input(f"Enter new address ({contacts[name]['address']}): ") or contacts[name]['address']
                
                contacts[name] = {'phone': phone, 'email': email, 'address': address}
                print("Contact updated successfully.")
            else:
                print("Contact not found.")
                
        elif choice == '5':
            name = input("Enter the exact name of the contact to delete: ").strip()
            if name in contacts:
                del contacts[name]
                print(f"Contact '{name}' deleted.")
            else:
                print("Contact not found.")
                
        elif choice == '6':
            print("Exiting Contact Book.")
            break
        else:
            print("Invalid choice. Please try again.")

if __name__ == "__main__":
    contact_book()