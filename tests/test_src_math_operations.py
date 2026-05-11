import pytest
from src import math_operations

class TestMathOperations:
    """
    Tests for the math_operations module, focusing on the newly added gcd function
    and ensuring existing functions like factorial still work.
    """

    @pytest.mark.parametrize("a, b, expected", [
        (48, 18, 6),
        (18, 48, 6),
        (17, 13, 1),  # Coprime numbers
        (10, 5, 5),
        (5, 10, 5),
        (7, 7, 7),
        (0, 5, 5),  # GCD(0, n) = n
        (5, 0, 5),  # GCD(n, 0) = n
        (1, 1, 1),
        (1, 100, 1),
        (100, 1, 1),
        (14, 28, 14), # One is a multiple of the other
        (28, 14, 14),
    ])
    def test_gcd_positive_integers(self, a, b, expected):
        """
        Verifies the gcd function for various pairs of positive integers,
        including coprime numbers and cases where one number is a multiple of the other.
        """
        assert math_operations.gcd(a, b) == expected

    def test_gcd_zero_zero(self):
        """
        Verifies the gcd function for gcd(0, 0), which typically returns 0
        when using the Euclidean algorithm directly.
        """
        assert math_operations.gcd(0, 0) == 0

    @pytest.mark.parametrize("a, b, expected", [
        (-10, 5, 5),    # gcd(-10, 5) -> gcd(5, -10 % 5) -> gcd(5, 0) -> 5
        (10, -5, -5),   # gcd(10, -5) -> gcd(-5, 10 % -5) -> gcd(-5, 0) -> -5
        (-10, -5, -5),  # gcd(-10, -5) -> gcd(-5, -10 % -5) -> gcd(-5, 0) -> -5
        (-48, 18, 6),   # gcd(-48, 18) -> gcd(18, -48 % 18) -> gcd(18, 6) -> 6
        (48, -18, -6),  # gcd(48, -18) -> gcd(-18, 48 % -18) -> gcd(-18, 12) -> gcd(12, -18 % 12) -> gcd(12, -6) -> gcd(-6, 12 % -6) -> gcd(-6, 0) -> -6
        (-48, -18, -6), # gcd(-48, -18) -> gcd(-18, -48 % -18) -> gcd(-18, -12) -> gcd(-12, -18 % -12) -> gcd(-12, -6) -> gcd(-6, -12 % -6) -> gcd(-6, 0) -> -6
        (-7, 7, 7),
        (7, -7, -7),
        (-7, -7, -7),
    ])
    def test_gcd_with_negative_integers(self, a, b, expected):
        """
        Verifies the gcd function's behavior with negative integers.
        The Euclidean algorithm with Python's modulo operator can return negative results
        if the second argument to modulo is negative.
        """
        assert math_operations.gcd(a, b) == expected

    @pytest.mark.parametrize("n, expected", [
        (0, 1),
        (1, 1),
        (2, 2),
        (3, 6),
        (4, 24),
        (5, 120),
        (10, 3628800),
    ])
    def test_factorial_positive_integers(self, n, expected):
        """
        Verifies the factorial function for non-negative integers.
        This function was present in the diff, so a basic check is included.
        """
        assert math_operations.factorial(n) == expected

    def test_factorial_negative_input_raises_recursion_error(self):
        """
        Verifies that factorial raises a RecursionError for negative input,
        as it will recurse indefinitely.
        """
        with pytest.raises(RecursionError):
            math_operations.factorial(-1)