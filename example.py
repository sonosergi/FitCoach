### this file is a draft for testing

import sqlite3
from user import *

user = User("johndoe", "johndoe@example.com")


# Generar una contraseña aleatoria y agregarla al perfil del usuario
password = user.passwordGen()

# Insertar los datos del usuario en la base de datos
conn = sqlite3.connect('users.db')
cursor = conn.cursor()
cursor.execute('INSERT INTO users (nickname, email, password) VALUES (?, ?, ?)', (user.nickname, user.email, password))
conn.commit()
conn.close()

print("Usuario creado exitosamente!")
