import streamlit as st
import pymupdf
import difflib

st.set_page_config(layout="wide")

# Función para extraer texto de un archivo PDF
def extract_text_from_pdf(pdf_file):
    doc = pymupdf.open(stream=pdf_file.read(), filetype="pdf")
    text = ""
    
    for page_num in range(doc.page_count):
        page = doc.load_page(page_num)
        text += page.get_text("text")
    
    return text

# Función para comparar el texto de dos PDFs
def compare_texts(text1, text2):
    d = difflib.HtmlDiff()  # Generar diferencias en HTML
    diff_html = d.make_file(text1.splitlines(), text2.splitlines())
    return diff_html

# Título de la aplicación
st.title("Comparador de PDFs :memo:")

# Instrucciones
st.write("""
    Esta aplicación te permite comparar dos archivos PDF visualmente. 
    Sube los PDFs en los campos de la izquierda y derecha para ver las diferencias resaltadas.
""")

# Crear dos columnas para cargar los PDFs
col1, col2 = st.columns(2)

with col1:
    st.header("Archivo PDF 1")
    pdf1 = st.file_uploader("Sube el primer archivo PDF", type="pdf", key="pdf1")

with col2:
    st.header("Archivo PDF 2")
    pdf2 = st.file_uploader("Sube el segundo archivo PDF", type="pdf", key="pdf2")

# Verificar que ambos PDFs hayan sido cargados
if pdf1 and pdf2:
    # Crear dos columnas para mostrar los textos
    col1, col2 = st.columns(2)

    with st.spinner("Extrayendo texto de los PDFs..."):
        text1 = extract_text_from_pdf(pdf1)
        text2 = extract_text_from_pdf(pdf2)

    with col1:
        st.subheader("Texto extraído del PDF 1")
        st.text_area("Texto del primer archivo PDF", text1, height=300)

    with col2:
        st.subheader("Texto extraído del PDF 2")
        st.text_area("Texto del segundo archivo PDF", text2, height=300)

    # Comparar y mostrar las diferencias
    with st.spinner("Comparando los archivos PDF..."):
        diff_html = compare_texts(text1, text2)

    st.markdown("### Diferencias entre los archivos PDF:")
    st.components.v1.html(diff_html, height=700, scrolling=True)

else:
    st.info("Por favor, sube dos archivos PDF para realizar la comparación.")
