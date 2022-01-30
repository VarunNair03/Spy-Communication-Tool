from json import load
from cryptography.fernet import Fernet
from key_generator import generate_key

def load_key():
    return open('secret.key','rb').read()

def encrypt_message(message):
    #generating the key from the generate key module. The key changes each time a message is passed into this function
    fernet = Fernet(load_key())
    encrypted_message = fernet.encrypt(message.encode())
    return encrypted_message

def decrypt_message(encrypted_message):
    fernet = Fernet(load_key())
    decode_message = (fernet.decrypt(encrypted_message)).decode()
    return decode_message


