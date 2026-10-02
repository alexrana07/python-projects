from cryptography.fernet import Fernet


# makes a new key and saves it in a file
def write_key():
    key = Fernet.generate_key()
    with open("key.key", "wb") as key_file:
        key_file.write(key)


# reads the key from the file
def load_key():
    file = open("key.key", "rb")
    key = file.read()
    file.close()
    return key


# run this line ONCE to make the key file, then put the # back
# write_key()

key = load_key()
fer = Fernet(key)


# saves a new password
def add():
    with open("passwords.txt", "a") as f:
        name = input("Account Name: ")
        password = input("Password: ")
        # lock the password before saving it
        f.write(name + "|" + fer.encrypt(password.encode()).decode() + "\n")


# shows all saved passwords
def view():
    with open("passwords.txt", "r") as f:
        for line in f.readlines():
            data = line.strip()
            # split the line into name and locked password
            name, password = data.split("|")
            # unlock the password before showing it
            print("Account:", name, "| Password:", fer.decrypt(password.encode()).decode())


while True:
    choice = input("Would you like to add a new password or view existing ones? (add/view) or 'q' to quit: ").strip().lower()

    if choice == "q":
        break

    elif choice == "add":
        add()

    elif choice == "view":
        view()

    else:
        print("Invalid input. Please enter 'add', 'view', or 'q' to quit.")