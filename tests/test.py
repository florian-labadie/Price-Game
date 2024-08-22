import unittest
from unittest.mock import patch
from src.price_game import price_game

class TestPriceGame(unittest.TestCase):

    @patch('builtins.input', side_effect=[5000, 7500, 8750, 9375, 9687, 9843, 9921, 9960, 9980, 9990, 9995, 9997, 9998, 9999])
    @patch('builtins.print')
    @patch('random.randint', return_value=9999)
    def test_price_game_success(self, mock_randint, mock_print, mock_input):
        price_game()
        self.assertIn(f"Congratulations! You found the secret number in 14 attempts.", [args[0] for args, _ in mock_print.call_args_list])

    @patch('builtins.input', side_effect=[5000, 20000, -10, 9999])
    @patch('builtins.print')
    @patch('random.randint', return_value=9999)
    def test_price_game_invalid_input(self, mock_randint, mock_print, mock_input):
        price_game()
        self.assertIn("Please enter a number between 1 and 10000.", [args[0] for args, _ in mock_print.call_args_list])

    @patch('builtins.input', side_effect=[9999])
    @patch('builtins.print')
    @patch('random.randint', return_value=9999)
    def test_price_game_first_try(self, mock_randint, mock_print, mock_input):
        price_game()
        self.assertIn("Congratulations! You found the secret number in 1 attempts.", [args[0] for args, _ in mock_print.call_args_list])

if __name__ == '__main__':
    unittest.main()
