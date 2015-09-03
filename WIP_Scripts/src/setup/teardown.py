from src.db import get_connection
import json

CONNECTION = get_connection()

def teardown_db():
    """Drops currently used database"""
    cursor = CONNECTION.cursor()
    with open('config/config.json') as data:
        cfg = json.load(data)
    cursor.execute("DROP DATABASE {}".format(cfg['database']['db']))
    #cursor.execute("DROP DATABASE %s", (db_name[0]),)

