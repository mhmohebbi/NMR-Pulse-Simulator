"""
Created on August 19th, 2019
@author: hossein.mohebbi
"""

# Import necessary GUI module
from PyQt4 import QtGui
from UI_Files.ContourPlotUI import Ui_Dialog
import sys
from matplotlib.backends.backend_qt4agg import FigureCanvasQTAgg as FigureCanvas
from matplotlib.backends.backend_qt4agg import NavigationToolbar2QT as NavigationToolbar
from matplotlib.figure import Figure


class Contour(QtGui.QDialog):
    """ Window Class """

    def __init__(self, x, y, z, title, parent=None):
        super(Contour, self).__init__(parent)

        self.ui = Ui_Dialog()
        self.ui.setupUi(self)
        self.x = x
        self.y = y
        self.z = z
        self.title = title

        # a figure instance to plot on
        self.figure = Figure()

        # this is the Canvas Widget that displays the `figure`
        # it takes the `figure` instance as a parameter to __init__
        self.canvas = FigureCanvas(self.figure)

        # this is the Navigation widget
        # it takes the Canvas widget and a parent
        self.toolbar = NavigationToolbar(self.canvas, self)

        # Just some button connected to `plot` method
        self.plot(self.x, self.y, self.z)

        # set the layout
        layout = QtGui.QVBoxLayout()
        layout.addWidget(self.toolbar)
        layout.addWidget(self.canvas)
        self.setLayout(layout)

    def plot(self, x, y, z):
        # create an axis
        ax = self.figure.add_subplot(111)
        # discards the old graph
        ax.clear()
        # plot data
        mpl = ax.contourf(x, y, z, 10)
        ax.set_title(self.title)
        ax.set_xlabel("Frequency Range (MHz)")
        ax.set_ylabel("k Range")
        self.figure.colorbar(mpl)

        # refresh canvas
        self.canvas.draw()


if __name__ == '__main__':
    app = QtGui.QApplication(sys.argv)
    window = Contour()
    window.show()
    sys.exit(app.exec_())