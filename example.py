def calculate_price(price_of_item, price_of_shipping):

    # we give free shipping for items of $50 or more
    
    if price_of_item >= 50:
        return price_of_item
    
    else:
        return price_of_item + price_of_shipping

# unit tests
def test_discount_30():
    assert calculate_price(30, 15) == 45

def test_discount_60():
    assert calculate_price(60, 15) == 60

def test_discount_50():
    assert calculate_price(50, 15) == 50

# program main
def main():
    banana_cost = 5
    shipping_cost = 15

    number_of_bananas = 12

    total_cost = calculate_price(banana_cost * number_of_bananas, shipping_cost)

    print(f"The price of buying {number_of_bananas} bananas for ${banana_cost} each is ${total_cost}")

if __name__ == "__main__":
    main()
