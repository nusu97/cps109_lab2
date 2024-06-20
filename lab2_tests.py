#!/usr/bin/python3
import unittest
import lab2_funcs


class TestLetterGradeFunction(unittest.TestCase):

    def test_grade_A(self):
        self.assertEqual(lab2_funcs.lettergrade(95), 'A')
        self.assertEqual(lab2_funcs.lettergrade(88), 'A')
        self.assertEqual(lab2_funcs.lettergrade(80), 'A')

    def test_grade_B(self):
        self.assertEqual(lab2_funcs.lettergrade(75), 'B')
        self.assertEqual(lab2_funcs.lettergrade(70), 'B')
        self.assertEqual(lab2_funcs.lettergrade(71), 'B')

    def test_grade_C(self):
        self.assertEqual(lab2_funcs.lettergrade(60), 'C')
        self.assertEqual(lab2_funcs.lettergrade(65), 'C')
        self.assertEqual(lab2_funcs.lettergrade(69), 'C')

    def test_grade_D(self):
        self.assertEqual(lab2_funcs.lettergrade(50), 'D')
        self.assertEqual(lab2_funcs.lettergrade(55), 'D')
        self.assertEqual(lab2_funcs.lettergrade(59), 'D')

    def test_grade_F(self):
        self.assertEqual(lab2_funcs.lettergrade(0), 'F')
        self.assertEqual(lab2_funcs.lettergrade(30), 'F')
        self.assertEqual(lab2_funcs.lettergrade(49), 'F')

    def test_invalid_input(self):
        self.assertIsNone(lab2_funcs.lettergrade(-10))
        self.assertIsNone(lab2_funcs.lettergrade(105))
        self.assertIsNone(lab2_funcs.lettergrade(101))


class TestCalculatorFunction(unittest.TestCase):

    def test_addition(self):
        self.assertEqual(lab2_funcs.calculator(5, 3, '+'), 8)
        self.assertEqual(lab2_funcs.calculator(-2, 7, '+'), 5)
        self.assertEqual(lab2_funcs.calculator(0, 0, '+'), 0)

    def test_subtraction(self):
        self.assertEqual(lab2_funcs.calculator(5, 3, '-'), 2)
        self.assertEqual(lab2_funcs.calculator(7, -2, '-'), 9)
        self.assertEqual(lab2_funcs.calculator(0, 0, '-'), 0)

    def test_multiplication(self):
        self.assertEqual(lab2_funcs.calculator(5, 3, '*'), 15)
        self.assertEqual(lab2_funcs.calculator(-2, -7, '*'), 14)
        self.assertEqual(lab2_funcs.calculator(0, 5, '*'), 0)

    def test_division(self):
        self.assertEqual(lab2_funcs.calculator(6, 2, '/'), 3)
        self.assertEqual(lab2_funcs.calculator(10, -2, '/'), -5)
        self.assertIsNone(lab2_funcs.calculator(5, 0, '/'))

    def test_exponentiation(self):
        self.assertEqual(lab2_funcs.calculator(2, 3, '**'), 8)
        self.assertEqual(lab2_funcs.calculator(5, 0, '**'), 1)
        self.assertEqual(lab2_funcs.calculator(4, -1, '**'), 0.25)

    def test_invalid_operator(self):
        self.assertIsNone(lab2_funcs.calculator(5, 3, 'invalid'))
        self.assertIsNone(lab2_funcs.calculator(2, 4, ''))
        self.assertIsNone(lab2_funcs.calculator(1, 1, None))


