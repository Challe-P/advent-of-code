"""Helper functions for the tests"""

import os


def get_test_data(day: int, year: int) -> str:
    """Function for getting the cached test data"""
    if day < 10:
        day = "0" + str(day)
    current_dir = os.path.dirname(__file__)
    testdata_path = os.path.join(current_dir, "test_data", f"{year}_{day}_input.txt")

    with open(testdata_path, encoding="utf-8", mode="r") as file:
        return file.read()


def get_example_data(day: int, year: int) -> str:
    """Function for getting the cached test data"""
    if day < 10:
        day = "0" + str(day)
    current_dir = os.path.dirname(__file__)
    testdata_path = os.path.join(current_dir, "example_data", f"{year}_{day}_input.txt")

    with open(testdata_path, encoding="utf-8", mode="r") as file:
        return file.read()
