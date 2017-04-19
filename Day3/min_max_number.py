def find_max_min(a):
    maximum = max(a)
    minimum = min(a)

    if maximum == minimum:
        result = [len(a)]
        return result

    min_max = [minimum, maximum]
    return min_max


print(find_max_min([4, 5, 1, 4, 0, 4]))
