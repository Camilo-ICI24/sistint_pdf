import os
import json
from pdf_utils import extraer_texto, limpiar_texto, obtener_top_palabras
from ai_utils import analizar
from diagramavenn import generar_venn

def main():
    n_input = input("Ingrese la cantidad de palabras a buscar: ")
    try:
        n = int(n_input)
        if n <= 0:
            raise ValueError()
    except:
        print("Valor inválido. Usando N = 10 por defecto...")
        n = 10

    pdf1 = input("Ingrese la ruta del primer PDF: ")
    pdf2 = input("Ingrese la ruta del segundo PDF: ")

    if not os.path.exists(pdf1) or not os.path.exists(pdf2):
        print("Archivos no válidos. Hay PDFs que no existen")
        return

    print("Procesando PDFs. Por favor espere...")

    texto1 = extraer_texto(pdf1)
    texto2 = extraer_texto(pdf2)

    palabras1 = limpiar_texto(texto1)
    palabras2 = limpiar_texto(texto2)

    top1 = obtener_top_palabras(palabras1, 50)
    top2 = obtener_top_palabras(palabras2, 50)

    # IA o fallback
    resultado = analizar(top1, top2, n)

    print("\n===== RESULTADO FINAL =====")
    print(json.dumps(resultado, indent=2, ensure_ascii=False))

    generar_venn(resultado)


if __name__ == "__main__":
    main()