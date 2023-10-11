def merge_list(list1, list2):
    if not isinstance(list1, list) or not isinstance(list2, list):
        raise TypeError("One or both inputs are not lists")
    
    for element in list1 and list2:
        if not isinstance(element, int):
            raise TypeError("Elements in list are not all integers")
        
    merged_list = list1 + list2

    n = len(merged_list)

    for i in range(n):
        for j in range(0, n - i - 1):
            if merged_list[j] > merged_list[j + 1]:
                merged_list[j], merged_list[j + 1] = merged_list[j + 1], merged_list[j]

    return merged_list
