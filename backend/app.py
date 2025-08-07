from flask import Flask, request, send_file, jsonify
from PIL import Image
import io
from flask_cors import CORS

app = Flask(__name__)

CORS(app)

ALLOWED_EXTENSIONS = {'png', 'jpg', 'jpeg', 'gif', 'bmp'}

def allowed_file(filename):
    return '.' in filename and filename.rsplit('.', 1)[1].lower() in ALLOWED_EXTENSIONS

@app.route('/convert', methods=['POST'])
def convert_image():
    if 'image' not in request.files:
        return jsonify({"error": "No image uploaded"}), 400
    file = request.files['image']
    if file.filename == '':
        return jsonify({"error": "No selected file"}), 400
    if not allowed_file(file.filename):
        return jsonify({"error": "Unsupported file type"}), 400

    # Formato de conversão desejado (ex: 'png', 'jpeg', etc)
    target_format = request.form.get('format', '').lower()
    if target_format not in ALLOWED_EXTENSIONS:
        return jsonify({"error": "Unsupported target format"}), 400

    try:
        img = Image.open(file.stream)
        img_io = io.BytesIO()
        # Para jpeg, salvar como 'JPEG'
        save_format = 'JPEG' if target_format == 'jpg' else target_format.upper()
        img.save(img_io, save_format)
        img_io.seek(0)
        return send_file(img_io, mimetype=f'image/{target_format}', as_attachment=True,
                         download_name=f'converted.{target_format}')
    except Exception as e:
        return jsonify({"error": str(e)}), 500

if __name__ == '__main__':
    app.run(debug=True)
