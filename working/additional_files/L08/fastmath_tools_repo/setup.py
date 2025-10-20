from setuptools import setup, find_packages

setup(
    name="fastmath_tools",
    version="0.1.0",
    author="Giovanni Ferrante",
    description="Fast math utilities with testing and profiling examples",
    packages=find_packages(),
    install_requires=["numpy", "numba"],
    python_requires=">=3.8",
)
