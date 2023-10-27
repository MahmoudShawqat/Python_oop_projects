# Register and login system
import os

class UserDatabase:
    def __init__(self, filename):
        # Initialize an empty dictionary to store user data
        self.db_users = {}
        # Store the filename
        self.filename = filename
        # Load existing users from the file
        self.load_users()

    # Method to load existing users from the file
    def load_users(self):
        try:
            # If the file doesn't exist, create an empty file
            if not os.path.isfile(self.filename):
                open(self.filename, "w").close()
            # Read user data from the file and store it in the dictionary
            with open(self.filename, "r") as file:
                for line in file:
                    line = line.strip().split(",")
                    self.db_users[line[0]] = line[1]
        except Exception as e:
            print(f"An error occurred: {e}")

    # Method to register a new user
    def register_user(self):
        try:
            while True:
                # Prompt the user for username and password
                username = input("Enter a username: ")
                password = input("Enter a password: ")

                # Check if the username already exists
                if username in self.db_users:
                    print("Username already exists. Please choose a different username.")
                else:
                    # If the username is unique, write the new user data to the file
                    with open(self.filename, "a+") as file:
                        file.write(f"{username},{password}\n")
                    print("Registration successful.")
                    break
        except Exception as e:
            print(f"An error occurred: {e}")

    # Method to authenticate a user
    def login(self):
        try:
            # Prompt the user for username and password
            username = input("Enter your username: ")
            password = input("Enter your password: ")

            # Check if the username and password are valid
            if username in self.db_users and self.db_users[username] == password:
                print("Login successful.")
            else:
                print("Invalid username or password.")
        except Exception as e:
            print(f"An error occurred: {e}")

    # Method to display the main menu
    def show_menu(self):
        try:
            # Display the menu options
            print("Menu:\n1. Register\n2. Login\n3. Exit")
            # Get the user's choice
            user_choice = input("")
            # Perform the selected action based on the user's choice
            if user_choice == "1":
                self.register_user()
            elif user_choice == "2":
                self.login()
            elif user_choice == "3":
                return
            else:
                print("Invalid choice. Please try again.")
        except Exception as e:
            print(f"An error occurred: {e}")
            
# Run the program if this script is executed directly
if __name__ == "__main__":
    # Initialize the UserDatabase with the specified file
    db = UserDatabase("user_data.txt")
    # Show the main menu
    db.show_menu()
