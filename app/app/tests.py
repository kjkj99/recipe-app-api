from django.test import SimpleTestCase
from app import calc


class CalcTest(SimpleTestCase):
    def test_add(self):
        res = calc.add(2, 4)
        self.assertEqual(res, 6)


    def test_sub(self):
        res = calc.sub(3, 1)
        self.assertEqual(res, 2)
