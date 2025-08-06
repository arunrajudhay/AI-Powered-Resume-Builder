from flask import Flask, render_template, request, redirect, url_for
from pymongo import MongoClient
import os

app = Flask(__name__)
app.config['UPLOAD_FOLDER'] = 'uploads'

# MongoDB connection
client = MongoClient("mongodb+srv://flaskuser:resumebuilder2025@resume-builder.kcv5vei.mongodb.net/?retryWrites=true&w=majority&appName=Resume-builder")
db = client["resume_app"]  # Database name
uploads_collection = db["uploads"]  # Collection name

@app.route('/')
def home():
    return render_template('index.html')

@app.route('/resume-options')
def resume_options():
    return render_template('resume-options.html')

@app.route('/upload-resume', methods=['GET'])
def upload_resume():
    return render_template('upload.html')

@app.route('/upload', methods=['POST'])
def upload():
    file = request.files.get('resume')
    if file:
        content = file.read()
        filename = file.filename
        size = len(content)

        # Save to MongoDB
        uploads_collection.insert_one({
            "filename": filename,
            "size": size,
            "content": content
        })

        print(f"Uploaded: {filename}, size: {size} bytes")
        return 'Upload processed and saved to MongoDB!'
    return 'No file uploaded!', 400

@app.route("/manual-resume", methods=["GET"])
def manual_resume():
    return render_template("manual-form.html", data={})

@app.route('/education-details')
def education_details():
    return render_template('edu-detail.html') 

@app.route('/experience')
def experience():
    return render_template('experience.html')

@app.route('/projects')
def projects():
    return render_template('projects.html')

@app.route('/select_template', methods=['GET', 'POST'])
def select_template():
    if request.method == 'POST':
        selected = request.form.get('selected_template')
        return redirect(url_for('preview_pdf', template=selected))
    return render_template('layouts.html')

@app.route('/preview_pdf')
def preview_pdf():
    template = request.args.get('template')
    return render_template('preview-pdf.html', template=template)

if __name__ == '__main__':
    app.run(debug=True)
