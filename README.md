# PDF Word-Analyzer

Lector de PDFs y analizador de las palabras más comunes entre dos textos y entre ellos.

---

## Tabla de Contenidos

* [Descripción](#descripción)
* [Características](#características)
* [Instalación](#instalación)
* [Uso](#uso)
* [Estructura del Proyecto](#estructura-del-proyecto)
* [Tecnologías](#tecnologías)
* [Configuración](#configuración)
* [Autores](#autores)

---

## Descripción

PDF Word-Analyzer es un programa en Python que recibe dos archivos PDF, sin importar su contenido ni temas tratados, para ser analizados de manera sintáctica mediante el uso de un agente de IA, extrayendo las palabras más populares entre un documento, otro y finalmente las que más aparecen en ambos archivos, para posteriormente ser representados de manera visual con un diagrama de Venn.

---

## Características

* Lectura y procesamiento de documentos
* Uso de agentes IA para análisis de texto
* Análisis de palabras más comunes y frecuencia
* Representación visual mediante diagramas de Venn

---

## Instalación

```bash
# Clonar el repositorio
git clone https://github.com/Camilo-ICI24/sistint_pdf.git

# Entrar al directorio
cd sistint_pdf

# Crear un ambiente virtual
python -m venv pdf
source pdf/bin/activate

# Instalar dependencias
pip install -r requirements.txt
```

---

## Uso

```bash
# Ejemplo de ejecución
python ianalysis.py
```

---

## Estructura del Proyecto

```
/sistint_pdf
│
├── ai_utils.py
├── diagramavenn.py
├── ianalysis.py
├── pdf_utils.py
├── openaiapikey.txt
├── requirements.txt
└── README.md
```

---

## Tecnologías utilizadas

* Python
* OpenAI API
* Matplotlib 
* Procesamiento de texto

---

## Configuración

Antes de ejecutar el código, es importante contar con una API key del agente de IA OpenAI con el objetivo de realizar el análisis de manera eficiente. Se recomienda almacenar esta llave en un archivo de texto llamado ```openaiapikey.txt``` para que el programa pueda leerlo y utilizarlo.

---

## Autores

* Camilo Cifuentes - Desarrollo principal y depuración

---