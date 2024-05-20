from PySide6.QtWidgets import QApplication
from controllers.gastos_w import GastosWindow



if __name__== '__main__':
     app=QApplication()
     window= GastosWindow()
     window.show()
     app.exec() 
     