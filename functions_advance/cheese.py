def sorting_cheeses(**kwargs):
    sorted_data = sorted(kwargs.items(), key=lambda x: (-len(x[1]), x[0]))

    result = ""
    for cheese_name,pieces in sorted_data:
        result += f"{cheese_name}\n"
        for piece in sorted(pieces,reverse=True):
            result += f"{piece}\n"
    return result
