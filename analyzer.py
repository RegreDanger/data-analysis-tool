import os
from pathlib import Path
import pandas as pd
import matplotlib.pyplot as plt
from reportlab.lib.pagesizes import letter
from reportlab.pdfgen import canvas

# Variable global para detectar si se terminó de crear un archivo
created = False

# Función para generar estadísticas descriptivas y gráficos
def analyze_data(file_path):
    # Leer archivo CSV
    data = pd.read_csv(file_path)
    
    # Generar estadísticas descriptivas
    stats = data.describe()
    print("Estadísticas descriptivas:")
    print(stats)
    folder = "images-" + Path(file_path).stem
    os.mkdir(f"{folder}")
    
    # Crear gráfico de histograma de cada columna numérica
    for column in data.select_dtypes(include=['float64', 'int64']).columns:
        plt.hist(data[column].dropna(), bins=10, alpha=0.5)
        plt.title(f"Histograma de {column}")
        plt.xlabel(column)
        plt.ylabel("Frecuencia")
        plt.savefig(f"{folder}/{column}_hist.png")
        plt.clf()  # Limpia para el siguiente gráfico

    # Generar reporte en PDF
    generate_pdf(stats, folder)

def generate_pdf(stats, folder):
    global created
    pdf_file = "report.pdf"
    c = canvas.Canvas(pdf_file, pagesize=letter)
    c.drawString(100, 750, "Reporte de Análisis de Datos")
    
    text = c.beginText(100, 730)
    text.setFont("Helvetica", 10)
    for line in stats.to_string().split('\n'):
        text.textLine(line)
    c.drawText(text)
    
    c.showPage()
    c.save()
    print(f"Reporte guardado en {pdf_file}")
    print(f"Imágenes guardadas en: {folder}")
    created = True  # Cambia el valor de `created` a True una vez que se guarda el PDF

if __name__ == "__main__":
    while True:
        analyze_data(input("Ingrese la dirección del archivo: "))
        if created:
            while True:
                try:
                    nextFile = int(input("¿Desea crear otro PDF de otro archivo?\nEscriba 1 para continuar, y 0 para salir: "))
                    if nextFile in [0, 1]:
                        break
                    else:
                        print("Ingrese 1 para continuar o 0 para salir.")
                except ValueError:
                    print("Ingrese un valor válido (0 o 1).")
            if nextFile == 0:
                break
