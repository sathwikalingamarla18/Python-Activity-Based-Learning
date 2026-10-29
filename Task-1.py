# Traffic Flow and Congestion Analysis

roads = ["Main Road", "Park Road", "Lake Road"]

# Vehicle counts during three time intervals
counts = [
    [40, 80, 120],
    [30, 45, 60],
    [50, 90, 110]
]

capacity = 100

for i in range(len(roads)):
    peak = max(counts[i])
    peak_interval = counts[i].index(peak) + 1

    if peak > capacity:
        level = "High Congestion"
        status = "Exceeds Capacity"
    elif peak >= 70:
        level = "Moderate Congestion"
        status = "Within Capacity"
    else:
        level = "Low Congestion"
        status = "Within Capacity"

    print("\nRoad:", roads[i])
    print("Vehicle Counts:", counts[i])
    print("Peak Traffic:", peak)
    print("Peak Time Interval:", peak_interval)
    print("Congestion Level:", level)
    print("Capacity Status:", status)