class TestDuplicatesFunction(unittest.TestCase):

    def test_three_of_a_kind(self):
        self.assertEqual(lab2_funcs.duplicates([1, 1, 1]), 'three-of-a-kind')
        self.assertEqual(lab2_funcs.duplicates((2, 2, 2)), 'three-of-a-kind')
        self.assertEqual(lab2_funcs.duplicates('xxx'), 'three-of-a-kind')

    def test_two_of_a_kind(self):
        self.assertEqual(lab2_funcs.duplicates([1, 1, 2]), 'two-of-a-kind')
        self.assertEqual(lab2_funcs.duplicates(
            ('a', 'b', 'b')), 'two-of-a-kind')
        self.assertEqual(lab2_funcs.duplicates('xyx'), 'two-of-a-kind')

    def test_one_of_a_kind(self):
        self.assertEqual(lab2_funcs.duplicates([1, 2, 3]), 'one-of-a-kind')
        self.assertEqual(lab2_funcs.duplicates((4, 5, 6)), 'one-of-a-kind')
        self.assertEqual(lab2_funcs.duplicates('xyz'), 'one-of-a-kind')

    def test_invalid_input(self):
        self.assertEqual(lab2_funcs.duplicates([]), 'invalid input')
        self.assertEqual(lab2_funcs.duplicates([1, 2]), 'invalid input')
        self.assertEqual(lab2_funcs.duplicates([1, 2, 3, 4]), 'invalid input')
        self.assertEqual(lab2_funcs.duplicates(('a', 'b')), 'invalid input')
        self.assertEqual(lab2_funcs.duplicates(
            ('a', 'b', 'c', 'd')), 'invalid input')
        self.assertEqual(lab2_funcs.duplicates('x'), 'invalid input')
        self.assertEqual(lab2_funcs.duplicates('xyzw'), 'invalid input')


class TestIncreasingFunction(unittest.TestCase):

    def test_increasing_strict(self):
        self.assertTrue(lab2_funcs.increasing([1, 2, 3], True))
        self.assertFalse(lab2_funcs.increasing([1, 2, 2], True))
        self.assertFalse(lab2_funcs.increasing([3, 2, 1], True))
        self.assertTrue(lab2_funcs.increasing([-1, 0, 1], True))

    def test_increasing_non_strict(self):
        self.assertTrue(lab2_funcs.increasing([1, 2, 3], False))
        self.assertTrue(lab2_funcs.increasing([1, 1, 2], False))
        self.assertFalse(lab2_funcs.increasing([3, 2, 1], False))
        self.assertTrue(lab2_funcs.increasing([0, 0, 0], False))

    def test_invalid_input(self):
        self.assertEqual(lab2_funcs.increasing([], True), 'invalid input')
        self.assertEqual(lab2_funcs.increasing([1, 2], True), 'invalid input')
        self.assertEqual(lab2_funcs.increasing(
            [1, 2, 3, 4], True), 'invalid input')
        self.assertEqual(lab2_funcs.increasing(
            [1, 2, 3], None), 'invalid input')
        self.assertEqual(lab2_funcs.increasing(
            [1, 2, 3], 'string'), 'invalid input')


class TestInversionsFunction(unittest.TestCase):

    def test_list_of_integer_inputs(self):
        self.assertEqual(lab2_funcs.inversions([1, 2, 3]), 0)
        self.assertEqual(lab2_funcs.inversions([2, 1, 3]), 1)
        self.assertEqual(lab2_funcs.inversions([2, 3, 1]), 2)
        self.assertEqual(lab2_funcs.inversions([3, 2, 1]), 3)

    def test_string_inputs(self):
        self.assertEqual(lab2_funcs.inversions('act'), 0)
        self.assertEqual(lab2_funcs.inversions('cat'), 1)
        self.assertEqual(lab2_funcs.inversions('tac'), 2)
        self.assertEqual(lab2_funcs.inversions('ton'), 3)

    def test_list_of_string_inputs(self):
        self.assertEqual(lab2_funcs.inversions(
            ['apple', 'banana', 'cherry']), 0)
        self.assertEqual(lab2_funcs.inversions(
            ['apple', 'cherry', 'banana']), 1)
        self.assertEqual(lab2_funcs.inversions(
            ['banana', 'cherry', 'apple']), 2)
        self.assertEqual(lab2_funcs.inversions(
            ['cherry', 'banana', 'apple']), 3)

    def test_invalid_inputs(self):
        self.assertEqual(lab2_funcs.inversions([]), -1)
        self.assertEqual(lab2_funcs.inversions([1, 2]), -1)
        self.assertEqual(lab2_funcs.inversions([1, 2, 3, 4]), -1)
        self.assertEqual(lab2_funcs.inversions(('a', 'b')), -1)
        self.assertEqual(lab2_funcs.inversions(('a', 'b', 'c', 'd')), -1)
        self.assertEqual(lab2_funcs.inversions('x'), -1)
        self.assertEqual(lab2_funcs.inversions('xyzw'), -1)


