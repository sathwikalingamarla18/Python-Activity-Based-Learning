wards = ["A", "B"]
beds = [[8, 10, 9], [5, 7, 6]]
capacity = [10, 8]
for i in range(len(wards)):
    for day in range(len(beds[i])):
        percent = beds[i][day] / capacity[i] * 100
        print(wards[i], "day", day + 1, percent, "%")
        if beds[i][day] > capacity[i]:
            print("Capacity exceeded!")

