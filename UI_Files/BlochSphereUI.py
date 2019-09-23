# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'BlochSphereUI.ui'
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
        Dialog.resize(747, 825)
        self.gridLayout = QtGui.QGridLayout(Dialog)
        self.gridLayout.setObjectName(_fromUtf8("gridLayout"))
        self.title_label = QtGui.QLabel(Dialog)
        font = QtGui.QFont()
        font.setFamily(_fromUtf8("Calibri"))
        font.setPointSize(16)
        font.setBold(True)
        font.setWeight(75)
        self.title_label.setFont(font)
        self.title_label.setAlignment(QtCore.Qt.AlignCenter)
        self.title_label.setObjectName(_fromUtf8("title_label"))
        self.gridLayout.addWidget(self.title_label, 0, 0, 1, 1)
        self.outerframe = QtGui.QGroupBox(Dialog)
        self.outerframe.setMaximumSize(QtCore.QSize(16777215, 400))
        self.outerframe.setToolTip(_fromUtf8("<html><head/><body><p>Guassmeter GUI</p></body></html>"))
        self.outerframe.setTitle(_fromUtf8(""))
        self.outerframe.setObjectName(_fromUtf8("outerframe"))
        self.gridLayout_2 = QtGui.QGridLayout(self.outerframe)
        self.gridLayout_2.setObjectName(_fromUtf8("gridLayout_2"))
        self.gridLayout.addWidget(self.outerframe, 1, 0, 1, 1)
        self.plot_tabWidget = QtGui.QTabWidget(Dialog)
        self.plot_tabWidget.setObjectName(_fromUtf8("plot_tabWidget"))
        self.BlochSphere = QtGui.QWidget()
        self.BlochSphere.setObjectName(_fromUtf8("BlochSphere"))
        self.verticalLayout = QtGui.QVBoxLayout(self.BlochSphere)
        self.verticalLayout.setObjectName(_fromUtf8("verticalLayout"))
        self.plot_tabWidget.addTab(self.BlochSphere, _fromUtf8(""))
        self.gridLayout.addWidget(self.plot_tabWidget, 2, 0, 1, 1)

        self.retranslateUi(Dialog)
        self.plot_tabWidget.setCurrentIndex(0)
        QtCore.QMetaObject.connectSlotsByName(Dialog)

    def retranslateUi(self, Dialog):
        Dialog.setWindowTitle(_translate("Dialog", "Bloch Sphere", None))
        self.title_label.setText(_translate("Dialog", "Bloch Sphere", None))
        self.plot_tabWidget.setTabText(self.plot_tabWidget.indexOf(self.BlochSphere), _translate("Dialog", "Green = Start, Red = End", None))


if __name__ == "__main__":
    import sys
    app = QtGui.QApplication(sys.argv)
    Dialog = QtGui.QDialog()
    ui = Ui_Dialog()
    ui.setupUi(Dialog)
    Dialog.show()
    sys.exit(app.exec_())

