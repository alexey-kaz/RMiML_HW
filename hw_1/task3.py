def top_k_nlogn(arr, k):
    dct = {}
    for i in arr:
        dct[i] = dct[i] + 1 if i in dct else 1
    return [i[0] for i in sorted(dct.items(), key=lambda item: item[1], reverse=True)][:k]


def top_k_n(arr, k):
    num_dct = {i: 0 for i in set(arr)}
    for i in arr:
        num_dct[i] += 1
    max_cnt = max(num_dct.values())
    cnt_dict = {i + 1: [] for i in range(max_cnt)}
    for num in num_dct:
        cnt_dict[num_dct[num]].append(num)
    res = []
    for count in range(max_cnt, 0, -1):
        res += cnt_dict[count]
    return res[:k]
