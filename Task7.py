products = ["Pen", "Book", "Bag"]
stock = [[20, 10], [5, 15], [8, 4]]  # warehouse 1, warehouse
target = [25, 25, 15]
for i in range(len(products)):
    total = stock[i][0] + stock[i][1]
    difference = target[i] - total
    print(products[i], "stock:", total)
    if difference > 0:
        print("Short by", difference)
    elif difference < 0:
        print("Surplus", -difference)
    else:
        print("Target met")

