""" Tests for 2023 solutions """
import unittest
import os
import aocd
from unittest.mock import patch
from year2023 import day1a
from year2023 import day1b
from year2023 import day2a
from year2023 import day2b
from year2023 import day3a
from year2023 import day3b
from year2023 import day4a
from year2023 import day4b
from year2023 import day5a
from year2023 import day6a
from year2023 import day6b
from year2023 import day7a
from year2023 import day7b
from year2023 import day8a
from year2023 import day8b
from year2023 import day9a
from year2023 import day9b


def get_test_data(day, year):
    """ Function for getting the cached test data """
    if day < 10:
        day = "0" + str(day)
    current_dir = os.path.dirname(__file__)
    testdata_path = os.path.join(current_dir, "testdata", f"{year}_{day}_input.txt")

    with open(testdata_path, encoding="utf-8", mode="r") as file:
        return file.read()

@patch('builtins.print')
class TestSolutions(unittest.TestCase):
    """ Tests for 2023 advent of code solutions """

    def setUp(self):
        patch('aocd.get_data', side_effect=get_test_data).start()

    def test1a(self, mock_print):
        """Tests day 1a"""
        day1a.main()
        mock_print.assert_called_once_with(55621)

    def test1b(self, mock_print):
        """Tests day 1b"""    
        day1b.main()
        mock_print.assert_called_once_with(53592)


    def test2a(self, mock_print):
        """Tests day 2a"""  
        day2a.main()
        mock_print.assert_called_once_with(2727)


    def test2b(self, mock_print):
        """Tests day 2b"""
        day2b.main()
        mock_print.assert_called_once_with(56580)

    def test3a(self, mock_print):
        """Tests day 3a"""
        day3a.main()
        mock_print.assert_called_once_with(536576)

    def test3b(self, mock_print):
        """Tests day 3b"""
        day3b.main()
        mock_print.assert_called_once_with(75741499)

    def test4a(self, mock_print):
        """Tests day 4a"""
        day4a.main()
        mock_print.assert_called_once_with(25571)

    def test4b(self, mock_print):
        """Tests day 4b"""
        day4b.main()
        mock_print.assert_called_once_with(8805731)

    def test5a(self, mock_print):
        """Tests day 5a"""
        day5a.main()
        mock_print.assert_called_once_with(389056265)

    def test6a(self, mock_print):
        """Tests day 6a"""
        day6a.main()
        mock_print.assert_called_once_with(220320)

    def test6b(self, mock_print):
        """Tests day """
        day6b.main()
        mock_print.assert_called_once_with(34454850)

    def test7a(self, mock_print):
        """Tests day 7a"""
        day7a.main()
        mock_print.assert_called_once_with(248113761)

    def test7b(self, mock_print):
        """Tests day 7b"""
        day7b.main()
        mock_print.assert_called_once_with(246285222)

    def test8a(self, mock_print):
        """Tests day 8a"""
        day8a.main()
        mock_print.assert_called_once_with(13207)

    def test8b(self, mock_print):
        """Tests day 8b"""
        day8b.main()
        mock_print.assert_called_once_with(12324145107121)

    def test9a(self, mock_print):
        """Tests day 9a"""
        day9a.main()
        mock_print.assert_called_once_with(2105961943)

    def test9b(self, mock_print):
        """Tests day 9b"""
        day9b.main()
        mock_print.assert_called_once_with(1019)

if __name__ == "__main__":
    unittest.main()
