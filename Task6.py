appliances = ["Fan", "AC", "Light"]
units = [[2, 2, 3, 2, 2, 1, 2],[5, 6, 5, 7, 6, 5, 4],[1, 1, 1, 1, 1, 1, 1]]
limit = 35
for i in range(len(appliances)):
    total = sum(units[i])
    print(appliances[i],"weekly units:", total)
    if total > limit:
        print("Above limit")

