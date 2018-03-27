import unittest

from Polynomial import Polynomial

class PolynomTests(unittest.TestCase):

    def test_init_empty_list_values(self):
        p = Polynomial([])

        self.assertEqual(p.coeffs, [0])

    def test_init_zero_degree(self):
        p = Polynomial([1])

        self.assertEqual(p.coeffs, [1])

    def test_init_polynom_monom(self):
        p = Polynomial([1, 0])

        self.assertEqual(p.coeffs, [1, 0])

    def test_init_senior_coeffs_isnull(self):
        p = Polynomial([0, 0, 1])

        self.assertEqual(p.coeffs, [1])

    def test_init_int_values_coeffs(self):
        p = Polynomial([1, 2, 3])

        self.assertEqual(p.coeffs, [1, 2, 3])

    def test_init_float_values_coeffs(self):
        p = Polynomial([1.9, 3.5, 7.6])

        self.assertEqual(p.coeffs, [1.9, 3.5, 7.6])

    def test_add_equal_degree_example_1(self):
        p1 = Polynomial([6, -2, 0])
        p2 = Polynomial([-1, 5, 4])
        res = p1 + p2
        self.assertEqual(res.coeffs, [5, 3, 4])

    def test_add_equal_degree_example_2(self):
        p1 = Polynomial([5, 4, 4])
        p2 = Polynomial([-5, -3, 0])
        res = p1 + p2
        self.assertEqual(res.coeffs, [1, 4])

    def test_add_equal_degree_example_3(self):
        p1 = Polynomial([10, -4, 6])
        p2 = Polynomial([-10, 4, -6])
        res = p1 + p2
        self.assertEqual(res.coeffs, [0])

    def test_add_equal_degree_example_4(self):
        p1 = Polynomial([])
        p2 = Polynomial([])
        res = p1 + p2
        self.assertEqual(res.coeffs, [0])

    def test_add_equal_degree_example_5(self):
        p1 = Polynomial([1])
        p2 = Polynomial([-1])
        res = p1 + p2
        self.assertEqual(res.coeffs, [0])

    def test_add_equal_degree_example_6(self):
        p1 = Polynomial([2])
        p2 = Polynomial([5])
        res = p1 + p2
        self.assertEqual(res.coeffs, [7])

    def test_add_not_equal_degree_example_1(self):
        p1 = Polynomial([2, 5, 2])
        p2 = Polynomial([3, -2, 3, -1])
        res = p1 + p2
        self.assertEqual(res.coeffs, [3, 0, 8, 1])

    def test_add_not_equal_degree_example_2(self):
        p1 = Polynomial([2, 5, 2])
        p2 = Polynomial([3, -2, -5, -2])
        res = p1 + p2
        self.assertEqual(res.coeffs, [3, 0, 0, 0])

    def test_add_not_equal_degree_example_3(self):
        p1 = Polynomial([3, 2, 5, 2])
        p2 = Polynomial([-3, -3, 1])
        res = p1 + p2
        self.assertEqual(res.coeffs, [3, -1, 2, 3])

    def test_add_not_equal_degree_example_4(self):
        p1 = Polynomial([3, 2, 5, 2])
        p2 = Polynomial([-2, -5, -2])
        res = p1 + p2
        self.assertEqual(res.coeffs, [3, 0, 0, 0])

    def test_add_not_equal_degree_example_5(self):
        p1 = Polynomial([3, 2, 5, 2])
        p2 = Polynomial([1])
        res = p1 + p2
        self.assertEqual(res.coeffs, [3, 2, 5, 3])

    def test_add_not_equal_degree_example_6(self):
        p1 = Polynomial([1])
        p2 = Polynomial([3, 2, 5, 2])
        res = p1 + p2
        self.assertEqual(res.coeffs, [3, 2, 5, 3])

    def test_add_not_equal_degree_example_7(self):
        p1 = Polynomial([0])
        p2 = Polynomial([3, 2, 5, 2])
        res = p1 + p2
        self.assertEqual(res.coeffs, [3, 2, 5, 2])

    def test_add_not_equal_degree_example_8(self):
        p1 = Polynomial([])
        p2 = Polynomial([3, 2, 5, 2])
        res = p1 + p2
        self.assertEqual(res.coeffs, [3, 2, 5, 2])

    def test_add_not_equal_degree_example_9(self):
        p1 = Polynomial([1, 7])
        p2 = Polynomial([3, 2, 5, 2])
        res = p1 + p2
        self.assertEqual(res.coeffs, [3, 2, 6, 9])

    def test_add_not_equal_degree_example_10(self):
        p1 = Polynomial([3, 2, 5, 2])
        p2 = 1
        res = p1 + p2
        self.assertEqual(res.coeffs, [3, 2, 5, 3])

    def test_add_not_equal_degree_example_11(self):
        p1 = Polynomial([2.9, 3.4, 1.2, 4.5])
        p2 = Polynomial([1.0, 5.3, 4.2, 3.3])
        res = p1 + p2
        self.assertEqual(res.coeffs, [3.9, 8.7, 5.4, 7.8])

    def test_add_not_equal_degree_example_12(self):
        p1 = Polynomial([2.9, 3.4, 1.2, 5.6])
        p2 = 1.2
        res = p1 + p2
        self.assertEqual(res.coeffs, [2.9, 3.4, 1.2, 6.8])

    def test_multiply_example_1(self):
        p1 = Polynomial([2, 5, 2])
        p2 = Polynomial([-2, 1])
        res = p1 * p2
        self.assertEqual(res.coeffs, [-4, -8, 1, 2])

    def test_multiply_example_2(self):
        p1 = Polynomial([2, 5, 2])
        p2 = Polynomial([0])
        res = p1 * p2
        self.assertEqual(res.coeffs, [0])

    def test_multiply_example_3(self):
        p1 = Polynomial([2, 5, 2])
        p2 = Polynomial([])
        res = p1 * p2
        self.assertEqual(res.coeffs, [0])

    def test_multiply_example_4(self):
        p1 = Polynomial([1, 0, 7])
        p2 = Polynomial([-8, 3])
        res1 = p1 * p2
        self.assertEqual(res1.coeffs, [-8, 3, -56, 21])

        res2 = res1 * p2
        self.assertEqual(res2.coeffs, [64, -48, 457, -336, 63])

    def test_multiply_example_5(self):
        p1 = Polynomial([2, 0, 4])
        p2 = 2
        res = p1 * p2
        self.assertEqual(res.coeffs, [4, 0, 8])

    def test_multiply_example_6(self):
        p1 = Polynomial([2.1, 0, 4.5])
        p2 = 2
        res = p1 * p2
        self.assertEqual(res.coeffs, [4.2, 0, 9])

    def test_equals_examples(self):
        p1 = Polynomial([2, 5, 2])
        p2 = Polynomial([2, 5, 2])
        self.assertTrue(p1 == p2)

        p1 = Polynomial([0, 2, 0, 2])
        p2 = Polynomial([2, 0, 2])
        self.assertTrue(p1 == p2)

        p1 = Polynomial([0, 1.9, 0.0, 2.5])
        p2 = Polynomial([1.9, 0, 2.5])
        self.assertTrue(p1 == p2)

    def test_poly_to_string_examples_1(self):
        p1 = Polynomial([-2, -3, -8])
        self.assertEqual(str(p1), '-2x2-3x-8')

        p2 = Polynomial([2, 5, 2])
        self.assertEqual(str(p2), '2x2+5x+2')

        p3 = Polynomial([-1, -1, -1])
        self.assertEqual(str(p3), '-x2-x-1')

        p4 = Polynomial([-1, -1, 0])
        self.assertEqual(str(p4), '-x2-x')

    def test_poly_to_string_examples_2(self):
        p1 = Polynomial([1])
        self.assertEqual(str(p1), '1')

        p2 = Polynomial([0, 0])
        self.assertEqual(str(p2), '0')

        p3 = Polynomial([-1])
        self.assertEqual(str(p3), '-1')

    def test_poly_to_string_examples_3(self):
        p1 = Polynomial([5, -6])
        self.assertEqual(str(p1), '5x-6')

        p2 = Polynomial([1.5, -2.4])
        self.assertEqual(str(p2), '1.5x-2.4')

        p3 = Polynomial([])
        self.assertEqual(str(p3), '0')

if __name__ == '__main__':
    unittest.main()