def parse_input(user_input):
    """
    Parses user input into a command and arguments.
    Handles empty inputs gracefully to prevent unpacking errors.
    """
    parts = user_input.split()
    if not parts:
        return "", []
    cmd = parts[0].strip().lower()
    args = parts[1:]
    return cmd, args

def add_contact(args, contacts):
    """
    Adds a new contact to the contacts dictionary.
    """
    try:
        name, phone = args
        contacts[name] = phone
        return "Contact added."
    except ValueError:
        return "Error: Please specify both username and phone. Usage: add [username] [phone]"

def change_contact(args, contacts):
    """
    Changes the phone number for an existing contact.
    """
    try:
        name, phone = args
        if name in contacts:
            contacts[name] = phone
            return "Contact updated."
        else:
            return f"Error: Contact '{name}' not found."
    except ValueError:
        return "Error: Please specify both username and phone. Usage: change [username] [phone]"

def show_phone(args, contacts):
    """
    Displays the phone number for a specified contact.
    """
    try:
        name = args[0]
        if name in contacts:
            return contacts[name]
        else:
            return f"Error: Contact '{name}' not found."
    except IndexError:
        return "Error: Please specify username. Usage: phone [username]"

def show_all(contacts):
    """
    Returns a formatted string containing all saved contacts.
    """
    if not contacts:
        return "No contacts found."
    
    result = []
    for name, phone in contacts.items():
        result.append(f"{name}: {phone}")
    return "\n".join(result)

def main():
    contacts = {}
    print("Welcome to the assistant bot!")
    
    while True:
        try:
            user_input = input("Enter a command: ")
        except (KeyboardInterrupt, EOFError):
            print("\nGood bye!")
            break
            
        command, args = parse_input(user_input)

        if not command:
            continue

        if command in ["close", "exit"]:
            print("Good bye!")
            break
        elif command == "hello":
            print("How can I help you?")
        elif command == "add":
            print(add_contact(args, contacts))
        elif command == "change":
            print(change_contact(args, contacts))
        elif command == "phone":
            print(show_phone(args, contacts))
        elif command == "all":
            print(show_all(contacts))
        else:
            print("Invalid command.")

if __name__ == "__main__":
    main()
