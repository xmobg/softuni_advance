def func_executor(*args):
    result = []

    for func, value in args:
        func_result = func(*value)
        result.append(f"{func.__name__} - {func_result}")
    return '\n'.join(result)