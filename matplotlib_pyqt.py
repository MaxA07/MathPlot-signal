from PyQt5.QtWidgets import QWidget, QApplication, QVBoxLayout
import sys
from PyQt5 import QtCore, QtWidgets
import qt_widget
from matplotlib.backends.backend_qt5agg import FigureCanvasQTAgg, NavigationToolbar2QT
from matplotlib.figure import Figure
import numpy as np


class MatplotlibWidget(QWidget):
    def __init__(self, parent=None):
        super(MatplotlibWidget, self).__init__(parent)
        self.figure = Figure()
        self.canvas = FigureCanvasQTAgg(self.figure)
        self.axis = self.figure.add_subplot(111)
        self.toolbar = NavigationToolbar2QT(self.canvas, self)
        self.layoutvertical = QVBoxLayout(self)
        self.layoutvertical.addWidget(self.canvas)
        self.layoutvertical.addWidget(self.toolbar)


class MainWidget(QWidget, qt_widget.Ui_Form):

    def __init__(self):
        super(MainWidget, self).__init__()

        self.setWindowFlag((QtCore.Qt.FramelessWindowHint))
        self.setAttribute(QtCore.Qt.WA_TranslucentBackground)
        self.center()

        self.setupUi(self)
        self.init_widget()
        self.pushButton.clicked.connect(self.plot_widget)
        self.pushButton_2.clicked.connect(self.clear_form)
        self.pushButton_3.clicked.connect(self.close_window)

    def center(self):
        qr = self.frameGeometry()
        cp = QtWidgets.QDesktopWidget().availableGeometry().center()
        qr.moveCenter(cp)
        self.move(qr.topLeft())

    def mousePressEvent(self, event):
        self.oldPos = event.globalPos()

    def mouseMoveEvent(self, event):
        try:
            delta = QtCore.QPoint(event.globalPos() - self.oldPos)
            self.move(self.x() + delta.x(), self.y() + delta.y())
            self.oldPos = event.globalPos()
        except AttributeError:
            pass

    def init_widget(self):
        self.matplotlibwidget = MatplotlibWidget()
        self.layoutvertical = QVBoxLayout(self.widget)
        self.layoutvertical.addWidget(self.matplotlibwidget)

    def plot_widget(self):
        frequency = 5;
        self.matplotlibwidget.axis.clear()
        t = np.arange(0, 3, 0.01)
        y = np.sin(2*np.pi*frequency*t)
        self.matplotlibwidget.axis.plot(t, y)
        self.matplotlibwidget.canvas.draw()

    def clear_form(self):
        self.matplotlibwidget.axis.clear()
        self.matplotlibwidget.canvas.draw()

    def close_window(self):
        self.close()


if __name__ == "__main__":
    app = QApplication(sys.argv)
    w = MainWidget()
    w.show()
    sys.exit(app.exec())
