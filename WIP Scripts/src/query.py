
def comment_to_query(comment):
    splitcomment = comment.split()
    #if len(splitcomment) != 2:
        #some error.
    hero_name = splitcomment[0].lower()
    patch_range = splitcomment[1].split('-')

    #check if one patch or two
    if len(patch_range) == 1:
        query_string = "SELECT Id FROM Patch WHERE Patch = %s"
        query_args = (patch_range,)

        return (query_string, query_args)
        
    elif len(patch_range) == 2:
        query_string = "SELECT Id FROM Patch WHERE Patch BETWEEN %s AND %s"
        query_args = (patch_range[0], patch_range[1])

        return (query_string, query_args)

def get_ids(query_string,query_args):
