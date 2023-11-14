def my_generator(start, end):
    current = start
    while current <  end:
        yield current
        current += 1
    
gen = my_generator(1, 5)
for num in gen:
    print(num)
    
my_list = [1, 2, 3, 4, 5]
my_iterator = iter(my_list)

while True:
    try:
        value = next(my_iterator)
        print(value)
    except StopIteration:
        break
    
