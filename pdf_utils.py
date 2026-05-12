import pdfplumber as pdfp
import re
from collections import Counter

stopwords = {
    "de", "la", "que", "el", "en", "y", "a", "los", "del",
    "se", "las", "por", "un", "para", "con", "no", "una",
    "su", "al", "lo", "como", "más", "pero", "sus",
    "le", "ya", "o", "este", "sí", "porque", "esta",
    "entre", "cuando", "muy", "sin", "sobre", "también",
    "me", "hasta", "hay", "donde", "quien", "desde"
}


def extraer_texto(pdf_path):
    texto = ""
    with pdfp.open(pdf_path) as pdf:
        for pagina in pdf.pages:
            texto += pagina.extract_text() or ""
    return texto

def limpiar_texto(texto):
    texto = texto.lower()
    texto = re.sub(r'[^a-záéíóúñ\s]', '', texto)
    palabras = texto.split()

    palabras = [p for p in palabras if p not in stopwords and len(p) > 2]

    return palabras


def obtener_top_palabras(palabras, limite=50):
    conteo = Counter(palabras)
    return conteo.most_common(limite)