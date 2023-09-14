import os
import unittest
from utils.zip_folder import zip_folder


class TestUtilities(unittest.TestCase):
    def test_zip(self):
        input_file = "taco"
        zip_folder("taco", "bell")

    def tearDown(self) -> None:
        os.remove("bell.zip")


if __name__ == '__main__':
    unittest.main()
