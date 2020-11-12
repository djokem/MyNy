# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'firmaInfo.ui'
#
# Created by: PyQt5 UI code generator 5.13.0
#
# WARNING! All changes made in this file will be lost!


from PyQt5 import QtCore, QtGui, QtWidgets
from PyQt5.QtWidgets import QTableWidgetItem
import firmaXMLOperations as fXML
import dodaj_lokaciju_dialog as dld
import statusDialog
import izmeni_lokaciju_dialog as izmeniLokaciju

class Ui_MainWindow(object):

    def __init__(self):
        self.myForm = QtWidgets.QMainWindow()

    def setupUi(self):
        self.myForm.setObjectName("MainWindow")
        self.myForm.setFixedSize(800,500)
        self.centralwidget = QtWidgets.QWidget(self.myForm)
        self.centralwidget.setObjectName("centralwidget")
        self.verticalLayout_2 = QtWidgets.QVBoxLayout(self.centralwidget)
        self.verticalLayout_2.setContentsMargins(-1, -1, -1, 0)
        self.verticalLayout_2.setSpacing(0)
        self.verticalLayout_2.setObjectName("verticalLayout_2")
        self.frame = QtWidgets.QFrame(self.centralwidget)
        font = QtGui.QFont()
        font.setFamily("Calibri Light")
        font.setPointSize(14)
        self.frame.setFont(font)
        self.frame.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame.setObjectName("frame")
        self.gridLayout = QtWidgets.QGridLayout(self.frame)
        self.gridLayout.setObjectName("gridLayout")
        self.matbrLabel = QtWidgets.QLabel(self.frame)
        self.matbrLabel.setObjectName("matbrLabel")
        self.gridLayout.addWidget(self.matbrLabel, 2, 0, 1, 1)
        self.firmaLabel = QtWidgets.QLabel(self.frame)
        font = QtGui.QFont()
        font.setFamily("Calibri Light")
        font.setPointSize(14)
        self.firmaLabel.setFont(font)
        self.firmaLabel.setObjectName("firmaLabel")
        self.gridLayout.addWidget(self.firmaLabel, 0, 0, 1, 1)
        self.matbrTxt = QtWidgets.QLineEdit(self.frame)
        self.matbrTxt.setReadOnly(True)
        self.matbrTxt.setObjectName("matbrTxt")
        self.gridLayout.addWidget(self.matbrTxt, 2, 1, 1, 1)
        self.firmaTxt = QtWidgets.QLineEdit(self.frame)
        self.firmaTxt.setEnabled(True)
        self.firmaTxt.setReadOnly(True)
        self.firmaTxt.setObjectName("firmaTxt")
        self.gridLayout.addWidget(self.firmaTxt, 0, 1, 1, 1)
        self.verticalLayout_2.addWidget(self.frame)
        self.groupBox = QtWidgets.QGroupBox(self.centralwidget)
        font = QtGui.QFont()
        font.setFamily("Calibri Light")
        font.setPointSize(14)
        self.groupBox.setFont(font)
        self.groupBox.setObjectName("groupBox")
        self.horizontalLayout = QtWidgets.QHBoxLayout(self.groupBox)
        self.horizontalLayout.setContentsMargins(8, 8, 8, 0)
        self.horizontalLayout.setSpacing(0)
        self.horizontalLayout.setObjectName("horizontalLayout")
        self.addBtn = QtWidgets.QPushButton(self.groupBox)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.addBtn.sizePolicy().hasHeightForWidth())
        self.addBtn.setSizePolicy(sizePolicy)
        self.addBtn.setObjectName("addBtn")
        self.horizontalLayout.addWidget(self.addBtn)
        self.updateBtn = QtWidgets.QPushButton(self.groupBox)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.updateBtn.sizePolicy().hasHeightForWidth())
        self.updateBtn.setSizePolicy(sizePolicy)
        self.updateBtn.setObjectName("updateBtn")
        self.horizontalLayout.addWidget(self.updateBtn)

        self.updateBtn.clicked.connect(self.izmeniLokaciju)

        self.deleteBtn = QtWidgets.QPushButton(self.groupBox)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.deleteBtn.sizePolicy().hasHeightForWidth())
        self.deleteBtn.setSizePolicy(sizePolicy)
        self.deleteBtn.setObjectName("deleteBtn")

        self.deleteBtn.clicked.connect(self.obrisiLokaciju)

        self.horizontalLayout.addWidget(self.deleteBtn)
        self.verticalLayout_2.addWidget(self.groupBox)
        self.frame_2 = QtWidgets.QFrame(self.centralwidget)
        font = QtGui.QFont()
        font.setFamily("Calibri Light")
        font.setPointSize(12)
        self.frame_2.setFont(font)
        self.frame_2.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame_2.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame_2.setObjectName("frame_2")
        self.horizontalLayout_2 = QtWidgets.QHBoxLayout(self.frame_2)
        self.horizontalLayout_2.setObjectName("horizontalLayout_2")
        self.tableWidget = QtWidgets.QTableWidget(self.frame_2)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Expanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.tableWidget.sizePolicy().hasHeightForWidth())
        self.tableWidget.setSizePolicy(sizePolicy)
        self.tableWidget.setFrameShadow(QtWidgets.QFrame.Sunken)
        self.tableWidget.setSelectionMode(QtWidgets.QAbstractItemView.SingleSelection)
        self.tableWidget.setObjectName("tableWidget")

        self.setTableWidgetProperties()
        self.fillTableWidget()

        self.horizontalLayout_2.addWidget(self.tableWidget)
        self.verticalLayout_2.addWidget(self.frame_2)
        self.nazadBtn = QtWidgets.QPushButton(self.centralwidget)
        font = QtGui.QFont()
        font.setFamily("Calibri Light")
        font.setPointSize(14)
        self.nazadBtn.setFont(font)
        self.nazadBtn.setObjectName("nazadBtn")
        self.verticalLayout_2.addWidget(self.nazadBtn)

        self.nazadBtn.clicked.connect(self.nazadBtnClick)

        self.myForm.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(self.myForm)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 794, 21))
        self.menubar.setObjectName("menubar")
        self.myForm.setMenuBar(self.menubar)
        self.statusbar = QtWidgets.QStatusBar(self.myForm)
        self.statusbar.setObjectName("statusbar")
        self.myForm.setStatusBar(self.statusbar)

        font = QtGui.QFont()
        font.setFamily("Calibri Light")
        font.setPointSize(16)
        font.setBold(True)
        self.firmaTxt.setFont(font)
        self.matbrTxt.setFont(font)
        self.setFirmaAttributes()

        self.addBtn.clicked.connect(self.addLokacija_dialog)

        self.retranslateUi()
        QtCore.QMetaObject.connectSlotsByName(self.myForm)

    def retranslateUi(self):
        _translate = QtCore.QCoreApplication.translate
        self.myForm.setWindowTitle(_translate("MainWindow", "Informacije o firmi"))
        self.matbrLabel.setText(_translate("MainWindow", "Mat. br.:"))
        self.firmaLabel.setText(_translate("MainWindow", "Firma:"))
        self.matbrTxt.setPlaceholderText(_translate("MainWindow", "12312312312"))
        self.firmaTxt.setPlaceholderText(_translate("MainWindow", "Komapnija d.o.o"))
        self.groupBox.setTitle(_translate("MainWindow", "Lokacije"))
        self.addBtn.setText(_translate("MainWindow", "Dodaj lokaciju"))
        self.updateBtn.setText(_translate("MainWindow", "Izmeni lokaciju"))
        self.deleteBtn.setText(_translate("MainWindow", "Obrisi lokaciju"))
        self.nazadBtn.setText(_translate("MainWindow", "Nazad"))

    def nazadBtnClick(self):
        self.myForm.hide()

    def setFirmaAttributes(self):
        self.firmaTxt.setText(fXML.getNazivFirma())
        self.matbrTxt.setText(fXML.getMatBr())

    def setTableWidgetProperties(self):
        self.firmaTxt.setText(fXML.getNazivFirma())
        self.matbrTxt.setText(fXML.getMatBr())
        self.lokacije = fXML.Lokacija.sve_lokacije()
        self.tableWidget.setRowCount(len(self.lokacije))
        self.tableWidget.setColumnCount(4)
        self.tableWidget.setUpdatesEnabled(True)
        self.tableWidget.setEditTriggers(QtWidgets.QAbstractItemView.NoEditTriggers)
        self.tableWidget.setColumnWidth(0, 0)
        self.tableWidget.setColumnWidth(1, 200)
        self.tableWidget.setColumnWidth(2, 150)
        self.tableWidget.setColumnWidth(3, 300)

        self.tableWidget.horizontalHeader().setStretchLastSection(True)
        self.tableWidget.setSelectionBehavior(QtWidgets.QAbstractItemView.SelectRows)

        font = QtGui.QFont()
        font.setFamily("Calibri Light")
        font.setPointSize(13)
        font.setBold(True)

        cid = QTableWidgetItem("Id")
        cid.setFont(font)

        cnaziv = QTableWidgetItem("Naziv")
        cnaziv.setFont(font)

        cmesto = QTableWidgetItem("Mesto")
        cmesto.setFont(font)

        cadresa = QTableWidgetItem("Adresa")
        cadresa.setFont(font)

        self.tableWidget.setHorizontalHeaderItem(0, cid)
        self.tableWidget.setHorizontalHeaderItem(1, cnaziv)
        self.tableWidget.setHorizontalHeaderItem(2, cmesto)
        self.tableWidget.setHorizontalHeaderItem(3, cadresa)

    def fillTableWidget(self):
        self.tableWidget.clearContents()
        self.lokacije.clear()
        self.lokacije = fXML.Lokacija.sve_lokacije()
        font = QtGui.QFont()
        font.setFamily("Calibri Light")
        font.setPointSize(11)
        font.setBold(False)
        for i in range(len(self.lokacije)):
            naziv = QTableWidgetItem(self.lokacije[i].naziv)
            naziv.setFont(font)
            mesto = QTableWidgetItem(self.lokacije[i].mesto)
            mesto.setFont(font)
            adresa = QTableWidgetItem(self.lokacije[i].adresa)
            adresa.setFont(font)

            self.tableWidget.setItem(i, 0, QTableWidgetItem(self.lokacije[i].id))
            self.tableWidget.setItem(i, 1, naziv)
            self.tableWidget.setItem(i, 2, mesto)
            self.tableWidget.setItem(i, 3, adresa)

        self.tableWidget.setColumnWidth(0, 0)
        self.tableWidget.hideColumn(0)

    def addLokacija_dialog(self):
        dialog = QtWidgets.QDialog()
        dialog.ui = dld.Ui_lokacijeDetalji()
        dialog.ui.setupUi(dialog)

        if dialog.exec_() == QtWidgets.QDialog.Accepted:
            fXML.Lokacija(dialog.ui.nazivTxt.text(), dialog.ui.mestoTxt.text(), dialog.ui.adresaTxt.text())
            self.fillTableWidget()
            self.tableWidget.update()

    def obrisiLokaciju(self):
        if len(self.tableWidget.selectedItems()) < 1:
            dialog = QtWidgets.QDialog()
            dialog.ui = statusDialog.Ui_Dialog()
            dialog.ui.setupUi(dialog)
            dialog.ui.statusLabel.setText("Niste izabrali ni jednu lokaciju!")
            dialog.exec_()
            return

        dialog = QtWidgets.QDialog()
        dialog.ui = statusDialog.Ui_Dialog()
        dialog.ui.setupUi(dialog)
        dialog.ui.statusLabel.setText("Da li ste sigurni?")

        if dialog.exec_() == QtWidgets.QDialog.Accepted:
            self.tableWidget.showColumn(0)
            result = fXML.Lokacija.obrisi_lokaciju(self.tableWidget.selectedItems()[0].text())
            self.tableWidget.hideColumn(0)
            dialog = QtWidgets.QDialog()
            dialog.ui = statusDialog.Ui_Dialog()
            dialog.ui.setupUi(dialog)
            dialog.ui.statusLabel.setText("Uspesno ste izbrisali lokaciju") if result else dialog.ui.statusLabel.setText("Lokacija nije izbrisana!")
            dialog.exec_()
            self.fillTableWidget()
            self.tableWidget.update()


    def izmeniLokaciju(self):

        if len(self.tableWidget.selectedItems()) < 1:
            dialog = QtWidgets.QDialog()
            dialog.ui = statusDialog.Ui_Dialog()
            dialog.ui.setupUi(dialog)
            dialog.ui.statusLabel.setText("Niste izabrali ni jednu lokaciju!")
            dialog.exec_()
        else:
            dialog = QtWidgets.QDialog()
            dialog.ui = izmeniLokaciju.Ui_lokacijeDetalji()
            dialog.ui.setupUi(dialog)

            dialog.ui.nazivUpTxt.setText(self.tableWidget.selectedItems()[0].text())
            dialog.ui.mestoUpTxt.setText(self.tableWidget.selectedItems()[1].text())
            dialog.ui.adresaUpTxt.setText(self.tableWidget.selectedItems()[2].text())

            if dialog.exec_() == QtWidgets.QDialog.Accepted:
                a = dialog.ui.nazivUpTxt.text() == self.tableWidget.selectedItems()[0].text()
                b = dialog.ui.mestoUpTxt.text() == self.tableWidget.selectedItems()[1].text()
                c = dialog.ui.adresaUpTxt.text() == self.tableWidget.selectedItems()[2].text()
                if not a or not b or not c:
                    lok = fXML.Lokacija()
                    self.tableWidget.showColumn(0)
                    lok.id = self.tableWidget.selectedItems()[0].text()
                    self.tableWidget.hideColumn(0)
                    lok.naziv = dialog.ui.nazivUpTxt.text()
                    lok.mesto = dialog.ui.mestoUpTxt.text()
                    lok.adresa = dialog.ui.adresaUpTxt.text()
                    result = fXML.Lokacija.izmeni_lokaciju(lok)
                    dialog1 = QtWidgets.QDialog()
                    dialog1.ui = statusDialog.Ui_Dialog()
                    dialog1.ui.setupUi(dialog1)
                    dialog1.ui.statusLabel.setText("Uspesno ste izmenili lokaciju") if result else dialog.ui.statusLabel.setText("Lokacija nije izmenjena jer ne postoji!")
                    dialog1.exec_()
                    self.fillTableWidget()
                    self.tableWidget.update()


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    MainWindow = QtWidgets.QMainWindow()
    ui = Ui_MainWindow()
    ui.setupUi()
    ui.myForm.show()
    sys.exit(app.exec_())
