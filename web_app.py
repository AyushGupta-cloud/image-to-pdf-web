from flask import Flask, render_template, request, send_file
from PIL import Image
import os
import uuid

app = Flask(__name__)

UPLOAD_FOLDER = "uploads"
OUTPUT_FOLDER = "outputs"

os.makedirs(UPLOAD_FOLDER, exist_ok=True)
os.makedirs(OUTPUT_FOLDER, exist_ok=True)

@app.route("/")
def home():
    return render_template("index.html")

@app.route("/convert", methods=["POST"])
def convert():
    files = request.files.getlist("images")

    image_paths = []

    unique_id = str(uuid.uuid4())
    output_path = os.path.join(OUTPUT_FOLDER, f"{unique_id}.pdf")

    for file in files:
        path = os.path.join(UPLOAD_FOLDER, file.filename)
        file.save(path)
        image_paths.append(path)

    images = [Image.open(p).convert("RGB") for p in image_paths]

    images[0].save(output_path, save_all=True, append_images=images[1:])

    return send_file(output_path, as_attachment=True)

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=10000)