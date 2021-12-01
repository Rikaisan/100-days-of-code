from words import word_list

with open("words.txt", "w") as file:
    file.writelines((f"{word}\n" for word in word_list))
