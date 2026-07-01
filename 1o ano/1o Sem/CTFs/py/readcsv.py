count = 0
with open("us-counties_2.csv", "r") as csv:
    for line in csv.readlines():
        if (line.split(',')[0] == "2020-02-08"):
            count += int(line.split(',')[4])

print(count)