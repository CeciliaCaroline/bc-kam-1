def words(string):
    word_list = string.split()
    word_dict = {}

    for item in word_list:
        if item in word_dict:
            word_dict[item] += 1
        else:
            word_dict[item] = 1

    for key in word_dict.keys():
        try:
            int(key)
            word_dict[int(key)] = word_dict.pop(key)
        except ValueError:
            continue
    return word_dict

