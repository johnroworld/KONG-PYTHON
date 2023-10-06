import flask
from flask import Flask, request, send_from_directory
from werkzeug.utils import secure_filename
import os

app = Flask(__name__)
app.config['UPLOAD_PATH'] = './uploads'

@app.route('/upload-service', methods=['POST'])

def upload_service():
    try:
        uploadedFile = request.files['input']
        fileName = secure_filename(uploadedFile.filename)

        if fileName == '':
            abort(400)

        uploadPath = os.path.join(app.config['UPLOAD_PATH'], fileName)
        uploadedFile.save(uploadPath)

        return "Successfully uploaded! Please see CDN URL: <a href='upload-service/{filename}'>{filename}</a>".format(uploadPath = uploadPath, filename = fileName)
    except Exception as e:
        return e

@app.route('/upload-service/<filename>', methods=['GET'])
def upload(filename):
    return send_from_directory(app.config['UPLOAD_PATH'], filename)

if __name__ == '__main__':
    app.run(host='0.0.0.0', port='5000')