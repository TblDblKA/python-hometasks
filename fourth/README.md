# Task 1
Launching (in terminal):

     python -m doctest -o NORMALIZE_WHITESPACE -v encode.py

Results in file: `./results/result1.txt`

# Task 2
Launching (in terminal):

     python -m pytest -v test_decode_pytest.py

Results in file: `./results/result2.txt`

# Task 3
Launching:

    python -m unittest -v test_fit_transform_unit.py

Results: `./results/result3.txt`

# Task 4
Launching:

    python -m pytest -v test_fit_transform_pytest.py

Results: `./results/result4.txt`

# Task 5
Launching:

    python -m unittest -v .\mock_current_year_test.py

Results: `./results/result5.txt`

Coverage test:

    python -m coverage run -m unittest mock_current_year_test.py

    python -m coverage report

    python -m coverage html

Coverage report will locate in `.\htmlcov\what_is_year_now_py.html`. In my repo coverage report allocates in file `coverage_report.html`