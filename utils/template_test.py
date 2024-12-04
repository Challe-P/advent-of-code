"""Tests for 2024 day xx"""

import unittest
from year2024.tests import test_utils
from year2024 import day_xx


class DayXXTests(unittest.TestCase):
    """Tests if the day xx solutions work"""

    year: int = 2024
    day: int = 0
    example_answer_a: int = 0
    real_answer_a: int = 0
    example_answer_b: int = 0
    real_answer_b: int = 0

    def test_xx_a_example(self):
        """Tests to see if a is solved correctly with example data"""
        data = test_utils.get_example_data(self.day, self.year)
        day_xx_obj = day_xx.DayXX(data=data)
        self.assertEqual(
            day_xx_obj.solve_a(),
            self.example_answer_a,
            "Solution for A is wrong with example data!",
        )

    @unittest.skip("skips because real data isn't pushed to GitHub")
    def test_xx_a_real(self):
        """Solves with real data, that doesn't get pushed. Deactivate when pushing to github"""
        data = test_utils.get_test_data(self.day, self.year)
        day_xx_obj = day_xx.DayXX(data=data)
        self.assertEqual(
            day_xx_obj.solve_a(),
            self.real_answer_a,
            "Solution for A is wrong with real data!",
        )

    def test_xx_b_example(self):
        """Tests to see if b is solved correctly with example data"""
        data = test_utils.get_example_data(self.day, self.year)
        day_xx_obj = day_xx.DayXX(data=data)
        self.assertEqual(
            day_xx_obj.solve_b(),
            self.example_answer_b,
            "Solution for B is wrong with example data!",
        )

    @unittest.skip("skips because real data isn't pushed to GitHub")
    def test_xx_b_real(self):
        """Solves with real data, that doesn't get pushed. Deactivate when pushing to github"""
        data = test_utils.get_test_data(self.day, self.year)
        day_xx_obj = day_xx.DayXX(data=data)
        self.assertEqual(
            day_xx_obj.solve_b(),
            self.real_answer_b,
            "Solution for B is wrong with real data!",
        )
