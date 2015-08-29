from src.query import comment_to_query

def func(x):
    return x + 1

def test_the_first_element_of_the_first_tuple_is_the_hero_select_string():
    assert comment_to_query("HERO_NAME 6.77")[0][0] == "SELECT Id FROM Hero WHERE Name = %s"

def test_the_second_element_of_the_first_tuple_is_a_tuple_of_query_arguments():
	assert comment_to_query("HERO_NAME 6.77")[0][1] == ("hero_name",)

def test_the_first_element_of_the_second_tuple_is_the_patch_select_string():
	assert comment_to_query("HERO_NAME 6.77")[1][0] == "SELECT Id FROM Patch WHERE Patch = %s"

def test_the_second_element_of_the_second_tuple_is_the_patch_query_args():
	assert comment_to_query("HERO_NAME 6.77")[1][1] == ('6.77',)


#two patch cases

def test_the_first_element_of_the_first_tuple_is_the_hero_select_string_2():
    assert comment_to_query("HERO_NAME 6.77-6.78")[0][0] == "SELECT Id FROM Hero WHERE Name = %s"

def test_the_second_element_of_the_first_tuple_is_a_tuple_of_query_arguments_2():
	assert comment_to_query("HERO_NAME 6.77-6.78")[0][1] == ("hero_name",)

def test_the_first_element_of_the_second_tuple_is_the_patch_select_string_2():
	assert comment_to_query("HERO_NAME 6.77-6.78")[1][0] == "SELECT Id FROM Patch WHERE Patch BETWEEN %s AND %s"

def test_the_second_element_of_the_second_tuple_is_the_patch_query_args_2():
	assert comment_to_query("HERO_NAME 6.77-6.78")[1][1] == ('6.77', '6.78')