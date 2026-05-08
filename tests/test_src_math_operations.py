import pytest
import sys
from src import math_operations as mo

class TestFactorial:
    """
    Tests for the factorial function in src/math_operations.py.
    """

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
        Verifies that factorial returns the correct value for non-negative integers.
        """
        assert mo.factorial(n) == expected

    def test_factorial_large_number(self):
        """
        Verifies that factorial handles a moderately large number correctly.
        """
        # Factorial of 15 is 1,307,674,368,000
        assert mo.factorial(15) == 1307674368000

    def test_factorial_negative_integer_raises_recursion_error(self):
        """
        Verifies that calling factorial with a negative integer raises a RecursionError
        due to infinite recursion, as per the current implementation.
        """
        with pytest.raises(RecursionError):
            mo.factorial(-1)

        with pytest.raises(RecursionError):
            mo.factorial(-5)

    def test_factorial_float_raises_recursion_error(self):
        """
        Verifies that calling factorial with a float raises a RecursionError
        due to infinite recursion, as per the current implementation (n-1 will never hit 0 or 1).
        """
        with pytest.raises(RecursionError):
            mo.factorial(2.5)

        with pytest.raises(RecursionError):
            mo.factorial(0.5)

    @pytest.mark.parametrize("invalid_input", [
        "abc",
        [1, 2],
        {"a": 1},
        None,
    ])
    def test_factorial_non_numeric_raises_type_error(self, invalid_input):
        """
        Verifies that calling factorial with non-numeric input raises a TypeError.
        """
        with pytest.raises(TypeError):
            mo.factorial(invalid_input)

    def test_factorial_max_recursion_depth(self):
        """
        Verifies that calling factorial with a number that exceeds the default
        recursion limit raises a RecursionError.
        """
        # Get the current recursion limit
        recursion_limit = sys.getrecursionlimit()
        # Test with a number slightly above the limit
        n_exceeding_limit = recursion_limit + 10

        # Temporarily increase recursion limit for this test if needed,
        # but for a number like recursion_limit + 10, it should fail.
        # The default limit is usually 1000.
        with pytest.raises(RecursionError):
            mo.factorial(n_exceeding_limit)