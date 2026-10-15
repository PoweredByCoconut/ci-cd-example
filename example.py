# this function will make shipping free for orders of $50 or more

def calculate_price(price_of_item, price_of_shipping):

    if price_of_item <= 50:

        # we include shipping for orders under $50
        return price_of_item + price_of_shipping

    else:

        # if they're $50 or more, we don't include shipping
        return price_of_item

# unit tests
# these have been updatet to account for shipping discounts
def test_discount_30():
    assert calculate_price(30, 15) == 45

def test_discount_60():
    assert calculate_price(60, 15) == 60

def test_discount_50():
    # a $50 order should also get the discount because the rule is $50 or more
    assert calculate_price(50, 15) == 50

# program main
def main():
    banana_cost = 5
    shipping_cost = 15

    number_of_bananas = 10

    total_cost = calculate_price(banana_cost * number_of_bananas, shipping_cost)

    print(f"The price of buying {number_of_bananas} bananas for ${banana_cost} each is ${total_cost}")

if __name__ == "__main__":
    main()
