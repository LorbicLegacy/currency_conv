# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'gui.ui'
#
# Created by: PyQt5 UI code generator 5.12.2
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtGui, QtWidgets
import data_list as dl
import currency_conv_cli as cc
import forex_python
import requests

class Ui_MainWindow(object):

    from_code = ""
    to_code = ""
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(600, 480)
        MainWindow.setMinimumSize(QtCore.QSize(600, 480))
        MainWindow.setMaximumSize(QtCore.QSize(600, 480))
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.fromBox = QtWidgets.QComboBox(self.centralwidget)
        self.fromBox.setGeometry(QtCore.QRect(70, 120, 211, 41))
        font = QtGui.QFont()
        font.setFamily("Microsoft YaHei")
        font.setPointSize(9)
        font.setBold(True)
        font.setWeight(75)
        self.fromBox.setFont(font)
        self.fromBox.setObjectName("fromBox")
        self.fromBox.addItem("")
        self.fromBox.addItem("")
        self.fromBox.addItem("")
        self.fromBox.addItem("")
        self.fromBox.addItem("")
        self.fromBox.addItem("")
        self.fromBox.addItem("")
        self.fromBox.addItem("")
        self.fromBox.addItem("")
        self.fromBox.addItem("")
        self.fromBox.addItem("")
        self.fromBox.addItem("")
        self.fromBox.addItem("")
        self.fromBox.addItem("")
        self.fromBox.addItem("")
        self.fromBox.addItem("")
        self.fromBox.addItem("")
        self.fromBox.addItem("")
        self.fromBox.addItem("")
        self.fromBox.addItem("")
        self.fromBox.addItem("")
        self.fromBox.addItem("")
        self.fromBox.addItem("")
        self.fromBox.addItem("")
        self.fromBox.addItem("")
        self.fromBox.addItem("")
        self.fromBox.addItem("")
        self.fromBox.addItem("")
        self.fromBox.addItem("")
        self.fromBox.addItem("")
        self.fromBox.addItem("")
        self.fromBox.addItem("")
        self.fromBox.addItem("")
        self.toBox = QtWidgets.QComboBox(self.centralwidget)
        self.toBox.setGeometry(QtCore.QRect(320, 120, 201, 41))
        font = QtGui.QFont()
        font.setFamily("Microsoft YaHei")
        font.setPointSize(9)
        font.setBold(True)
        font.setWeight(75)
        self.toBox.setFont(font)
        self.toBox.setObjectName("toBox")
        self.toBox.addItem("")
        self.toBox.addItem("")
        self.toBox.addItem("")
        self.toBox.addItem("")
        self.toBox.addItem("")
        self.toBox.addItem("")
        self.toBox.addItem("")
        self.toBox.addItem("")
        self.toBox.addItem("")
        self.toBox.addItem("")
        self.toBox.addItem("")
        self.toBox.addItem("")
        self.toBox.addItem("")
        self.toBox.addItem("")
        self.toBox.addItem("")
        self.toBox.addItem("")
        self.toBox.addItem("")
        self.toBox.addItem("")
        self.toBox.addItem("")
        self.toBox.addItem("")
        self.toBox.addItem("")
        self.toBox.addItem("")
        self.toBox.addItem("")
        self.toBox.addItem("")
        self.toBox.addItem("")
        self.toBox.addItem("")
        self.toBox.addItem("")
        self.toBox.addItem("")
        self.toBox.addItem("")
        self.toBox.addItem("")
        self.toBox.addItem("")
        self.toBox.addItem("")
        self.toBox.addItem("")
        self.fromLabel = QtWidgets.QLabel(self.centralwidget)
        self.fromLabel.setGeometry(QtCore.QRect(130, 90, 81, 21))
        font = QtGui.QFont()
        font.setPointSize(15)
        self.fromLabel.setFont(font)
        self.fromLabel.setAlignment(QtCore.Qt.AlignCenter)
        self.fromLabel.setObjectName("fromLabel")
        self.toLabel = QtWidgets.QLabel(self.centralwidget)
        self.toLabel.setGeometry(QtCore.QRect(400, 90, 41, 21))
        font = QtGui.QFont()
        font.setPointSize(15)
        self.toLabel.setFont(font)
        self.toLabel.setAlignment(QtCore.Qt.AlignCenter)
        self.toLabel.setObjectName("toLabel")
        self.inputField = QtWidgets.QPlainTextEdit(self.centralwidget)
        self.inputField.setGeometry(QtCore.QRect(70, 200, 211, 71))
        font = QtGui.QFont()
        font.setPointSize(16)
        self.inputField.setFont(font)
        self.inputField.setFocusPolicy(QtCore.Qt.ClickFocus)
        self.inputField.setFrameShadow(QtWidgets.QFrame.Raised)
        self.inputField.setObjectName("inputField")
        self.outputField = QtWidgets.QLabel(self.centralwidget)
        self.outputField.setGeometry(QtCore.QRect(70, 310, 451, 81))
        font = QtGui.QFont()
        font.setPointSize(16)
        self.outputField.setFont(font)
        self.outputField.setFrameShape(QtWidgets.QFrame.Box)
        self.outputField.setText("")
        self.outputField.setAlignment(QtCore.Qt.AlignCenter)
        self.outputField.setObjectName("outputField")
        self.convertButton = QtWidgets.QPushButton(self.centralwidget)
        self.convertButton.setGeometry(QtCore.QRect(320, 200, 201, 71))
        font = QtGui.QFont()
        font.setFamily("Lobster Two")
        font.setPointSize(22)
        self.convertButton.setFont(font)
        self.convertButton.setObjectName("convertButton")
        self.titleName = QtWidgets.QLabel(self.centralwidget)
        self.titleName.setGeometry(QtCore.QRect(180, 20, 250, 40))
        font = QtGui.QFont()
        font.setFamily("Pricedown")
        font.setPointSize(36)
        self.titleName.setFont(font)
        self.titleName.setAlignment(QtCore.Qt.AlignCenter)
        self.titleName.setObjectName("titleName")

        MainWindow.setCentralWidget(self.centralwidget)


        self.menubar = QtWidgets.QMenuBar(MainWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 600, 21))
        self.menubar.setObjectName("menubar")
        MainWindow.setMenuBar(self.menubar)
        self.statusbar = QtWidgets.QStatusBar(MainWindow)
        self.statusbar.setObjectName("statusbar")
        MainWindow.setStatusBar(self.statusbar)

        ###################################
        ### main function actions here  ###
        self.toBox.currentIndexChanged.connect(self.get_data_toBox)
        self.fromBox.currentIndexChanged.connect(self.get_data_fromBox)
        self.convertButton.clicked.connect(self.convert_currency)





        ####################################
        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "CurrencyConv"))
        MainWindow.setWindowIcon(QtGui.QIcon('ccicon.png'))
        self.fromBox.setItemText(0, _translate("MainWindow", "Select Currency"))
        self.fromBox.setItemText(1, _translate("MainWindow", "AUD - Australian Dollar"))
        self.fromBox.setItemText(2, _translate("MainWindow", "BGN - Bulgarian Lev"))
        self.fromBox.setItemText(3, _translate("MainWindow", "BRL - Brazilian Real"))
        self.fromBox.setItemText(4, _translate("MainWindow", "CAD - Canadian Doller"))
        self.fromBox.setItemText(5, _translate("MainWindow", "CHF - Swiss Franc"))
        self.fromBox.setItemText(6, _translate("MainWindow", "CNY - Chinese Yuan"))
        self.fromBox.setItemText(7, _translate("MainWindow", "CZK - Czeck Koruna"))
        self.fromBox.setItemText(8, _translate("MainWindow", "DKK - Danish Krone"))
        self.fromBox.setItemText(9, _translate("MainWindow", "EUR - Europian Euro"))
        self.fromBox.setItemText(10, _translate("MainWindow", "GBP - British Pound"))
        self.fromBox.setItemText(11, _translate("MainWindow", "HKD - Honk Kong Doller"))
        self.fromBox.setItemText(12, _translate("MainWindow", "HRK - Croatian Kuna"))
        self.fromBox.setItemText(13, _translate("MainWindow", "HUF - Hungarian Forint"))
        self.fromBox.setItemText(14, _translate("MainWindow", "IDR - Indonesian Rupiah"))
        self.fromBox.setItemText(15, _translate("MainWindow", "ILS - Israeli New Sheqel"))
        self.fromBox.setItemText(16, _translate("MainWindow", "INR - Indian Rupee"))
        self.fromBox.setItemText(17, _translate("MainWindow", "ISK - Icelandic Krona"))
        self.fromBox.setItemText(18, _translate("MainWindow", "JPY - Japanese Yen"))
        self.fromBox.setItemText(19, _translate("MainWindow", "KRW - South Korean Won"))
        self.fromBox.setItemText(20, _translate("MainWindow", "MXN - Mexican Peso"))
        self.fromBox.setItemText(21, _translate("MainWindow", "MYR - Malasian Ringgit"))
        self.fromBox.setItemText(22, _translate("MainWindow", "NOK - Norwegian Krone"))
        self.fromBox.setItemText(23, _translate("MainWindow", "NZD - New Zealand Doller"))
        self.fromBox.setItemText(24, _translate("MainWindow", "PHP - Philippine Peso"))
        self.fromBox.setItemText(25, _translate("MainWindow", "PLN - Polish Zloty"))
        self.fromBox.setItemText(26, _translate("MainWindow", "RON - Romanian Leu"))
        self.fromBox.setItemText(27, _translate("MainWindow", "RUB - Russian Rubel"))
        self.fromBox.setItemText(28, _translate("MainWindow", "SEK - Swedish Krona "))
        self.fromBox.setItemText(29, _translate("MainWindow", "SGD - Singapore Doller"))
        self.fromBox.setItemText(30, _translate("MainWindow", "THB - Thai Baht"))
        self.fromBox.setItemText(31, _translate("MainWindow", "TRY - Turkish New Lira"))
        self.fromBox.setItemText(32, _translate("MainWindow", "USD - United States Doller"))
        self.fromBox.setItemText(33, _translate("MainWindow", "ZAR - South African Rand"))
        self.toBox.setItemText(0, _translate("MainWindow", "Select Currency"))
        self.toBox.setItemText(1, _translate("MainWindow", "AUD - Australian Dollar"))
        self.toBox.setItemText(2, _translate("MainWindow", "BGN - Bulgarian Lev"))
        self.toBox.setItemText(3, _translate("MainWindow", "BRL - Brazilian Real"))
        self.toBox.setItemText(4, _translate("MainWindow", "CAD - Canadian Doller"))
        self.toBox.setItemText(5, _translate("MainWindow", "CHF - Swiss Franc"))
        self.toBox.setItemText(6, _translate("MainWindow", "CNY - Chinese Yuan"))
        self.toBox.setItemText(7, _translate("MainWindow", "CZK - Czeck Koruna"))
        self.toBox.setItemText(8, _translate("MainWindow", "DKK - Danish Krone"))
        self.toBox.setItemText(9, _translate("MainWindow", "EUR - Europian Euro"))
        self.toBox.setItemText(10, _translate("MainWindow", "GBP - British Pound"))
        self.toBox.setItemText(11, _translate("MainWindow", "HKD - Honk Kong Doller"))
        self.toBox.setItemText(12, _translate("MainWindow", "HRK - Croatian Kuna"))
        self.toBox.setItemText(13, _translate("MainWindow", "HUF - Hungarian Forint"))
        self.toBox.setItemText(14, _translate("MainWindow", "IDR - Indonesian Rupiah"))
        self.toBox.setItemText(15, _translate("MainWindow", "ILS - Israeli New Sheqel"))
        self.toBox.setItemText(16, _translate("MainWindow", "INR - Indian Rupee"))
        self.toBox.setItemText(17, _translate("MainWindow", "ISK - Icelandic Krona"))
        self.toBox.setItemText(18, _translate("MainWindow", "JPY - Japanese Yen"))
        self.toBox.setItemText(19, _translate("MainWindow", "KRW - South Korean Won"))
        self.toBox.setItemText(20, _translate("MainWindow", "MXN - Mexican Peso"))
        self.toBox.setItemText(21, _translate("MainWindow", "MYR - Malasian Ringgit"))
        self.toBox.setItemText(22, _translate("MainWindow", "NOK - Norwegian Krone"))
        self.toBox.setItemText(23, _translate("MainWindow", "NZD - New Zealand Doller"))
        self.toBox.setItemText(24, _translate("MainWindow", "PHP - Philippine Peso"))
        self.toBox.setItemText(25, _translate("MainWindow", "PLN - Polish Zloty"))
        self.toBox.setItemText(26, _translate("MainWindow", "RON - Romanian Leu"))
        self.toBox.setItemText(27, _translate("MainWindow", "RUB - Russian Rubel"))
        self.toBox.setItemText(28, _translate("MainWindow", "SEK - Swedish Krona "))
        self.toBox.setItemText(29, _translate("MainWindow", "SGD - Singapore Doller"))
        self.toBox.setItemText(30, _translate("MainWindow", "THB - Thai Baht"))
        self.toBox.setItemText(31, _translate("MainWindow", "TRY - Turkish New Lira"))
        self.toBox.setItemText(32, _translate("MainWindow", "USD - United States Doller"))
        self.toBox.setItemText(33, _translate("MainWindow", "ZAR - South African Rand"))
        self.fromLabel.setText(_translate("MainWindow", "From"))
        self.toLabel.setText(_translate("MainWindow", "To"))
        self.inputField.setPlaceholderText(_translate("MainWindow", "Enter the value here"))
        self.convertButton.setText(_translate("MainWindow", "CONVERT"))
        self.titleName.setText(_translate("MainWindow", "Currency Conv"))

