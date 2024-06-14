def convert_list_to_dictionary(list_1, list_2, list_3, list_4):
    zip_lists = zip(list_1, list_2, list_3, list_4)
    dictionary = {x: (a, b, c) for x, a, b, c in zip_lists}
    return dictionary


list1 = ["SamsungS22", "Iphone13", "Xiaomi12"]
list2 = [1000, 1100, 900]
list3 = ["SD8Gen1", "A15", "SD898"]
list4 = [108, 12, 108]
response_dict = convert_list_to_dictionary(list1, list2, list3, list4)
print("The Dictionary is: ")
print(response_dict)
