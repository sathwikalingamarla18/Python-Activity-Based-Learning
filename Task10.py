points = [(0, 0), (3, 4), (6, 4)]
distances = []
for i in range(len(points) - 1):
    x1, y1 = points[i]
    x2, y2 = points[i + 1]
    d = ((x2 - x1)**2 + (y2 - y1)**2)**0.5
    distances.append(d)
    print("Segment", i + 1, "distance:", d)
print("Longest segment:", max(distances))

