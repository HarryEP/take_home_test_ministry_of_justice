# Take Home Test

## Setup

To install what you will need, run `pip3 install -r requirements.txt`

## The program

There are 3 scripts in the root of this repo/directory:

- test_1.py
- test_2.py
- test_3.py

## Explanation of the scripts

### test_1.py

Test 1 extracts and structures the data from the file `sample.log`. Then it is automatically tested.

To run this, run the command `python3 test_1.py` in your terminal.

### test_2.py

This test gets data from an court data API and matches it with data from the file `people.csv`. It then finds the nearest court for said person with the court type that they've desired.

To run this, run the command `python3 test_2.py` in your terminal.

### test_3.py

This test was a broken function. It now finds the sum of hours/minutes/seconds provided. It also verifies that the input date provided is in the valid format.

To run this, run the command `python3 test_3.py` in your terminal.

### test_test_3.py

This contains unit tests for test_3.py, run this using the command `pytest test_test_3.py` in the terminal.
