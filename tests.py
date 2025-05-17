import unittest
from unittest.mock import patch, MagicMock
import numpy as np
from l_squares import find_least_sqrt
import calculator
import pandas as pd


class TestLeastSquaresFit(unittest.TestCase):
    def test_perfect_line(self):
        # Дані лежать точно на прямій y = 2x + 1
        x = np.array([0, 1, 2, 3, 4])
        y = 2 * x + 1
        a, b = find_least_sqrt(x, y)
        self.assertAlmostEqual(a, 2.0, places=4)
        self.assertAlmostEqual(b, 1.0, places=4)

    def test_least_sqrt(self):
        # y = 4
        x = np.array([0, 1, 2, 3])
        y = 4 * x
        a, b = find_least_sqrt(x, y)
        self.assertAlmostEqual(a, 4.0, places=4)
        self.assertAlmostEqual(b, 0.0, places=4)


class TestOpenFile(unittest.TestCase):

    @patch("calculator.askopenfilename", return_value="test_table.csv")
    @patch("calculator.pd.read_csv")
    @patch("calculator.label")
    @patch("calculator.x_data_label")
    @patch("calculator.y_data_label")
    def test_open_file_success(self, mock_y_label, mock_x_label, mock_label, mock_read_csv, mock_askopen):
        # Мокануємо DataFrame, як його повинен повертати pandas.read_csv
        mock_read_csv.return_value = pd.DataFrame({
            "x": [1, 2, 3],
            "y": [2, 4, 6]
        })

        calculator.open_file()

        # Перевіряємо, що label оновив текст (файл завантажено)
        mock_label.config.assert_called()
        text_arg = mock_label.config.call_args[1]["text"]
        self.assertIn("файл завантажено", text_arg)

        # Перевіряємо, що x_data_label і y_data_label теж оновились
        mock_x_label.config.assert_called()
        mock_y_label.config.assert_called()


if __name__ == "__main__":
    unittest.main()



