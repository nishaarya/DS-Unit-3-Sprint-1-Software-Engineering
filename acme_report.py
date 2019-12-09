from random import randint, sample, uniform
from acme import Product

ADJECTIVES = ['Awesome', 'Shiny', 'Impressive', 'Portable', 'Improved']
NOUNS = ['Anvil', 'Catapult' 'Disguise' 'Mousetrap', '???']

#average
def avg(list):
    """Function to calculate the average value of a list of numerical values"""
    return sum(list)/len(list)

#generate_produts()
def generate_products(num_products = 30):

    """
    Function to randomly generate a list of n products where n is the
    parameter passed to the function
    """
#price and weight should both be from 5 to 100
#flammability` should be from 0.0 to 2.5
    products =[]
    for i in range(num_products):
        name = sample(ADJECTIVES, 1)[0] + " " + sample(NOUNS, 1)[0]
        price = randint(5, 100)
        weight = randint(5, 100)
        flammability = uniform(0, 2.5)
        products.append(Product(name, price, weight, flammability))
    return products

def inventory_report(products):

    names = [prod.name for prod in products]
    prices = [prod.price for prod in products]
    weights = [prod.weight for prod in products]
    flams = [prod.flammability  for prod in products]

    num_prod_names = len(set(names))
    avg_price = avg(prices)
    avg_weight = avg(weights)
    avg_flam = avg(flams)

    # Print out the information in a neat way.
    print(f"ACME CORPORATION OFFICIAL INVENTORY REPORT")
    print(f"Unique product names: {num_prod_names}")
    print(f"Average price: ${avg_price:,.02f}")
    print(f"Average weight: {avg_weight:.02f}")
    print(f"Average flammability: {avg_flam:.02f}")

# Used the following to test the generate_products code:
# print(generate_products()[0].name)
if __name__ == '__main__':
    inventory_report(generate_products())
