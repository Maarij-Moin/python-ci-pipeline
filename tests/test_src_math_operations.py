import pytest
from src import math_operations

class TestMathOperations:
    """
    Tests for the math_operations module, specifically focusing on the new floor_div function.
    """

    @pytest.mark.parametrize("a, b, expected", [
        (10, 3, 3),
        (10, 2, 5),
        (7, 4, 1),
        (0, 5, 0),
        (5, 1, 5),
        (100, 10, 10),
        (1, 2, 0),
        (-10, 3, -4),  # -3.33 -> -4
        (-10, 2, -5),
        (10, -3, -4),  # -3.33 -> -4
        (-10, -3, 3),  # 3.33 -> 3
        (-1, 2, -1),   # -0.5 -> -1
        (1, -2, -1),   # -0.5 -> -1
        (-2, 1, -2),
        (-2, -1, 2),
    ])
    def test_floor_div_integers(self, a, b, expected):
        """
        Verifies the floor_div function with various integer inputs, including positive,
        negative, and zero values, ensuring correct floor division behavior.
        """
        assert math_operations.floor_div(a, b) == expected

    @pytest.mark.parametrize("a, b, expected", [
        (10.5, 3.0, 3.0),
        (10.0, 2.5, 4.0),
        (7.8, 4.2, 1.0),
        (0.0, 5.5, 0.0),
        (5.1, 1.0, 5.0),
        (1.0, 2.0, 0.0),
        (-10.5, 3.0, -4.0),  # -3.5 -> -4.0
        (-10.0, 2.5, -4.0),
        (10.5, -3.0, -4.0),  # -3.5 -> -4.0
        (-10.5, -3.0, 3.0),  # 3.5 -> 3.0
        (-1.0, 2.0, -1.0),
        (1.0, -2.0, -1.0),
    ])
    def test_floor_div_floats(self, a, b, expected):
        """
        Verifies the floor_div function with various floating-point inputs,
        ensuring correct floor division behavior for floats.
        """
        assert math_operations.floor_div(a, b) == expected

    def test_floor_div_by_zero_integers(self):
        """
        Ensures that floor_div raises a ZeroDivisionError when the divisor is an integer zero.
        """
        with pytest.raises(ZeroDivisionError):
            math_operations.floor_div(10, 0)

    def test_floor_div_by_zero_floats(self):
        """
        Ensures that floor_div raises a ZeroDivisionError when the divisor is a float zero.
        """
        with pytest.raises(ZeroDivisionError):
            math_operations.floor_div(10.5, 0.0)

    def test_floor_div_large_numbers(self):
        """
        Verifies floor_div with large integer inputs to ensure correctness and handle potential
        overflows (though Python integers handle arbitrary size).
        """
        a = 10**18
        b = 3
        expected = 10**18 // 3
        assert math_operations.floor_div(a, b) == expected

    def test_floor_div_small_numbers(self):
        """
        Verifies floor_div with small floating-point numbers close to zero.
        """
        a = 0.0001
        b = 0.00003
        expected = a // b
        assert math_operations.floor_div(a, b) == expected

    def test_floor_div_result_type(self):
        """
        Verifies that the return type of floor_div is an integer for integer inputs
        and a float for float inputs.
        """
        assert isinstance(math_operations.floor_div(10, 3), int)
        assert isinstance(math_operations.floor_div(10.0, 3.0), float)
        assert isinstance(math_operations.floor_div(10, 3.0), float)
        assert isinstance(math_operations.floor_div(10.0, 3), float)

    @pytest.mark.parametrize("a, b", [
        ("10", 2),
        (10, "2"),
        ("10", "2"),
        (None, 2),
        (10, None),
        ([10], 2),
        (10, [2]),
    ])
    def test_floor_div_invalid_types(self, a, b):
        """
        Ensures that floor_div raises a TypeError for invalid input types (e.g., strings, None, lists).
        """
        with pytest.raises(TypeError):
            math_operations.floor_div(a, b)