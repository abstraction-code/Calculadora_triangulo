import sys
from PyQt5 import QtWidgets, uic

qtCreatorFile = "frmPrueba.ui"
Ui_MainWindow, QtBaseClass = uic.loadUiType(qtCreatorFile)

class Formulario(QtWidgets.QMainWindow):
    def __init__(self, parent = None):
        super(Formulario, self).__init__(parent)
        uic.loadUi("frmPrueba.ui", self)

        self.btnProcesar.clicked.connect(self.procesar)
        self.btnLimpiar.clicked.connect(self.limpiar)
        self.btnSalir.clicked.connect(self.salir)

        self.show()
    
    def procesar(self):
        self.lblTexto.setText("Mi nombre es Coty")

    def limpiar(self):
        self.lblTexto.setText("Pulsa nuevamente en procesar")

    def salir(self):
        self.close()

if __name__ == "__main__":
    app = QtWidgets.QApplication(sys.argv)
    window = Formulario()
    app.exec() 