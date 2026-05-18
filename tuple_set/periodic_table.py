chemical_elements = set()
n = int(input())

for _ in range(n):
    chemical_elements.update(input().split())

for name in chemical_elements:
    print(name)
