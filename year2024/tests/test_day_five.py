"""Tests for 2024 day five"""

import unittest
from year2024.tests import test_utils
from year2024 import day_five


class DayFiveTests(unittest.TestCase):
    """Tests if the day five solutions work"""

    year: int = 2024
    day: int = 5
    example_answer_a: int = 143
    real_answer_a: int = 5713
    example_answer_b: int = 123
    real_answer_b: int = 5180

    def test_five_a_example(self):
        """Tests to see if a is solved correctly with example data"""
        data = test_utils.get_example_data(self.day, self.year)
        day_five_obj = day_five.DayFive(data=data)
        self.assertEqual(
            day_five_obj.solve_a(),
            self.example_answer_a,
            "Solution for A is wrong with example data!",
        )

    @unittest.skip("skips because real data isn't pushed to GitHub")
    def test_five_a_real(self):
        """Solves with real data, that doesn't get pushed. Deactivate when pushing to github"""
        data = test_utils.get_test_data(self.day, self.year)
        day_five_obj = day_five.DayFive(data=data)
        self.assertEqual(
            day_five_obj.solve_a(),
            self.real_answer_a,
            "Solution for A is wrong with real data!",
        )

    def test_five_b_example(self):
        """Tests to see if b is solved correctly with example data"""
        data = test_utils.get_example_data(self.day, self.year)
        day_five_obj = day_five.DayFive(data=data)
        self.assertEqual(
            day_five_obj.solve_b(),
            self.example_answer_b,
            "Solution for B is wrong with example data!",
        )

    @unittest.skip("skips because real data isn't pushed to GitHub")
    def test_five_b_real(self):
        """Solves with real data, that doesn't get pushed. Deactivate when pushing to github"""
        data = test_utils.get_test_data(self.day, self.year)
        day_five_obj = day_five.DayFive(data=data)
        self.assertLess(day_five_obj.solve_b(), 6173)
        self.assertEqual(
            day_five_obj.solve_b(),
            self.real_answer_b,
            "Solution for B is wrong with real data!",
        )
