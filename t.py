def my_func():
    with open('data.txt') as f:
        number = int(f.read())

    return number

