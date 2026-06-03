def even_odd_filter(**kwargs):
    result = {}
    for key, values in kwargs.items():
        if key  == 'even':
            result[key] = [x for x in values if x % 2 == 0 ]
        elif key == 'odd':
            result[key] = [x for x in values if x % 2 != 0]

    return dict(
        sorted(
            result.items(),
            key = lambda x : len(x[1]),
            reverse = True
        )
    )
