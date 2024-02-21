import random
import sys
lottery = [random.randint(0, 9) for _ in range(7)]
print(lottery)
guess = input()
counter = 0
for char in guess:
    if int(char) != lottery[counter]:
        print("Your guess isn't correct.")
        sys.exit(0)
    counter += 1
print("You won the lottery!")

