def calc_average(total):
    return total / 5


def determine_grade(grade):
    if 90 <= grade <= 100:
        return "A"
    elif 80 <= grade <= 89:
        return "B"
    elif 70 <= grade <= 79:
        return "C"
    elif 60 <= grade <= 69:
        return "D"
    else:
        return "F"


summation = 0
for counter in range(1, 6):
    summation += int(input("Enter test score " + str(counter) + ":"))
print("Average test score: " + str(calc_average(summation)))
print("Letter grade: " + str(determine_grade(calc_average(summation))))
