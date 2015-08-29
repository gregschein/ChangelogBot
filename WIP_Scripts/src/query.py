
def comment_to_query(comment):
    """Takes in comment, returns query values to find database entry Ids"""

    splitcomment = comment.split()
    #if len(splitcomment) != 2:
        #some error.
    hero_name = splitcomment[0].lower()
    patch_range = splitcomment[1].split('-')
    patch_range.sort(key=float)

    query_hero = ["SELECT Id FROM Hero WHERE Name = %s"]
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

def get_ids(database, query_string, query_args):
    """Takes output of comment_to_query and a database connection,
     returns entry id of the hero and relevant patches"""

    cursor = database.cursor()

    cursor.execute(query_string[0], query_args[0])
    hero_id = cursor.fetchone()

    cursor.execute(query_string[1], query_args[1])
    patch_id = cursor.fetchall()

    return(hero_id, patch_id)


