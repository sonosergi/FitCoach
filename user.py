import sqlite3
import json
import string
import random
import uuid

class User:
    def __init__(self, nickname, email):
        self.id = str(uuid.uuid4()) # generate a unique id for the user
        self.nickname = nickname
        self.email = email
        self.profile = {
            'id': self.id,
            'nickname': self.nickname,
            'email': self.email
        }

        self.conn = sqlite3.connect('users.db')
        self.cursor = self.conn.cursor()

        # Create table if it doesn't exist
        self.cursor.execute('''
            CREATE TABLE IF NOT EXISTS users
            (id INTEGER PRIMARY KEY, nickname TEXT, email TEXT, password TEXT, weight REAL, height REAL, grassIndex REAL)
            ''')
        self.conn.commit()

    def __del__(self):
        self.conn.close()

    def biometrics(self, weight, height, grassIndex):
        self.weight = weight
        self.height = height
        self.grassIndex = grassIndex
        self.biometric_data = {
            'weight': weight,
            'height': height,
            'grassIndex': grassIndex
            }
        return json.dumps(self.profile)

    def passwordGen(self):
        length = 16  # Length of generated password
        allowed_chars = string.ascii_letters + string.digits + string.punctuation  # Allowed characters in the password
        password = ''.join(random.choice(allowed_chars) for i in range(length))  # Generate the password
        self.profile['password'] = password  # Add the 'password' key and value
        self.cursor.execute('INSERT INTO users (nickname, email, password) VALUES (?, ?, ?)', (self.nickname, self.email, self.profile['password']))
        self.conn.commit()
        return json.dumps(self.profile)

    def change_password(self):
        old_password = input("Enter your current password: ")
        if old_password != self.profile['password']:
            print("Incorrect password.")
            return False
        new_password = input("Enter your new password: ")
        confirm_password = input("Confirm your new password: ")
        if new_password != confirm_password:
            print("Passwords do not match.")
            return False
        self.profile['password'] = new_password
        self.cursor.execute('UPDATE users SET password = ? WHERE id = ?', (new_password, self.id))
        self.conn.commit()
        print("Password changed successfully.")
        return True

    def login(self, nickname, password):
        self.cursor.execute('SELECT * FROM users WHERE nickname = ? AND password = ?', (nickname, password))
        user = self.cursor.fetchone()
        if user:
            self.profile['id'] = user[0]
            self.profile['nickname'] = user[1]
            self.profile['email'] = user[2]
            self.profile['password'] = user[3]
            self.profile['weight'] = user[4]
            self.profile['height'] = user[5]
            self.profile['grassIndex'] = user[6]
            print(f"Welcome, {self.profile['nickname']}!")
            return True
        else:
            print("Incorrect credentials.")
            return False


    def planning(self):
        pass  # OpenAI (test, goal setting, ...)
