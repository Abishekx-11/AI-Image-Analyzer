from flask import Flask, render_template, url_for, request
from werkzeug.utils import secure_filename
import os
from dotenv import load_dotenv

load_dotenv()

app = Flask(__name__)


app.config['UPLOAD_FOLDER'] = 'uploads'

@app.route("/")
def home():
    return render_template("home.html")

@app.route("/upload", methods=['POST'])
def upload():
    if 'image' not in request.files:
        return "No Image"
    
    file = request.files['image']

    if file.filename == '':
        return "No Image selected"
    if file:
        filename = secure_filename(file.filename)
        filepath = os.path.join(app.config['UPLOAD_FOLDER'], filename)
        file.save(filepath)

        return f"Image uploaded successfully: {filename}"
    
    return "Upload failed"







if __name__ == "__main__":
    app.run(debug=True)



    
