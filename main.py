from flask import Flask, request, render_template, redirect, url_for, flash
from werkzeug.utils import secure_filename
import os
import shutil
from rembg import remove
from PIL import Image
from datetime import datetime

app = Flask(__name__)
app.secret_key = "supersecretkey"

# Crear las carpetas static/results y static/process si no existen al iniciar la aplicación
if not os.path.exists("static/results"):
    os.makedirs("static/results")
if not os.path.exists("static/process"):
    os.makedirs("static/process")

@app.route("/")
def index():
    return render_template("index.html", title="Remover Fondo de Imágenes", message="Ingresa una imagen aquí y luego muestra el resultado.")

@app.route("/upload", methods=["POST"])
def upload_image():
    file = request.files["file"]
    
    # Validar el tipo de archivo
    if file.content_type not in ["image/png", "image/jpeg"]:
        flash("Solo se permiten archivos PNG y JPG", "danger")
        return redirect(url_for("index"))

    # Obtener la fecha y hora actual
    timestamp = datetime.now().strftime("%Y%m%d_%H%M%S")

    # Guardar la imagen original
    original_filename = f"original_{timestamp}_{secure_filename(file.filename)}"
    original_file_location = os.path.join("static", original_filename)
    file.save(original_file_location)

    # Procesar la imagen para remover el fondo
    input_image = Image.open(original_file_location)
    output_image = remove(input_image)

    # Convertir a modo RGB si es necesario
    if output_image.mode == 'RGBA':
        output_image = output_image.convert('RGBA')

    # Crear una imagen con fondo blanco
    white_background = Image.new("RGB", output_image.size, (255, 255, 255))
    white_background.paste(output_image, mask=output_image.split()[3])  # 3 is the alpha channel

    # Guardar la imagen procesada en las carpetas static/process y static/results
    processed_filename = f"processed_{timestamp}_{secure_filename(file.filename)}"
    processed_file_location_process = os.path.join("static/process", processed_filename)
    processed_file_location_results = os.path.join("static/results", processed_filename)
    white_background.save(processed_file_location_process)
    white_background.save(processed_file_location_results)

    return render_template("result.html", original_filename=original_filename, processed_filename=processed_filename)

if __name__ == "__main__":
    app.run(debug=True)