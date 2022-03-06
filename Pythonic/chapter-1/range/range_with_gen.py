def my_range(start, end, step=1):
    while start < end:
        yield start
        start += step


custom_range = my_range(10, 20, 3)

for i in custom_range:
    print(i)
