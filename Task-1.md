### Problem Statement
To develop a Python program to analyze traffic flow across multiple roads during different time intervals. The program should calculate the peak traffic for each road, identify the time interval with the highest number of vehicles, classify congestion levels as low, moderate, or high, and identify roads where the number of vehicles exceeds the specified road capacity.

### Algorithm
1. Start the program.
2. Initialize the names of multiple roads.
3. Store the vehicle counts for each road across different time intervals.
4. Set the maximum road capacity to 100 vehicles.
5. Use a for loop to process each road.
6. Find the maximum vehicle count using the max() function.
7. Identify the peak time interval using the index() function.
8. Classify the congestion level:
   - If peak traffic is greater than 100, classify it as High Congestion.
   - If peak traffic is between 70 and 100, classify it as Moderate Congestion.
   - Otherwise, classify it as Low Congestion.
9. Check whether peak traffic exceeds the road capacity.
10. Display the road name, vehicle counts, peak traffic, peak time interval, congestion level, and capacity status.
11. Repeat the process for all roads.
12. Stop the program.

 '''Mermaid Flowchart
 flowchart TD
    A([Start]) --> B[Initialize road names]
    B --> C[Store vehicle counts for each road]
    C --> D[Set road capacity = 100]
    D --> E[Select the next road]
    E --> F[Find peak traffic using max]
    F --> G[Find peak time interval]
    G --> H{Peak traffic > 100?}
    H -- Yes --> I[High Congestion]
    H -- No --> J{Peak traffic >= 70?}
    J -- Yes --> K[Moderate Congestion]
    J -- No --> L[Low Congestion]
    I --> M[Check capacity status]
    K --> M
    L --> M
    M --> N[Display road analysis]
    N --> O{Are more roads available?}
    O -- Yes --> E
    O -- No --> P([Stop])'''
How to understand the flowchart:
- Oval: Start and stop.
- Rectangle: Processing steps.
- Diamond: Decision-making.
- Arrows: Direction of program execution.
-
- ### Code:
- roads = ["Main Road", "Park Road", "Lake Road"]
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

### Sample Input
Road Names:
Main Road
Park Road
Lake Road
Vehicle Counts:
Main Road: 40, 80, 120
Park Road: 30, 45, 60
Lake Road: 50, 90, 110

Road Capacity: 100 vehicles

### Sample Output
Road: Main Road
Vehicle Counts: [40, 80, 120]
Peak Traffic: 120
Peak Time Interval: 3
Congestion Level: High Congestion
Capacity Status: Exceeds Capacity

Road: Park Road
Vehicle Counts: [30, 45, 60]
Peak Traffic: 60
Peak Time Interval: 3
Congestion Level: Low Congestion
Capacity Status: Within Capacity

Road: Lake Road
Vehicle Counts: [50, 90, 110]
Peak Traffic: 110
Peak Time Interval: 3
Congestion Level: High Congestion
Capacity Status: Exceeds Capacity

