from cryptography.fernet import Fernet

file = open('key.key', 'rb')
key = file.read()
file.close()

message = input('>')
encoded = message.encode()

f = Fernet(key)
encrypted = f.encrypt(encoded)
print(encoded)
print(encrypted)
