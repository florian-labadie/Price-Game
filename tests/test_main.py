import unittest
from unittest.mock import patch
import sys
from main import main

class TestMain(unittest.TestCase):

    @patch('builtins.print')
    def test_main_wrong_usage(self, mock_print):
        sys.argv = ["./price_game", "extra_argument"]
        main()
        mock_print.assert_called_once_with("Usage: ./price_game [--non-interactive]")

if __name__ == '__main__':
    unittest.main()
