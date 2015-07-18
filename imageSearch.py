import os
from flask import Flask, request, redirect, url_for, send_from_directory
from werkzeug import secure_filename
import urllib
import uuid
import crop_face
import query

query.loadModel()
#UPLOAD_FOLDER = 'input_images/'
ALLOWED_EXTENSIONS = set(['JPG', 'png', 'jpg', 'jpeg', 'gif'])

app = Flask(__name__)
#app.config['UPLOAD_FOLDER'] = UPLOAD_FOLDER

@app.route('/')
def hello():
 return 'Welcome'
    
@app.route('/down')
def down():
    link=request.args.get('url')
    urllib.urlretrieve(link, os.path.basename(link))
    crop_face.faceCrop(os.path.basename(link))
    fname,ext = os.path.splitext(os.path.basename(link))
    return query.queryModel(fname+'_cropped'+ext)
    #return "Image downloaded"
    
    
def allowed_file(filename):
    return '.' in filename and \
           filename.rsplit('.', 1)[1] in ALLOWED_EXTENSIONS

@app.route('/upload', methods=['GET', 'POST'])
def upload_file():
    if request.method == 'POST':
        file = request.files['file']
        if file and allowed_file(file.filename):
            filename = secure_filename(file.filename)
            file.save(filename)
            crop_face.faceCrop(filename)
            fname,ext = os.path.splitext(filename)
            return query.queryModel(fname+'_cropped'+ext)
            #return "File uploaded" #redirect(url_for('uploaded_file',
                                    #filename=filename))
    return '''
    <!doctype html>
    <title>Upload new File</title>
    <h1>Upload new File</h1>
    <form action="" method=post enctype=multipart/form-data>
      <p><input type=file name=file>
         <input type=submit value=Upload>
    </form>
    '''
@app.route('/show')#change these names
def show():
    return redirect("https://www.google.com") #redirect to linedin profiel url here
 
@app.route('/show/<filename>')
def uploaded_file(filename):
    return send_from_directory(filename)

app.run(host=os.environ['IP'],port=int(os.environ['PORT']))
