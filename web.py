import os
import json
from flask import Flask, render_template, flash, request, redirect, url_for, send_from_directory
from werkzeug.utils import secure_filename
from testdata import TestData
from data import Data

UPLOAD_FOLDER = '/home/abhijitp/temp_files'
ALLOWED_EXTENSIONS = set(['png', 'jpg', 'jpeg', 'gif'])

app = Flask(__name__)
app.config['UPLOAD_FOLDER'] = UPLOAD_FOLDER


@app.route('/index')
def index():
    # td = TestData()
    # data = td.get()
    data = Data()
    data = request.args.get('data')
    print("#################")
    print(data)
    # messages = request.args['messages']
    # return render_template("index.html", data=json.loads(messages))
    return render_template("index.html", data=data)


def allowed_file(filename):
    return '.' in filename and \
           filename.rsplit('.', 1)[1].lower() in ALLOWED_EXTENSIONS


@app.route('/', methods=['GET', 'POST'])
@app.route('/upload', methods=['GET', 'POST'])
def upload_file():
    if request.method == 'POST':
        # check if the post request has the file part
        if 'file' not in request.files:
            flash('No file part')
            return redirect(request.url)
        file = request.files['file']
        # if user does not select file, browser also
        # submit an empty part without filename
        if file.filename == '':
            flash('No selected file')
            return redirect(request.url)
        if file and allowed_file(file.filename):
            filename = secure_filename(file.filename)
            file.save(os.path.join(app.config['UPLOAD_FOLDER'], filename))
            data = Data()
            # TODO Call the extract function and set result in response
            text = TestData.extract(filename)
            data.set('Filename', filename)
            data.set('Extracted text', text)
            # return redirect(url_for('uploaded_file', filename=filename))
            # messages = json.dumps(data)
            # return redirect(url_for('index', messages=messages))
            # return redirect(url_for('index', data=data))
            return render_template("index.html", data=data)
    return '''
        <!doctype html>
        <title>Upload Image</title>
        <h1>Upload an image</h1>
        <form method=post enctype=multipart/form-data>
          <input type=file name=file>
          <input type=submit value=Upload>
        </form>
        '''


@app.route('/uploads/<filename>')
def uploaded_file(filename):
    return send_from_directory(app.config['UPLOAD_FOLDER'], filename)


if __name__ == "__main__":
    app.run(debug=True)