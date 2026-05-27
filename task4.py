def parse_input(user_input):
    parts = user_input.split()
    if not parts:
        return "", []
    cmd = parts[0].strip().lower()
    args = parts[1:]
    return cmd, args

def add_contact(args, contacts):
    try:
        name, phone = args
        contacts[name] = phone
        return "Contact added."
    except ValueError:
        return "Error: Please specify both username and phone. Usage: add [username] [phone]"

def change_contact(args, contacts):
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
    try:
        name = args[0]
        if name in contacts:
            return contacts[name]
        else:
            return f"Error: Contact '{name}' not found."
    except IndexError:
        return "Error: Please specify username. Usage: phone [username]"

def show_all(contacts):
    if not contacts:
        return "No contacts found."
    
    result = []
    for name, phone in contacts.items():
        result.append(f"{name}: {phone}")
    return "\n".join(result)

def show_help():
    return (
        "Available commands:\n"
        "  help                    - show this help message\n"
        "  hello                   - greet the bot\n"
        "  add [username] [phone]  - add a new contact\n"
        "  change [username] [phone]- update an existing contact's phone\n"
        "  phone [username]        - show the phone number of a contact\n"
        "  all                     - show all saved contacts\n"
        "  exit / close            - exit the assistant bot"
    )

def main():
    contacts = {}
    print("Welcome to the assistant bot! (Type 'help' to see available commands)")
    
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
        elif command == "help":
            print(show_help())
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
