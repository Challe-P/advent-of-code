"""Tests for 2024 day three"""

import unittest
from year2024.tests import test_utils
from year2024 import day_three


class DayThreeTests(unittest.TestCase):
    """Tests if the day three solutions work"""

    year: int = 2024
    day: int = 3
    example_answer_a: int = 161
    real_answer_a: int = 187194524
    example_answer_b: int = 48
    real_answer_b: int = 127092535

    def test_three_a_example(self):
        """Tests to see if a is solved correctly with example data"""
        data = test_utils.get_example_data(self.day, self.year)
        day_three_obj = day_three.DayThree(data=data)
        self.assertEqual(
            day_three_obj.solve_a(),
            self.example_answer_a,
            "Solution for A is wrong with example data!",
        )

    @unittest.skip("skips because real data isn't pushed to GitHub")
    def test_three_a_real(self):
        """Solves with real data, that doesn't get pushed. Deactivate when pushing to github"""
        data = test_utils.get_test_data(self.day, self.year)
        day_three_obj = day_three.DayThree(data=data)
        self.assertEqual(
            day_three_obj.solve_a(),
            self.real_answer_a,
            "Solution for A is wrong with real data!",
        )

    def test_three_b_example(self):
        """Tests to see if b is solved correctly with example data"""
        data = test_utils.get_example_data(self.day, self.year)
        day_three_obj = day_three.DayThree(data=data)
        self.assertEqual(
            day_three_obj.solve_b(),
            self.example_answer_b,
            "Solution for B is wrong with example data!",
        )

    @unittest.skip("skips because real data isn't pushed to GitHub")
    def test_three_b_real(self):
        """Solves with real data, that doesn't get pushed. Deactivate when pushing to github"""
        data = test_utils.get_test_data(self.day, self.year)
        day_three_obj = day_three.DayThree(data=data)
        self.assertEqual(
            day_three_obj.solve_b(),
            self.real_answer_b,
            "Solution for B is wrong with real data!",
        )
