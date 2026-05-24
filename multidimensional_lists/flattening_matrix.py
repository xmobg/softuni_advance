nums = []
n = int(input())

for i in range(n):
    data = [int(x) for x in input().split(", ")]
    nums.extend(data)

print(nums)
