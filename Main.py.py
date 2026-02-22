users = {}
events = []
registrations = {}

def register():
    username = input("Enter username: ")
    password = input("Enter password: ")
    role = input("Enter role (admin/student): ")

    if username in users:
        print("User already exists ❌")
    else:
        users[username] = {"password": password, "role": role}
        print("Registration successful ✅")

def login():
    username = input("Enter username: ")
    password = input("Enter password: ")

    if username in users and users[username]["password"] == password:
        print("Login successful ✅")
        if users[username]["role"] == "admin":
            admin_menu()
        else:
            student_menu(username)
    else:
        print("Invalid credentials ❌")

def admin_menu():
    while True:
        print("\n--- Admin Menu ---")
        print("1. Add Event")
        print("2. View Events")
        print("3. Logout")

        choice = input("Enter choice: ")

        if choice == "1":
            event_name = input("Enter event name: ")
            events.append(event_name)
            print("Event added ✅")
        elif choice == "2":
            print("Events:")
            for i, event in enumerate(events):
                print(f"{i+1}. {event}")
        elif choice == "3":
            break
        else:
            print("Invalid choice")

def student_menu(username):
    while True:
        print("\n--- Student Menu ---")
        print("1. View Events")
        print("2. Register for Event")
        print("3. Logout")

        choice = input("Enter choice: ")

        if choice == "1":
            print("Events:")
            for i, event in enumerate(events):
                print(f"{i+1}. {event}")

        elif choice == "2":
            event_number = int(input("Enter event number: ")) - 1
            if 0 <= event_number < len(events):
                registrations.setdefault(username, []).append(events[event_number])
                print("Registered successfully ✅")
            else:
                print("Invalid event number ❌")

        elif choice == "3":
            break
        else:
            print("Invalid choice")

def main():
    while True:
        print("\n=== College Club System ===")
        print("1. Register")
        print("2. Login")
        print("3. Exit")

        choice = input("Enter choice: ")

        if choice == "1":
            register()
        elif choice == "2":
            login()
        elif choice == "3":
            print("Goodbye 👋")
            break
        else:
            print("Invalid choice")
register()