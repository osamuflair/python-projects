# CLI Password Manager
import csv
import base64 #for encryption
class PasswordManager:

    def __init__(self):
        self.passwords = {} #starts by creating an empty dictionary
        self.load()

    def load(self):
        #loads previously saved password from csv file
        try:
            with open("password.csv", "r") as csv_file:
              csv_reader = csv.reader(csv_file)
              next(csv_reader)
              for line in csv_reader:
                   site_name, user_name, password = line
                   decoded = base64.b64decode(password).decode()
                   #decoding the file first before calling add_password, to prevent multiple encoding
                   self.add_password(site_name, user_name, decoded)
        except FileNotFoundError:
             pass #first time executing
        

    def add_password(self, site_name, user_name, password):
        encoded = base64.b64encode(password.encode()).decode() #encodes the password
        if site_name in self.passwords:
            self.passwords[site_name].append({"user_name": user_name, "password": encoded})
        else:
            self.passwords[site_name] = [{"user_name": user_name, "password": encoded}]

    
    def view_passwords(self):
        if not self.passwords:
            print("No Password Found")
        else:
            for site_name, other in self.passwords.items():
                for value in other:
                    decoded = base64.b64decode(value['password']).decode()
                    #decodes the password before displaying it

                    print(f"Site Name: {site_name}\nUser Name: {value['user_name']}\nPassword: {decoded}")
                    print("")



    def delete_password(self, site_name, user_name):
        if site_name in self.passwords:
            for value in self.passwords[site_name]:
                if value['user_name'] == user_name:
                    self.passwords[site_name].remove(value)
                    break
            if len(self.passwords[site_name]) == 0:
                del self.passwords[site_name]

    def clear(self):
        self.passwords = {}

    def close(self):
        header = ["site_name", "user_name", "password"]

        with open("password.csv", "w", newline="") as new_csv:
            csv_writer = csv.writer(new_csv)
            csv_writer.writerow(header)

            for site_name, others in self.passwords.items():
                for item in others:
                    line = [
                         site_name,
                         item["user_name"],
                         item["password"]
                    ]
                    csv_writer.writerow(line)


def main():
    user = PasswordManager()
    print("Welcome to your Password Manager")

    while True:
        print("Press 1 to view your passwords  Press 2 to add a new password")
        print("Press 3 to delete a password    Press 4 to clear all passwords")
        print("Press 0 to close password manager")

        
        try:
            k = int(input(" "))
        except ValueError:
            print("Enter number 0 to 4")
            continue

        if k == 1:
            user.view_passwords()
            print("\n")
        elif k == 2:
            site_name = input("Enter the site name: ")
            user_name = input("Enter your username: ")
            password = input("Enter your password: ")
            user.add_password(site_name, user_name, password)
            print("\n")
        elif k == 3:
            site_name = input("Enter the site name: ")
            user_name = input("Enter the user name to be deleted: ")
            user.delete_password(site_name, user_name)
            print("\n")
        elif k == 4:
            user.clear()
            print("\n")
        elif k == 0:
            user.close()
            break
        else:
            print("Enter numbers from 0 to 4")
            print("\n")
main()