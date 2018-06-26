# Solutions to Cracking the Coding Interview, 5th edition (Python 3)
(being updated with new solutions daily)

## Repo structure and naming
`src/`: the source modules grouped under one package.

`tests/`: unit test files.

Each source module is the solution to one question from the book. Source module names follow a `qxxyy.py` pattern where `xx` is the chapter number and `yy` is the question number. For instance, `q0102.py` refers to chapter 1, question 2.

Each source module has its own test file. Test files follow Python test discovery convention: a `test_` prefix is added to source module name. For example, `test_q0101.py` is the test file for `q0101.py`.

## How to import source modules
Source modules are grouped under a package called `src` and can be imported from a parent directory as:

`from src import q0101`

or

`import src.q0101`

## How to run the unit tests
To run all tests, simply use Python test dicovery (from root of the repo):

`python -m unittest`

For a specific test file such as `test_q0101.py`, run (from root of the repo):

`python -m unittest tests/test_q0101.py`

