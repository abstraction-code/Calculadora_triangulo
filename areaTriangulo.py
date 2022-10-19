import sys #Importar un modulo del sistema ejecuta el formulario
from PyQt5 import QtWidgets, uic #importa algunos metodos de los librerias

qtCreatorFile = "frmAreaTriangulo.ui" #Es una variable y asigna el archivo ruta
Ui_MainWindow, QtBaseClass = uic.loadUiType(qtCreatorFile) #Hace una lectura de la variable qtCreatorfile

class Formulario(QtWidgets.QMainWindow):  #Crea el formulario
    def __init__(self, parent = None):
        super(Formulario, self).__init__(parent)
        uic.loadUi("frmAreaTriangulo.ui", self)

        self.show() #Muestra el formulario
    
        self.btnCalcular.clicked.connect(self.calcular) #Se conectan los botones
        self.btnLimpiar.clicked.connect(self.limpiar)
        self.btnSalir.clicked.connect(self.salir)

    def calcular(self):
        
        #Entrada de datos
        base=int(self.txtBase.text())
        altura=int(self.txtAltura.text())

        #Proceso de datos
        area=(base*altura)/2

        #Salida de resultados
        self.txts.setText("El área del triangulo :\n")
        self.txts.append("El valor de la base es : " + str(base))
        self.txts.append("El valor de la altura es : " + str(altura))
        self.txts.append("El valor del area es : " + str(area))

    def limpiar(self):
        self.txtBase.clear() #Cualquiera de los dos sirve.
        self.txtAltura.setText("")
        self.txts.setText("")

    def salir(self):
        self.close()

if __name__ == "__main__":
    app = QtWidgets.QApplication(sys.argv)
    window = Formulario()
    app.exec() 