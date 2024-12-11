import unittest
from logger import Logger

class TestLogger(unittest.TestCase):
    def test_write_metadata(self):
        logger = Logger('test.log')
        logger.write_metadata(100, 0.9, "Ebola", 0.7, 0.25)
        logger.close()

        with open('test.log', 'r') as f:
            lines = f.readlines()
        self.assertIn("Population Size: 100\n", lines)
        self.assertIn("Vaccination Percentage: 0.9\n", lines)
        self.assertIn("Virus Name: Ebola\n", lines)
        self.assertIn("Mortality Rate: 0.7\n", lines)
        self.assertIn("Reproduction Rate: 0.25\n", lines)

if __name__ == '__main__':
    unittest.main()
