def grocery_store(**products):
    sorted_products = sorted(
        products.items(),
        key = lambda x : (-x[1], -len(x[0]), x[0])
    )
    result = []
    for product, quantity in sorted_products:
        result.append(f"{product}: {quantity}")

    return '\n'.join(result)