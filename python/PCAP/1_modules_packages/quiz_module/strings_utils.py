import string_utils

def halve_strings(string_list):
    halved_string_tuples = []
    for string in string_list:
        halved_string_tuples.append(string_utils.halve_string(string))
        
    return halved_string_tuples
