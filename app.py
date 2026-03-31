from flask import Flask, render_template, request, send_file
import PyPDF2
import os

app = Flask(__name__)

UPLOAD_FOLDER = 'uploads'
OUTPUT_FOLDER = 'outputs'

os.makedirs(UPLOAD_FOLDER, exist_ok=True)
os.makedirs(OUTPUT_FOLDER, exist_ok=True)

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/merge', methods=['POST'])
def merge_pdfs():
    files = request.files.getlist('pdfs')

    merger = PyPDF2.PdfMerger()

    for file in files:
        filepath = os.path.join(UPLOAD_FOLDER, file.filename)
        file.save(filepath)
        merger.append(filepath)

    output_path = os.path.join(OUTPUT_FOLDER, 'merged.pdf')
    merger.write(output_path)
    merger.close()

    return send_file(output_path, as_attachment=True)

if __name__ == '__main__':
    if __name__ == '__main__':
     app.run()