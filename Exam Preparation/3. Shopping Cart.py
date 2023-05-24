def shopping_cart(*args):
    f_reslt = ''
    range_dict = {"Soup":3, "Pizza":4, "Dessert":2}
    product_dict = {"Soup":[], "Pizza":[], "Dessert":[]}
    for item in args:
        if item == "Stop":
            break
        else:
            meal, product = item[0], item[1]
            if product not in product_dict[meal] and len(product_dict[meal]) < range_dict[meal]:
                product_dict[meal].append(product)

    result = sorted(product_dict.items(), key=lambda x:(-len(x[1]), x[0]))
    for item in result:
        meal = item[0]
        products = item[1]
        sorted_product = sorted(products)
        f_reslt += f"{meal}:\n"
        for parts in sorted_product:
            f_reslt += f" - {parts}\n"

    res = not any(product_dict.values())
    if not res:
        return f_reslt
    else:
        return "No products in the cart!"


print(shopping_cart(
    ('Pizza', 'ham'),
    ('Soup', 'carrots'),
    ('Pizza', 'cheese'),
    ('Pizza', 'flour'),
    ('Dessert', 'milk'),
    ('Pizza', 'mushrooms'),
    ('Pizza', 'tomatoes'),
    'Stop',
))

# print(shopping_cart(
#     'Stop',
#     ('Pizza', 'ham'),
#     ('Pizza', 'mushrooms'),
# ))
# print(shopping_cart(
#     ('Pizza', 'ham'),
#     ('Dessert', 'milk'),
#     ('Pizza', 'ham'),
#     'Stop',
# ))
# print(shopping_cart(
#     ('Pizza', 'ham'),
#     ('Soup', 'carrots'),
#     ('Pizza', 'cheese'),
#     ('Pizza', 'flour'),
#     ('Dessert', 'milk'),
#     ('Pizza', 'mushrooms'),
#     ('Pizza', 'tomatoes'),
#     ('Dessert', 'milk2'),
#     ('Dessert', 'milk3'),
#     'Stop',))
