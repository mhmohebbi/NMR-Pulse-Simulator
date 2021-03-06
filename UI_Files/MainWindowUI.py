# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'MainWindowUI.ui'
#
# Created by: PyQt4 UI code generator 4.11.4
#
# WARNING! All changes made in this file will be lost!

from PyQt4 import QtCore, QtGui

try:
    _fromUtf8 = QtCore.QString.fromUtf8
except AttributeError:
    def _fromUtf8(s):
        return s

try:
    _encoding = QtGui.QApplication.UnicodeUTF8
    def _translate(context, text, disambig):
        return QtGui.QApplication.translate(context, text, disambig, _encoding)
except AttributeError:
    def _translate(context, text, disambig):
        return QtGui.QApplication.translate(context, text, disambig)

class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName(_fromUtf8("MainWindow"))
        MainWindow.resize(1080, 878)
        self.centralwidget = QtGui.QWidget(MainWindow)
        self.centralwidget.setObjectName(_fromUtf8("centralwidget"))
        self.gridLayout = QtGui.QGridLayout(self.centralwidget)
        self.gridLayout.setObjectName(_fromUtf8("gridLayout"))
        self.title_label = QtGui.QLabel(self.centralwidget)
        font = QtGui.QFont()
        font.setFamily(_fromUtf8("Calibri"))
        font.setPointSize(16)
        font.setBold(True)
        font.setWeight(75)
        self.title_label.setFont(font)
        self.title_label.setAlignment(QtCore.Qt.AlignCenter)
        self.title_label.setObjectName(_fromUtf8("title_label"))
        self.gridLayout.addWidget(self.title_label, 0, 0, 1, 2)
        self.pushButton_sphere = QtGui.QPushButton(self.centralwidget)
        self.pushButton_sphere.setMinimumSize(QtCore.QSize(200, 0))
        self.pushButton_sphere.setMaximumSize(QtCore.QSize(400, 16777215))
        self.pushButton_sphere.setObjectName(_fromUtf8("pushButton_sphere"))
        self.gridLayout.addWidget(self.pushButton_sphere, 8, 0, 1, 2, QtCore.Qt.AlignHCenter)
        self.frame_4 = QtGui.QFrame(self.centralwidget)
        self.frame_4.setMinimumSize(QtCore.QSize(0, 90))
        self.frame_4.setFrameShape(QtGui.QFrame.StyledPanel)
        self.frame_4.setFrameShadow(QtGui.QFrame.Raised)
        self.frame_4.setObjectName(_fromUtf8("frame_4"))
        self.gridLayout_8 = QtGui.QGridLayout(self.frame_4)
        self.gridLayout_8.setObjectName(_fromUtf8("gridLayout_8"))
        spacerItem = QtGui.QSpacerItem(40, 20, QtGui.QSizePolicy.Expanding, QtGui.QSizePolicy.Minimum)
        self.gridLayout_8.addItem(spacerItem, 2, 4, 1, 1)
        spacerItem1 = QtGui.QSpacerItem(40, 20, QtGui.QSizePolicy.Expanding, QtGui.QSizePolicy.Minimum)
        self.gridLayout_8.addItem(spacerItem1, 1, 4, 1, 1)
        spacerItem2 = QtGui.QSpacerItem(40, 20, QtGui.QSizePolicy.Expanding, QtGui.QSizePolicy.Minimum)
        self.gridLayout_8.addItem(spacerItem2, 2, 5, 1, 1)
        spacerItem3 = QtGui.QSpacerItem(40, 20, QtGui.QSizePolicy.Expanding, QtGui.QSizePolicy.Minimum)
        self.gridLayout_8.addItem(spacerItem3, 2, 1, 1, 1)
        self.pushButton_pulse = QtGui.QPushButton(self.frame_4)
        self.pushButton_pulse.setMinimumSize(QtCore.QSize(150, 23))
        self.pushButton_pulse.setObjectName(_fromUtf8("pushButton_pulse"))
        self.gridLayout_8.addWidget(self.pushButton_pulse, 1, 2, 1, 2)
        spacerItem4 = QtGui.QSpacerItem(40, 20, QtGui.QSizePolicy.Expanding, QtGui.QSizePolicy.Minimum)
        self.gridLayout_8.addItem(spacerItem4, 1, 1, 1, 1)
        spacerItem5 = QtGui.QSpacerItem(40, 20, QtGui.QSizePolicy.Expanding, QtGui.QSizePolicy.Minimum)
        self.gridLayout_8.addItem(spacerItem5, 2, 0, 1, 1)
        self.radioButton_rectangle = QtGui.QRadioButton(self.frame_4)
        self.radioButton_rectangle.setChecked(True)
        self.radioButton_rectangle.setObjectName(_fromUtf8("radioButton_rectangle"))
        self.gridLayout_8.addWidget(self.radioButton_rectangle, 2, 2, 1, 2)
        self.radioButton_polar = QtGui.QRadioButton(self.frame_4)
        self.radioButton_polar.setObjectName(_fromUtf8("radioButton_polar"))
        self.gridLayout_8.addWidget(self.radioButton_polar, 3, 2, 1, 1, QtCore.Qt.AlignHCenter)
        self.gridLayout.addWidget(self.frame_4, 3, 0, 1, 1)
        self.outerframe = QtGui.QGroupBox(self.centralwidget)
        self.outerframe.setMaximumSize(QtCore.QSize(16777215, 400))
        self.outerframe.setToolTip(_fromUtf8("<html><head/><body><p>Guassmeter GUI</p></body></html>"))
        self.outerframe.setTitle(_fromUtf8(""))
        self.outerframe.setObjectName(_fromUtf8("outerframe"))
        self.gridLayout_2 = QtGui.QGridLayout(self.outerframe)
        self.gridLayout_2.setObjectName(_fromUtf8("gridLayout_2"))
        self.rabi_freq_doubleSpinBox = QtGui.QDoubleSpinBox(self.outerframe)
        self.rabi_freq_doubleSpinBox.setMinimumSize(QtCore.QSize(80, 0))
        self.rabi_freq_doubleSpinBox.setDecimals(1)
        self.rabi_freq_doubleSpinBox.setMinimum(0.0)
        self.rabi_freq_doubleSpinBox.setMaximum(90000.0)
        self.rabi_freq_doubleSpinBox.setSingleStep(2.0)
        self.rabi_freq_doubleSpinBox.setProperty("value", 10.0)
        self.rabi_freq_doubleSpinBox.setObjectName(_fromUtf8("rabi_freq_doubleSpinBox"))
        self.gridLayout_2.addWidget(self.rabi_freq_doubleSpinBox, 3, 2, 1, 1)
        self.label_11 = QtGui.QLabel(self.outerframe)
        self.label_11.setMaximumSize(QtCore.QSize(40, 16777215))
        self.label_11.setObjectName(_fromUtf8("label_11"))
        self.gridLayout_2.addWidget(self.label_11, 4, 4, 1, 1)
        self.label_14 = QtGui.QLabel(self.outerframe)
        self.label_14.setMaximumSize(QtCore.QSize(100, 16777215))
        self.label_14.setObjectName(_fromUtf8("label_14"))
        self.gridLayout_2.addWidget(self.label_14, 3, 1, 1, 1)
        self.label_7 = QtGui.QLabel(self.outerframe)
        self.label_7.setMaximumSize(QtCore.QSize(100, 16777215))
        self.label_7.setObjectName(_fromUtf8("label_7"))
        self.gridLayout_2.addWidget(self.label_7, 4, 1, 1, 1)
        self.open_pushButton = QtGui.QPushButton(self.outerframe)
        self.open_pushButton.setMaximumSize(QtCore.QSize(60, 16777215))
        self.open_pushButton.setObjectName(_fromUtf8("open_pushButton"))
        self.gridLayout_2.addWidget(self.open_pushButton, 2, 7, 1, 1)
        self.file_lineEdit = QtGui.QLineEdit(self.outerframe)
        self.file_lineEdit.setText(_fromUtf8(""))
        self.file_lineEdit.setObjectName(_fromUtf8("file_lineEdit"))
        self.gridLayout_2.addWidget(self.file_lineEdit, 2, 2, 1, 5)
        self.step_doubleSpinBox = QtGui.QDoubleSpinBox(self.outerframe)
        self.step_doubleSpinBox.setMinimumSize(QtCore.QSize(80, 0))
        self.step_doubleSpinBox.setDecimals(1)
        self.step_doubleSpinBox.setMinimum(10.0)
        self.step_doubleSpinBox.setMaximum(90000.0)
        self.step_doubleSpinBox.setSingleStep(50.0)
        self.step_doubleSpinBox.setProperty("value", 250.0)
        self.step_doubleSpinBox.setObjectName(_fromUtf8("step_doubleSpinBox"))
        self.gridLayout_2.addWidget(self.step_doubleSpinBox, 5, 2, 1, 1)
        self.label_6 = QtGui.QLabel(self.outerframe)
        self.label_6.setMinimumSize(QtCore.QSize(0, 30))
        self.label_6.setMaximumSize(QtCore.QSize(16777215, 33))
        self.label_6.setAlignment(QtCore.Qt.AlignCenter)
        self.label_6.setObjectName(_fromUtf8("label_6"))
        self.gridLayout_2.addWidget(self.label_6, 0, 0, 1, 9)
        self.label_15 = QtGui.QLabel(self.outerframe)
        self.label_15.setMaximumSize(QtCore.QSize(40, 16777215))
        self.label_15.setObjectName(_fromUtf8("label_15"))
        self.gridLayout_2.addWidget(self.label_15, 3, 3, 1, 1)
        self.label_9 = QtGui.QLabel(self.outerframe)
        self.label_9.setMaximumSize(QtCore.QSize(40, 16777215))
        self.label_9.setObjectName(_fromUtf8("label_9"))
        self.gridLayout_2.addWidget(self.label_9, 4, 6, 1, 1)
        self.label_12 = QtGui.QLabel(self.outerframe)
        self.label_12.setMaximumSize(QtCore.QSize(100, 16777215))
        self.label_12.setObjectName(_fromUtf8("label_12"))
        self.gridLayout_2.addWidget(self.label_12, 5, 1, 1, 1)
        self.label_5 = QtGui.QLabel(self.outerframe)
        self.label_5.setMaximumSize(QtCore.QSize(100, 16777215))
        self.label_5.setObjectName(_fromUtf8("label_5"))
        self.gridLayout_2.addWidget(self.label_5, 2, 1, 1, 1)
        self.high_range_doubleSpinBox = QtGui.QDoubleSpinBox(self.outerframe)
        self.high_range_doubleSpinBox.setMinimumSize(QtCore.QSize(80, 0))
        self.high_range_doubleSpinBox.setDecimals(1)
        self.high_range_doubleSpinBox.setMinimum(-90000.0)
        self.high_range_doubleSpinBox.setMaximum(90000.0)
        self.high_range_doubleSpinBox.setSingleStep(10.0)
        self.high_range_doubleSpinBox.setProperty("value", 15.0)
        self.high_range_doubleSpinBox.setObjectName(_fromUtf8("high_range_doubleSpinBox"))
        self.gridLayout_2.addWidget(self.high_range_doubleSpinBox, 4, 5, 1, 1)
        self.label_8 = QtGui.QLabel(self.outerframe)
        self.label_8.setMaximumSize(QtCore.QSize(40, 16777215))
        self.label_8.setObjectName(_fromUtf8("label_8"))
        self.gridLayout_2.addWidget(self.label_8, 4, 3, 1, 1)
        self.label_13 = QtGui.QLabel(self.outerframe)
        self.label_13.setMaximumSize(QtCore.QSize(40, 16777215))
        self.label_13.setObjectName(_fromUtf8("label_13"))
        self.gridLayout_2.addWidget(self.label_13, 5, 3, 1, 1)
        self.low_range_doubleSpinBox = QtGui.QDoubleSpinBox(self.outerframe)
        self.low_range_doubleSpinBox.setMinimumSize(QtCore.QSize(80, 0))
        self.low_range_doubleSpinBox.setDecimals(1)
        self.low_range_doubleSpinBox.setMinimum(-90000.0)
        self.low_range_doubleSpinBox.setMaximum(90000.0)
        self.low_range_doubleSpinBox.setSingleStep(10.0)
        self.low_range_doubleSpinBox.setProperty("value", -15.0)
        self.low_range_doubleSpinBox.setObjectName(_fromUtf8("low_range_doubleSpinBox"))
        self.gridLayout_2.addWidget(self.low_range_doubleSpinBox, 4, 2, 1, 1)
        self.k_step_doubleSpinBox = QtGui.QDoubleSpinBox(self.outerframe)
        self.k_step_doubleSpinBox.setMinimumSize(QtCore.QSize(80, 0))
        self.k_step_doubleSpinBox.setDecimals(2)
        self.k_step_doubleSpinBox.setMinimum(0.01)
        self.k_step_doubleSpinBox.setMaximum(90000.0)
        self.k_step_doubleSpinBox.setSingleStep(0.1)
        self.k_step_doubleSpinBox.setProperty("value", 0.01)
        self.k_step_doubleSpinBox.setObjectName(_fromUtf8("k_step_doubleSpinBox"))
        self.gridLayout_2.addWidget(self.k_step_doubleSpinBox, 7, 2, 1, 1)
        self.label_10 = QtGui.QLabel(self.outerframe)
        self.label_10.setMaximumSize(QtCore.QSize(100, 16777215))
        self.label_10.setObjectName(_fromUtf8("label_10"))
        self.gridLayout_2.addWidget(self.label_10, 6, 1, 1, 1)
        self.low_range_doubleSpinBox_k = QtGui.QDoubleSpinBox(self.outerframe)
        self.low_range_doubleSpinBox_k.setMinimumSize(QtCore.QSize(80, 0))
        self.low_range_doubleSpinBox_k.setDecimals(2)
        self.low_range_doubleSpinBox_k.setMinimum(0.01)
        self.low_range_doubleSpinBox_k.setMaximum(90000.0)
        self.low_range_doubleSpinBox_k.setSingleStep(0.5)
        self.low_range_doubleSpinBox_k.setProperty("value", 0.5)
        self.low_range_doubleSpinBox_k.setObjectName(_fromUtf8("low_range_doubleSpinBox_k"))
        self.gridLayout_2.addWidget(self.low_range_doubleSpinBox_k, 6, 2, 1, 1)
        self.high_range_doubleSpinBox_k = QtGui.QDoubleSpinBox(self.outerframe)
        self.high_range_doubleSpinBox_k.setMinimumSize(QtCore.QSize(80, 0))
        self.high_range_doubleSpinBox_k.setDecimals(2)
        self.high_range_doubleSpinBox_k.setMinimum(0.02)
        self.high_range_doubleSpinBox_k.setMaximum(90000.0)
        self.high_range_doubleSpinBox_k.setSingleStep(0.5)
        self.high_range_doubleSpinBox_k.setProperty("value", 1.5)
        self.high_range_doubleSpinBox_k.setObjectName(_fromUtf8("high_range_doubleSpinBox_k"))
        self.gridLayout_2.addWidget(self.high_range_doubleSpinBox_k, 6, 5, 1, 1)
        self.label_19 = QtGui.QLabel(self.outerframe)
        self.label_19.setMaximumSize(QtCore.QSize(100, 16777215))
        self.label_19.setObjectName(_fromUtf8("label_19"))
        self.gridLayout_2.addWidget(self.label_19, 7, 1, 1, 1)
        self.label_17 = QtGui.QLabel(self.outerframe)
        self.label_17.setMaximumSize(QtCore.QSize(40, 16777215))
        self.label_17.setObjectName(_fromUtf8("label_17"))
        self.gridLayout_2.addWidget(self.label_17, 6, 4, 1, 1)
        self.gridLayout.addWidget(self.outerframe, 2, 0, 1, 2)
        self.widget = QtGui.QWidget(self.centralwidget)
        self.widget.setObjectName(_fromUtf8("widget"))
        self.gridLayout_6 = QtGui.QGridLayout(self.widget)
        self.gridLayout_6.setObjectName(_fromUtf8("gridLayout_6"))
        self.pulse_1_plot_tabWidget = QtGui.QTabWidget(self.widget)
        self.pulse_1_plot_tabWidget.setObjectName(_fromUtf8("pulse_1_plot_tabWidget"))
        self.Pulse_Plot_1 = QtGui.QWidget()
        self.Pulse_Plot_1.setObjectName(_fromUtf8("Pulse_Plot_1"))
        self.gridLayout_3 = QtGui.QGridLayout(self.Pulse_Plot_1)
        self.gridLayout_3.setObjectName(_fromUtf8("gridLayout_3"))
        self.pulse_1_plot_tabWidget.addTab(self.Pulse_Plot_1, _fromUtf8(""))
        self.gridLayout_6.addWidget(self.pulse_1_plot_tabWidget, 0, 0, 1, 1)
        self.pulse_2_plot_tabWidget = QtGui.QTabWidget(self.widget)
        self.pulse_2_plot_tabWidget.setObjectName(_fromUtf8("pulse_2_plot_tabWidget"))
        self.Pulse_Plot_2 = QtGui.QWidget()
        self.Pulse_Plot_2.setObjectName(_fromUtf8("Pulse_Plot_2"))
        self.gridLayout_7 = QtGui.QGridLayout(self.Pulse_Plot_2)
        self.gridLayout_7.setObjectName(_fromUtf8("gridLayout_7"))
        self.pulse_2_plot_tabWidget.addTab(self.Pulse_Plot_2, _fromUtf8(""))
        self.gridLayout_6.addWidget(self.pulse_2_plot_tabWidget, 1, 0, 1, 1)
        self.gridLayout.addWidget(self.widget, 5, 0, 1, 1)
        self.frame_3 = QtGui.QFrame(self.centralwidget)
        self.frame_3.setMinimumSize(QtCore.QSize(0, 124))
        self.frame_3.setFrameShape(QtGui.QFrame.StyledPanel)
        self.frame_3.setFrameShadow(QtGui.QFrame.Raised)
        self.frame_3.setObjectName(_fromUtf8("frame_3"))
        self.gridLayout_4 = QtGui.QGridLayout(self.frame_3)
        self.gridLayout_4.setObjectName(_fromUtf8("gridLayout_4"))
        spacerItem6 = QtGui.QSpacerItem(40, 20, QtGui.QSizePolicy.Expanding, QtGui.QSizePolicy.Minimum)
        self.gridLayout_4.addItem(spacerItem6, 2, 0, 1, 1)
        self.checkBox_x = QtGui.QCheckBox(self.frame_3)
        self.checkBox_x.setChecked(True)
        self.checkBox_x.setObjectName(_fromUtf8("checkBox_x"))
        self.gridLayout_4.addWidget(self.checkBox_x, 2, 1, 1, 1, QtCore.Qt.AlignRight)
        self.pushButton_expects = QtGui.QPushButton(self.frame_3)
        self.pushButton_expects.setMinimumSize(QtCore.QSize(150, 23))
        self.pushButton_expects.setObjectName(_fromUtf8("pushButton_expects"))
        self.gridLayout_4.addWidget(self.pushButton_expects, 1, 2, 1, 1)
        self.radioButton_f = QtGui.QRadioButton(self.frame_3)
        self.radioButton_f.setChecked(True)
        self.radioButton_f.setObjectName(_fromUtf8("radioButton_f"))
        self.gridLayout_4.addWidget(self.radioButton_f, 3, 1, 1, 1, QtCore.Qt.AlignRight)
        self.radioButton_contour = QtGui.QRadioButton(self.frame_3)
        self.radioButton_contour.setObjectName(_fromUtf8("radioButton_contour"))
        self.gridLayout_4.addWidget(self.radioButton_contour, 3, 3, 1, 1, QtCore.Qt.AlignLeft)
        spacerItem7 = QtGui.QSpacerItem(40, 20, QtGui.QSizePolicy.Expanding, QtGui.QSizePolicy.Minimum)
        self.gridLayout_4.addItem(spacerItem7, 1, 1, 1, 1)
        spacerItem8 = QtGui.QSpacerItem(40, 20, QtGui.QSizePolicy.Expanding, QtGui.QSizePolicy.Minimum)
        self.gridLayout_4.addItem(spacerItem8, 1, 3, 1, 1)
        self.radioButton_k = QtGui.QRadioButton(self.frame_3)
        self.radioButton_k.setObjectName(_fromUtf8("radioButton_k"))
        self.gridLayout_4.addWidget(self.radioButton_k, 3, 2, 1, 1, QtCore.Qt.AlignHCenter)
        spacerItem9 = QtGui.QSpacerItem(40, 20, QtGui.QSizePolicy.Expanding, QtGui.QSizePolicy.Minimum)
        self.gridLayout_4.addItem(spacerItem9, 2, 4, 1, 1)
        self.pushButton_compare = QtGui.QPushButton(self.frame_3)
        self.pushButton_compare.setEnabled(False)
        self.pushButton_compare.setMinimumSize(QtCore.QSize(100, 0))
        self.pushButton_compare.setMaximumSize(QtCore.QSize(101, 16777215))
        self.pushButton_compare.setObjectName(_fromUtf8("pushButton_compare"))
        self.gridLayout_4.addWidget(self.pushButton_compare, 5, 2, 1, 1, QtCore.Qt.AlignHCenter)
        self.checkBox_z = QtGui.QCheckBox(self.frame_3)
        self.checkBox_z.setChecked(True)
        self.checkBox_z.setObjectName(_fromUtf8("checkBox_z"))
        self.gridLayout_4.addWidget(self.checkBox_z, 2, 3, 1, 1, QtCore.Qt.AlignLeft)
        self.checkBox_y = QtGui.QCheckBox(self.frame_3)
        self.checkBox_y.setChecked(True)
        self.checkBox_y.setObjectName(_fromUtf8("checkBox_y"))
        self.gridLayout_4.addWidget(self.checkBox_y, 2, 2, 1, 1, QtCore.Qt.AlignHCenter)
        spacerItem10 = QtGui.QSpacerItem(20, 5, QtGui.QSizePolicy.Minimum, QtGui.QSizePolicy.Fixed)
        self.gridLayout_4.addItem(spacerItem10, 0, 2, 1, 1)
        self.gridLayout.addWidget(self.frame_3, 3, 1, 1, 1)
        self.progressBar = QtGui.QProgressBar(self.centralwidget)
        self.progressBar.setProperty("value", 0)
        self.progressBar.setObjectName(_fromUtf8("progressBar"))
        self.gridLayout.addWidget(self.progressBar, 9, 0, 1, 2)
        self.frame = QtGui.QFrame(self.centralwidget)
        self.frame.setFrameShape(QtGui.QFrame.StyledPanel)
        self.frame.setFrameShadow(QtGui.QFrame.Raised)
        self.frame.setObjectName(_fromUtf8("frame"))
        self.gridLayout_5 = QtGui.QGridLayout(self.frame)
        self.gridLayout_5.setObjectName(_fromUtf8("gridLayout_5"))
        self.expectation_plot_tabWidget = QtGui.QTabWidget(self.frame)
        self.expectation_plot_tabWidget.setObjectName(_fromUtf8("expectation_plot_tabWidget"))
        self.Expectation_Plot = QtGui.QWidget()
        self.Expectation_Plot.setObjectName(_fromUtf8("Expectation_Plot"))
        self.verticalLayout = QtGui.QVBoxLayout(self.Expectation_Plot)
        self.verticalLayout.setObjectName(_fromUtf8("verticalLayout"))
        self.expectation_plot_tabWidget.addTab(self.Expectation_Plot, _fromUtf8(""))
        self.gridLayout_5.addWidget(self.expectation_plot_tabWidget, 0, 0, 1, 1)
        self.gridLayout.addWidget(self.frame, 5, 1, 1, 1)
        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QtGui.QMenuBar(MainWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 1080, 21))
        self.menubar.setObjectName(_fromUtf8("menubar"))
        MainWindow.setMenuBar(self.menubar)
        self.statusbar = QtGui.QStatusBar(MainWindow)
        self.statusbar.setObjectName(_fromUtf8("statusbar"))
        MainWindow.setStatusBar(self.statusbar)

        self.retranslateUi(MainWindow)
        self.pulse_1_plot_tabWidget.setCurrentIndex(0)
        self.pulse_2_plot_tabWidget.setCurrentIndex(0)
        self.expectation_plot_tabWidget.setCurrentIndex(0)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        MainWindow.setWindowTitle(_translate("MainWindow", "Pulse Simulator GUI", None))
        self.title_label.setText(_translate("MainWindow", "Pulse Simulator", None))
        self.pushButton_sphere.setText(_translate("MainWindow", "View Bloch Sphere", None))
        self.pushButton_pulse.setText(_translate("MainWindow", "Plot Pulse", None))
        self.radioButton_rectangle.setText(_translate("MainWindow", "Rectangular Form ", None))
        self.radioButton_polar.setText(_translate("MainWindow", "Polar Form", None))
        self.label_11.setText(_translate("MainWindow", "<html><head/><body><p><span style=\" font-size:9pt; font-weight:600;\">to</span></p></body></html>", None))
        self.label_14.setText(_translate("MainWindow", "<html><head/><body><p align=\"right\"><span style=\" font-size:9pt; font-weight:600;\">Rabi Frequency:</span></p></body></html>", None))
        self.label_7.setText(_translate("MainWindow", "<html><head/><body><p align=\"right\"><span style=\" font-size:9pt; font-weight:600;\">∆f Range:</span></p></body></html>", None))
        self.open_pushButton.setText(_translate("MainWindow", "Open File", None))
        self.label_6.setText(_translate("MainWindow", "<html><head/><body><p><span style=\" font-size:9pt; font-weight:792;\">Configurations</span></p></body></html>", None))
        self.label_15.setText(_translate("MainWindow", "<html><head/><body><p><span style=\" font-size:9pt; font-weight:600;\">MHz</span></p></body></html>", None))
        self.label_9.setText(_translate("MainWindow", "<html><head/><body><p><span style=\" font-size:9pt; font-weight:600;\">MHz</span></p></body></html>", None))
        self.label_12.setText(_translate("MainWindow", "<html><head/><body><p align=\"right\"><span style=\" font-size:9pt; font-weight:600;\">∆f Resolution:</span></p></body></html>", None))
        self.label_5.setText(_translate("MainWindow", "<html><head/><body><p align=\"right\"><span style=\" font-size:9pt; font-weight:600;\">Load CSV File:</span></p></body></html>", None))
        self.label_8.setText(_translate("MainWindow", "<html><head/><body><p><span style=\" font-size:9pt; font-weight:600;\">MHz </span></p></body></html>", None))
        self.label_13.setText(_translate("MainWindow", "<html><head/><body><p><span style=\" font-size:9pt; font-weight:600;\">KHz </span></p></body></html>", None))
        self.label_10.setText(_translate("MainWindow", "<html><head/><body><p align=\"right\"><span style=\" font-size:9pt; font-weight:600;\">∆k Range:</span></p></body></html>", None))
        self.label_19.setText(_translate("MainWindow", "<html><head/><body><p align=\"right\"><span style=\" font-size:9pt; font-weight:600;\">∆k Resolution:</span></p></body></html>", None))
        self.label_17.setText(_translate("MainWindow", "<html><head/><body><p><span style=\" font-size:9pt; font-weight:600;\">to</span></p></body></html>", None))
        self.pulse_1_plot_tabWidget.setTabText(self.pulse_1_plot_tabWidget.indexOf(self.Pulse_Plot_1), _translate("MainWindow", "Amplitude vs.Time", None))
        self.pulse_2_plot_tabWidget.setTabText(self.pulse_2_plot_tabWidget.indexOf(self.Pulse_Plot_2), _translate("MainWindow", "Phase vs. Time", None))
        self.checkBox_x.setText(_translate("MainWindow", "<Sx> - Blue", None))
        self.pushButton_expects.setText(_translate("MainWindow", "Plot Expectations", None))
        self.radioButton_f.setText(_translate("MainWindow", "∆f Range", None))
        self.radioButton_contour.setText(_translate("MainWindow", "Contour Plot", None))
        self.radioButton_k.setText(_translate("MainWindow", "∆k Range", None))
        self.pushButton_compare.setText(_translate("MainWindow", "Compare Pulses", None))
        self.checkBox_z.setText(_translate("MainWindow", "<Sz> - Green", None))
        self.checkBox_y.setText(_translate("MainWindow", "<Sy> - Red", None))
        self.expectation_plot_tabWidget.setTabText(self.expectation_plot_tabWidget.indexOf(self.Expectation_Plot), _translate("MainWindow", "Expectation Values", None))


if __name__ == "__main__":
    import sys
    app = QtGui.QApplication(sys.argv)
    MainWindow = QtGui.QMainWindow()
    ui = Ui_MainWindow()
    ui.setupUi(MainWindow)
    MainWindow.show()
    sys.exit(app.exec_())