class TestSumSquaresFunction(unittest.TestCase):

    def test_sum_squares_positive_1(self):
        # 1 + 4 + 9 + 16 + 25 = 55
        self.assertEqual(lab2_funcs.sumsquares(5), 55)

    def test_sum_squares_positive_2(self):
        self.assertEqual(lab2_funcs.sumsquares(3), 14)  # 1 + 4 + 9 = 14

    def test_sum_squares_zero(self):
        self.assertEqual(lab2_funcs.sumsquares(0), 0)  # No squares to sum

    def test_large_input(self):
        # Sum of squares up to 10000
        self.assertEqual(lab2_funcs.sumsquares(10000), 333383335000)


class TestSumEvenFunction(unittest.TestCase):

    def test_sum_even_positive_1(self):
        self.assertEqual(lab2_funcs.sumeven(6), 30)  # 2 + 4 + 6 + 8 + 10 = 30

    def test_sum_even_positive_2(self):
        self.assertEqual(lab2_funcs.sumeven(4), 12)  # 0 + 2 + 4 + 6 = 12

    def test_sum_even_zero(self):
        self.assertEqual(lab2_funcs.sumeven(0), 0)  # No even numbers to sum

    def test_sum_even_large(self):
        # Sum of first 1 million even numbers
        self.assertEqual(lab2_funcs.sumeven(10**6), 999999000000)


class TestStringToFloatList(unittest.TestCase):

    def test_positive_integers(self):
        self.assertEqual(lab2_funcs.stringtofloatlist(
            "1.0,2.0,3.0,4.0"), [1.0, 2.0, 3.0, 4.0])

    def test_positive_floats(self):
        self.assertEqual(lab2_funcs.stringtofloatlist(
            "0.1,0.2,0.3,0.4"), [0.1, 0.2, 0.3, 0.4])

    def test_mixed_integers_and_floats(self):
        self.assertEqual(lab2_funcs.stringtofloatlist(
            "1.0,0.5,2.0,1.5"), [1.0, 0.5, 2.0, 1.5])

    def test_negative_numbers(self):
        self.assertEqual(lab2_funcs.stringtofloatlist(
            "-1.0,-2.0,-3.0,-4.0"), [-1.0, -2.0, -3.0, -4.0])

    def test_single_number(self):
        self.assertEqual(lab2_funcs.stringtofloatlist("3.14"), [3.14])

    def test_mixed_input(self):
        self.assertEqual(lab2_funcs.stringtofloatlist(
            "1.0,2.5,-3.0,4.2"), [1.0, 2.5, -3.0, 4.2])


class TestOddDigitSum(unittest.TestCase):

    def test_positive_integer(self):
        self.assertEqual(lab2_funcs.odddigitsum(
            123456789), 25)  # 1 + 3 + 5 + 7 + 9 = 25

    def test_negative_integer(self):
        self.assertEqual(lab2_funcs.odddigitsum(-13579),
                         25)  # 1 + 3 + 5 + 7 + 9 = 25

    def test_positive_integer_with_even_digits(self):
        self.assertEqual(lab2_funcs.odddigitsum(24680), 0)  # No odd digits

    def test_negative_integer_with_even_digits(self):
        self.assertEqual(lab2_funcs.odddigitsum(-24680), 0)  # No odd digits

    def test_zero(self):
        self.assertEqual(lab2_funcs.odddigitsum(0), 0)  # No odd digits

    def test_single_odd_digit(self):
        self.assertEqual(lab2_funcs.odddigitsum(7), 7)  # Single odd digit

    def test_single_even_digit(self):
        self.assertEqual(lab2_funcs.odddigitsum(4), 0)  # Single even digit

    def test_large_input(self):
        self.assertEqual(lab2_funcs.odddigitsum(
            123456789123456789123456789), 75)  # Sum of all odd digits


