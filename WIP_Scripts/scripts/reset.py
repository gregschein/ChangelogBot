import MySQLdb as mdb
from seed import seed_heroes, seed_patch
from migration import migrate

db = mdb.connect(host='localhost', user= 'root', passwd='admin')

def reset_db():
	c= db.cursor()
	c.execute('DROP DATABASE db_stuff')
	c.execute('CREATE DATABASE db_stuff CHARACTER SET = utf8mb4	COLLATE = utf8mb4_unicode_ci')
	db_new = mdb.connect(host='localhost', user= 'root', passwd='admin', db='db_stuff')
	migrate(db_new)
	seed_heroes()
	seed_patch()

if __name__ == '__main__':
	reset_db()