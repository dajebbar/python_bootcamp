def mean(lst):
    return f"{sum(lst)/len(lst):.3f}"

def median(lst):
    if not lst:
        return None
    
    lst_sort = sorted(lst)
    n = len(lst_sort)
    medium = n // 2

    if n % 2 == 1:
        return lst_sort[medium]
    else:
        return (lst_sort[medium - 1] + lst_sort[medium]) / 2


if __name__== "__main__":
    lst = [12,34,45]
    print("____Test stats.py____")
    print(mean(lst))
    print(median(lst))