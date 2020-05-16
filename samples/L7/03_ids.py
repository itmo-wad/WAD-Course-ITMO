from flask import Flask, render_template, request, redirect, url_for, flash, send_from_directory
from flask_bootstrap import Bootstrap
import os


ALLOWED_EXTENSIONS = {'txt', 'pdf', 'png', 'jpg', 'jpeg', 'gif'}

app = Flask(__name__)
app.config['UPLOAD_FOLDER'] = './upload'
app.config['SECRET_KEY'] = 'the random string'
Bootstrap(app)

counter = 0

@app.route('/', methods=['GET', 'POST'])
def upload_file():
    global counter
    if request.method == 'POST':
        file = request.files["file"]
        counter += 1
        file.save(os.path.join(app.config['UPLOAD_FOLDER'], str(counter) + ".jpg"))
        flash('Successfully saved', 'success')
            
    return render_template("form.html")
    
       
@app.route('/uploads/<filename>')
def uploaded_file(filename):
    return send_from_directory(app.config['UPLOAD_FOLDER'], filename)
    

if __name__ == "__main__":
    app.run(host='localhost', port=5000, debug=True)