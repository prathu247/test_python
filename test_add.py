import unittest
import re

def add(a):
    try:
        if not a.strip():
            return 0
        if a.startswith('//'):
            match = re.match(r'//(.)\n(.*)', a)
            if match:
                delimiter, a = match.groups()
                delimiter = re.escape(delimiter)
                a = re.sub(delimiter, ',', a) 
        a = a.replace('\n', ',')
        value = a.split(',')
        value_int_list = list(map(int, value))
        negative_numbers = [num for num in value_int_list if num < 0]
        if negative_numbers:
            raise ValueError(f"Negative numbers are not allowed: {negative_numbers}")
        total = sum(value_int_list)
        return total
    except ValueError as e:
        print(e)


class TestAddFunction(unittest.TestCase):
    def test_basic(self):
        self.assertEqual(add("1,2,3,4,5"), 15)

    def test_single_number(self):
        self.assertEqual(add("7"), 7)

    def test_empty_string(self):
        self.assertEqual(add(""), 0)

    def test_negative_numbers(self):
        with self.assertRaises(ValueError) as context:
            add("-1,-2,-3")
        self.assertEqual(str(context.exception), "Negative numbers are not allowed: [-1, -2, -3]")

    def test_new_line_delimiters(self):
        self.assertEqual(add("1\n2,3"), 6)

    def test_custom_delimiter(self):
        self.assertEqual(add("//;\n1;2;3"), 6)


if __name__ == "__main__":
    unittest.main()
