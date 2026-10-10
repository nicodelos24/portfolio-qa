# Currículum definitivo

Versión elegida por Nicolás el 9 de octubre de 2026: el archivo local `CV-Nicolas-.pdf`, con la **primera foto mejorada** y tamaño de imagen de **3,6 × 3,6 cm**. Se conserva el PDF elegido sin regenerarlo ni cambiar su contenido; aquí usa el nombre estable del portafolio.

- [CV en PDF](CV-Nicolas-De-Los-Santos-QA.pdf): una página A4, listo para enviar.
- [Versión HTML](CV-Nicolas-De-Los-Santos-QA.html): diseño editable, con la fotografía incrustada.
- [Contenido en Markdown](../cv-qa.md): texto del currículum.
- [Foto elegida](foto-perfil.png): primera mejora de resolución, realizada con IA a partir de la imagen aportada por el autor.
- [Instrucción de edición](prompt-foto.txt): prompt de la herramienta integrada `image_gen`.

La foto no recibió el segundo retoque suave. El último cambio aprobado solo aumentó su tamaño de presentación de 3 a 3,6 cm. El texto del CV se mantiene igual al de las copias comparadas.

## Actualizar el CV

1. Actualizar el contenido en `../cv-qa.md` y en el HTML. El Markdown no regenera automáticamente el diseño.
2. Mantener la imagen incrustada para que el HTML sea independiente de rutas locales. Si se sustituye, actualizar también `foto-perfil.png` y registrar la decisión.
3. Exportar a PDF con LibreOffice, revisarlo visualmente y comprobar que conserva una página y todos los datos. Desde la raíz del repositorio:

```bash
libreoffice --headless --convert-to pdf --outdir cv cv/CV-Nicolas-De-Los-Santos-QA.html
python3 herramientas/verificar-portfolio.py
```

La exportación sustituye el PDF existente. Las fechas internas del PDF pueden cambiar al regenerarlo: comprobar el contenido y la presentación, no exigir el mismo hash para futuras ediciones.

## Identificación de la copia aprobada

SHA-256 del PDF elegido y copiado sin cambios:

```text
070eae114deb1492baa5668f5f470c4ba60f45ad9278f4a39897bdcf9d57e21c
```

Las variantes descartadas se retiraron de las carpetas de trabajo. Git conserva las versiones que ya habían sido publicadas; no se reescribe el historial.
