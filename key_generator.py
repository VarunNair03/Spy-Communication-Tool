from cryptography.fernet import Fernet

def generate_key():
    key = Fernet.generate_key()
    with open('secret.key','wb') as key_file: 
        key_file.write(key) #this allows us to store the key in a .key file so that we can access it throughout the folder for encrytion and decryption
        print("key is generated!") 