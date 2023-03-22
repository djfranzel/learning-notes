
# when the program is executed, introspection allows user to get information about the object
# when program is executed, reflection allows user to change info about the object

# this function will accept any object, and convert all string values to ''
def empty_strings(user_object):
    for prop_name in user_object.__dict__.keys(): # returns a list of keys so it is iterable
        prop_value = getattr(user_object, prop_name) # gets attribute, why not user_object[prop_name] ?
        if isinstance(prop_value, str): # checks if value is an instance of the class str
            setattr(user_object, prop_name, '') # sets attribute, why not user_object[prop_name] ?


