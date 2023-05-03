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

    def planning(self):
        pass  # OpenAI (test, goal setting, ...)

    def Login(self):
        pass