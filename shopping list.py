

items = []
prices = []
total = 0

while True :
    item = input(" enter the items (Q/q) to quit ")
    if item.lower() == 'q':
        break
    else:
        price=int(input(f" the price of the {item} is  "))
        items.append(item)
        prices.append(price)
print(" ---------- the cart-----------------")

for item in items :
    print(item)

for price in prices:
    total =  total + price
print(f" the total is {total}")