from reportlab.lib.pagesizes import landscape
from reportlab.lib.units import mm
from reportlab.pdfgen import canvas
from conexion import get_db_connection
from ticket.encabezado import encabezado, footer


def generate_pdf(fecha_inicio, fecha_fin ):

    cnx = get_db_connection()
    if cnx is None:
        print("Error al conectar con la base de datos.")
        return

    cursor = cnx.cursor()

    if fecha_inicio <= fecha_fin:
        query = "SELECT fecha, concepto, valor FROM gastos WHERE fecha BETWEEN %s AND %s"
        cursor.execute(query, (fecha_inicio, fecha_fin))

    else:
        query = "SELECT fecha, concepto, valor FROM gastos"
        cursor.execute(query)
        
    #* Crear un nuevo documento PDF
    c = canvas.Canvas("ticket24.pdf", pagesize=(98*mm, 210*mm))

    #* Ruta del logo de la empresa
    logo_path = "assets/iconos/ambienteslogo.png"  


    #* Agregar el encabezado al PDF
    encabezado(c, logo_path)

    #* Escribir los datos en el PDF
    y = 90*mm  # Posición inicial en el eje y
    total_valor = 0  # Variable para acumular la suma total de los valores

    # Obtener los datos y calcular el total
    rows = cursor.fetchall()
    espacio_lineas = 5
    # Escribir los datos en el PDF
    for row_data in rows:
        fecha, concepto, valor = row_data
        c.drawString(10 * mm, y, f"Fecha: {fecha}")
        y -= 5 * mm
        c.drawString(10 * mm, y, f"Concepto: {concepto}")
        y -= 5 * mm
        c.drawString(10 * mm, y, f"Valor: {valor:,.0f}")  # Formato con coma como separador de miles
        y -= 5 * mm
        total_valor += valor
        y -= 5 * mm  # Añadir un pequeño espacio entre registros
        if y < 20 * mm:  # Ajustar para evitar que el texto se salga de la página
            break
    
    # Dibujar una línea doble y punteada
    y -= -2 * mm
    c.setDash([2, 2], 0)  # Establecer un patrón de línea punteada
    c.line(3 * mm, y, 95 * mm, y)  # Línea superior
    c.line(3* mm, y - 2, 95 * mm, y - 2)  # Línea inferior
    
   # Agregar la suma total de los valores
    total_valor_str = f"${total_valor:,.0f}".replace(',', '.')  # Formato con punto como separador de miles
    y -= 10 * mm
    c.drawString(10 * mm, y, f"Total: {total_valor_str}")

    # Agregar el pie de página al PDF
    footer(c)

    
    c.save()  # Guardar el PDF
    cursor.close()
    cnx.close()

