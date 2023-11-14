def get_element(my_list, index):
    try:
        return my_list[index]
    except IndexError:
        print("Index out of range!")
        return None
    
my_list = [1, 2, 3, 4, 5]
index = int(input("Enter an index: "))
result = get_element(my_list, index)
if result is not None:
    print(f"The result is {result}")
else:
    print("Error occured!")