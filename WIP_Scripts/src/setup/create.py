from db import get_connection
import json

def create_database():              #pass it a
    with open('config/config.json') as data:
        cfg = json.load(data)
    db = get_connection()
    cursor = db.cursor()
    cursor.execute("CREATE DATABASE {} CHARACTER SET = utf8mb4 COLLATE = utf8mb4_unicode_ci".format(cfg['database']['db']))
