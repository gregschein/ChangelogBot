import json

def seed_heroes(database):
    """Seeds Heroes table"""
    with open('config/data/heroes.json') as data:
        heroes = json.load(data)

    heroes_tuples = map(lambda x: (x["name"], x["description"]), heroes["heroes"])
    cursor = database.cursor()
    statement = "INSERT INTO Heroes (name, description) VALUES (%s, %s)"
    cursor.executemany(statement, heroes_tuples)
    database.commit()
		
def seed_patch(database):
    """Seeds Patch table"""
    with open('config/data/patches.json') as data:
        patches = json.load(data)

    patches_tuples = map(lambda x: (x,), patches['patch'])
    cursor = database.cursor()
    statement = "INSERT INTO Patch (patch) VALUES (%s)"
    cursor.executemany(statement, patches_tuples)
    database.commit()

#def seed_patchlog():


#if __name__ == '__main__':
	#seed_heroes()		
	#seed_patch()
