import unittest
from product import Product
from basket import ShoppingBasket

class TestProduct(unittest.TestCase):

    def setUp(self):
        self.product = Product('milk', 34.45, 4)


    def test_product_name(self):
        actual = self.product.name
        expected = 'milk'
        self.assertEqual(actual, expected)

    def test_product_price(self):
        actual = self.product.price
        expected = 34.45
        self.assertEqual(actual, expected)

    def test_product_quantitny(self):        
        self.assertEqual(self.product.quantity, 4)

    def test_product_repr(self):
        self.assertEqual(repr(self.product), 
        "Product(name='milk', price=34.45, quantity=4)")





class TestBasketwithNoProducts(unittest.TestCase):

    def setUp(self):
        self.basket = ShoppingBasket()

    def test_basket_empty(self):
        self.assertEqual(len(self.basket), 0)


    def test_getting_product_raise_an_error(self):
        self.assertRaises(IndexError, self.basket.get_product, 3)

    def test_basket_total_equala_zero(self):
        self.assertEqual(self.basket.total(), 0.00)




class TestBasketwithOneProduct(unittest.TestCase):

    def setUp(self):  
        self.product =  Product('milk', 3.0)     
        self.basket = ShoppingBasket()
        self.basket.add_product(self.product.name, self.product.price)

    def test_basket_should_be_one_product(self):
        self.assertEqual(len(self.basket), 1)


    def test_amount_should_have_tax(self):
        self.assertEqual(self.basket.total(), 3.63)

    def test_getting_product(self):
        self.assertEqual(self.basket.get_product(0).name, self.product.name)

    def test_getting_product_out_of_range(self):
        self.assertRaises(IndexError, self.basket.get_product, 1)



class TestBasketwith_two_Products(unittest.TestCase):

    def setUp(self):  
        self.product1 =  Product('milk', 3.0)
        self.product2 =  Product('water', 2.0)         
        self.basket = ShoppingBasket()
        self.basket.add_product(self.product1.name, self.product1.price)
        self.basket.add_product(self.product2.name, self.product2.price)

    def test_basket_should_be_one_product(self):
        self.assertEqual(len(self.basket), 2)

    def test_amount_should_have_tax(self):
        self.assertEqual(self.basket.total(), 6.05)

    def test_getting_product(self):
        self.assertEqual(self.basket.get_product(1).name, self.product2.name)

    def test_getting_product_out_of_range(self):
        self.assertRaises(IndexError, self.basket.get_product, 2)

if __name__=='__main__':
    unittest.main()