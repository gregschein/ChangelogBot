import json
import os

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

def seed_changelog(database):
    """Seeds Patchnotes table"""
    cursor = database.cursor()

    with open('config/data/patches.json') as data:
        patches = json.load(data)

    statement = "INSERT INTO Heroes_Patchnotes (description, hero_id, patch_id) VALUES (%s, %s, %s)"
    for hero in os.listdir('config/data/changelogs'):
        with open('config/data/changelogs/'+hero) as f:
            changes = json.load(f)
            cursor.execute("SELECT Id FROM Heroes WHERE Name = %s", (hero[:-5].lower(),))
            hero_id = cursor.fetchone()[0]

            relevant_patches = []
            for patch in changes:
                if patch in patches['patch']:
                    cursor.execute("SELECT Id FROM Patch WHERE Patch = %s", (patch,))
                    patch_id = cursor.fetchone()[0]
                    relevant_patches.append((changes[patch], hero_id, patch_id))
            cursor.executemany(statement, relevant_patches)
    database.commit()

