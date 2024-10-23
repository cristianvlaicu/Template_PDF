    # Vamos a crear un cuaderno pdf cón múltiples categrías o temas y varias páginas por tema.

from fpdf import FPDF

import pandas as pd

C = 100  # color.

    # Creamos instancia de pdf acudiendo al módulo FPDF. Y le damos formato: orientación Portrait, unidades en mm y formato A4.
pdf = FPDF(orientation="P", unit="mm", format="A4")
pdf.set_auto_page_break(auto=False, margin=0)

df = pd.read_csv("topics.csv", sep=',')

# con este bucle for creamos de manera repetida las páginas Principales pdf (donde pone el tema principal) con sus celdas y encabezados.
for index, row in df.iterrows():  # se pone iterrow para que recorra todas las filas al completo del archivo .csv.
    pdf.add_page()                # es la llamada a la instancia FPDF para crear una página en formato pdf.

    # Creamos la cabecera, título de la página:
    pdf.set_font(family="Times", style="B", size=24)                             # se ajusta el fromato del texto de las celdas (recuadros),
    pdf.set_text_color(254, 0, 0)                                        # y el color.
    pdf.cell(w=0, h=12, txt=f'{row['Order']}: {row["Topic"]}', align="C", ln=1)  # cremos la celda dónode se aloja la cabecera.
          # (w=ancho de la célula; h=altura; texto, alin=donde está el texto (izq, centro, der); ln=saltos de línea hasta la siguiente celda).

    # Creamos linea que subraya el título de cada página inicial de los temas.
    pdf.line(45,21,166,21)      # desde la posición en horizontal (x) 45 mm hasta los 200 mm (longitud horizontal de la raya). Y la altura (posición vertical y) es de 21 mm.
    pdf.set_draw_color(C, C, C)  # seleccionamos el color rgb de la guía.

    # bucle for para crear la líneas que hay en las páginas (iniciales de cada tema) que sirven como guía para escribir recto.
    for y in range(33, 275, 12):                   # desde la distancia de 33 mm, hata los 275 mm, dibujar una "raya" cada 12 mm.
        pdf.line(10, y, 200, y)            # desde la posición en horizontal (x) 10 mm hasta los 200 mm (longitud horizontal de la raya).
        pdf.set_draw_color(C, C, C)  # seleccionamos el color rgb de la guía.

    # Creamos el pié de página en las páginas principales de los temas.
    pdf.ln(265)                                       # dónde se crean los dos pie de página (tema y paginador)
    pdf.set_font(family="Times", style="I", size=8)   # formato del texto.
    pdf.set_text_color(C, C, C)         # color
    pdf.cell(w=0, h=10, txt=row["Topic"], align="L")  # ajustamos la celda con los parámetros que queremos.

    # añadimos nº de páginas con su estilo y color.
    pdf.set_font(family="Times", style="B", size=12)
    pdf.set_text_color(100, 100, 100)
    pdf.cell(w=0, h=10, txt=str(pdf.page_no()), align="R")

    for i in range(row["Pages"] - 1): # creamos bucle for con las páginas en blanco que hay para cada tema.
        pdf.add_page()

        # Creamos el pié de página para las págins vacías.
        pdf.ln(277)
        pdf.set_font(family="Times", style="I", size=8)
        pdf.set_text_color(C, C, C)
        pdf.cell(w=0, h=10, txt=row["Topic"], align="L")

        # añadimos nº de páginas con su estilo y color.
        pdf.set_font(family="Times", style="B", size=12)
        pdf.set_text_color(100, 100, 100)
        pdf.cell(w=0, h=10, txt=str(pdf.page_no()), align="R")

        # bucle for para crear la líneas que hay en las páginas que sirven como guía para escribir recto.
        for y in range(20, 275, 12):
            pdf.line(10, y, 200, y)
            pdf.set_draw_color(C, C, C)

pdf.output('template.pdf')