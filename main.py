import unittest

class SimpleTestCase(unittest.TestCase):


    def setUp(self):

        """Call before every test case."""
        self.foo = "test"
        #self.file = open("blah", "r")


    def tearDown(self):

        """Call after every test case."""
        ##self.file.close()


    def testA(self):
        assert self.foo == "test"


if __name__ == "__main__":

    unittest.main()  # run all tests