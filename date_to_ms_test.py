import date_to_ms
import os
import unittest

class SimplisticTest(unittest.TestCase):

  def test_str(self):
    """A minimal test to ensure this use case executes successfully."""
    self.assertEqual(0, os.system("python date_to_ms.py -s '01/12/2011'"))

  def test_timestamp(self):
    """A minimal test to ensure this use case executes successfully."""
    self.assertEqual(0, os.system("python date_to_ms.py -ts 1515571200"))

  def test_help(self):
    """A minimal test to ensure this use case executes successfully."""
    self.assertEqual(0, os.system("python date_to_ms.py"))

if __name__ == '__main__':
    unittest.main()