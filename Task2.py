seats = [["A", "RESERVED", ""], ["B", "", "C"]]
students = ["Ravi", "Maya"]
i = 0
while i < len(seats):
    j = 0
    while j < len(seats[i]):
        if seats[i][j] == "":
            if students:
                seats[i][j] = students.pop(0)
        j += 1
    i += 1
print(seats)
print("Vacant:", sum(row.count("") for row in seats))


