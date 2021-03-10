
def find_greatest_number(incoming_list):
    """
    Required parameter, incoming_list, should be a list.
    Find the largest number in the list.
    """
    #return_value = max(incoming_list)
    #return return_value

    MAGIC_LOW_NUMBER = None
    retval = MAGIC_LOW_NUMBER

    # 1,2,3,4,5,1
    # MAGIC_LOW_NUMBER,    1     ->STORE 1
    #1                ,    2     ->STORE 2
    #2,                ,   3     ->STORE 3
    #3,                ,    4     ->STORE 4 
    #4,               ,    5    ->STORE 5
    #5,               ,    1     ->??? nothing    
    for value in incoming_list:
        if not retval:
            retval = value
        if value > retval:
            retval = value


    

def find_least_number(incoming_list):
    """
    Required parameter, incoming_list, should be a list.
    Find the smallest/least number in the list.
    """
    
    return_value = min(incoming_list)
    return return_value
    

def add_list_numbers(incoming_list):
    """
    Required parameter, incoming_list, should be a list.
    Add all the values together and return it.
    """
    if incoming_list:    #if incoming_list is not None and len(incoming_list) > 0
        return_value = sum(incoming_list)
    else:
        return_value = 0
    return return_value
    

def longest_value_key(incoming_dict):
    """
    Required parameter, incoming_dict, should be a dict.
    Find the KEY that has a value with the highest length, use the len() function
    """
    #return_value = max(incoming_dict, key=len)
    #return return_value
    if not incoming_dict:
            return None

    all_keys = incoming_dict.keys()
    if not all_keys:
        return None

    Key_with_longest_value = None
    for key in all_keys:
            if not Key_with_longest_value:
            Key_with_longest_value = key

        if len(incoming_dict[key]) > len(incoming_dict[Key_with_longest_value]):
            Key_with_longest_value = key
            return Key_with_longest_value
