import sqlite3

class UDBase:
	def __init__(self, path):
		self.__connection = sqlite3.connect(path)
	def connect(self, path):
		self.__connection = sqlite3.connect(path)
	def disconnect(self):
		self.__connection.close()
	def getData(self, id):
		s = "SELECT * FROM users WHERE id=?"
		return self.__connection.cursor().execute(s, [id]).fetchone()
	def setData(self, id, **kwargs):
		if self.getData(id):
			q = ", ".join("{}=?".format(k) for k in kwargs)
			s = "UPDATE users SET {} WHERE id=?".format(q)
			self.__connection.cursor().execute(s, list(kwargs.values()) + [id])
		else:
			l = 'id'
			r = '?'
			for k in kwargs:
				l = ", ".join([l, k])
				r = ", ".join([r, "?"])
			s = "INSERT INTO users ({}) VALUES ({})".format(l, r)
			self.__connection.cursor().execute(s, [id] + list(kwargs.values()))
		self.__connection.commit()
