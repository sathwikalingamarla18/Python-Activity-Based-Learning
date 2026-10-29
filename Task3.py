marks = [[80, 70, 90], [60, 75, 65], [95, 88, 92]]
names = ["Ana", "Ben", "Cia"]
for i in range(len(marks)):
    print(names[i], "total =", sum(marks[i]))
for j in range(len(marks[0])):
    total = 0
    for i in range(len(marks)):
        total += marks[i][j]
    print("Subject", j + 1, "average =", total / len(marks))
print("Top student:", names[marks.index(max(marks, key=sum))])

