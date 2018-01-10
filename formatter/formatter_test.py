import unittest
import sys
import os
from pathlib import Path
from format_base import Formatter

class Test_formatter_test(unittest.TestCase):
    def test_format(self):
        fb.FormatNames(self)
        file_check = Path("../data/name_db/English_names_formatted.csv")
        if file_check.is_file():
            print('File creation successful')
        else:
            self.fail("File not created. Test failed.")

    #test_format(self)
if __name__ == '__main__':
    try:
        unittest.main()
    except Exception as e:
        print(repr(e))
        os.system("PAUSE")
