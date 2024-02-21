numbers = []
for _ in range(20):
    numbers.append(int(input("Enter a number: ")))
print("Lowest number in the list: " + str(min(numbers)))
print("Highest number in the list: " + str(max(numbers)))
print("Total of the numbers in the list: " + str(sum(numbers)))
print("Average of the numbers in the list: " + str(sum(numbers)/len(numbers)))