########### USER DEFINED FUNCTIONS ##############
    
    def get_data_fromBox(self,j):
        #for count in range(self.fromBox.count()):
         #   print(self.fromBox.itemText(count))
        print("Current index",j,"selection changed ",self.fromBox.currentText())
        self.from_code = dl.code_dict[str(j)]
  
    def get_data_toBox(self,i):
        #for count in range(self.toBox.count()):
            #print(self.toBox.itemText(count))
        print("Current index",i,"selection changed ",self.toBox.currentText())
        self.to_code = dl.code_dict[str(i)]

    def convert_currency(self):

        rate = 0
        value = 1
        try:
            value = self.inputField.toPlainText()
        except:
            value = 1
        value = float(value)
        print(value,type(value))
        print("Converting from",self.from_code,"to",self.to_code)

        try:
            rate = cc.currency_rate(self.from_code,self.to_code,value)
            print(cc.currency_rate(self.from_code,self.to_code,value))
            self.outputField.setText(str(rate))

        except forex_python.converter.RatesNotAvailableError:
            print("Select Currency and enter value")
            self.outputField.setText("Select Currency and enter value")

        except requests.exceptions.ConnectionError:
            print("Connection Failed")
            self.outputField.setText("Connection Failed")


        




if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    MainWindow = QtWidgets.QMainWindow()
    ui = Ui_MainWindow()
    ui.setupUi(MainWindow)
    MainWindow.show()
    sys.exit(app.exec_())
