import app
import unittest


class GetComplimentTest(unittest.TestCase):
    def test_compliment(self):
        self.assertEqual(app.get_compliment(),
                         f'Hello there, user! You are so {app.compliments[0]}!')


if __name__ == '__main__':
    unittest.main()
