import unittest
from Lesson17 import ex6_1
from Lesson17 import ex7_2
from Lesson17 import ex11_2
from Lesson17 import ex16_2

class AllTests(unittest.TestCase):

    def test_dict(self):
        self.assertEqual(ex6_1.for_dict(('Bitcoin', 'Ether', 'Ripple', 'Litecoin'), ('BTC', 'ETH', 'XRP', 'LTC')),
                         {'Bitcoin': 'BTC', 'Ether': 'ETH', 'Ripple': 'XRP', 'Litecoin': 'LTC'})

    def test_cel_calc(self):
        self.assertEqual(ex7_2.cels(0), 'Температура по Кельвину: 273.15 Температура по Фарренгейту: 32.0')

    def test_kel_calc(self):
        self.assertEqual(ex7_2.kelv(0), 'Tемпература по Цельсию: -273.15 Температура по Фарренгейту: -459.67')

    def test_far_calc(self):
        self.assertEqual(ex7_2.farren(0), 'Температура по Кельвину: 255.37 Tемпература по Цельсию: -17.78')

    def test_email(self):
        self.assertEqual(ex11_2.hide_email('dinay8@gmail.com'), 'din***@**.com')

    def test_num_phone(self):
        self.assertEqual(ex16_2.phone_num('063-999-99-99'), '(+38) 063 999-99-99')
        self.assertEqual(ex16_2.phone_num('063 999-99-99'), '(+38) 063 999-99-99')
        self.assertEqual(ex16_2.phone_num('063-99999-99'), '(+38) 063 999-99-99')
        self.assertEqual(ex16_2.phone_num('+38063999-99-99'), '(+38) 063 999-99-99')
        self.assertEqual(ex16_2.phone_num('380639999999'), '(+38) 063 999-99-99')

if __name__ == '__main__':
    unittest.main()