# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'edit_line_ui.ui'
#
# Created by: PyQt5 UI code generator 5.9.2
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtGui, QtWidgets
#################################################
from PyQt5.QtWidgets import  QFileDialog, QMainWindow
from line import edit_line, convertToBinaryData,insertBLOB,get_name
#################################################

#class Ui_edit_ui(object):
##################################################
class Ui_edit_ui(QMainWindow):
##################################################
    #def setupUi(self, edit_ui):
    ############################################
    def setupUi(self, edit_ui,index):
    ############################################
        edit_ui.setObjectName("edit_ui")
        edit_ui.resize(1303, 672)
        self.label = QtWidgets.QLabel(edit_ui)
        self.label.setGeometry(QtCore.QRect(0, 30, 1301, 21))
        self.label.setAlignment(QtCore.Qt.AlignCenter)
        self.label.setObjectName("label")
        self.x = QtWidgets.QLineEdit(edit_ui)
        self.x.setGeometry(QtCore.QRect(50, 100, 113, 28))
        self.x.setInputMask("")
        self.x.setObjectName("x")
        self.y = QtWidgets.QLineEdit(edit_ui)
        self.y.setGeometry(QtCore.QRect(50, 140, 113, 28))
        self.y.setObjectName("y")
        self.z = QtWidgets.QLineEdit(edit_ui)
        self.z.setGeometry(QtCore.QRect(50, 180, 113, 28))
        self.z.setObjectName("z")
        self.comboBox = QtWidgets.QComboBox(edit_ui)
        self.comboBox.setGeometry(QtCore.QRect(190, 100, 76, 24))
        self.comboBox.setObjectName("comboBox")
        self.comboBox.addItem("")
        self.comboBox.addItem("")
        self.comboBox_2 = QtWidgets.QComboBox(edit_ui)
        self.comboBox_2.setGeometry(QtCore.QRect(190, 140, 76, 24))
        self.comboBox_2.setObjectName("comboBox_2")
        self.comboBox_2.addItem("")
        self.comboBox_2.addItem("")
        self.comboBox_3 = QtWidgets.QComboBox(edit_ui)
        self.comboBox_3.setGeometry(QtCore.QRect(190, 180, 76, 24))
        self.comboBox_3.setObjectName("comboBox_3")
        self.comboBox_3.addItem("")
        self.comboBox_3.addItem("")
        self.label_id = QtWidgets.QLabel(edit_ui)
        self.label_id.setGeometry(QtCore.QRect(590, 60, 51, 20))
        self.label_id.setObjectName("label_id")
        ################################################
        self.label_id.setText(str(index))
        ################################################
        self.label_name = QtWidgets.QLabel(edit_ui)
        self.label_name.setGeometry(QtCore.QRect(650, 60, 58, 16))
        self.label_name.setObjectName("label_name")
        ################################################
        self.label_name.setText("text")
        ################################################
        self.button_edit = QtWidgets.QPushButton(edit_ui)
        self.button_edit.setGeometry(QtCore.QRect(1130, 100, 90, 28))
        self.button_edit.setObjectName("button_edit")
        ##############################################################
        self.button_edit.clicked.connect(lambda: edit_line(index,self.x.text(),self.comboBox.currentText(),self.y.text(),self.comboBox_2.currentText(),self.z.text(),self.comboBox_3.currentText()))##
        ##############################################################

        self.retranslateUi(edit_ui)
        QtCore.QMetaObject.connectSlotsByName(edit_ui)

    def retranslateUi(self, edit_ui):
        _translate = QtCore.QCoreApplication.translate
        edit_ui.setWindowTitle(_translate("edit_ui", "Dialog"))
        self.label.setText(_translate("edit_ui", "Edit an object"))
        self.x.setText(_translate("edit_ui", "x"))
        self.y.setText(_translate("edit_ui", "y"))
        self.z.setText(_translate("edit_ui", "z"))
        self.comboBox.setItemText(0, _translate("edit_ui", "mm"))
        self.comboBox.setItemText(1, _translate("edit_ui", "cm"))
        self.comboBox_2.setItemText(0, _translate("edit_ui", "mm"))
        self.comboBox_2.setItemText(1, _translate("edit_ui", "cm"))
        self.comboBox_3.setItemText(0, _translate("edit_ui", "mm"))
        self.comboBox_3.setItemText(1, _translate("edit_ui", "cm"))
        self.label_id.setText(_translate("edit_ui", "id"))
        self.label_name.setText(_translate("edit_ui", "name"))
        self.button_edit.setText(_translate("edit_ui", "Edit object"))


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    edit_ui = QtWidgets.QDialog()
    ui = Ui_edit_ui()
    ui.setupUi(edit_ui)
    edit_ui.show()
    sys.exit(app.exec_())

