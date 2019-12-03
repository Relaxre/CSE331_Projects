def merge_sort(unsorted, threshold, reverse):
    """
    The function to merge the list to two list contained the half of the unsorted list
    :param unsorted: The unsorted list
    :param threshold: The size limit of each list
    :param reverse: The value true or false
    :return: the list processed by insertion list.
    """
    list_length = len(unsorted)
    if list_length <= threshold or list_length == 1:
        org_list = insertion_sort(unsorted, reverse)
        return org_list
    mid = list_length // 2
    fir_list = unsorted[0:mid]
    sec_list = unsorted[mid:list_length]
    fir_list = merge_sort(fir_list, threshold, reverse)
    sec_list = merge_sort(sec_list, threshold, reverse)
    sorted_list = merge(fir_list, sec_list, reverse)
    return sorted_list


def merge(first, second, reverse):
    """
    The function to merge the list
    :param first: First list got from the function merge_sort
    :param second: Second list got from the function merge_sort
    :param reverse: The value true or false
    :return: Return the sorted list in desired order
    """
    single_list = first + second
    i = j = 0
    if reverse is False:
        while i+j < len(single_list):
            if j == len(second) or (i < len(first) and first[i] < second[j]):
                single_list[i+j] = first[i]
                i = i+1
            else:
                single_list[i+j] = second[j]
                j = j+1
    else:
        while i+j < len(single_list):
            if j == len(second) or (i < len(first) and first[i] > second[j]):
                single_list[i+j] = first[i]
                i = i+1
            else:
                single_list[i+j] = second[j]
                j = j+1
    return single_list


def insertion_sort(unsorted, reverse):
    """
    The function to sort the list by insertion sort method
    :param unsorted: The unsorted list
    :param reverse: The value of true or false
    :return: The sorted list
    """
    if reverse is False:
        n = len(unsorted)
        for i in range(1, n):
            j = i
            while (j > 0) and (unsorted[j] < unsorted[j - 1]):
                temp = unsorted[j]
                unsorted[j] = unsorted[j-1]
                unsorted[j-1] = temp
                j -= 1
    else:
        n = len(unsorted)
        for i in range(1, n):
            j = i
            while (j > 0) and (unsorted[j] > unsorted[j - 1]):
                temp = unsorted[j]
                unsorted[j] = unsorted[j-1]
                unsorted[j-1] = temp
                j -= 1
    return unsorted