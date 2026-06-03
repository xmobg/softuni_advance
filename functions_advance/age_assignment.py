def age_assignment(*names, **kwargs):
    result = []
    for name in sorted(names):
        age = kwargs[name[0]]
        result.append(f"{name} is {age} years old.")
    return '\n'.join(result)