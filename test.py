import random

choices = {'1': 0, '2': 0, '3': 0, '4': 0, '5': 0, '6': 0}
probabilities = [0.2068, 0.2068, 0.2068, 0.0689, 0.2068, 0.1034]

dice = [1, 2, 3, 4, 5, 6]
for i in range(100):
    choices[str(random.choices(dice, probabilities)[0])] += 1

print(choices)
