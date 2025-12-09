"""Tests for 2025 day 4"""

import unittest
from year2025.tests import test_utils
from year2025 import day_4


class DayTests(unittest.TestCase):
    """Tests if the day 4 solutions work"""

    year: int = 2025
    day: int = 4
    example_answer_a: int = 13
    real_answer_a: int = 1437
    example_answer_b: int = 43
    real_answer_b: int = 8765

    def test__a_example(self):
        """Tests to see if a is solved correctly with example data"""
        data = test_utils.get_example_data(self.day, self.year)
        day__obj = day_4.DayFour(data=data)
        self.assertEqual(
            day__obj.solve_a(),
            self.example_answer_a,
            "Solution for A is wrong with example data!",
        )

    @unittest.skip("skips because real data isn't pushed to GitHub")
    def test__a_real(self):
        """Solves with real data, that doesn't get pushed. Deactivate when pushing to github"""
        data = test_utils.get_test_data(self.day, self.year)
        day__obj = day_4.DayFour(data=data)
        self.assertEqual(
            day__obj.solve_a(),
            self.real_answer_a,
            "Solution for A is wrong with real data!",
        )

    def test__b_example(self):
        """Tests to see if b is solved correctly with example data"""
        data = test_utils.get_example_data(self.day, self.year)
        day__obj = day_4.DayFour(data=data)
        self.assertEqual(
            day__obj.solve_b(),
            self.example_answer_b,
            "Solution for B is wrong with example data!",
        )

    @unittest.skip("skips because real data isn't pushed to GitHub")
    def test__b_real(self):
        """Solves with real data, that doesn't get pushed. Deactivate when pushing to github"""
        data = test_utils.get_test_data(self.day, self.year)
        day__obj = day_4.DayFour(data=data)
        self.assertEqual(
            day__obj.solve_b(),
            self.real_answer_b,
            "Solution for B is wrong with real data!",
        )
