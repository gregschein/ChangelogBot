import MySQLdb as mdb
from reset import reset_db

try:
	db = mdb.connect(host='localhost', user= 'root', passwd='admin', db='db_stuff')
except Exception OperationalError:
	#db = mdb.connect(host='localhost', user= 'root', passwd='admin')
	#c=db.cursor()
	#c.execute('CREATE DATABASE db_stuff	CHARACTER SET = utf8mb4	COLLATE = utf8mb4_unicode_ci')
	#db = mdb.connect(host='localhost', user= 'root', passwd='admin', db='db_stuff')
	TO DO LOGGING
if __name__ == '__main__':
	print "hello"