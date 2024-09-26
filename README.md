# RemoveBG

RemoveBG es una herramienta para eliminar el fondo de imágenes utilizando la biblioteca 'rembg'.

## Tabla de Contenidos

- [RemoveBG](#removebg)
  - [Tabla de Contenidos](#tabla-de-contenidos)
  - [Descripción](#descripción)
  - [Tecnologías Utilizadas](#tecnologías-utilizadas)
  - [Instalación](#instalación)
  - [Uso](#uso)
    - [Subir una Imagen](#subir-una-imagen)
    - [Enviar una Imagen en Base64](#enviar-una-imagen-en-base64)
  - [Estructura del Proyecto](#estructura-del-proyecto)
  - [Contribuir](#contribuir)
  - [Licencia](#licencia)

## Descripción

RemoveBG permite a los usuarios eliminar el fondo de imágenes PNG y JPG. La aplicación web proporciona una interfaz simple donde los usuarios pueden subir una imagen y ver el resultado procesado con el fondo eliminado. También soporta la recepción y devolución de imágenes en formato Base64.

## Tecnologías Utilizadas

- Python
- Flask
- rembg
- Pillow (PIL)
- HTML/CSS (para las plantillas)

## Instalación

Para instalar las dependencias necesarias, asegúrate de tener 'pip' instalado y ejecuta el siguiente comando:
```
pip install -r requirements.txt
```

Asegúrate de que el archivo 'requirements.txt' contenga las siguientes líneas:

'Flask'
'rembg'
'Pillow'

## Uso

Para usar la herramienta, simplemente ejecuta el script 'main.py' con Python:
```
python main.py
```

Luego, abre tu navegador web y navega a 'http://127.0.0.1:5000/' para acceder a la aplicación.

### Subir una Imagen

1. Navega a la página principal.
2. Sube una imagen en formato PNG o JPG.
3. La imagen procesada se mostrará con el fondo eliminado.

### Enviar una Imagen en Base64

Puedes enviar una imagen en formato Base64 a la ruta '/upload_base64' mediante una solicitud POST. La imagen procesada se devolverá en formato Base64.

Ejemplo de solicitud JSON para '/upload_base64':

'{
    "image_base64": "data:image/png;base64,iVBORw0KGgoAAAANSUhEUgAA..."
}'

## Estructura del Proyecto

La estructura del proyecto es la siguiente:
```
BackgrounSignature/
│
├── static/
│   ├── results/
│   ├── process/
│   └── (otros archivos estáticos como CSS, JS, etc.)
│
├── templates/
│   ├── index.html
│   └── result.html
│
├── main.py
├── README.md
└── requirements.txt
```

- 'static/': Contiene archivos estáticos como imágenes procesadas, CSS, y JS.
- 'templates/': Contiene las plantillas HTML para la aplicación.
- 'main.py': El archivo principal de la aplicación Flask.
- 'README.md': Este archivo.
- 'requirements.txt': Lista de dependencias del proyecto.

## Contribuir

Si deseas contribuir a este proyecto, por favor sigue estos pasos:

1. Haz un fork del repositorio.
2. Crea una nueva rama ('git checkout -b feature/nueva-funcionalidad').
3. Realiza tus cambios y haz commit ('git commit -am 'Añadir nueva funcionalidad'').
4. Haz push a la rama ('git push origin feature/nueva-funcionalidad').
5. Abre un Pull Request.

## Licencia

Este proyecto está licenciado bajo la Licencia MIT. Consulta el archivo LICENSE para más detalles.