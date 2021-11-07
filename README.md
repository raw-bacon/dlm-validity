# dlm-validity
A scipt using Z3 to check validity of distributive l-monoid formulas

# Setup
This might only work for Linux, probably also for OSX, probably not for Windows.
Build and install [Z3](https://github.com/Z3Prover/z3) with the `--python` flag, i.e., execute
```
git clone https://github.com/Z3Prover/z3
cd z3
python scripts/mk_make.py --python
cd build
make
make install
```
and run
```
pip install z3-solver
```
to get Z3 ready.
