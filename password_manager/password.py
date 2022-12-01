from cryptography.fernet import Fernet


def write_key():
    key = Fernet.generate_key()
    with open('password_manager/key.key','Wb') as key_file:
        key_file.write(key)


def load_key():
    file = open('password_manager/key.key','rb')
    key = file.read()
    file.close()
    return key

pwd = input ("What is the master password? ")
key =load_key() + pwd.encode()
fer =Fernet(key)

def view():
    with open('password_manager/password.txt', 'r') as f:
        for line in f.readlines():
            data = line.rstrip()
            user, passw = data.split("|")
            print("user: ", user, "| Password: ", fer.decrypt(passw.encode()).decode())

def add():
    user = input("Ente name: ")
    passw = input("Password: ")
    with open('password_manager/password.txt', 'a') as f:
        f.write(user+ " | "+ fer.encrypt(passw.encode()).decode() + "\n")

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