class TestMaxByType(unittest.TestCase):

    def test_all_integer(self):
        self.assertEqual(lab2_funcs.maxbytype([3, 1, 4, 2]), (4, None, None))

    def test_all_float(self):
        self.assertEqual(lab2_funcs.maxbytype(
            [3.14, 1.0, 4.2]), (None, 4.2, None))

    def test_all_string(self):
        self.assertEqual(lab2_funcs.maxbytype(
            ['apple', 'banana', 'cherry']), (None, None, 'cherry'))

    def test_mixed_input_small(self):
        self.assertEqual(lab2_funcs.maxbytype(
            [3, 1.5, 'apple', 4.2, 'banana']), (3, 4.2, 'banana'))

    def test_empty_input(self):
        self.assertEqual(lab2_funcs.maxbytype([]), (None, None, None))

    def test_mixed_types_with_none(self):
        self.assertEqual(lab2_funcs.maxbytype(
            [3, 1.5, None, 4.2, 'banana']), (3, 4.2, 'banana'))

    def test_mixed_types_with_none2(self):
        mixed_input_with_none = list(range(1000)) + [3.14, 1.0, 4.2] + [None, 'banana', 'cherry']
        self.assertEqual(lab2_funcs.maxbytype(
            mixed_input_with_none), (999, 4.2, 'cherry'))

    def test_large_input(self):
        large_input = list(range(1000000)) + \
            [None] + ['apple', 'banana', 'cherry']
        self.assertEqual(lab2_funcs.maxbytype(
            large_input), (999999, None, 'cherry'))


class TestListExponential(unittest.TestCase):

    def test_positive_exponents(self):
        self.assertEqual(lab2_funcs.listexponential(5, 2), [1, 2, 4, 8, 16])

    def test_negative_exponent(self):
        self.assertEqual(lab2_funcs.listexponential(3, -2),
                         [1, -2, 4])  # Negative exponent is allowed

    def test_float_base(self):
        self.assertEqual(lab2_funcs.listexponential(
            4, 0.5), [1, 0.5, 0.25, 0.125])

    def test_large_exponent(self):
        self.assertEqual(lab2_funcs.listexponential(6, 10),
                         [1, 10, 100, 1000, 10000, 100000])

    def test_large_base(self):
        self.assertEqual(lab2_funcs.listexponential(5, 1000), [
                         1, 1000, 1000000, 1000000000, 1000000000000])

    def test_mixed_inputs(self):
        self.assertEqual(lab2_funcs.listexponential(
            4, -0.5), [1, -0.5, 0.25, -0.125])

    def test_zero_base(self):
        # Any number to the power of 0 is 1
        self.assertEqual(lab2_funcs.listexponential(5, 0), [1, 0, 0, 0, 0])


class TestDigitCat(unittest.TestCase):

    def test_digits_only(self):
        self.assertEqual(lab2_funcs.digitcat("abc123def456"), 123456)

    def test_no_digits(self):
        self.assertIsNone(lab2_funcs.digitcat("abcxyz"))

    def test_empty_string(self):
        self.assertIsNone(lab2_funcs.digitcat(""))

    def test_digits_with_spaces(self):
        self.assertEqual(lab2_funcs.digitcat("1 2 3 4"), 1234)

    def test_digits_with_special_characters(self):
        self.assertEqual(lab2_funcs.digitcat("1$2#3%4"), 1234)

    def test_negative_number(self):
        self.assertEqual(lab2_funcs.digitcat("abc-123def"), 123)

    def test_decimal_number(self):
        self.assertEqual(lab2_funcs.digitcat("abc3.14def"), 314)

    def test_large_number(self):
        self.assertEqual(lab2_funcs.digitcat("abc1234567890def"), 1234567890)

    def test_mixed_input(self):
        self.assertEqual(lab2_funcs.digitcat("a1b2c3d4"), 1234)


if __name__ == '__main__':
    unittest.main(exit=True)
