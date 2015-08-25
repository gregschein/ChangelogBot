import MySQLdb as mdb

# Create db object here
db = mdb.connect('localhost', 'root', 'admin', 'db_stuff')
# call migration function here

# define migration function here

def migrate(database):
	c=database.cursor()
	c.execute("CREATE TABLE Heroes(Id INT PRIMARY KEY AUTO_INCREMENT NOT NULL, Name VARCHAR(64),Description TEXT)")
	c.execute("CREATE TABLE Heroes_Patchnotes(Id INT PRIMARY KEY AUTO_INCREMENT NOT NULL, Hero_Id INT NOT NULL, Patch_Id INT NOT NULL, Description TEXT)")
	c.execute("CREATE TABLE Patch(Id INT PRIMARY KEY AUTO_INCREMENT NOT NULL, Patch VARCHAR(64))")
# migration function takes whatever mdb,connect() returns as a parameter
if __name == "__main__":
	migrate(db)
