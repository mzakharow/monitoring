from PyQt5 import QtWidgets
from PyQt5.QtWidgets import QWidget, QGridLayout
import pyqtgraph as pg
from utils import TimeAxisItem, timestamp


class ExampleWidget(QWidget):
    def __init__(self, parent=None):
        QWidget.__init__(self, parent)
        self.plot = pg.PlotWidget(
            title="Ошибки в ЖР",
            labels={'left': 'Количество'},
            axisItems={'bottom': TimeAxisItem(orientation='bottom')}
        )
        self.plot.setYRange(0, 1000)
        self.plot.setXRange(timestamp(), timestamp() + 100)
        self.plot.showGrid(x=True, y=True)

        self.layout = QGridLayout(self)
        self.layout.addWidget(self.plot, 0, 0)

        self.plotCurve = self.plot.plot(pen='y')

        self.plotData = {'x': [], 'y': []}

    def updatePlot(self, newValue):
        self.plotData['y'].append(newValue)
        self.plotData['x'].append(timestamp())

        self.plotCurve.setData(self.plotData['x'], self.plotData['y'])

app = QtWidgets.QApplication([])
window = ExampleWidget()
window.show()
app.exec_()