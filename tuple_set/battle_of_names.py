odd_set = set()
even_set = set()

n = int(input())
for row in range(1, n + 1):
    total_sum = 0
    name = input()
    for char in name:
        total_sum += ord(char)
    result = total_sum // row
    if result % 2 == 0:
        even_set.add(result)
    else:
        odd_set.add(result)

if sum(odd_set) == sum(even_set):
    result_set = odd_set.union(even_set)
    print(", ".join(str(x) for x in result_set))
elif sum(odd_set) > sum(even_set):
    result_set = odd_set.difference(even_set)
    print(", ".join(str(x) for x in result_set))
elif sum(odd_set) < sum(even_set):
    result_set = odd_set.symmetric_difference(even_set)
    print(", ".join(str(x) for x in result_set))
