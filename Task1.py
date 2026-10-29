roads = ["Main", "Park", "Lake"]
counts = [[40, 80, 120], [30, 45, 60], [50, 90, 110]]
capacity = 100
for i in range(len(roads)):
    peak = max(counts[i])
    level = "High" if peak > capacity else "Normal"
    print(roads[i], "peak:", peak, level)
