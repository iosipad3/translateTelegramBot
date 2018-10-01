from database.dbase import *

import sqlite3
# Create users database, if it's not exists yet
connection = sqlite3.connect("database/users.db")
connection.cursor().execute("""CREATE TABLE IF NOT EXISTS user_settings
(username TEXT, langFrom TEXT, langTo TEXT, PRIMARY KEY(username))""")
connection.commit()
connection.close()
# Creating connection with users.db
UsersDBase = primitiveDBase("database/users.db")
