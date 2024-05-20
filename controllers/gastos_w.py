import datetime
from conexion import get_db_connection
from PySide6.QtWidgets import QWidget,QTableWidgetItem, QApplication, QMainWindow
from views.gastos_final import Ui_Form
from ticket.imprimir import generate_pdf



class GastosWindow(QWidget, Ui_Form):
    def __init__(self):    
        super().__init__()
        self.setupUi(self)
        self.load_data()

        #TODO SIGNAL
    
        self.calcular_pushButton.clicked.connect(self.calcular)
        self.imprimir_pushButton.clicked.connect(self.imprimir)
        self.cancelar_pushButton.clicked.connect(self.cerrar_ventana)

        self.buscar_pushButton.clicked.connect(self.buscar)

    
    def load_data(self): 

        #? Conectar a la base de datos
        cnx = get_db_connection()
        if cnx is None:
            print("Error al conectar con la base de datos.")
            return
        cursor = cnx.cursor()
        query = "SELECT * FROM gastos"
        cursor.execute(query)

        # Depuración: imprimir los nombres de las columnas
        columns = [desc[0] for desc in cursor.description]
        self.registro_gastos_tableWidget.setColumnCount(len(columns))
        self.registro_gastos_tableWidget.setHorizontalHeaderLabels(columns)

        self.registro_gastos_tableWidget.setRowCount(0)
        for row_num, row_data in enumerate(cursor):
            self.registro_gastos_tableWidget.insertRow(row_num)
            for col_num, data in enumerate(row_data):
                self.registro_gastos_tableWidget.setItem(row_num, col_num, QTableWidgetItem(str(data)))

        cursor.close()
        cnx.close()        

    #def config_tabla(self):
     #   headers = ('id', 'fecha', 'cajero', 'concepto', 'valor', 'tipo', 'liquidacion')   
        # CREAMOS LAS CABECERAS (TÍTULOS)
      #  self.registro_gastos_tableWidget.setHorizontalHeaderLabels(headers)
       # self.registro_gastos_tableWidget.setRowCount(0)
    
    def buscar(self):
         
        cnx = get_db_connection()
        if cnx is None:
            print("Error al conectar con la base de datos.")
            return
        
        #*Rango de Fechas 
        fecha_inicio = self.fecha_i_dateEdit.date().toString("yyyy-MM-dd")
        fecha_fin = self.fecha_f_dateEdit.date().toString("yyyy-MM-dd")

        cursor = cnx.cursor()
        query = "SELECT * FROM gastos WHERE fecha BETWEEN %s AND %s"
        cursor.execute(query, (fecha_inicio, fecha_fin))

        # Limpiar la tabla antes de cargar los nuevos resultados
        self.registro_gastos_tableWidget.setRowCount(0)

        for row_num, row_data in enumerate(cursor):
            self.registro_gastos_tableWidget.insertRow(row_num)
            for col_num, data in enumerate(row_data):
                self.registro_gastos_tableWidget.setItem(row_num, col_num, QTableWidgetItem(str(data)))

        cursor.close()
        cnx.close()

    def calcular(self):
        
        cnx = get_db_connection()
        if cnx is None:
            print("Error al conectar con la base de datos.")
            return
        cursor = cnx.cursor()

        # Verificar si se ha seleccionado un rango de fechas
        fecha_inicio = self.fecha_i_dateEdit.date().toString("yyyy-MM-dd")
        fecha_fin = self.fecha_f_dateEdit.date().toString("yyyy-MM-dd")

        if fecha_inicio <= fecha_fin:
            query = "SELECT SUM(valor) FROM gastos WHERE fecha BETWEEN %s AND %s"
            cursor.execute(query, (fecha_inicio, fecha_fin))

        else:
            query = "SELECT SUM(valor) FROM gastos"
            cursor.execute(query)

        total = cursor.fetchone()[0]  #* Obtener el resultado de la suma

        # Convertir el total a una cadena y formatearla manualmente con el punto de miles
        formato_suma = "{:,.0f}".format(total)

        # Reemplazar la coma con el punto si es necesario
        formato_suma = formato_suma.replace(',', '.')

        # Agregar el signo de pesos colombiano
        formato_suma = f"${formato_suma}"

        # Mostrar el total en una casilla aparte
        self.resultado_label.setText(formato_suma)

        cursor.close()
        cnx.close()


    def imprimir(self):
       
        fecha_inicio = self.fecha_i_dateEdit.date().toString("yyyy-MM-dd")
        fecha_fin = self.fecha_f_dateEdit.date().toString("yyyy-MM-dd")
        generate_pdf(fecha_inicio, fecha_fin)

    def cerrar_ventana(self):
        self.close()
    
    