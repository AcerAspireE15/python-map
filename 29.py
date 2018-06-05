# 1
new_list = [100, 200, 300, 400, 500]

def function(price):

    price = price - (price * 10)/100

    return price

result = list(map(function, new_list))

print(result)


# 2
def discount(price):
    price = price - (price * 10) / 100
    return price


product_prices = [100, 200, 300, 400, 500]

updated_prices = list(map(discount, product_prices))

print(updated_prices)