
def comment_to_query(comment):
    """Takes in comment, returns query values to find database entry Ids"""

    splitcomment = comment.split()
    patch_range = splitcomment.pop().split('-')
    patch_range.sort(key=float)
    hero_name = ""
    for word in splitcomment:
        hero_name += word + " "
    hero_name += "\b"

    query_hero = ["SELECT Id FROM Heroes WHERE Name = %s"]
    query_hero.append((hero_name,))

    #check if one patch or two
    if len(patch_range) == 1:
        query_patch = ["SELECT Id FROM Patch WHERE Patch = %s"]
        query_patch.append((patch_range[0],))

        return (query_hero, query_patch)
        
    elif len(patch_range) == 2:
        query_patch = ["SELECT Id FROM Patch WHERE Patch BETWEEN %s AND %s"]
        query_patch.append((patch_range[0], patch_range[1]))
        return (query_hero, query_patch)

def get_ids(database, query_hero, query_patch):
    """Takes output of comment_to_query and a database connection,
     returns entry id of the hero and relevant patches"""

    cursor = database.cursor()

    cursor.execute(query_hero[0], query_hero[1])
    hero_id = cursor.fetchone()

    cursor.execute(query_patch[0], query_patch[1])
    patch_id = cursor.fetchall()

    return(hero_id, patch_id)

def get_changelog(database, hero_id, patch_id):

    cursor = database.cursor()

    # statement = "SELECT Description, Patch_Id FROM Heroes_Patchnotes WHERE Hero_Id = %s AND Patch_Id IN %s ORDER BY Patch_Id"
    statement = "SELECT Heroes_Patchnotes.Description, Patch.Patch FROM Heroes_Patchnotes LEFT JOIN Patch on Heroes_Patchnotes.Patch_Id = Patch.id WHERE Heroes_Patchnotes.Hero_Id = %s AND Heroes_Patchnotes.Patch_Id IN %s ORDER BY Heroes_Patchnotes.Patch_Id"
    cursor.execute(statement, (hero_id, patch_id))
    changelog = cursor.fetchall()
    return changelog


