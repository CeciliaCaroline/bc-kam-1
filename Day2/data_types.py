def data_type(compare):
    if isinstance(compare, str):
        return len(compare)

    if compare is None:
        return 'no value'

    if isinstance(compare, bool):
        return compare

    if isinstance(compare, int):
        if compare < 100:
            return 'less than 100'
        elif compare > 100:
            return 'more than 100'
        else:
            return 'equal to 100'

    if isinstance(compare, list):
        if len(compare) > 2:
            return compare[2]
        else:
            return None
