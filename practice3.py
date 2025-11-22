import math

N = int(input("Enter the number of repetitions needed to find the pi value : "))
y = 0

for x in range(0, N):
    y0 = 4 * (((-1) ** x) / ((2 * x) + 1))
    y = y0 + y
print(f"How many terms to compute? {N}")
print(f"The final value of y is {y:8f}")

Accuracy = math.pi - y
print(f"The accuracy is {Accuracy}")
