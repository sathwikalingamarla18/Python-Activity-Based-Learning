teams = ["Tigers", "Lions", "Eagles"]
wins = [3, 2, 3]
draws = [1, 2, 0]
points = []
for i in range(len(teams)):
    points.append(wins[i] * 3 + draws[i])
ranking = sorted(zip(points, teams), reverse=True)
for score, team in ranking:
    print(team, score, "points")

