import unittest

class SimpleTest(unittest.TestCase):

    def test(self):
        x=7
        if(x>1):
            for i in range(2,x):
                if(x%i == 0):
                    self.assertFalse(False)
            self.assertFalse(True)

if __name__ == '__main__':
    unittest.main()