import sys

colors_list = ["red", "blue", "yellow"]
color1 = input("Please enter your first color:").lower()
color2 = input("Please enter your second color:").lower()
print(color1)
print(color2)
if color1 not in colors_list or color2 not in colors_list:
    print("Invalid input.")
    sys.exit()

colors_set = {color1, color2}

if len(colors_set) == 1:
    print("You can't enter two of the same color.")
    sys.exit()

purple_set = {"red", "blue"}
orange_set = {"red", "yellow"}
green_set = {"blue", "yellow"}

if colors_set == purple_set:
    print("When you mix red and blue, you get purple.")
elif colors_set == orange_set:
    print("When you mix red and yellow, you get orange.")
elif colors_set == green_set:
    print("When you mix blue and yellow, you get green.")

