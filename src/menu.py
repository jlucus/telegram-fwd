def show_menu():
    menu_options = """
    Please choose an option:
    1. Compose a new message
    2. Send a message to a specific channel
    3. Filter messages
    4. Exit
    """
    print(menu_options)
    choice = input("Enter your choice: ")

    if choice == '1':
        compose_message()
    elif choice == '2':
        send_to_channel()
    elif choice == '3':
        filter_messages()
    elif choice == '4':
        print("Exiting the menu.")
    else:
        print("Invalid choice. Please try again.")
        show_menu()

def compose_message():
    message = input("Enter your message: ")
    print(f"Composed message: {message}")
    # Logic to send the message can be added here

def send_to_channel():
    channel_id = input("Enter the channel ID: ")
    message = input("Enter your message: ")
    print(f"Sending message to channel {channel_id}: {message}")
    # Logic to send the message to the specified channel can be added here

def filter_messages():
    print("Filtering options will be implemented here.")
    # Logic for filtering messages can be added here