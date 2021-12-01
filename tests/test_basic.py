from unittest import TestCase, main
from .context import Dimension, L, M, T, DIMLESS


class TestDimension(TestCase):

    def test_equal(self):
        self.assertEqual(Dimension("L"), L)
        self.assertEqual(Dimension("M"), M)
        self.assertEqual(Dimension("T"), T)
        self.assertEqual(Dimension(), DIMLESS)

    def test_not_equal(self):
        self.assertNotEqual(Dimension("L"), Dimension("M"))
        self.assertNotEqual(Dimension("L"), Dimension("T"))
        self.assertNotEqual(Dimension("L"), Dimension())
        self.assertNotEqual(Dimension("LMT"), Dimension("TMLT"))
        self.assertNotEqual(Dimension("LMT-2"), Dimension("LMT"))

    def test_sequence_equal(self):
        self.assertEqual(Dimension("LMT"), Dimension("TML"))
        self.assertEqual(Dimension("LM-2T"), Dimension("LTM-2"))

    def test_dict_equal(self):
        self.assertEqual(Dimension("L").dim_dict, {'L': 1, 'M': 0, 'T': 0})
        self.assertEqual(Dimension("LT-1").dim_dict, {'L': 1, 'M': 0, 'T': -1})


if __name__ == '__main__':
    main()
