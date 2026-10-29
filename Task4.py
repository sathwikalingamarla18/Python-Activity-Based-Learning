branches = ["East", "West"]
products = ["Pen", "Book", "Bag"]
sales = [[10, 20, 5], [15, 12, 8]]
for i in range(len(branches)):
    print(branches[i], "total:", sum(sales[i]))
    best = sales[i].index(max(sales[i]))
    print("Best product:", products[best])

