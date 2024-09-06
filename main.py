from flask import Flask, request, jsonify
from flask_cors import CORS
from deepface import DeepFace
import os

app = Flask(__name__)
CORS(app)

# Ensure the upload folder exists
UPLOAD_FOLDER = 'uploads'
if not os.path.exists(UPLOAD_FOLDER):
    os.makedirs(UPLOAD_FOLDER)

@app.route('/upload', methods=['POST'])
def upload_file():
    if 'file' not in request.files:
        return jsonify({"error": "No file part"}), 400
    
    file = request.files['file']
    if file.filename == '':
        return jsonify({"error": "No selected file"}), 400
    
    file_path = os.path.join(UPLOAD_FOLDER, file.filename)
    file.save(file_path)
    
    # Analyze the image using DeepFace
    result = DeepFace.analyze(img_path=file_path, actions=['age', 'gender', 'race', 'emotion'])
    return jsonify(result)

if __name__ == '__main__':
    app.run(debug=True)
