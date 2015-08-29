import MySQLdb as mdb
import json

def get_db():
    """Returns connection to database specified in config.json"""

    with open('config/config.json') as data:
        cfg = json.load(data)
    db_connection = mdb.connect(
    	cfg['database']['host'], 
    	cfg['database']['username'], 
    	cfg['database']['password'], 
    	cfg['database']['db'])
    return db_connection

def get_connection():
    """Returns connection to MySQL installation"""
    with open('config/config.json') as data:
        cfg = json.load(data)
    db_connection = mdb.connect(
    	cfg['database']['host'], 
    	cfg['database']['username'], 
    	cfg['database']['password'])
    return db_connection
