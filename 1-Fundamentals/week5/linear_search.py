def linear_search(the_list, target):
    for x in range(len(the_list)):
        if the_list[x] == target:
            print("Found at index", x)
            return x
    print(target, "does't  exist in the list")
    return -1

# my_list = [6, 3, 4, 2, 5, 7]
# linear_search(my_list, 6)
# linear_search(my_list, 9)
# linear_search(my_list, 2)

def linear_search_dictionary(the_dictionary, target):
    for key, value in the_dictionary.items():
        if the_dictionary[key] == target:
            print("Found at key", key)
            return
    print("Target is not in the dictionary.")

my_dictionary = {"red": 5, "blue": 3, "yellow": 12, "green": 7}
linear_search_dictionary(my_dictionary, 5)
linear_search_dictionary(my_dictionary, 3)
linear_search_dictionary(my_dictionary, 8)
