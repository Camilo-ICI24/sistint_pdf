import matplotlib.pyplot as plt
from matplotlib_venn import venn2

def generar_venn(resultado):
    palabras1 = set([item["palabra"] for item in resultado["pdf1"]])
    palabras2 = set([item["palabra"] for item in resultado["pdf2"]])
    venn = venn2([palabras1, palabras2], set_labels=('Documento 1', 'Documento 2'))

    solo1 = palabras1 - palabras2
    solo2 = palabras2 - palabras1
    comunes = palabras1 & palabras2

    if venn.get_label_by_id('10'):
        venn.get_label_by_id('10').set_text("\n".join(solo1))

    if venn.get_label_by_id('01'):
        venn.get_label_by_id('01').set_text("\n".join(solo2))

    if venn.get_label_by_id('11'):
        venn.get_label_by_id('11').set_text("\n".join(comunes))

    plt.title("Diagrama de Venn - Palabras más frecuentes por PDF")
    plt.show()