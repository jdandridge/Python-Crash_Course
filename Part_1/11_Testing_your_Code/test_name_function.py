import unittest
from name_function import get_formatted_name as gfn


class NamesTestCase(unittest.TestCase):
    """Tests for 'name_function.py'."""

    def test_first_last_name(self):
        """Do names like 'Jovan Dandridge' work?"""
        formatted_name = gfn('jovan', 'dandridge')
        self.assertEqual(formatted_name, 'Jovan Dandridge')

    def test_first_last_middle_name(self):
        """Do names like 'Jovan Terry Dandridge' work?"""
        formatted_name = gfn('jovan', 'dandridge', 'terry')
        self.assertEqual(formatted_name, 'Jovan Terry Dandridge')


if __name__ == '__main__':
    unittest.main()
