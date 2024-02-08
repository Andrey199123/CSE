def maximum(value1, value2):
    if value1 > value2:
        return value1
    else:
        return value2


val1 = int(input("Enter your first value here:"))
val2 = int(input("Enter your second value here:"))
print("Greatest value: " + str(maximum(val1, val2)))
