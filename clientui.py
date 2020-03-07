# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'client.ui'
#
# Created by: PyQt5 UI code generator 5.14.1
#
# WARNING! All changes made in this file will be lost!


from PyQt5 import QtCore, QtGui, QtWidgets, Qt
from pyqtgraph import PlotWidget
import time
import datetime
# from utils import TimeAxisItem
from handler import TimeAxisItem


def timestamp():
    return int(time.mktime(datetime.datetime.now().timetuple()))


class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(802, 507)
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.layout = Qt.QHBoxLayout(self)
        # self.layout = QGridLayout(self)

        self.errorWidget = PlotWidget(self.centralwidget, axisItems={'bottom': TimeAxisItem(orientation='bottom')})
        # self.errorWidget = PlotWidget(
        #     self.centralwidget,
        #     title="Ошибки в ЖР",
        #     labels={'left': 'Количество'},
        #     axisItems={'bottom': TimeAxisItem(orientation='bottom')}
        # )
        self.errorWidget.setGeometry(QtCore.QRect(0, 0, 801, 301))
        self.errorWidget.setObjectName("errorWidget")
        self.layout.addWidget(self.errorWidget)
        # self.errorWidget.setYRange(0, 5000)
        # self.errorWidget.setXRange(timestamp(), timestamp() + 100)
        # self.errorWidget.showGrid(x=True, y=True)

        self.queueWidget = PlotWidget(self.centralwidget)
        self.queueWidget.setGeometry(QtCore.QRect(0, 330, 801, 151))
        self.queueWidget.setObjectName("queueWidget")
        MainWindow.setCentralWidget(self.centralwidget)
        self.statusbar = QtWidgets.QStatusBar(MainWindow)
        self.statusbar.setObjectName("statusbar")
        MainWindow.setStatusBar(self.statusbar)

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "MainWindow"))
