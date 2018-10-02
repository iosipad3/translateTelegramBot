import sqlite3

class UDBase:
	def __init__(self, path):
		self.__connection = sqlite3.connect(path)
	def connect(self, path):
		self.__connection = sqlite3.connect(path)
	def disconnect(self):
		self.__connection.close()
	def getData(self, username):
		s = "SELECT * FROM users WHERE username=?"
		return self.__connection.cursor().execute(s, [username]).fetchone()
	def setData(self, username, **kwargs):
		if self.getData(username):
			q = ", ".join("{}=?".format(k) for k in kwargs)
			s = "UPDATE users SET {} WHERE username=?".format(q)
			self.__connection.cursor().execute(s, list(kwargs.values()) + [username])
		else:
			l = 'username'
			r = '?'
			for k in kwargs:
				l = ", ".join([l, k])
				r = ", ".join([r, "?"])
			s = "INSERT INTO users ({}) VALUES ({})".format(l, r)
			self.__connection.cursor().execute(s, [username] + list(kwargs.values()))
		self.__connection.commit()
