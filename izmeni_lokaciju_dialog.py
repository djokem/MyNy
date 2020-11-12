# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'izmeni_lokaciju_dialog.ui'
#
# Created by: PyQt5 UI code generator 5.13.0
#
# WARNING! All changes made in this file will be lost!


from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_lokacijeDetalji(object):
    def setupUi(self, lokacijeDetalji):
        lokacijeDetalji.setObjectName("lokacijeDetalji")
        lokacijeDetalji.resize(420, 223)
        self.verticalLayout = QtWidgets.QVBoxLayout(lokacijeDetalji)
        self.verticalLayout.setObjectName("verticalLayout")
        self.groupBox = QtWidgets.QGroupBox(lokacijeDetalji)
        font = QtGui.QFont()
        font.setFamily("Calibri Light")
        font.setPointSize(12)
        self.groupBox.setFont(font)
        self.groupBox.setAlignment(QtCore.Qt.AlignCenter)
        self.groupBox.setObjectName("groupBox")
        self.formLayout = QtWidgets.QFormLayout(self.groupBox)
        self.formLayout.setContentsMargins(50, 20, 30, 20)
        self.formLayout.setHorizontalSpacing(10)
        self.formLayout.setObjectName("formLayout")
        self.label = QtWidgets.QLabel(self.groupBox)
        self.label.setObjectName("label")
        self.formLayout.setWidget(0, QtWidgets.QFormLayout.LabelRole, self.label)
        self.label_2 = QtWidgets.QLabel(self.groupBox)
        self.label_2.setObjectName("label_2")
        self.formLayout.setWidget(1, QtWidgets.QFormLayout.LabelRole, self.label_2)
        self.label_3 = QtWidgets.QLabel(self.groupBox)
        self.label_3.setObjectName("label_3")
        self.formLayout.setWidget(2, QtWidgets.QFormLayout.LabelRole, self.label_3)
        self.nazivUpTxt = QtWidgets.QLineEdit(self.groupBox)
        self.nazivUpTxt.setObjectName("nazivUpTxt")
        self.formLayout.setWidget(0, QtWidgets.QFormLayout.FieldRole, self.nazivUpTxt)
        self.mestoUpTxt = QtWidgets.QLineEdit(self.groupBox)
        self.mestoUpTxt.setObjectName("mestoUpTxt")
        self.formLayout.setWidget(1, QtWidgets.QFormLayout.FieldRole, self.mestoUpTxt)
        self.adresaUpTxt = QtWidgets.QLineEdit(self.groupBox)
        self.adresaUpTxt.setObjectName("adresaUpTxt")
        self.formLayout.setWidget(2, QtWidgets.QFormLayout.FieldRole, self.adresaUpTxt)
        self.verticalLayout.addWidget(self.groupBox)
        self.buttonBox = QtWidgets.QDialogButtonBox(lokacijeDetalji)
        self.buttonBox.setOrientation(QtCore.Qt.Horizontal)
        self.buttonBox.setStandardButtons(QtWidgets.QDialogButtonBox.Cancel|QtWidgets.QDialogButtonBox.Ok)
        self.buttonBox.setObjectName("buttonBox")
        self.verticalLayout.addWidget(self.buttonBox)

        self.retranslateUi(lokacijeDetalji)
        self.buttonBox.accepted.connect(lokacijeDetalji.accept)
        self.buttonBox.rejected.connect(lokacijeDetalji.reject)
        QtCore.QMetaObject.connectSlotsByName(lokacijeDetalji)

    def retranslateUi(self, lokacijeDetalji):
        _translate = QtCore.QCoreApplication.translate
        lokacijeDetalji.setWindowTitle(_translate("lokacijeDetalji", "Dialog"))
        self.groupBox.setTitle(_translate("lokacijeDetalji", "Promena informacija o lokaciji"))
        self.label.setText(_translate("lokacijeDetalji", "Naziv:"))
        self.label_2.setText(_translate("lokacijeDetalji", "Mesto:"))
        self.label_3.setText(_translate("lokacijeDetalji", "Adresa:"))


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    lokacijeDetalji = QtWidgets.QDialog()
    ui = Ui_lokacijeDetalji()
    ui.setupUi(lokacijeDetalji)
    lokacijeDetalji.show()
    sys.exit(app.exec_())
