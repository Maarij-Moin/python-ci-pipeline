import pytest
import cmath # For comparing complex numbers
from src.math_operations import sqrt

class TestSqrtFunction:
    """
    Tests for the sqrt function added to math_operations.py.
    """

    @pytest.mark.parametrize("input_val, expected_output", [
        (4, 2.0),
        (9, 3.0),
        (1, 1.0),
        (0, 0.0),
        (100, 10.0),
        (0.25, 0.5),
        (2.25, 1.5),
        (16.0, 4.0),
        (0.0001, 0.01),
        (1_000_000, 1000.0),
    ])
    def test_sqrt_positive_real_numbers(self, input_val, expected_output):
        """
        Verifies that sqrt correctly calculates the square root for positive real numbers (integers and floats).
        """
        assert sqrt(input_val) == expected_output

    def test_sqrt_non_perfect_square(self):
        """
        Verifies that sqrt calculates the square root for a non-perfect square with reasonable precision.
        """
        assert sqrt(2) == pytest.approx(1.4142135623730951)
        assert sqrt(3) == pytest.approx(1.7320508100000000)

    def test_sqrt_negative_number_returns_complex(self):
        """
        Verifies that sqrt returns a complex number for negative input, as per Python's default behavior for `**0.5`.
        """
        result = sqrt(-4)
        assert isinstance(result, complex)
        assert result == cmath.sqrt(-4) # Compare with cmath.sqrt for correctness
        assert result.real == pytest.approx(0.0)
        assert result.imag == pytest.approx(2.0)

        result_neg_float = sqrt(-9.0)
        assert isinstance(result_neg_float, complex)
        assert result_neg_float == cmath.sqrt(-9.0)
        assert result_neg_float.real == pytest.approx(0.0)
        assert result_neg_float.imag == pytest.approx(3.0)

    def test_sqrt_large_float(self):
        """
        Verifies sqrt handles large floating-point numbers correctly.
        """
        large_num = 1.23456789e+20
        expected_sqrt = large_num**0.5
        assert sqrt(large_num) == pytest.approx(expected_sqrt)

    def test_sqrt_small_float(self):
        """
        Verifies sqrt handles very small floating-point numbers correctly.
        """
        small_num = 1.0e-30
        expected_sqrt = small_num**0.5
        assert sqrt(small_num) == pytest.approx(expected_sqrt)

    @pytest.mark.parametrize("input_val", [
        "not_a_number",
        [1, 2],
        None,
        {"key": "value"}
    ])
    def test_sqrt_invalid_input_types(self, input_val):
        """
        Verifies that sqrt raises a TypeError for non-numeric input types.
        """
        with pytest.raises(TypeError):
            sqrt(input_val)