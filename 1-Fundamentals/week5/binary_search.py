
def binary_serch(the_list, target):
    lower_bound = 0
    upper_bound = len(the_list) - 1

    while lower_bound <= upper_bound:
        pivot = (lower_bound + upper_bound) // 2
        if the_list[pivot] == target:
            return pivot
        elif the_list[pivot] > target:
            upper_bound = pivot-1
        elif the_list[pivot] < target:
            lower_bound = pivot+1

    return -1


res = binary_serch([1, 3, 5, 7, 9, 10], 9)
print(res)
