"""
Created on August 20th, 2019
@author: hossein.mohebbi
"""

# Import necessary GUI module
from PyQt4 import QtGui, QtCore
from UI_Files.ComparisonUI import Ui_Dialog
from PyQt4.QtGui import *

import sys


class Compare(QtGui.QDialog):
    """ Window Class """

    def __init__(self, dic, parent=None):
        #QtGui.QDialog.__init__(self)
        super(Compare, self).__init__(parent)
        self.ui = Ui_Dialog()
        self.ui.setupUi(self)
        self.pulse_dic = dic

        # base attributes
        self.running = True
        self.original = False

        self.table = self.ui.tableWidget
        self.table.setColumnCount(2)
        self.table.setHorizontalHeaderLabels("Pulse File;Line Style;".split(";"))
        header = self.table.horizontalHeader()
        header.setResizeMode(0, QtGui.QHeaderView.Stretch)
        self.table.setRowCount(4)

        self.pulse_count = 0

        # table styles
        self.dash = '         --------'
        self.dot = '         .............'
        self.dotdash = '         _._._._._.'
        self.available_styles = ['dash', 'dot', 'dotdash']
        self.ui.pulse_comboBox.addItems(['Pulse 2', 'Pulse 3', 'Pulse 4'])

        for style in self.pulse_dic:
            self.table.setItem(self.pulse_count, 0, QTableWidgetItem(self.pulse_dic[style]))
            if style == "dash":
                index = self.available_styles.index("dash")
                del self.available_styles[index]
                self.table.setItem(self.pulse_count, 1, QTableWidgetItem(self.dash))
            elif style == "dot":
                index = self.available_styles.index("dot")
                del self.available_styles[index]
                self.table.setItem(self.pulse_count, 1, QTableWidgetItem(self.dot))
            elif style == "dotdash":
                index = self.available_styles.index("dotdash")
                del self.available_styles[index]
                self.table.setItem(self.pulse_count, 1, QTableWidgetItem(self.dotdash))
            else:
                self.table.setItem(self.pulse_count, 1, QTableWidgetItem('         ________'))

            self.pulse_count += 1

        if self.pulse_count > 1:
            self.ui.pushButton_remove.setEnabled(True)

        self.ui.pushButton_apply.clicked.connect(self.apply)
        self.ui.pushButton_cancel.clicked.connect(self.cancel)
        self.ui.pushButton_remove.clicked.connect(self.remove)
        self.ui.toolButton_add.clicked.connect(self.add_file)

    # function to find file directory
    def add_file(self):
        filename = QtGui.QFileDialog.getOpenFileName(self, 'Open File', '.','(*.CSV)')
        self.ui.pushButton_remove.setEnabled(True)

        if filename in self.pulse_dic.values():
            msg = QMessageBox()
            msg.setIcon(QMessageBox.Warning)
            msg.setText("Pulse file already used.")
            msg.setInformativeText("Please enter a different file.")
            msg.setWindowTitle("File Error")
            msg.setStandardButtons(QMessageBox.Ok)
            msg.exec_()
        elif filename == '':
            pass
        else:
            self.table.setItem(self.pulse_count, 0, QTableWidgetItem(filename))
            self.pulse_dic.update({self.available_styles[0]: str(filename)})

            if self.available_styles[0] == 'dash':
                self.table.setItem(self.pulse_count, 1, QTableWidgetItem(self.dash))

            if self.available_styles[0] == 'dot':
                self.table.setItem(self.pulse_count, 1, QTableWidgetItem(self.dot))

            if self.available_styles[0] == 'dotdash':
                self.table.setItem(self.pulse_count, 1, QTableWidgetItem(self.dotdash))

            del self.available_styles[0]
            self.pulse_count += 1
            if self.pulse_count == 4:
                self.ui.toolButton_add.setEnabled(False)

    def remove(self):
        pulse = str(self.ui.pulse_comboBox.currentText())
        empty_selection = False
        try:
            if pulse == 'Pulse 2':
                pulse_style = str(self.table.item(1, 1).text())
                if pulse_style == self.dash:
                    style = 'dash'
                elif pulse_style == self.dot:
                    style = 'dot'
                else:
                    style = 'dotdash'
            elif pulse == 'Pulse 3':
                pulse_style = str(self.table.item(2, 1).text())
                if pulse_style == self.dash:
                    style = 'dash'
                elif pulse_style == self.dot:
                    style = 'dot'
                else:
                    style = 'dotdash'
            else:
                pulse_style = str(self.table.item(3, 1).text())
                if pulse_style == self.dash:
                    style = 'dash'
                elif pulse_style == self.dot:
                    style = 'dot'
                else:
                    style = 'dotdash'
        except AttributeError:
            empty_selection = True
            pass
        if empty_selection is True:
            pass
        else:
            items = self.table.findItems(pulse_style, QtCore.Qt.MatchContains)
            self.ui.toolButton_add.setEnabled(True)

            # Remove From Dictionary As Well
            self.available_styles.append(style)
            del self.pulse_dic[style]

            rows = []
            for item in items:
                row = item.row()
                rows.append(row)
            row_counter = 0
            for row in rows:
                self.table.removeRow(row - row_counter)
                row_counter += 1
            self.table.setRowCount(4)

            self.pulse_count -= 1
            if self.pulse_count == 0:
                self.ui.pushButton_remove.setEnabled(False)

    def apply(self):
        self.running = False
        self.close()

    def cancel(self):
        self.original = True
        self.running = False
        self.close()


if __name__ == '__main__':
    app = QtGui.QApplication(sys.argv)
    window = Compare({'C:/Users/Lab1/Desktop/PulseSimulation/Shaped_Pulses/data.csv': 'dotdash'})
    window.show()
    sys.exit(app.exec_())