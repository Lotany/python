pwd = input ("What is the master password? ")

#pip install cryptography

def view():
    with open('password_manager/password.txt', 'r') as f:
        for line in f.readlines():
            data = line.rstrip()
            user, passw = data.split("|")
            print("user: ", user, "| Password: ", passw)

def add():
    user = input("Ente name: ")
    passw = input("Password: ")
    with open('password_manager/password.txt', 'a') as f:
        f.write(user+ " | "+ passw + "\n")

while True:
    mode = input("Would you like to ad a new password or view existing ones(view/add/q) ").lower()
    if mode =="q":
        break

    if mode == "view":
        view()
    elif mode == "add":
        add()

    else:
        print("Invalid Mode. ")