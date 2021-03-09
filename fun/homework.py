def find_greatest_number(incoming):
    """
    Required parameter, incoming_list, should be a list.
    Find the largest number in the list.
    """
    incoming = [11,15,17,19]
    incoming.sort()
    return_value = incoming[-1]
    return return_value
    

def find_least_number(incoming_list):
    """
    Required parameter, incoming_list, should be a list.
    Find the smallest/least number in the list.
    """
    incoming_list = [1,2,3,4,5,6,7,8]
    return_value = min(incoming_list)
    return return_value
    

def add_list_numbers(incoming_list):
    """
    Required parameter, incoming_list, should be a list.
    Add all the values together and return it.
    """
    incoming_list = [1,2,3,-4]
    return_value = sum(incoming_list)
    return return_value
    

def longest_value_key(incoming_dict):
    """
    Required parameter, incoming_dict, should be a dict.
    Find the KEY that has a value with the highest length, use the len() function
    """
    incoming_dict = {"dog", "cat", "a", "asdfasdfasdfasdfasdf"}
    return_value = max(incoming_dict, key=len)
    return return_value
    
