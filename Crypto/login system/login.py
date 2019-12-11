from cryptography.fernet import Fernet
import os

file = open('key.key', 'rb')
key = file.read()
file.close()
f = Fernet(key)
file1 = 0
name = 0
password = 0
a = 0
while a == 0:
    ls = input('''Enter 1 to login
Enter 2 to sign up
>''')
    if ls == '1':
        name = input('''Please enter your name
>''')
        password = input('''Please enter your password
>''')
        if os.path.isfile('./'+name+'.txt.encrypted'):
            print('Account found')
            with open('./'+name+'.txt.encrypted', 'rb') as f:
                data = f.read()
    
            fernet = Fernet(key)
            decrypted = fernet.decrypt(data)
            decoded = decrypted.decode()
            if password == decoded:
                print('Confirmation succesull')
            else:
                print('Error')
        else:
            print('Account not found')
            
        a = 1
    elif ls == '2':
        a = 1
        name = input('''Please enter your name
>''')
        password = input('''Please enter a password
>''')
        encoded = password.encode()
        f = Fernet(key)
        encrypted = f.encrypt(encoded)
        
        file = open(name+'.txt.encrypted', 'wb')
        file.write(encrypted)
        file.close()
        
    else:
        print('Error, Try again')
        