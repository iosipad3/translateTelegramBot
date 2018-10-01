import sqlite3

class primitiveDBase():
	def __init__(self, path):
		'''Initialization with .db path'''
		self.connection = sqlite3.connect(path)
	def getData(self, **kwargs):
		pass
	def setData(self, **kwargs):
		#
		self.connection.commit()
	def disconnect(self):
		self.connection.close()
