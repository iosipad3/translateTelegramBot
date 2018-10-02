from database.database import *

import sqlite3
# Create users database, if it's not exists yet
connection = sqlite3.connect("database/users.db")
connection.cursor().execute("""CREATE TABLE IF NOT EXISTS users
(username TEXT, lang_from TEXT, lang_to TEXT, PRIMARY KEY(username))""")
connection.commit()
connection.close()
# Creating connection with users.db
UsersDBase = UDBase("database/users.db")
