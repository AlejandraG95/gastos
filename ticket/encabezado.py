from reportlab.lib.units import mm
#from reportlab.pdfgen import canvas
#from reportlab.lib import pdfencrypt
from datetime import datetime
from PIL import Image

#* ENCABEZADO

def encabezado(c,logo_path, empresa='AMBIENTES SEGUROS SAS', nit = '901697756', ciudad='Cali - Valle del Cauca', movil='3001562169', correo='admin@ambientes-seguros.com'):
    
    # Preprocesar la imagen para manejar la transparencia
    logo_img = Image.open(logo_path)
    if logo_img.mode in ('RGBA', 'LA') or (logo_img.mode == 'P' and 'transparency' in logo_img.info):
        # Convertir imagen con transparencia a un fondo blanco
        background = Image.new('RGB', logo_img.size, (255, 255, 255))
        background.paste(logo_img, (0, 0), logo_img)
        logo_path = "processed_logo.png"
        background.save(logo_path)

    # Tamaño y posición del logo
    logo_w= 30 * mm
    logo_h = 30 * mm
    logo_x = (98 * mm - logo_w) / 2  # Centrar el logo horizontalmente
    logo_y = 175 * mm  # Ajustar la posición vertical del logo

    # Dibujar el logo
    c.drawImage(logo_path, logo_x, logo_y, width=logo_w, height=logo_h)


    # Obtener el ancho del texto
    empresa_w = c.stringWidth(empresa, "Helvetica", 12)
    nit_w = c.stringWidth(nit, "Helvetica", 12)
    ciudad_w = c.stringWidth(ciudad, "Helvetica", 12)
    movil_w = c.stringWidth(movil, "Helvetica", 12)
    correo_w= c.stringWidth(correo, "Helvetica", 12)

    # Obtener la fecha actual
    current_date = datetime.now().strftime("%d/%m/%Y")
    date_w = c.stringWidth(current_date, "Helvetica", 12)

    # Obtener el ancho de la página
    pagina_w = 98*mm

# Calcular la posición centrada
    empresa_x = (pagina_w - empresa_w) / 2
    nit_x = (pagina_w - nit_w) /2.3
    ciudad_x = (pagina_w - ciudad_w) / 2.8
    movil_x = (pagina_w - movil_w) / 2.45
    correo_x = (pagina_w - correo_w) / 3.6
    date_x = (pagina_w - date_w)/2.5


# Definir la separación vertical entre líneas
    espacio_lineas = 5

# Calcular las posiciones verticales
    empresa_y = 170*mm
    nit_y = empresa_y - espacio_lineas - 10
    ciudad_y = nit_y - espacio_lineas - 10
    movil_y = ciudad_y - espacio_lineas - 10
    correo_y = movil_y - espacio_lineas - 10
    date_y = correo_y - espacio_lineas-10

    # Agregar el encabezado al PDF con la información proporcionada
    c.drawString(empresa_x, empresa_y, empresa)
    c.drawString(nit_x, nit_y, f"NIT: {nit}")
    c.drawString(ciudad_x,ciudad_y,  f"Ciudad: {ciudad}")
    c.drawString(movil_x, movil_y, f"Móvil: {movil}")
    c.drawString(correo_x, correo_y, f"Correo: {correo}")
    c.drawString(date_x, date_y, f"Fecha: {current_date}")


#* PIE DE PAGINA

def footer(c, empresa='Ambientes Seguros S.A.S ©', parqueadero='Software: AS-Parking', pagina_web='www.ambientes-seguros.com'):
    
   # Obtener el año actual
    current_year = datetime.now().year
    empresa_text = f"{empresa} {current_year}"

    # Obtener el ancho del texto del pie de página
    empresa_w = c.stringWidth(empresa_text, "Helvetica", 10)
    parqueadero_w = c.stringWidth(parqueadero, "Helvetica", 10)
    pagina_web_w = c.stringWidth(pagina_web, "Helvetica", 10)

    pagina_w = 98*mm

    # Calcular la posición centrada del pie de página

    empresa_x = (pagina_w - empresa_w) / 2.6           
    parqueadero_x = (pagina_w - parqueadero_w) / 2.3
    pagina_web_x = (pagina_w - pagina_web_w) / 2.4

    # Posiciones verticales del pie de página
    footer_y = 10 * mm
    parqueadero_y = footer_y + 5 * mm
    empresa_y = parqueadero_y + 5 * mm

    # Agregar el pie de página al PDF
    c.drawString(empresa_x, empresa_y, empresa_text)
    c.drawString(parqueadero_x, parqueadero_y, parqueadero)
    c.drawString(pagina_web_x, footer_y, pagina_web)