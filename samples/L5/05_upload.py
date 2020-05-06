from flask import Flask, render_template, request, redirect, url_for, flash, send_from_directory
from flask_bootstrap import Bootstrap
import os
from werkzeug.utils import secure_filename


ALLOWED_EXTENSIONS = {'txt', 'pdf', 'png', 'jpg', 'jpeg', 'gif'}

app = Flask(__name__)
app.config['UPLOAD_FOLDER'] = './upload'
app.config['SECRET_KEY'] = 'the random string'
Bootstrap(app)

def allowed_file(filename):
    return '.' in filename and filename.rsplit('.', 1)[1].lower() in ALLOWED_EXTENSIONS
    
@app.route('/', methods=['GET', 'POST'])
def upload_file():
    if request.method == 'POST':
        if 'file' not in request.files:
            flash('No file part', 'danger')
            return redirect(request.url)
            
        file = request.files['file']
        if file.filename == '':
            flash('No selected file', 'danger')
            return redirect(request.url)
            
        if not allowed_file(file.filename):
            flash('Invalid file extension', 'danger')
            return redirect(request.url)
            
        if file and allowed_file(file.filename):
            filename = secure_filename(file.filename)
            file.save(os.path.join(app.config['UPLOAD_FOLDER'], filename))
            
            flash('Successfully saved', 'success')
            return redirect(url_for('uploaded_file', filename=filename))
        
            
    return render_template("form.html")
    
       
@app.route('/uploads/<filename>')
def uploaded_file(filename):
    return send_from_directory(app.config['UPLOAD_FOLDER'], filename)
    

if __name__ == "__main__":
    app.run(host='localhost', port=5000, debug=True)