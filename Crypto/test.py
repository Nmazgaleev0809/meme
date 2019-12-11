from cryptography.fernet import Fernet

file = open('key2.key', 'rb') #wb when writing rb when reading
key = file.read()
file.close()
a = 0
while a == 0:
    password = input('''Please enter a password
>''')
    confirm_password = input('''Please confirm your password
>''')
    if password == confirm_password:
        print("Confirmation succesfull")
        a = 1
    else:
        print('Error, please try again')
encoded = password.encode()
f = Fernet(key)
encrypted = f.encrypt(encoded)

file = open('password.txt', 'wb')
file.write(encrypted)
file.close()
print(encrypted)