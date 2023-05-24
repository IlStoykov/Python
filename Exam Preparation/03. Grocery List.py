"""с 91 точки"""
def shop_from_grocery_list(bud, *args):
    budget = int(bud)
    product_list = args[0]
    products = args[1:]
    for item in products:
        product = item[0]
        price = float(item[1])
        if  product in product_list:
            if budget >= price:
                budget -= price
                product_list.remove(product)
            else:
                break

    if budget and not product_list:
        return f"Shopping is successful. Remaining budget: {budget:.2f}."
    else:
        return f"You did not buy all the products. Missing products: {', '.join([str(x) for x in product_list])}."


# print(shop_from_grocery_list(
#     100,
#     ["tomato", "cola"],
#     ("cola", 5.8),
#     ("tomato", 10.0),
#     ("tomato", 20.45),
# ))

# print(shop_from_grocery_list(
#     100,
#     ["tomato", "cola", "chips", "meat"],
#     ("cola", 5.8),
#     ("tomato", 10.0),
#     ("meat", 22),
# ))
#
print(shop_from_grocery_list(
    100,
    ["tomato1", "cola", "chips", "meat", "chocolate"],
    ("cola", 15.8),
    ("chocolate", 30),
    ("tomato", 15.85),
    ("chips", 30),
    ("meat", 22.99),
))
