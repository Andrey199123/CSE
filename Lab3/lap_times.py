lap_list = []
for laps in range(1, int(input("Enter the number of times you have to run around a racetrack:")) + 1):
    lap_list.append(int(input("Enter lap " + str(laps) + ":")))
print("Fastest lap time: " + str(min(lap_list)))
print("Slowest lap time: " + str(max(lap_list)))
print("Average lap time: " + str(sum(lap_list)/len(lap_list)))
