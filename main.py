from flask import Flask, redirect, render_template, url_for, request, flash, send_from_directory
import colorgram
import os
from werkzeug.utils import secure_filename


UPLOADS_FOLDER = 'static/image'
ALLOWED_EXTENSION = {'txt', 'pdf', 'png', 'jpg', 'jpeg', 'gif','heif', 'heic'}

app = Flask(__name__)
app.config['SECRET_KEY'] = 'hebh4brbfj4'
app.config['UPLOAD_FOLDER'] = UPLOADS_FOLDER


@app.route('/', methods=['POST', 'GET'])
def home():
    if request.method == 'POST':
        
        file = request.files['myImage']
        filename = secure_filename(file.filename)
        if file.filename == '':
            flash('No selected file')
            return redirect(request.url)
        
        
        else:
            
            file.save(os.path.join(os.path.abspath(os.path.dirname(__file__)),
                                   app.config['UPLOAD_FOLDER'], secure_filename(
                                       file.filename)
                                   )
                      )
            color = colorgram.extract(f'./static/image/{filename}', 6)
            context = {
                'image': f'/static/image/{filename}',
                'alt': filename,
                'colors': color,
            }
            return render_template('index.html', data=context)

    else:
        color = colorgram.extract('./static/image/tt.jpg', 20)
        context = {
            'image': '/static/image/tt.jpg',
            'colors': color,
            
            
        }
        return render_template('index.html', data=context)


if __name__ == '__main__':
    app.run(debug=True,)
