import sys
from PyQt5 import QtWidgets
from checkout import Ui_Dialog  # Import UI dari file Python hasil konversi

class CheckoutApp(QtWidgets.QDialog):
    def __init__(self):
        super().__init__()
        self.ui = Ui_Dialog()
        self.ui.setupUi(self)

if __name__ == "__main__":
    app = QtWidgets.QApplication(sys.argv)
    window = CheckoutApp()
    window.show()
    sys.exit(app.exec_())
