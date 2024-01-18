def create_an_empty_list():
    empty_list = []
    return empty_list

def create_a_list():
    my_list = [1, 2, 3, 4]
    return my_list

def add_element_to_end_of_list(add_list, element):
    add_list.append(element)
    return add_list

def add_element_to_start_of_list(start_list, element):
    start_list.insert(0,element)
    return start_list

def remove_element_from_end_of_list(l):
    l.pop()
    return l

def remove_element_from_start_of_list(my_list):
    del my_list[0]
    return my_list

def retrieve_first_element_from_list(my_list):
    return my_list[0]

def retrieve_element_from_index(my_list, index):
    return my_list[index]

def retrieve_last_element_from_list(my_list):
    return my_list[-1]