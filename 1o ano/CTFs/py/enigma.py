flag = ''
with open("nomes.txt", "r", encoding="windows 1252") as file:
    sixLetterNames = open("nomes6.txt", "w")
    for name in file.readlines():
        if len(name)-1 == 12:
            sixLetterNames.write(name)
            flag += (name[5])

print(flag)