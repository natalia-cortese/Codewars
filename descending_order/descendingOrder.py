"""
Challenge: Your task is to make a function that can take any non-negative integer 
as a argument and return it with it's digits in descending order. 
Essentially, rearrange the digits to create the highest possible number.
"""
import unittest

def descending_order(num):
	reversedNum=''.join(sorted(str(num), reverse=True))
	return int(reversedNum)

class TestingDescendingOrder(unittest.TestCase):

    def test_all_numbers_equals(self):
        value = 11111111
        expected_value = 11111111

        solution = descending_order(value)

        assert expected_value == solution
        
    def test_reverse_sort_num(self):
        self.assertEqual(descending_order(12345), 54321)
        self.assertEqual(descending_order(987612), 987621)
        self.assertEqual(descending_order(54321), 54321)  # Test con número ya ordenado en reversa
        self.assertEqual(descending_order(0), 0)          # Test con 0
        self.assertEqual(descending_order(1), 1)          # Test con 1
        self.assertEqual(descending_order(10), 10)    
        