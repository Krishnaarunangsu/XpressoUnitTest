import unittest

class TestStringMethods(unittest.TestCase):

    def test_upper(self):
        """
        Test Upper Case

        Args:
            self

        Returns:
        """
        self.assertEqual('foo'.upper(), 'FOO')

    def test_isupper(self):
        """
        Test Upper Case

        Args:
            self

        Returns:
        """
        self.assertTrue('FOO'.isupper())
        self.assertFalse('Foo'.isupper())

    def test_split(self):
        """
        Test Upper Case

        Args:
            self

        Returns:
        """
        s = 'hello world'
        self.assertEqual(s.split(), ['hello', 'world'])
        # check that s.split fails when the separator is not a string
        with self.assertRaises(TypeError):
            s.split(2)

if __name__ == '__main__':
    unittest.main()
