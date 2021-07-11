import numpy as np
from PyQt5.QtWidgets import QMainWindow, QApplication
from PyQt5 import uic
from PyQt5.QtCore import QSize
from PyQt5.QtGui import QIcon
import torch

# This import statement is necessary for the app to work well with the resources

import res_rc


def NormalizeData01(data, min_, max_):
    """
    Normalize value from 0 to 1
    :param data: Value to normalize
    :param min_: Minimum value in the series
    :param max_: Maximum value in the series
    :return: Normalized value
    """
    return (data - min_) / (max_ - min_)


class MainWindow(QMainWindow):

    # MAIN WINDOW CONFIGURATION

    def __init__(self):
        QMainWindow.__init__(self)
        uic.loadUi("screen.ui", self)
        self.setWindowTitle('Home')
        self.about.setVisible(False)
        self.valid.setVisible(False)
        self.about_line.setVisible(False)
        self.result.setVisible(False)
        self.prediction.setVisible(False)
        self.model = torch.load('clothing_size.pth')
        self.device = torch.device('cuda' if torch.cuda.is_available() else 'cpu')
        self.predictor_button.clicked.connect(self._openpredictor)
        self.about_button.clicked.connect(self._openabout)
        self.predict_bt.clicked.connect(self._getsize)

    def _openpredictor(self):
        """
        Sets "predict" screen visible and hides "about" screen.
        """
        self.predictor.setVisible(True)
        self.about.setVisible(False)
        self.about_line.setVisible(False)
        self.predictor_line.setVisible(True)

    def _openabout(self):
        """
        Hides "predict" screen and shows "about" screen.
        """
        self.predictor.setVisible(False)
        self.about.setVisible(True)
        self.about_line.setVisible(True)
        self.predictor_line.setVisible(False)

    def _getsize(self):
        """
        Gets values from the number placeholders, normalizes de values, input the normalized the values to the model
        and shows up the results of the model in a label.
        """
        if self.weight_value.value() != 0 and self.height_value.value() != 0:
            values = np.array(
                [NormalizeData01(self.weight_value.value(), 22, 136), NormalizeData01(self.age_value.value(), 0, 117),
                 NormalizeData01(self.height_value.value(), 137.16, 193.04)], dtype='float64')
            self.model.to(self.device)
            self.model.eval()
            outputs = self.model(torch.from_numpy(values).float().to(self.device))
            size = torch.argmax(outputs).item()
            if size == 0:
                self.prediction.setText('Extra Small')
            elif size == 1:
                self.prediction.setText('Small')
            elif size == 2:
                self.prediction.setText('Medium')
            elif size == 3:
                self.prediction.setText('Large')
            elif size == 4:
                self.prediction.setText('Extra Large')
            elif size == 5:
                self.prediction.setText('Extra Extra Large')
            elif size == 6:
                self.prediction.setText('Extra Extra Extra Large')
            self.result.setVisible(True)
            self.prediction.setVisible(True)
            self.valid.setVisible(False)
        else:
            self.valid.setVisible(True)


if __name__ == '__main__':
    app = QApplication([])
    app_icon = QIcon()
    app_icon.addFile('res/logo.png', QSize(300, 300))
    app.setWindowIcon(app_icon)
    window = MainWindow()
    window.show()
    app.exec_()
