def negative_positive(*numbers):
    negative_sum = sum([n for n in numbers if n < 0])
    positive_sum = sum([n for n in numbers if n > 0])
    return negative_sum, positive_sum

negative, positive = negative_positive(
    *[int(x) for x in input().split()]
)
print(negative)
print(positive)
if abs(negative) > positive:
    print("The negatives are stronger than the positives")
else:
    print("The positives are stronger than the negatives")
