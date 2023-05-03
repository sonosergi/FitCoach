import sqlite3
import uuid
import random
import string

class User:
    def __init__(self, nickname, email, weight, height, grassIndex):
        self.id = str(uuid.uuid4()) # generate a unique id for the user
        self.nickname = nickname
        self.email = email
        length = 16  # Length of generated password
        allowed_chars = string.ascii_letters + string.digits + string.punctuation  # Allowed characters in the password
        password = ''.join(random.choice(allowed_chars) for i in range(length))  # Generate the password
        self.password = password
        self.weight = weight
        self.height = height
        self.grassIndex = grassIndex

        # Connect to the database and insert the user data
        self.conn = sqlite3.connect('Madrid.db')
        self.cursor = self.conn.cursor()

        # Create table if it doesn't exist
        self.cursor.execute('''
            CREATE TABLE IF NOT EXISTS Madrid
            (id TEXT PRIMARY KEY,
            nickname TEXT, 
            email TEXT, 
            password TEXT, 
            weight REAL, 
            height REAL, 
            grassIndex REAL)
            ''')
        instruction = f"INSERT INTO Madrid VALUES ('{self.id}', '{self.nickname}', '{self.email}', '{self.password}', {self.weight}, {self.height}, {self.grassIndex})"
        self.cursor.execute(instruction)
        self.conn.commit()
        self.conn.close()


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

if __name__ == '__main__':

    user = User("johndoe2", "johndoe2@example.com", 75, 168, 13)
    print("Usuario creado exitosamente!")

