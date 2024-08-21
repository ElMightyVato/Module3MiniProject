import re

# Main menu created first to see the type of functions I need to create for each option.
def main_menu():
    while True:
        print("\nWelcome to the Contact Management System!")
        print("Menu:")
        print("1. Add a new contact")
        print("2. Edit an existing contact")
        print("3. Delete a contact")
        print("4. Search for a contact")
        print("5. Display all contacts")
        print("6. Export contacts to a text file")
        print("7. Import contacts from a text file")
        print("8. Quit")

        try:
            choice = int(input("Please choose an option (1-8): "))
        except ValueError:
            print("Invalid input. Please enter a number between 1 and 8.")
            continue

        if choice == 1:
            add_contact()
        elif choice == 2:
            edit_contact()
        elif choice == 3:
            delete_contact()
        elif choice == 4:
            search_contact()
        elif choice == 5:
            display_all_contacts()
        elif choice == 6:
            export_contacts()
        elif choice == 7:
            import_contacts()
        elif choice == 8:
            print("Goodbye!")
            break
        else:
            print("Invalid option. Please choose a number between 1 and 8.")

# I'm using a dictionary to store the contacts
contacts = {}

# Regular expressions for input validation
email_regex = r'^[a-zA-Z0-9_.+-]+@[a-zA-Z0-9-]+\.[a-zA-Z0-9-.]+$'  #using these to make sure they are inputing the correct information
phone_regex = r'^\+?[0-9]{7,15}$'

# Helper functions
def add_contact():
    print("\n--- Add a New Contact ---")
    phone = input("Enter phone number (unique identifier): ")
    if not re.match(phone_regex, phone):
        print("Invalid phone number format. Must be 7-15 digits.")
        return

    if phone in contacts:
        print("This phone number already exists.")
        return

    name = input("Enter name: ")
    email = input("Enter email: ")
    if not re.match(email_regex, email):
        print("Invalid email format.")
        return

    additional_info = input("Enter additional information (address, notes, etc.): ")

    contacts[phone] = {
        'Name': name,
        'Phone': phone,
        'Email': email,
        'Additional Info': additional_info
    }
    print(f"Contact {name} added successfully.")

def edit_contact():
    print("\n--- Edit an Existing Contact ---")
    phone = input("Enter phone number of the contact to edit: ")
    if phone not in contacts:
        print("Contact not found.")
        return

    name = input(f"Enter new name (leave blank to keep '{contacts[phone]['Name']}'): ") or contacts[phone]['Name']
    email = input(f"Enter new email (leave blank to keep '{contacts[phone]['Email']}'): ") or contacts[phone]['Email']
    if not re.match(email_regex, email):
        print("Invalid email format.")
        return
    additional_info = input(f"Enter new additional information (leave blank to keep '{contacts[phone]['Additional Info']}'): ") or contacts[phone]['Additional Info']

    contacts[phone] = {
        'Name': name,
        'Phone': phone,
        'Email': email,
        'Additional Info': additional_info
    }
    print("Contact updated successfully.")

def delete_contact():
    print("\n--- Delete a Contact ---")
    phone = input("Enter phone number of the contact to delete: ")
    if phone in contacts:
        del contacts[phone]
        print("Contact deleted.")
    else:
        print("Contact not found.")

def search_contact():
    print("\n--- Search for a Contact ---")
    phone = input("Enter phone number of the contact to search for: ")
    if phone in contacts:
        print(f"Name: {contacts[phone]['Name']}")
        print(f"Phone: {contacts[phone]['Phone']}")
        print(f"Email: {contacts[phone]['Email']}")
        print(f"Additional Info: {contacts[phone]['Additional Info']}")
    else:
        print("Contact not found.")

def display_all_contacts():
    print("\n--- All Contacts ---")
    if not contacts:
        print("No contacts to display.")
    else:
        for phone, info in contacts.items():
            print(f"Name: {info['Name']}")
            print(f"Phone: {info['Phone']}")
            print(f"Email: {info['Email']}")
            print(f"Additional Info: {info['Additional Info']}\n")

# Export contacts to a text file (plain text)
def export_contacts():
    print("\n--- Export Contacts to File ---")
    filename = input("Enter the file name to export contacts (e.g., contacts.txt): ")
    try:
        with open(filename, 'w') as file:
            for phone, info in contacts.items():
                file.write(f"{phone},{info['Name']},{info['Email']},{info['Additional Info']}\n")
        print(f"Contacts successfully exported to {filename}.")
    except Exception as e:
        print(f"An error occurred while exporting contacts: {e}")

# Import contacts from a text file (plain text)
def import_contacts():
    print("\n--- Import Contacts from File ---")
    filename = input("Enter the file name to import contacts from (e.g., contacts.txt): ")
    try:
        with open(filename, 'r') as file:
            for line in file:
                contact_data = line.strip().split(',')
                if len(contact_data) == 4:
                    phone, name, email, additional_info = contact_data
                    if re.match(phone_regex, phone) and re.match(email_regex, email):
                        contacts[phone] = {
                            'Name': name,
                            'Phone': phone,
                            'Email': email,
                            'Additional Info': additional_info
                        }
        print(f"Contacts successfully imported from {filename}.")
    except Exception as e:
        print(f"An error occurred while importing contacts: {e}")



# Run the CMS
if __name__ == "__main__":
    main_menu()
