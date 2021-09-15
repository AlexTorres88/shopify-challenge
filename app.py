from flask import Flask, render_template, request
from werkzeug.utils import redirect, secure_filename
from config import *
import boto3

# App definition
app = Flask(__name__)

# Create connection to s3 bucket
s3_resource = boto3.resource('s3')

# Methods
def get_files():
    files=[]
    bucket = s3_resource.Bucket(BUCKET_NAME)
    for file in bucket.objects.all():
        files.append(file.key)
    return files

# Routes
@app.route('/')  
def home():
    files = get_files()
    return render_template("index.html", files=files)

@app.route('/upload',methods=['POST'])
def upload():
    if request.method == 'POST':
        img = request.files['file']
        if img:
                filename = secure_filename(img.filename)
                img.save(filename)
                s3_resource.Object(BUCKET_NAME, filename).upload_file(Filename=filename)
        else:
            return render_template('index.html', msg="No file provided", files=get_files())
    
    return redirect('/')

@app.route('/delete', methods=['POST'])
def delete():
    file = request.form.get("file")
    s3_resource.Object(BUCKET_NAME, file).delete()

    return redirect('/')

# Error hanlder
@app.errorhandler(404)
def page_not_found(e):
    return render_template('404.html', title="404"), 404

if __name__ == "__main__":
    app.run(debug=True)
