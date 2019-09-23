# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'ComparisonUI.ui'
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

class Ui_Dialog(object):
    def setupUi(self, Dialog):
        Dialog.setObjectName(_fromUtf8("Dialog"))
        Dialog.resize(525, 282)
        Dialog.setAcceptDrops(False)
        self.gridLayout = QtGui.QGridLayout(Dialog)
        self.gridLayout.setObjectName(_fromUtf8("gridLayout"))
        self.tableWidget = QtGui.QTableWidget(Dialog)
        self.tableWidget.setObjectName(_fromUtf8("tableWidget"))
        self.tableWidget.setColumnCount(0)
        self.tableWidget.setRowCount(0)
        self.gridLayout.addWidget(self.tableWidget, 4, 0, 1, 3)
        self.title_label = QtGui.QLabel(Dialog)
        font = QtGui.QFont()
        font.setFamily(_fromUtf8("Calibri"))
        font.setPointSize(16)
        font.setBold(True)
        font.setWeight(75)
        self.title_label.setFont(font)
        self.title_label.setAlignment(QtCore.Qt.AlignCenter)
        self.title_label.setObjectName(_fromUtf8("title_label"))
        self.gridLayout.addWidget(self.title_label, 0, 0, 1, 3)
        self.pulse_comboBox = QtGui.QComboBox(Dialog)
        self.pulse_comboBox.setObjectName(_fromUtf8("pulse_comboBox"))
        self.gridLayout.addWidget(self.pulse_comboBox, 2, 1, 1, 1)
        self.label_14 = QtGui.QLabel(Dialog)
        self.label_14.setMaximumSize(QtCore.QSize(100, 16777215))
        self.label_14.setObjectName(_fromUtf8("label_14"))
        self.gridLayout.addWidget(self.label_14, 2, 0, 1, 1)
        self.pushButton_remove = QtGui.QPushButton(Dialog)
        self.pushButton_remove.setEnabled(False)
        self.pushButton_remove.setObjectName(_fromUtf8("pushButton_remove"))
        self.gridLayout.addWidget(self.pushButton_remove, 2, 2, 1, 1)
        self.toolButton_add = QtGui.QToolButton(Dialog)
        self.toolButton_add.setObjectName(_fromUtf8("toolButton_add"))
        self.gridLayout.addWidget(self.toolButton_add, 1, 0, 1, 1)
        self.pushButton_cancel = QtGui.QPushButton(Dialog)
        self.pushButton_cancel.setObjectName(_fromUtf8("pushButton_cancel"))
        self.gridLayout.addWidget(self.pushButton_cancel, 5, 2, 1, 1)
        self.pushButton_apply = QtGui.QPushButton(Dialog)
        self.pushButton_apply.setObjectName(_fromUtf8("pushButton_apply"))
        self.gridLayout.addWidget(self.pushButton_apply, 5, 1, 1, 1)

        self.retranslateUi(Dialog)
        QtCore.QMetaObject.connectSlotsByName(Dialog)

    def retranslateUi(self, Dialog):
        Dialog.setWindowTitle(_translate("Dialog", "Comparing Pulses", None))
        self.title_label.setText(_translate("Dialog", "Pulse Comparison", None))
        self.label_14.setText(_translate("Dialog", "<html><head/><body><p align=\"right\"><span style=\" font-size:9pt; font-weight:600;\">Selected Pulse:</span></p></body></html>", None))
        self.pushButton_remove.setText(_translate("Dialog", "Remove ", None))
        self.toolButton_add.setText(_translate("Dialog", "Add CSV File Pulse +", None))
        self.pushButton_cancel.setText(_translate("Dialog", "Cancel", None))
        self.pushButton_apply.setText(_translate("Dialog", "Apply", None))


if __name__ == "__main__":
    import sys
    app = QtGui.QApplication(sys.argv)
    Dialog = QtGui.QDialog()
    ui = Ui_Dialog()
    ui.setupUi(Dialog)
    Dialog.show()
    sys.exit(app.exec_())

