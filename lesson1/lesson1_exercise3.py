def my_generator(start, end):
    current = start
    while current <  end:
        yield current**2
        current += 1

gen = my_generator(1, 10)
for i in gen:
    print(i)