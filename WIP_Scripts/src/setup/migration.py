import MySQLdb as mdb

# Create db object here
# call migration function here

# define migration function here

def migrate(database):
    """Setup Heroes, Patch, and Heroes_Patchnotes Tables"""
    cursor = database.cursor()
    cursor.execute("CREATE TABLE Heroes("+
		"Id INT PRIMARY KEY AUTO_INCREMENT NOT NULL,"
		+" Name VARCHAR(64), Description TEXT)")
    cursor.execute("CREATE TABLE Patch("+
		"Id INT PRIMARY KEY AUTO_INCREMENT NOT NULL,"+
		" Patch VARCHAR(64))")
    cursor.execute("CREATE TABLE Heroes_Patchnotes("+
		"Id INT PRIMARY KEY AUTO_INCREMENT NOT NULL,"+
		" Hero_Id INT NOT NULL, Patch_Id INT NOT NULL,"+
		" Description TEXT,"+
		" FOREIGN KEY (Hero_Id) REFERENCES Heroes(Id),"+
		" FOREIGN KEY (Patch_Id) REFERENCES Patch(Id))")
# migration function takes whatever mdb,connect() returns as a parameter
