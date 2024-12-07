"""Tests for 2024 day seven"""

import unittest
from year2024.tests import test_utils
from year2024 import day_seven


class DaySevenTests(unittest.TestCase):
    """Tests if the day seven solutions work"""

    year: int = 2024
    day: int = 7
    example_answer_a: int = 3749
    real_answer_a: int = 1038838357795
    example_answer_b: int = 11387
    real_answer_b: int = 254136560217241

    def test_seven_a_example(self):
        """Tests to see if a is solved correctly with example data"""
        data = test_utils.get_example_data(self.day, self.year)
        day_seven_obj = day_seven.DaySeven(data=data)
        self.assertEqual(
            day_seven_obj.solve_a(),
            self.example_answer_a,
            "Solution for A is wrong with example data!",
        )

    @unittest.skip("skips because real data isn't pushed to GitHub")
    def test_seven_a_real(self):
        """Solves with real data, that doesn't get pushed. Deactivate when pushing to github"""
        data = test_utils.get_test_data(self.day, self.year)
        day_seven_obj = day_seven.DaySeven(data=data)
        self.assertGreater(day_seven_obj.solve_a(), 1038838357435)
        self.assertEqual(
            day_seven_obj.solve_a(),
            self.real_answer_a,
            "Solution for A is wrong with real data!",
        )

    def test_seven_b_example(self):
        """Tests to see if b is solved correctly with example data"""
        data = test_utils.get_example_data(self.day, self.year)
        day_seven_obj = day_seven.DaySeven(data=data)
        self.assertEqual(
            day_seven_obj.solve_b(),
            self.example_answer_b,
            "Solution for B is wrong with example data!",
        )

    @unittest.skip("skips because real data isn't pushed to GitHub")
    def test_seven_b_real(self):
        """Solves with real data, that doesn't get pushed. Deactivate when pushing to github"""
        data = test_utils.get_test_data(self.day, self.year)
        day_seven_obj = day_seven.DaySeven(data=data)
        self.assertEqual(
            day_seven_obj.solve_b(),
            self.real_answer_b,
            "Solution for B is wrong with real data!",
        )
