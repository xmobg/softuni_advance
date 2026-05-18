longest_intersection = 0
n = int(input())
longest_intersection_set = set()
for _ in range(n):
    line = input()
    first_part, second_part = line.split("-")
    start1,end1 = first_part.split(",")
    set1 = set(range(int(start1),int(end1) + 1))
    start2,end2 = second_part.split(",")
    set2 = set(range(int(start2),int(end2) + 1))
    set3 = set1.intersection(set2)
    if len(set3) > longest_intersection:
        longest_intersection_set = set3
        longest_intersection = len(set3)

print(f"Longest intersection is {sorted(longest_intersection_set)} with length {longest_intersection}")