from unittest import TestCase
from spreadsheet import SpreadSheet


class TestSpreadSheet(TestCase):

    def test_evaluate_valid_integer(self):
        spreadsheet = SpreadSheet()
        spreadsheet.set("A1", "1")
        self.assertEqual(1, spreadsheet.evaluate("A1"))

    def test_evaluate_non_valid_integer(self):
        spreadsheet = SpreadSheet()
        spreadsheet.set("A1", "1.5")
        self.assertEqual("#Error", spreadsheet.evaluate("A1"))

    def test_evaluate_valid_string(self):
        spreadsheet = SpreadSheet()
        spreadsheet.set("A1", "'Apple'")
        self.assertEqual("Apple", spreadsheet.evaluate("A1"))

    def test_evaluate_non_valid_string(self):
        spreadsheet = SpreadSheet()
        spreadsheet.set("A1", "'Apple")
        self.assertEqual("#Error", spreadsheet.evaluate("A1"))

    def test_evaluate_simple_formula_valid_string(self):
        spreadsheet = SpreadSheet()
        spreadsheet.set("A1", "='Apple'")
        self.assertEqual("Apple", spreadsheet.evaluate("A1"))

    def test_evaluate_simple_formula_valid_integer(self):
        spreadsheet = SpreadSheet()
        spreadsheet.set("A1", "=1")
        self.assertEqual("1", spreadsheet.evaluate("A1"))

    def test_evaluate_simple_formula_non_valid_string(self):
        spreadsheet = SpreadSheet()
        spreadsheet.set("A1", "='Apple")
        self.assertEqual("#Error", spreadsheet.evaluate("A1"))

    def test_evaluate_simple_formula_non_valid_integer(self):
        spreadsheet = SpreadSheet()
        spreadsheet.set("A1", "=1.5")
        self.assertEqual("#Error", spreadsheet.evaluate("A1"))

    def test_formula_reference_valid_integer(self):
        spreadsheet = SpreadSheet()
        spreadsheet.set("B1", "42")
        spreadsheet.set("A1", "=B1")
        self.assertEqual("42", spreadsheet.evaluate("A1"))

    def test_formula_reference_non_valid_integer(self):
        spreadsheet = SpreadSheet()
        spreadsheet.set("B1", "42.5")
        spreadsheet.set("A1", "=B1")
        self.assertEqual("#Error", spreadsheet.evaluate("A1"))

    def test_formula_reference_circular_loop(self):
        spreadsheet = SpreadSheet()
        spreadsheet.set("B1", "=A1")
        spreadsheet.set("A1", "=B1")
        self.assertEqual("#Circular", spreadsheet.evaluate("A1"))

    def test_simple_addition(self):
        spreadsheet = SpreadSheet()
        spreadsheet.set("A1", "=1+3")
        self.assertEqual("4", spreadsheet.evaluate("A1"))

    def test_simple_incorrect_addition(self):
        spreadsheet = SpreadSheet()
        spreadsheet.set("A1", "=1+3.5")
        self.assertEqual("#Error", spreadsheet.evaluate("A1"))

    def test_division_by_zero(self):
        spreadsheet = SpreadSheet()
        spreadsheet.set("A1", "=1/0")
        self.assertEqual("#Error", spreadsheet.evaluate("A1"))