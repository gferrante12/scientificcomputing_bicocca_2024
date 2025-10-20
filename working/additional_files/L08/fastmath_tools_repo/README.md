# fastmath_tools

Repository for:
- Building and packaging a Python module
- Unit and regression testing with GitHub Actions
- Profiling and speeding up code with Numba

## Installation
```
pip install .
pip install -r requirements.txt
```

## Testing
```
pytest -v
```

## Install dependencies for the next step
python3 -m pip install --upgrade build
pip install --upgrade twine

## Publishing to Test PyPI
```
python setup.py sdist bdist_wheel
pip install ./dist/fastmath_tools-0.1.0-py3-none-any.whl
twine upload --repository testpypi dist/*
```
