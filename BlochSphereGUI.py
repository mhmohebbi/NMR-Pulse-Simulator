"""
Created on August 23rd, 2019
@author: hossein.mohebbi
"""

# Import necessary GUI module
from PyQt4 import QtGui
from UI_Files.BlochSphereUI import Ui_Dialog
from PyQt4.QtGui import *
from mpl_toolkits.mplot3d import Axes3D
from matplotlib.figure import Figure
import numpy as np
import matplotlib.pyplot as plt
from matplotlib.backends.backend_qt4agg import FigureCanvasQTAgg as FigureCanvas
from matplotlib.backends.backend_qt4agg import NavigationToolbar2QT as NavigationToolbar
import sys


class ThreeDSurface_GraphWindow(FigureCanvas): #Class for 3D window
    def __init__(self):
        self.fig =plt.figure()
        FigureCanvas.__init__(self, self.fig) #creating FigureCanvas
        self.axes = self.fig.gca(projection='3d')#generates 3D Axes object
        # self.axes.hold(False)#clear axes on each run

        self.axes.set_aspect("equal")


class Bloch(QtGui.QDialog):
    """ Window Class """

    def __init__(self, parent=None):
        #QtGui.QDialog.__init__(self)
        super(Bloch, self).__init__(parent)
        self.ui = Ui_Dialog()
        self.ui.setupUi(self)

        self.ThreeDWin = ThreeDSurface_GraphWindow()#creating 3D Window
        self.ui.verticalLayout.addWidget(self.ThreeDWin)

        # this is the Navigation widget
        # it takes the Canvas widget and a parent
        self.toolbar = NavigationToolbar(self.ThreeDWin, self)
        self.ui.gridLayout_2.addWidget(self.toolbar)

        u, v = np.mgrid[0:2 * np.pi:100j, 0:np.pi:100j]
        x = np.cos(u) * np.sin(v)
        y = np.sin(u) * np.sin(v)
        z = np.cos(v)
        self.ThreeDWin.axes.plot_wireframe(x, y, z, alpha=0.1, color="#CD853F")

        self.x = []
        self.y = []
        self.z = []

        self.ThreeDWin.axes.set_xlabel('<Sx>(t)')
        self.ThreeDWin.axes.set_ylabel('<Sy>(t)')
        self.ThreeDWin.axes.set_zlabel('<Sz>(t)')

    def points(self, theta, phi):
        self.x.append(np.cos(phi) * np.sin(theta))
        self.y.append(np.sin(phi) * np.sin(theta))
        self.z.append(np.cos(theta))
        return

    def plot(self, x, y, z):
        length = len(x)
        #for i in range(length):
        #    self.ThreeDWin.axes.scatter(x[i], y[i], z[i], color="r", c="r", s=2)

        self.ThreeDWin.axes.scatter(x[0], y[0], z[0], color="g", c="g", s=100)
        self.ThreeDWin.axes.plot(x, y, z, 'bo', markersize=2)
        self.ThreeDWin.axes.scatter(x[length-1], y[length-1], z[length-1], color="r", c="r", s=100)


if __name__ == '__main__':
    app = QtGui.QApplication(sys.argv)
    window = Bloch()
    window.show()
    sys.exit(app.exec_())