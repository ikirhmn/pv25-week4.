from PyQt5 import QtCore, QtGui, QtWidgets

class Ui_Dialog(object):
    def setupUi(self, Dialog):
        Dialog.setObjectName("Dialog")
        Dialog.resize(421, 435)
        
        self.label = QtWidgets.QLabel(Dialog)
        self.label.setGeometry(QtCore.QRect(150, 10, 121, 21))
        font = QtGui.QFont()
        font.setPointSize(11)
        font.setBold(True)
        font.setWeight(75)
        self.label.setFont(font)
        self.label.setAlignment(QtCore.Qt.AlignCenter)
        self.label.setObjectName("label")
        
        self.label_2 = QtWidgets.QLabel(Dialog)
        self.label_2.setGeometry(QtCore.QRect(10, 40, 47, 13))
        self.label_2.setObjectName("label_2")
        
        self.comboBox = QtWidgets.QComboBox(Dialog)
        self.comboBox.setGeometry(QtCore.QRect(10, 60, 401, 22))
        self.comboBox.setObjectName("comboBox")
        self.comboBox.addItem("Pilih Produk")
        self.comboBox.addItem("Bimoli 1L (Rp. 20.000)")
        self.comboBox.addItem("Indomie Ayam Bawang 1 pcs (Rp. 3.000)")
        self.comboBox.addItem("Indomie Rendang 1 pcs (Rp. 3.000)")
        self.comboBox.addItem("Beras Ramos 5kg (Rp. 75.000)")
        self.comboBox.addItem("Gula Pasir 1kg (Rp. 16.000)")
        self.comboBox.addItem("Garam Dapur 500g (Rp. 5.000)")
        self.comboBox.addItem("Tepung Terigu Segitiga 1kg (Rp. 14.000)")
        self.comboBox.addItem("Susu UHT Frisian Flag 1L (Rp. 22.000)")
        self.comboBox.addItem("Teh Botol Sosro 350ml (Rp. 4.500)")
        self.comboBox.addItem("Aqua 600ml (Rp. 3.500)")
        self.comboBox.addItem("Kopi Kapal Api 165g (Rp. 18.000)")
        self.comboBox.addItem("Beng-beng 1 pcs (Rp. 2.500)")
        self.comboBox.addItem("SilverQueen Almond 65g (Rp. 18.000)")
        self.comboBox.addItem("Chitato 120g (Rp. 15.000)")
        self.comboBox.addItem("Kacang Garuda 200g (Rp. 10.000)")
        self.comboBox.addItem("Sabun Lifebuoy 80g (Rp. 4.000)")
        self.comboBox.addItem("Shampoo Pantene 170ml (Rp. 25.000)")
        self.comboBox.addItem("Deterjen Rinso 1.8kg (Rp. 30.000)")

        
        self.spinBox = QtWidgets.QSpinBox(Dialog)
        self.spinBox.setGeometry(QtCore.QRect(10, 110, 401, 22))
        self.spinBox.setObjectName("spinBox")
        self.spinBox.setMinimum(1)
        
        self.label_3 = QtWidgets.QLabel(Dialog)
        self.label_3.setGeometry(QtCore.QRect(10, 90, 47, 13))
        self.label_3.setObjectName("label_3")
        
        self.label_4 = QtWidgets.QLabel(Dialog)
        self.label_4.setGeometry(QtCore.QRect(10, 140, 47, 13))
        self.label_4.setObjectName("label_4")
        
        self.spinBox_2 = QtWidgets.QSpinBox(Dialog)
        self.spinBox_2.setGeometry(QtCore.QRect(10, 160, 401, 22))
        self.spinBox_2.setObjectName("spinBox_2")
        self.spinBox_2.setMaximum(100)
        
        self.pushButton = QtWidgets.QPushButton(Dialog)
        self.pushButton.setGeometry(QtCore.QRect(10, 210, 191, 23))
        self.pushButton.setObjectName("pushButton")
        self.pushButton.clicked.connect(self.add_to_cart)
        
        self.pushButton_2 = QtWidgets.QPushButton(Dialog)
        self.pushButton_2.setGeometry(QtCore.QRect(220, 210, 191, 23))
        self.pushButton_2.setObjectName("pushButton_2")
        self.pushButton_2.clicked.connect(self.clear_cart)
        
        self.textBrowser = QtWidgets.QTextBrowser(Dialog)
        self.textBrowser.setGeometry(QtCore.QRect(10, 260, 401, 101))
        self.textBrowser.setObjectName("textBrowser")
        
        self.label_5 = QtWidgets.QLabel(Dialog)
        self.label_5.setGeometry(QtCore.QRect(10, 370, 200, 16))
        font.setPointSize(10)
        font.setBold(True)
        self.label_5.setFont(font)
        self.label_5.setObjectName("label_5")
        
        self.label_6 = QtWidgets.QLabel(Dialog)
        self.label_6.setGeometry(QtCore.QRect(90, 410, 241, 16))
        font.setPointSize(8)
        font.setBold(False)
        self.label_6.setFont(font)
        self.label_6.setAlignment(QtCore.Qt.AlignCenter)
        self.label_6.setObjectName("label_6")
        
        self.retranslateUi(Dialog)
        QtCore.QMetaObject.connectSlotsByName(Dialog)
        
        self.products = {
            "Bimoli 1L (Rp. 20.000)": 20000,
            "Indomie Ayam Bawang 1 pcs (Rp. 3.000)": 3000,
            "Indomie Rendang 1 pcs (Rp. 3.000)": 3000,
            "Beras Ramos 5kg (Rp. 75.000)": 75000,
            "Gula Pasir 1kg (Rp. 16.000)": 16000,
            "Garam Dapur 500g (Rp. 5.000)": 5000,
            "Tepung Terigu Segitiga 1kg (Rp. 14.000)": 14000,
            "Susu UHT Frisian Flag 1L (Rp. 22.000)": 22000,
            "Teh Botol Sosro 350ml (Rp. 4.500)": 4500,
            "Aqua 600ml (Rp. 3.500)": 3500,
            "Kopi Kapal Api 165g (Rp. 18.000)": 18000,
            "Beng-beng 1 pcs (Rp. 2.500)": 2500,
            "SilverQueen Almond 65g (Rp. 18.000)": 18000,
            "Chitato 120g (Rp. 15.000)": 15000,
            "Kacang Garuda 200g (Rp. 10.000)": 10000,
            "Sabun Lifebuoy 80g (Rp. 4.000)": 4000,
            "Shampoo Pantene 170ml (Rp. 25.000)": 25000,
            "Deterjen Rinso 1.8kg (Rp. 30.000)": 30000
        }

        self.total_price = 0

    def retranslateUi(self, Dialog):
        _translate = QtCore.QCoreApplication.translate
        Dialog.setWindowTitle(_translate("Dialog", "POS Application"))
        self.label.setText(_translate("Dialog", "POS Application"))
        self.label_2.setText(_translate("Dialog", "Product"))
        self.label_3.setText(_translate("Dialog", "Quantity"))
        self.label_4.setText(_translate("Dialog", "Discount (%)"))
        self.pushButton.setText(_translate("Dialog", "Add to Cart"))
        self.pushButton_2.setText(_translate("Dialog", "Clear"))
        self.label_5.setText(_translate("Dialog", "Total: Rp. 0"))
        self.label_6.setText(_translate("Dialog", "Rizki Rahman Maulana | F1D022093"))
    
    def add_to_cart(self):
        product_name = self.comboBox.currentText()
        quantity = self.spinBox.value()
        discount = self.spinBox_2.value()
        
        if product_name == "Pilih Produk":
            return
        
        price_per_item = self.products.get(product_name, 0)
        subtotal = price_per_item * quantity
        discount_amount = subtotal * (discount / 100)
        final_price = subtotal - discount_amount
        
        self.total_price += final_price
        
        self.textBrowser.append(f"{product_name} x{quantity} - Rp. {final_price:,.0f}")
        self.label_5.setText(f"Total: Rp. {self.total_price:,.0f}")
    
    def clear_cart(self):
        self.textBrowser.clear()
        self.total_price = 0
        self.label_5.setText("Total: Rp. 0")
        
if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    Dialog = QtWidgets.QDialog()
    ui = Ui_Dialog()
    ui.setupUi(Dialog)
    Dialog.show()
    sys.exit(app.exec_())
