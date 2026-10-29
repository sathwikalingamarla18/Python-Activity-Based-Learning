items = [("P1", 20, 5), ("P2", -3, 4), ("P3", 50, 0)]
for code, price, stock in items:
    if price < 0 or stock < 0:
        print(code, "invalid record")
    else:
        print(code, "value:", price * stock)
        if stock < 3:
            print(code, "needs replenishment")

