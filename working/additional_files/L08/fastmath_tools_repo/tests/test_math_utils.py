import numpy as np
from fastmath_tools.math_utils import gaussian, integrate_simpson

def test_gaussian_symmetry():
    x = np.linspace(-2, 2, 100)
    assert np.allclose(gaussian(x), gaussian(-x))

def test_integration_accuracy():
    result = integrate_simpson(np.exp, 0, 1, N=1000)
    expected = np.e - 1
    assert abs(result - expected) < 1e-4

def test_regression_gaussian_value():
    val = gaussian(0)
    assert abs(val - 0.39894228) < 1e-6
