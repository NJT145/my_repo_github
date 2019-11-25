
def remove_duplicates(list_item):
    return list(dict.fromkeys(list_item))

def reduce_2Dto1D(list_item_2D):
    return [item for list_item_1D in list_item_2D for item in list_item_1D]
