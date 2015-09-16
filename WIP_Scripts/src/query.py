
def comment_to_query(comment):
    """Takes in comment, returns query values to find database entry Ids"""

    splitcomment = comment.split()
    #if len(splitcomment) != 2:
        #some error.
    hero_name = splitcomment[0].lower()
    patch_range = splitcomment[1].split('-')
    patch_range.sort(key=float)

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

    statement = "SELECT Description, Patch_Id FROM Heroes_Patchnotes WHERE Hero_Id = %s AND Patch_Id IN %s"
    cursor.execute(statement, (hero_id, patch_id))
    changelog = cursor.fetchall()
    for change in changelog:
        print change


