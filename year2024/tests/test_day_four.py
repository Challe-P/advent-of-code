"""Tests for 2024 day four"""

import unittest
from year2024.tests import test_utils
from year2024 import day_four


class DayTests(unittest.TestCase):
    """Tests if the day four solutions work"""

    year: int = 2024
    day: int = 4
    example_answer_a: int = 18
    real_answer_a: int = 2662
    example_answer_b: int = 9
    real_answer_b: int = 2034

    def test_four_a_example(self):
        """Tests to see if a is solved correctly with example data"""
        data = test_utils.get_example_data(self.day, self.year)
        day_four_obj = day_four.DayFour(data=data)
        self.assertEqual(
            day_four_obj.solve_a(),
            self.example_answer_a,
            "Solution for A is wrong with example data!",
        )

    @unittest.skip("skips because real data isn't pushed to GitHub")
    def test_four_a_real(self):
        """Solves with real data, that doesn't get pushed. Deactivate when pushing to github"""
        data = test_utils.get_test_data(self.day, self.year)
        day_four_obj = day_four.DayFour(data=data)
        self.assertEqual(
            day_four_obj.solve_a(),
            self.real_answer_a,
            "Solution for A is wrong with real data!",
        )

    def test_four_b_example(self):
        """Tests to see if b is solved correctly with example data"""
        data = test_utils.get_example_data(self.day, self.year)
        day_four_obj = day_four.DayFour(data=data)
        self.assertEqual(
            day_four_obj.solve_b(),
            self.example_answer_b,
            "Solution for B is wrong with example data!",
        )

    @unittest.skip("skips because real data isn't pushed to GitHub")
    def test_four_b_real(self):
        """Solves with real data, that doesn't get pushed. Deactivate when pushing to github"""
        data = test_utils.get_test_data(self.day, self.year)
        day_four_obj = day_four.DayFour(data=data)
        self.assertEqual(
            day_four_obj.solve_b(),
            self.real_answer_b,
            "Solution for B is wrong with real data!",
        )
