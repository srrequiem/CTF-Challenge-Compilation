from Crypto.Cipher import AES
from Crypto.Random.random import randint
from hashlib import sha256
import signal
import os
import sys

assert("FLAG" in os.environ)
flag = os.environ["FLAG"]
assert(flag.startswith("flag{"))
assert(flag.endswith("}"))

allow_pin_recover = False # This function is not ready, let's disable it

db = {}
recover_db = {}

def handler(signum, frame):
    print("Time's up!")
    exit()

def hash_psw(pin1, pin2, passphrase = b"donttrustbigred!"):
    c1 = AES.new(expand_pin(pin1), AES.MODE_ECB)
    c2 = AES.new(expand_pin(pin2), AES.MODE_ECB)
    return c1.encrypt(c2.decrypt(c1.encrypt(passphrase))).hex()

def login():
    username = input("Username: ").encode()
    user_pin = input("Your pin: ").encode()
    server_pin = input("Server pin: ").encode()

    if username not in db:
        print("Username not found")
    elif db[username] != hash_psw(user_pin, server_pin):
        print(f"Auth failed.")
    else:
        print(f"Logged in as {username.decode()}")
        if username == b"admin":
            print(flag)

def register():
    username = input("Username (min 3 characters): ")
    if username.encode() in db or len(username) < 3:
        print("Username too short or already in use!")
        return
    user_pin = input("Your pin (6 digits): ").encode()
    if not user_pin.isdigit() or len(user_pin) != 6:
        print("Invalid pin")
        return
    passphrase = input("Recovery password (16 bytes, hex encoded): ")
    if len(passphrase) != 32:
        print("Wrong length!")
        return
    try:
        passphrase = bytes.fromhex(passphrase)
        server_pin = str(randint(1,999999)).zfill(6)
        print(f"Server pin for the user {username}: {server_pin}")
        token = hash_psw(user_pin, server_pin.encode())
        token2 = hash_psw(user_pin, server_pin.encode(), passphrase)
        db[username.encode()] = token
        recover_db[username.encode()] = (user_pin, server_pin.encode(), token2)
        print(f"User {username}:{token} successfully created!")
    except:
        print("Something's wrong...")

def pin_recover():
    username = input("Username: ").encode()
    passphrase = input("Recovery password (hex): ")
    passphrase = bytes.fromhex(passphrase)
    if username not in db:
        print("Username not found")
    else:
        pin1, pin2, token = recover_db[username]
        pass_token = hash_psw(pin1, pin2, passphrase)
        print(f"DEBUG token: {pass_token}") # TODO: remove this
        if pass_token == token and allow_pin_recover:
            print(pin1, pin2)
        else:
            print("Pin is not valid or function disabled by the administrator.")

def initialize_db():
    admin_pin1 = str(randint(1,999999)).zfill(6).encode()
    admin_pin2 = str(randint(1,999999)).zfill(6).encode()
    admin_token = hash_psw(admin_pin1, admin_pin2)
    db[b"admin"] = admin_token
    rec_token = hash_psw(admin_pin1, admin_pin2, b"big_red_hates_me")
    recover_db[b"admin"] = (admin_pin1, admin_pin2, rec_token)

def expand_pin(pin):
    return sha256(pin).digest()[:16]

def menu():
    print()
    print("What do you want to do?")
    print("1. Register")
    print("2. Login")
    print("3. Pin recovery")
    print("0. Exit")
    print()

    try:
        choice = int(input())
        assert choice in [0,1,2,3]
        if choice == 1:
            register()
        elif choice == 2:
            login()
        elif choice == 3:
            pin_recover()
        else:
            exit()
    except Exception as e:
        print("Invalid option!")

initialize_db()
signal.signal(signal.SIGALRM, handler)
signal.alarm(180)
while True:
    menu()
