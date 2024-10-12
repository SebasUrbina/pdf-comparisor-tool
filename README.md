
# Comparador de PDFs con Streamlit

Esta es una aplicación sencilla creada con **Streamlit** y **PyMuPDF** para comparar dos archivos PDF y visualizar las diferencias entre ellos, con una interfaz organizada en dos columnas para una experiencia de usuario optimizada.

## Características

- **Comparación lado a lado**: Carga dos archivos PDF y visualiza el texto de cada uno en columnas separadas.
- **Diferencias resaltadas**: Después de cargar los archivos, las diferencias entre ellos se muestran de manera destacada usando colores para indicar adiciones, eliminaciones o modificaciones.
- **Extracción automática de texto**: Utiliza PyMuPDF para extraer el texto de los archivos PDF.
- **Interfaz intuitiva**: La aplicación guía al usuario para cargar archivos y proporciona mensajes amigables cuando es necesario.

## Requisitos

- Python 3.7 o superior.
- Las siguientes librerías de Python:

  ```bash
  pip install streamlit pymupdf
  ```

## Cómo ejecutar la aplicación

1. Clona este repositorio o descarga los archivos.
   
2. Navega al directorio donde se encuentra el archivo principal de la aplicación (`app.py`).

3. Ejecuta el siguiente comando para iniciar la aplicación:

   ```bash
   streamlit run app.py
   ```

4. Esto abrirá una ventana en tu navegador donde podrás cargar los archivos PDF y ver sus diferencias.

## Uso de la aplicación

- **Paso 1**: Sube el primer archivo PDF en la columna izquierda.
- **Paso 2**: Sube el segundo archivo PDF en la columna derecha.
- **Paso 3**: La aplicación mostrará el texto de ambos PDFs lado a lado.
- **Paso 4**: Las diferencias entre los documentos aparecerán resaltadas al final de la página.