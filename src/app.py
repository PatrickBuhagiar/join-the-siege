from flask import Flask, request, jsonify

from src.services.document_classifier_service_config import get_document_classifier_service

app = Flask(__name__)

ALLOWED_EXTENSIONS = {'pdf', 'png', 'jpg'}


def allowed_file(filename):
    return '.' in filename and filename.rsplit('.', 1)[1].lower() in ALLOWED_EXTENSIONS


# Dependency injection
document_classifier_service = get_document_classifier_service()


@app.route('/classify_file', methods=['POST'])
def classify_file_route():
    if 'file' not in request.files:
        return jsonify({"error": "No file part in the request"}), 400

    file = request.files['file']
    if file.filename == '':
        return jsonify({"error": "No selected file"}), 400

    if not allowed_file(file.filename):
        return jsonify({"error": f"File type not allowed"}), 400

    try:
        label = document_classifier_service.classify(file)
        return jsonify({"file_class": label}), 200
    except ValueError as e:
        return jsonify({"error": str(e)}), 400
    except Exception as e:
        return jsonify({"error": str(e)}), 500


if __name__ == '__main__':
    app.run(debug=False)
