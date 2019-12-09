#!usr/bin/env python
import unittest
from acme import Product
from acme_report import generate_products, ADJECTIVES, NOUNS

# Add at least *2* more test methods to `AcmeProductTests` for the base Product class
class AcmeProductTests(unittest.TestCase):
    """Making sure Acme products are the tops!"""

# test price
    def test__price(self):
        prod = Product('Test Product')
        self.assertEqual(prod.price, 10)

#test weight
    def test__weight(self):
        prod = Product('Test Product')
        self.assertEqual(prod.weight, 20)

#test stealability and explode
    def test_steal_explode(self):

        prod = Product("Test Product", 10, 10, 0.2)
        self.assertEqual(prod.stealability(), "Kinda Stealable")
        self.assertEqual(prod.explode(), "...boom!")

# test_default_num_products` which checks that it really does receive a list of length 30
class AcmeReportTests(unittest.TestCase):
    def test_default_num_products(self):
        inventory = generate_products()
        self.assertEqual(len(inventory), 30)

# test_legal_names` which checks that the generated names for a default batch of products are all valid possible names to generate
    def test_legal_names(self):

        prods = generate_products()
        for item in prods:
            name = item.name.split(" ")
            adj = name[0]
            noun = name[1]
            self.assertIn(adj, ADJECTIVES)
            self.assertIn(noun, NOUNS)

if __name__ == '__main__':
    unittest.main()
