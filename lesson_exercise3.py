my_list = ["apple", "banana", "orange"]
my_iterator = iter(my_list)
while True:
    try:
        value = next(my_iterator)[::-1]
        print(value)
    except StopIteration:
        break