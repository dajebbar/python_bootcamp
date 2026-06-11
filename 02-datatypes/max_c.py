def max_difference(num_lst):
    lst_of_max = []
    idx = num_lst[0]
    res = 0
    for num in num_lst[1:]:
        res = abs(num - idx)
        lst_of_max.append(res)
        idx = num
    print(lst_of_max)
    return max(lst_of_max)

lst = [1, 7, 3, 10, 5]
print(max_difference(lst))

lst = [10, 11, 15, 3]
print(max_difference(lst))