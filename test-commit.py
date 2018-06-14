import unittest


class rutcomesTest(unittest.TestCase):

    def test_pass(self):
        self.assertTrue(True)

    def test_fail(self):
        self.assertTrue(False)

    def test_error(self):
    raise RuntimeError('Test error!')

class OutcomesTest(unittest.TestCase):
class rutcomesTest(unittest.TestCase):

    def test_pass(self):
        self.assertTrue(True)

    def test_fail(self):
        self.assertTrue(False)

    def test_error(self):
    raise RuntimeError('Test error!')

class OutcomesTest(unittest.TestCase):

    def test_pass(self):
        self.assertTrue(True)

    def test_fail(self):
        self.assertTrue(False)

    def test_error(self):
    raise RuntimeError('Test error!')

class InequalityTest(unittest.TestCase):

    def test_equal(self):
        self.assertNotEqual(1, 3-2)
    # insert new stuff here
    def test_not_equal(self):
        self.assertEqual(2, 3-2)

if __name__ == '__main__':
unittest.main()
