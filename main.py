import unittest

class SimpleTestCase(unittest.TestCase):


    def setUp(self):

        """Call before every test case."""
        self.foo = "test"
        #self.file = open("blah", "r")

        print("1. Setup parameters")


    def tearDown(self):

        """Call after every test case."""
        ##self.file.close()
        print("2. Destroy instances")


    def testA(self):
        print("3. Running test")

        assert self.foo == "test"


if __name__ == "__main__":

    unittest.main()  # run all tests