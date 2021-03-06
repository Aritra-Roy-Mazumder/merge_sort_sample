import random
import strings

def create_list():
    lst_len = int(input("Enter how long you want your data set to be: "))
    lst = []
    for x in range(lst_len):
        pick = random.randint(1, lst_len)
        lst.append(pick)
    # print(lst)
    print(strings.commas(len(lst)))
    return lst


def merge_sort(working_list):

    if len(working_list) > 1:
        mid_section = len(working_list)//2
        sublist_left = working_list[:mid_section]
        sublist_right = working_list[mid_section:]

        merge_sort(sublist_left)
        merge_sort(sublist_right)

        index_left = 0
        index_right = 0
        index = 0

        while index_left < len(sublist_left) and index_right < len(sublist_right):

            if sublist_left[index_left] <= sublist_right[index_right]:
                working_list[index] = sublist_left[index_left]

                index_left += 1
                index += 1

            else:
                working_list[index] = sublist_right[index_right]
                index_right += 1
                index += 1

        while index_left < len(sublist_left):
                working_list[index] = sublist_left[index_left]
                index_left += 1
                index += 1

        while index_right < len(sublist_right):
                working_list[index] = sublist_right[index_right]
                index_right += 1
                index += 1
    return working_list

