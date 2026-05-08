import pytest
from src import math_operations

class TestPowFunction:
    """
    Tests for the newly added 'pow' function in math_operations.py.
    """

    @pytest.mark.parametrize(
        "base, exponent, expected",
        [
            (2, 3, 8),          # Positive integers
            (5, 0, 1),          # Exponent is zero
            (0, 5, 0),          # Base is zero, positive exponent
            (0, 0, 1),          # Zero to the power of zero (Python's behavior)
            (-2, 3, -8),        # Negative base, odd exponent
            (-2, 2, 4),         # Negative base, even exponent
            (10, 1, 10),        # Exponent is one
            (1, 10, 1),         # Base is one
            (100, 2, 10000),    # Larger numbers
            (1.5, 2, 2.25),     # Float base, integer exponent
            (2, 0.5, pytest.approx(1.41421356237)), # Integer base, float exponent (sqrt)
            (0.5, 0.5, pytest.approx(0.70710678118)), # Float base, float exponent
        ],
        ids=[
            "positive_integers",
            "exponent_zero",
            "base_zero_positive_exponent",
            "zero_to_zero",
            "negative_base_odd_exponent",
            "negative_base_even_exponent",
            "exponent_one",
            "base_one",
            "larger_numbers",
            "float_base_integer_exponent",
            "integer_base_float_exponent",
            "float_base_float_exponent",
        ]
    )
    def test_pow_basic_cases(self, base, exponent, expected):
        """
        Verifies the 'pow' function with various valid numeric inputs,
        including positive, negative, zero, and float bases/exponents.
        """
        assert math_operations.pow(base, exponent) == expected

    @pytest.mark.parametrize(
        "base, exponent, expected",
        [
            (2, -1, 0.5),       # Positive base, negative exponent
            (2, -2, 0.25),      # Positive base, negative exponent
            (0.5, -1, 2.0),     # Float base, negative exponent
            (-2, -1, -0.5),     # Negative base, negative odd exponent
            (-2, -2, 0.25),     # Negative base, negative even exponent
        ],
        ids=[
            "positive_base_negative_exponent_1",
            "positive_base_negative_exponent_2",
            "float_base_negative_exponent",
            "negative_base_negative_odd_exponent",
            "negative_base_negative_even_exponent",
        ]
    )
    def test_pow_negative_exponents(self, base, exponent, expected):
        """
        Verifies the 'pow' function correctly handles negative exponents,
        resulting in fractional values.
        """
        assert math_operations.pow(base, exponent) == expected

    def test_pow_large_numbers(self):
        """
        Verifies the 'pow' function handles large integer inputs correctly.
        """
        assert math_operations.pow(10, 10) == 10_000_000_000
        assert math_operations.pow(2, 63) == 9223372036854775808

    @pytest.mark.parametrize(
        "base, exponent",
        [
            ("a", 2),           # String base
            (2, "b"),           # String exponent
            (None, 2),          # None base
            (2, None),          # None exponent
            ([1], 2),           # List base
            (2, {1}),           # Set exponent
        ],
        ids=[
            "string_base",
            "string_exponent",
            "none_base",
            "none_exponent",
            "list_base",
            "set_exponent",
        ]
    )
    def test_pow_type_errors(self, base, exponent):
        """
        Verifies that 'pow' raises a TypeError when non-numeric types are provided
        as base or exponent, as expected from Python's built-in `**` operator.
        """
        with pytest.raises(TypeError):
            math_operations.pow(base, exponent)

    def test_pow_float_precision(self):
        """
        Verifies that 'pow' returns results with appropriate floating-point precision.
        """
        # Using pytest.approx for float comparisons
        assert math_operations.pow(2.0, 0.5) == pytest.approx(1.4142135623730951)
        assert math_operations.pow(3.14, 2.71) == pytest.approx(30.63914902047392)