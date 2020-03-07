from PyQt5 import QtWidgets, QtCore, QtGui
import client
import pyqtgraph as pg
import handler
from datetime import datetime
from random import randint


class MessengerWindow(QtWidgets.QMainWindow, client.Ui_MainWindow):
    def __init__(self):
        super().__init__()
        self.setupUi(self)

    # graph ->


        # self.x = list(range(100))  # 100 time points
        # self.y = [randint(0, 100) for _ in range(100)]  # 100 data points
        self.y, self.x = handler.read_file()
        # self.errorWidget.setBackground('w')

        color = self.palette().color(QtGui.QPalette.Window)
        # color = (255, 0, 0)
        pen = pg.mkPen(color=color)
        self.data_line = self.errorWidget.plot(self.x, self.y, pen=pen)

        # update graph
        self.timer = QtCore.QTimer()
        self.timer.setInterval(1000)
        self.timer.timeout.connect(self.update_plot_data)
        self.timer.start()

    def update_plot_data(self):
        pass
        # self.x = self.x[1:]  # Remove the first y element.
        # self.x.append(self.x[-1] + 1)  # Add a new value 1 higher than the last.
        #
        # self.y = self.y[1:]  # Remove the first
        # self.y.append(randint(0, 100))  # Add a new random value.
        #
        # self.data_line.setData(self.x, self.y)  # Update the data.
    # <- graph


app = QtWidgets.QApplication([])
window = MessengerWindow()
window.show()
app.exec_()