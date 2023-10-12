def reverse_sort_dictionary(dict_input):
    reverse_items = sorted(dict_input.items(), key=lambda x: x[0], reverse=True)

    result = [(name, data[0]) for name, data in reverse_items]

    return result
