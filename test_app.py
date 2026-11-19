import unittest

from app import final_price


class TestFinalPrice(unittest.TestCase):
    def test_final_price_applies_discount(self):
        self.assertEqual(final_price(100_000, 10), 90_000)


    def test_final_price_can_have_no_discount(self):
        self.assertEqual(final_price(50_000, 0), 50_000)


    def test_final_price_rejects_invalid_values(self):
        for price, discount in [(-1, 10), (100, -1), (100, 101)]:
            with self.subTest(price=price, discount=discount):
                with self.assertRaises(ValueError):
                    final_price(price, discount)
