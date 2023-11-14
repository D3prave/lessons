def reverse_string(string):
    list = []
    for i in range(len(string)):
        list.append(string[len(string)-1-i])
    return "".join(list)

list1 = "test"
list2 = reverse_string(list1)
print(list2)