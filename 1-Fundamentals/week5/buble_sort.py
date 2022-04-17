

def bubble_sort(the_list):
    for i in range(0, len(the_list)-1):
        list_changed = False
        for j in range(0, len(the_list)-1):
            item = the_list[j]
            next = the_list[j+1]

            if item > next:
                the_list[j] = next
                the_list[j+1] = item
                list_changed = True

            print(the_list, i, j)
        if list_changed == False:
            break


unsorted_list = [101, 49, 3, 12, 56]
bubble_sort(unsorted_list)
print(unsorted_list)
