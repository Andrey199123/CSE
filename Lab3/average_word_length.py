word = " "
word_list = []
while word != "":
    word = input("Enter a word: ")
    word_list.append(len(word))
print("Average word length: " + str(round(sum(word_list)/(len(word_list)-1))))
