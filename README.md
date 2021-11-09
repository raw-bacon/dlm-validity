# dlm-validity
A scipt using [Z3](https://github.com/Z3Prover/z3) to check validity of distributive l-monoid formulas

# Setup
This might only work for Linux, probably also for OSX, probably not for Windows.

Build and install Z3 with the `--python` flag, i.e., execute
```bash
git clone https://github.com/Z3Prover/z3
cd z3
python scripts/mk_make.py --python
cd build
make
make install
```
and run
```bash
pip install z3-solver
```
to get Z3 ready.

# Usage
Clone this repository using
```
git clone https://github.com/raw-bacon/dlm-validity
```
then `cd` into it and get a python shell by running
either `python` or `python3`. To check whether
`xyx ^ z <= yxy v z` is valid in all distributive _l_-monoids,
run the following lines of python:
```python
from dlm import check
left = set(["xyx", "z"])
right = set(["yxy", "z"])
check(left, right)
```
The program will output `no solution`, indicating that the formula is valid.
The output of
```python
from dlm import check
left = set(["xyx"])
right = set(["yxy"])
check(left, right)
```
will be something like
```
[xy = 1, xyx = 2, x = 3, yxy = -1,  = 2, yx = 1, y = 0]
```
encoding a counterexample to the inequation `xyx <= yxy`.

# Conventions
Variables are single case-sensitive characters
like `x`, `X`, or `@`.
Although this gives an upper bound on the number of variables
a formula may contain, this should not be an issue.
The empty string stands for the identity element.

