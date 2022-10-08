class MedianFinder:
    def __init__(self):
        self.lst = []

    def add_num(self, num):
        self.lst.append(num)

    def find_median(self):
        lst_sorted = sorted(self.lst)
        length = len(lst_sorted)
        if length == 0:
            return 0
        elif len(lst_sorted) % 2:
            return round(lst_sorted[length // 2], 5)
        return round((lst_sorted[length // 2] + lst_sorted[length // 2 - 1]) / 2, 5)
