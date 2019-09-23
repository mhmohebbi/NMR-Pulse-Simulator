"""
Created on August 2nd, 2019
@author: hossein.mohebbi
"""

# Import necessary modules
from PyQt4 import QtGui, QtCore
from UI_Files.MainWindowUI import Ui_MainWindow
from PyQt4.QtGui import QMessageBox
from CSV.csv_reading import read_csv
from Tasks.expectation_vals import ExpectVal
from Tasks.block_sphere_plotting import SphereVal
from Tasks.contour_plotting_vals import ContourPlotExpectVal
from Tasks.pulse_plotting import Pulse
import ContourPlotGUI
import ComparisonGUI
import BlochSphereGUI
import numpy as np
from collections import OrderedDict
import sys


class FRangeNotAccepted(Exception):
   """Raised when f range goes from high to low or has the same value"""
   pass


class KRangeNotAccepted(Exception):
   """Raised when k range goes from high to low or has the same value"""
   pass


class FRangeNotAllowed(Exception):
   """Raised when f range given instead of one value"""
   pass


class KRangeNotAllowed(Exception):
   """Raised when k range given instead of one value"""
   pass


class Main(QtGui.QMainWindow):
    """ Window Class """

    def __init__(self):
        QtGui.QMainWindow.__init__(self)
        self.ui = Ui_MainWindow()
        self.ui.setupUi(self)

        # configuring styles
        self.labelStyle = {'color': '#000000', 'font-size': '9pt'}
        color = 'w'

        # configuring graphs
        pg.setConfigOptions(antialias=True)
        self.pulse_plot_1 = pg.PlotWidget()
        self.pulse_plot_1.setMouseEnabled(x=True, y=False)
        self.pulse_plot_1.showGrid(x=True, y=True)
        self.pulse_plot_1.setLimits(xMin=0) # , yMin=0)

        self.pulse_plot_2 = pg.PlotWidget()
        self.pulse_plot_2.setMouseEnabled(x=True, y=False)
        self.pulse_plot_2.showGrid(x=True, y=True)
        self.pulse_plot_2.setLimits(xMin=0) # , yMin=0)

        self.expectations_plot = pg.PlotWidget()
        self.expectations_plot.setMouseEnabled(x=True, y=True)
        self.expectations_plot.showGrid(x=True, y=True)

        # Default Graph Appearance
        self.pulse_plot_1.setBackground(color)
        self.pulse_plot_1.setLabel('left', "Amp.", **self.labelStyle)
        self.pulse_plot_1.setLabel('bottom', "Time (ns)", **self.labelStyle)
        self.ui.gridLayout_3.addWidget(self.pulse_plot_1)

        self.pulse_plot_2.setBackground(color)
        self.pulse_plot_2.setLabel('left', "Phase (deg)", **self.labelStyle)
        self.pulse_plot_2.setLabel('bottom', "Time (ns)", **self.labelStyle)
        self.ui.gridLayout_7.addWidget(self.pulse_plot_2)

        self.expectations_plot.setBackground(color)
        self.expectations_plot.setLabel('left', "Exp.", **self.labelStyle)
        self.expectations_plot.setLabel('bottom', "Frequency (MHz)", **self.labelStyle)
        self.ui.verticalLayout.addWidget(self.expectations_plot)

        # Button clicks
        self.ui.pushButton_expects.clicked.connect(self.expects)
        self.ui.pushButton_pulse.clicked.connect(self.pulse)
        self.ui.open_pushButton.clicked.connect(self.open_file)
        self.ui.pushButton_compare.clicked.connect(self.compare)
        self.ui.pushButton_sphere.clicked.connect(self.bloch_sphere)

        # Default Attributes
        self.compare_dic = OrderedDict()
        self.original_dic = OrderedDict()

    # function to view bloch sphere window
    def bloch_sphere(self):
        # opens new dialog
        data = read_csv(self.ui.file_lineEdit.text())
        k = self.ui.low_range_doubleSpinBox_k.value()
        w = self.ui.low_range_doubleSpinBox.value()
        w1 = self.ui.rabi_freq_doubleSpinBox.value()
        try:
            if k != self.ui.high_range_doubleSpinBox_k.value():
                raise KRangeNotAllowed
            if w != self.ui.high_range_doubleSpinBox.value():
                raise FRangeNotAllowed

            sphere_plot = SphereVal(k, w, w1, data)
            vector_paths = sphere_plot.sigmas()
            x = vector_paths[0]
            y = vector_paths[1]
            z = vector_paths[2]
            window = BlochSphereGUI.Bloch(self)
            window.show()
            window.plot(x, y, z)

        except IOError:
            msg = QMessageBox()
            msg.setIcon(QMessageBox.Warning)
            msg.setText("CSV shaped pulse file not found.")
            msg.setInformativeText("Please recheck directory for file.")
            msg.setWindowTitle("Input Error")
            msg.setStandardButtons(QMessageBox.Ok)
            msg.exec_()
        except ValueError:
            msg = QMessageBox()
            msg.setIcon(QMessageBox.Warning)
            msg.setText("Error inside the CSV file.")
            msg.setInformativeText("Please ensure the pulses have been entered in correct formatting. "
                                   "(time, amp, phase)")
            msg.setWindowTitle("CSV Error")
            msg.setStandardButtons(QMessageBox.Ok)
            msg.exec_()
        except FRangeNotAllowed:
            msg = QMessageBox()
            msg.setIcon(QMessageBox.Warning)
            msg.setText("Given a range for value of f.")
            msg.setInformativeText("Ensure lower and higher value are the same.")
            msg.setWindowTitle("Input Error")
            msg.setStandardButtons(QMessageBox.Ok)
            msg.exec_()
        except KRangeNotAllowed:
            msg = QMessageBox()
            msg.setIcon(QMessageBox.Warning)
            msg.setText("Given a range for value of k.")
            msg.setInformativeText("Ensure lower and higher value are the same.")
            msg.setWindowTitle("Input Error")
            msg.setStandardButtons(QMessageBox.Ok)
            msg.exec_()
        except IndexError:
            pass

    # function to add compare pulse files
    def compare(self):
        default_file = str(self.ui.file_lineEdit.text())
        if default_file in self.compare_dic.values():
            for style in self.compare_dic:
                if self.compare_dic[style] == default_file and style != 'solid':
                    del self.compare_dic[style]

        self.compare_dic['solid'] = default_file

        self.original_dic = self.compare_dic.copy()

        # opens new dialog // mutates, pass by reference
        window = ComparisonGUI.Compare(self.compare_dic, self)
        window.show()
        while window.running:
            QtGui.qApp.processEvents()
        if window.original is True:
            self.compare_dic = self.original_dic.copy()

        if len(self.compare_dic) > 1:
            self.ui.radioButton_contour.setEnabled(False)
        else:
            self.ui.radioButton_contour.setEnabled(True)

    # function to find file directory
    def open_file(self):
        self.filename = QtGui.QFileDialog.getOpenFileName(self, 'Open File', '.','(*.CSV)')
        self.ui.file_lineEdit.setText(str(self.filename))

    # function to plot pulse
    def pulse(self):
        self.pulse_plot_1.clear()
        self.pulse_plot_2.clear()

        try:
            data = read_csv(self.ui.file_lineEdit.text())
            # first value = time, second value = amplitudes. third = phase, fourth = x comp, fifth = y comp
            pulse = Pulse(data).get_pulse_arrays()
            if self.ui.radioButton_polar.isChecked():
                self.ui.pulse_1_plot_tabWidget.setTabText(0, 'X Component')
                self.ui.pulse_2_plot_tabWidget.setTabText(0, 'Y Component')
                self.pulse_plot_1.setLabel('left', "X Comp", **self.labelStyle)
                self.pulse_plot_2.setLabel('left', "Y Comp", **self.labelStyle)
                self.pulse_plot_1.plot(pulse[0], pulse[3], pen='k', name='pulse1')
                self.pulse_plot_2.plot(pulse[0], pulse[4], pen='k', name='pulse2')
            else:
                self.ui.pulse_1_plot_tabWidget.setTabText(0, 'Amplitude vs. Time')
                self.ui.pulse_2_plot_tabWidget.setTabText(0, 'Phase vs. Time')
                self.pulse_plot_1.setLabel('left', "Amp.", **self.labelStyle)
                self.pulse_plot_2.setLabel('left', "Phase (deg)", **self.labelStyle)
                self.pulse_plot_1.plot(pulse[0], pulse[1], pen='k', name='pulse1')
                self.pulse_plot_2.plot(pulse[0], pulse[2], pen='k', name='pulse2')

        except IOError:
            msg = QMessageBox()
            msg.setIcon(QMessageBox.Warning)
            msg.setText("CSV shaped pulse file not found.")
            msg.setInformativeText("Please recheck directory for file.")
            msg.setWindowTitle("Input Error")
            msg.setStandardButtons(QMessageBox.Ok)
            msg.exec_()
        except ValueError:
            msg = QMessageBox()
            msg.setIcon(QMessageBox.Warning)
            msg.setText("Error inside the CSV file.")
            msg.setInformativeText("Please ensure the pulses have been entered in correct formatting. "
                                   "(time, amp, phase)")
            msg.setWindowTitle("CSV Error")
            msg.setStandardButtons(QMessageBox.Ok)
            msg.exec_()

    def expects(self):
        self.expectations_plot.clear()

        high_w = self.ui.high_range_doubleSpinBox.value()
        low_w = self.ui.low_range_doubleSpinBox.value()

        high_k = self.ui.high_range_doubleSpinBox_k.value()
        low_k = self.ui.low_range_doubleSpinBox_k.value()

        w1 = self.ui.rabi_freq_doubleSpinBox.value()
        w_step = self.ui.step_doubleSpinBox.value()
        k_step = self.ui.k_step_doubleSpinBox.value()

        try:
            if low_w > high_w:
                raise FRangeNotAccepted

            if low_k > high_k:
                raise KRangeNotAccepted

        except KRangeNotAccepted:
            msg = QMessageBox()
            msg.setIcon(QMessageBox.Warning)
            msg.setText("K Range must go from low to high.")
            msg.setInformativeText("Please recheck values.")
            msg.setWindowTitle("Input Error")
            msg.setStandardButtons(QMessageBox.Ok)
            msg.exec_()

        except FRangeNotAccepted:
            msg = QMessageBox()
            msg.setIcon(QMessageBox.Warning)
            msg.setText("Frequency Range must go from low to high.")
            msg.setInformativeText("Please recheck values.")
            msg.setWindowTitle("Input Error")
            msg.setStandardButtons(QMessageBox.Ok)
            msg.exec_()

        # ensures always at least one file in dic
        default_file = str(self.ui.file_lineEdit.text())
        self.compare_dic['solid'] = default_file

        for style in self.compare_dic:
            # error checking
            try:
                data = read_csv(self.compare_dic[style])
                expect_val = ExpectVal((low_k, high_k), k_step, (low_w, high_w), w_step, w1, data)
                w_range = expect_val.w_range
                # for scaling purposes
                w_range_for_graph = [i * (10 ** (-6)) for i in expect_val.w_range]
                w_expect_vals = expect_val.sigma_w()
                k_range = expect_val.k_range
                k_expect_vals = expect_val.sigma_k()
                self.ui.pushButton_compare.setEnabled(True)

                if style == 'dash':
                    line_style = QtCore.Qt.DashLine
                elif style == 'dot':
                    line_style = QtCore.Qt.DotLine
                elif style == 'dotdash':
                    line_style = QtCore.Qt.DashDotLine
                else:
                    line_style = QtCore.Qt.SolidLine

                # plotting expectations
                if self.ui.checkBox_x.isChecked():
                    if self.ui.radioButton_f.isChecked():
                        # error checking
                        if low_k != high_k:
                            raise KRangeNotAllowed
                        if low_w == high_w:
                            raise FRangeNotAccepted
                        s_x = w_expect_vals[0]
                        self.expectations_plot.plot(w_range_for_graph, s_x, pen=pg.mkPen('b', style=line_style), name='Sx')
                        self.expectations_plot.setLabel('bottom', "Frequency (MHz)", **self.labelStyle)
                    elif self.ui.radioButton_k.isChecked():
                        # error checking
                        if low_w != high_w:
                            raise FRangeNotAllowed
                        if low_k == high_k:
                            raise KRangeNotAccepted
                        s_x = k_expect_vals[0]
                        self.expectations_plot.plot(k_range, s_x, pen=pg.mkPen('b', style=line_style), name='Sx')
                        self.expectations_plot.setLabel('bottom', "k Range", **self.labelStyle)
                    else:
                        # error checking
                        if low_w == high_w:
                            raise FRangeNotAccepted
                        if low_k == high_k:
                            raise KRangeNotAccepted

                        x = np.array(w_range_for_graph)
                        y = np.array(k_range)

                        matrix = ContourPlotExpectVal(k_range, w_range, w1, data)
                        matrix.start()
                        while matrix.progress_complete is False:
                            self.ui.progressBar.setValue(matrix.progress)
                            QtGui.qApp.processEvents()
                        self.ui.progressBar.setValue(100)

                        sigma_x = matrix.matrix_dic["z_sigma_x"]

                        z = np.array(sigma_x)
                        window = ContourPlotGUI.Contour(x, y, z, "Contour Plot for Sigma X Exp.", self)
                        window.show()

                if self.ui.checkBox_y.isChecked():
                    if self.ui.radioButton_f.isChecked():
                        # error checking
                        if low_k != high_k:
                            raise KRangeNotAllowed
                        if low_w == high_w:
                            raise FRangeNotAccepted
                        s_y = w_expect_vals[1]
                        self.expectations_plot.plot(w_range_for_graph, s_y, pen=pg.mkPen('r', style=line_style), name='Sy')
                        self.expectations_plot.setLabel('bottom', "Frequency (MHz)", **self.labelStyle)
                    elif self.ui.radioButton_k.isChecked():
                        # error checking
                        if low_w != high_w:
                            raise FRangeNotAllowed
                        if low_k == high_k:
                            raise KRangeNotAccepted
                        s_y = k_expect_vals[1]
                        self.expectations_plot.plot(k_range, s_y, pen=pg.mkPen('r', style=line_style), name='Sy')
                        self.expectations_plot.setLabel('bottom', "k Range", **self.labelStyle)
                    else:
                        # error checking
                        if low_w == high_w:
                            raise FRangeNotAccepted
                        if low_k == high_k:
                            raise KRangeNotAccepted

                        x = np.array(w_range_for_graph)
                        y = np.array(k_range)

                        matrix = ContourPlotExpectVal(k_range, w_range, w1, data)
                        matrix.start()
                        while matrix.progress_complete is False:
                            self.ui.progressBar.setValue(matrix.progress)
                            QtGui.qApp.processEvents()
                        self.ui.progressBar.setValue(100)

                        sigma_y = matrix.matrix_dic["z_sigma_y"]

                        z = np.array(sigma_y)
                        window = ContourPlotGUI.Contour(x, y, z, "Contour Plot for Sigma Y Exp.", self)
                        window.show()

                if self.ui.checkBox_z.isChecked():
                    if self.ui.radioButton_f.isChecked():
                        # error checking
                        if low_k != high_k:
                            raise KRangeNotAllowed
                        if low_w == high_w:
                            raise FRangeNotAccepted
                        s_z = w_expect_vals[2]
                        self.expectations_plot.plot(w_range_for_graph, s_z, pen=pg.mkPen('#008000', style=line_style))
                        self.expectations_plot.setLabel('bottom', "Frequency (MHz)", **self.labelStyle)
                    elif self.ui.radioButton_k.isChecked():
                        # error checking
                        if low_w != high_w:
                            raise FRangeNotAllowed
                        if low_k == high_k:
                            raise KRangeNotAccepted
                        s_z = k_expect_vals[2]
                        self.expectations_plot.plot(k_range, s_z, pen=pg.mkPen('#008000', style=line_style), name='Sz')
                        self.expectations_plot.setLabel('bottom', "k Range", **self.labelStyle)
                    else:
                        # error checking
                        if low_w == high_w:
                            raise FRangeNotAccepted
                        if low_k == high_k:
                            raise KRangeNotAccepted

                        x = np.array(w_range_for_graph)
                        y = np.array(k_range)

                        matrix = ContourPlotExpectVal(k_range, w_range, w1, data)
                        matrix.start()
                        while matrix.progress_complete is False:
                            self.ui.progressBar.setValue(matrix.progress)
                            QtGui.qApp.processEvents()
                        self.ui.progressBar.setValue(100)

                        sigma_z = matrix.matrix_dic["z_sigma_z"]

                        z = np.array(sigma_z)
                        window = ContourPlotGUI.Contour(x, y, z, "Contour Plot for Sigma Z Exp.", self)
                        window.show()

            except KRangeNotAccepted:
                msg = QMessageBox()
                msg.setIcon(QMessageBox.Warning)
                msg.setText("K Range must go from low to high and cannot be the same.")
                msg.setInformativeText("Please recheck values.")
                msg.setWindowTitle("Input Error")
                msg.setStandardButtons(QMessageBox.Ok)
                msg.exec_()

            except FRangeNotAccepted:
                msg = QMessageBox()
                msg.setIcon(QMessageBox.Warning)
                msg.setText("Frequency Range must go from low to high and cannot be the same.")
                msg.setInformativeText("Please recheck values.")
                msg.setWindowTitle("Input Error")
                msg.setStandardButtons(QMessageBox.Ok)
                msg.exec_()

            except FRangeNotAllowed:
                msg = QMessageBox()
                msg.setIcon(QMessageBox.Warning)
                msg.setText("Given a range for value of f.")
                msg.setInformativeText("Ensure lower and higher value are the same.")
                msg.setWindowTitle("Input Error")
                msg.setStandardButtons(QMessageBox.Ok)
                msg.exec_()

            except KRangeNotAllowed:
                msg = QMessageBox()
                msg.setIcon(QMessageBox.Warning)
                msg.setText("Given a range for value of k.")
                msg.setInformativeText("Ensure lower and higher value are the same.")
                msg.setWindowTitle("Input Error")
                msg.setStandardButtons(QMessageBox.Ok)
                msg.exec_()

            except IOError:
                msg = QMessageBox()
                msg.setIcon(QMessageBox.Warning)
                msg.setText("CSV shaped pulse file not found.")
                msg.setInformativeText("Please recheck directory for file.")
                msg.setWindowTitle("Input Error")
                msg.setStandardButtons(QMessageBox.Ok)
                msg.exec_()

            except ValueError:
                msg = QMessageBox()
                msg.setIcon(QMessageBox.Warning)
                msg.setText("Error inside the CSV file.")
                msg.setInformativeText("Please ensure the pulses have been entered in correct formatting. "
                                       "(time, amp, phase)")
                msg.setWindowTitle("CSV Error")
                msg.setStandardButtons(QMessageBox.Ok)
                msg.exec_()

            except IndexError:
                pass


if __name__ == '__main__':
    app = QtGui.QApplication(sys.argv)
    window = Main()
    window.show()
    sys.exit(app.exec_())