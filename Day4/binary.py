class BinarySearch(list):
    def __init__(self, a, b):
        self.length = a
        self.created_list_length = a
        self.list_step = b

        for i in range(self.created_list_length):
            list.append(self, self.list_step)
            self.list_step += b

    def search(self, item):
        low = 0
        high = self.length - 1
        counter = 0

        try:
            index = self.index(item)
            last_item = self[-1]
            if item == last_item:
                while low <= high:
                    mid = (low + high) / 2
                    counter += 1
                    if self.index(item) == mid:
                        return {'count': counter, 'index': mid}
                    else:
                        if item < self[int(mid)]:
                            high = mid - 1
                        else:
                            low = mid + 1
            return {'count': 0, 'index': index}
        except ValueError:
            index = -1

        return {'count': counter, 'index': index}


print(BinarySearch(100, 10))
