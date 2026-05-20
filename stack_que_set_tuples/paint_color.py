
substrings = input().split()

found_colors = []
valid_colors = {"red", "yellow", "blue", "orange", "purple", "green"}


while len(substrings) > 0:
    if len(substrings) == 1:

        first = substrings.pop(0)
        last = ""
        comb1 = first
        comb2 = first
    else:

        first = substrings.pop(0)
        last = substrings.pop(-1)
        comb1 = first + last
        comb2 = last + first


    if comb1 in valid_colors:
        found_colors.append(comb1)
    elif comb2 in valid_colors:
        found_colors.append(comb2)
    else:

        first = first[:-1]
        last = last[:-1]


        mid_idx = len(substrings) // 2


        if last:
            substrings.insert(mid_idx, last)
        if first:
            substrings.insert(mid_idx, first)


final_colors = []
for color in found_colors:
    if color in {"red", "yellow", "blue"}:
        final_colors.append(color)
    elif color == "orange" and "red" in found_colors and "yellow" in found_colors:
        final_colors.append(color)
    elif color == "purple" and "red" in found_colors and "blue" in found_colors:
        final_colors.append(color)
    elif color == "green" and "yellow" in found_colors and "blue" in found_colors:
        final_colors.append(color)


print(final_colors)
