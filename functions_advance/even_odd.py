def even_odd(*args):
    command = args[-1]
    numbers = args[:-1]
    if command == "even":
        return [num for num in numbers if num % 2 == 0]
    return [num for num in numbers if num % 2 != 0]
