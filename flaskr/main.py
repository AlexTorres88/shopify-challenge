from flask import Blueprint, render_template, redirect, request
from flask_login import login_required, current_user
from werkzeug.utils import secure_filename
from aws_connection import s3_resource
from flaskr.methods import get_files, get_bucket_name

main = Blueprint('main', __name__)

# Routes
@main.route('/')  
@login_required
def home():
    bucket_name = get_bucket_name(current_user)
    files = get_files(bucket_name)
    return render_template("index.html", files=files)

@main.route('/download',methods=['POST'])
@login_required
def download():
    bucket_name = get_bucket_name(current_user)
    file = request.form.get("file")
    bucket = s3_resource.Bucket(bucket_name)
    bucket.download_file(file, file)

    return redirect('/')

@main.route('/upload',methods=['POST'])
@login_required
def upload():
    if request.method == 'POST':
        imgs = request.files.getlist('file')
        bucket = get_bucket_name(current_user)
        if imgs[0].filename != '':
            for img in imgs:
                filename = secure_filename(img.filename)
                img.save(filename)
                s3_resource.Object(bucket, filename).upload_file(Filename=filename)
        else:
            return render_template('index.html', msg="Please select a file to upload.", files=get_files())
    
    return redirect('/')

@main.route('/delete', methods=['POST'])
@login_required
def delete():
    file = request.form.get("file")
    s3_resource.Object(get_bucket_name(current_user), file).delete()

    return redirect('/')