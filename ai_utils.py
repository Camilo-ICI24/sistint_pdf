import json
import re
from openai import OpenAI

def cargar_api_key():
    try:
        with open("openaiapikey.txt", "r") as f:
            return f.read().strip()
    except:
        return None


api_key = cargar_api_key()

cliente = OpenAI(api_key=api_key) if api_key else None

def analizar_con_ia(top1, top2, n):
    if not cliente:
        raise Exception("No hay API key")

    prompt = f"""
    Tengo frecuencias de palabras de dos documentos.
    
    Documento 1: {top1}
    Documento 2: {top2}

    Tareas:
    1. Elimina palabras irrelevantes
    2. Agrupa palabras similares
    3. Identifica el tema principal de cada documento
    4. Identifica el tema en común entre ambos documentos (si existe)

    Devuelve:

    - Top {n} palabras Documento 1 con frecuencia
    - Top {n} palabras Documento 2 con frecuencia
    - Top {n} palabras en común con frecuencia en cada documento

    Además agrega:

    - tema_pdf1: breve descripción del tema del documento 1
    - tema_pdf2: breve descripción del tema del documento 2
    - tema_comun: tema que conecta ambos documentos (si no existe, escribe "No hay tema común claro")

    Formato JSON:
    {{
        "pdf1": [{{"palabra": "...", "frecuencia": n}}],
        "pdf2": [{{"palabra": "...", "frecuencia": n}}],
        "comunes": [
            {{
                "palabra": "...",
                "frecuencia_doc1": n,
                "frecuencia_doc2": n,
                "total": n
            }}
        ],
        "tema_pdf1": "...",
        "tema_pdf2": "...",
        "tema_comun": "..."
    }}
    """

    response = cliente.responses.create(
        model="gpt-5-mini",
        input=prompt
    )

    texto = response.output[0].content[0].text

    json_str = re.search(r'\{.*\}', texto, re.DOTALL).group()
    return json.loads(json_str)

# Sin IA, solo intersección básica
def fallback_local(top1, top2, n):
    dict1 = dict(top1)
    dict2 = dict(top2)

    top_doc1 = [
        {"palabra": p, "frecuencia": f}
        for p, f in top1[:n]
    ]

    top_doc2 = [
        {"palabra": p, "frecuencia": f}
        for p, f in top2[:n]
    ]

    comunes = list(set(dict1.keys()) & set(dict2.keys()))

    comunes_ordenadas = sorted(
        comunes,
        key=lambda x: dict1.get(x, 0) + dict2.get(x, 0),
        reverse=True
    )[:n]

    comunes_resultado = [
        {
            "palabra": p,
            "frecuencia_doc1": dict1.get(p, 0),
            "frecuencia_doc2": dict2.get(p, 0),
            "total": dict1.get(p, 0) + dict2.get(p, 0)
        }
        for p in comunes_ordenadas
    ]

    return {
        "pdf1": top_doc1,
        "pdf2": top_doc2,
        "comunes": comunes_resultado
    }

def analizar(top1, top2, n):
    try:
        print("Usando IA...")
        return analizar_con_ia(top1, top2, n)
    except Exception as e:
        print(f"IA no disponible ({e}) → usando plan B: fallback")
        return fallback_local(top1, top2, n)