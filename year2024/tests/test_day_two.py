""" Tests for 2024 day two """
import unittest
from year2024.tests import test_utils
from year2024 import day_two

class DayTwoTests(unittest.TestCase):
    """ Tests if the day two solutions work """
    year: int = 2024
    day: int = 2
    example_answer_a: int = 2
    real_answer_a: int = 369
    example_answer_b: int = 4
    real_answer_b: int = 428

    def test_two_a_example(self):
        """ Tests to see if a is solved correctly with example data """
        data = test_utils.get_example_data(self.day, self.year)
        day_two_obj = day_two.DayTwo(data = data)
        self.assertEqual(day_two_obj.solve_a(), self.example_answer_a,
                        "Solution for A is wrong with example data!")

    #@unittest.skip("skips because real data isn't pushed to GitHub")
    def test_two_a_real(self):
        """ Solves with real data, that doesn't get pushed. Deactivate when pushing to github """
        data = test_utils.get_test_data(self.day, self.year)
        day_two_obj = day_two.DayTwo(data = data)
        self.assertEqual(day_two_obj.solve_a(), self.real_answer_a,
                        "Solution for A is wrong with real data!")

    def test_two_b_example(self):
        """ Tests to see if b get's solved correctly with example data """
        data = test_utils.get_example_data(self.day, self.year)
        day_two_obj = day_two.DayTwo(data = data)
        self.assertEqual(day_two_obj.solve_b(), self.example_answer_b,
                        "Solution for B is wrong with example data!")

    #@unittest.skip("skips because real data isn't pushed to GitHub")
    def test_two_b_real(self):
        """ Solves with real data, that doesn't get pushed. Deactivate when pushing to github """
        data = test_utils.get_test_data(self.day, self.year)
        day_two_obj = day_two.DayTwo(data = data)
        self.assertEqual(day_two_obj.solve_b(), 428,
                        "Solution for B is wrong with real data!")
