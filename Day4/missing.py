def find_missing(list1, list2):
    if list1 and list2:

        asy_difference_set = set(list1).symmetric_difference(set(list2))
        asy_difference_list = list(asy_difference_set)
        if len(asy_difference_list) == 0:
            return 0
        else:
            return asy_difference_list[0]
    return 0


print(find_missing([1, 2, 3], [1, 2, 3, 4]))
