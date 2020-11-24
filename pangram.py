import string

def is_pangram(s):
    # Create list from string using list comprehension
    my_list = [x for x in s]
    # Equates to new_list.append(i.lower()) using branching logic at the end of
    # the list comp expression, this is less efficient but more readable and compact.
    new_list = [x.lower() for x in my_list if x in string.ascii_lowercase or x in string.ascii_uppercase]
    # Remove duplicates from new arr and copy to final testable list by instantiating a new list object 
    final_list = list(set(new_list))

    if len(final_list) >= 26:
        return True
    return False
