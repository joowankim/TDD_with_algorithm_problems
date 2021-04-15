from unittest import TestCase

from problems.dragonCurve.DragonCurve import rotate


class Test(TestCase):
    def test_rotate(self):
        self.assertEqual((-5, 4), rotate((4, 5)))
        with self.assertRaises(Exception):
            rotate('s')
