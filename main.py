from flask import Flask, render_template, request, redirect, url_for, send_from_directory
from werkzeug import secure_filename
import json, os
app = Flask(__name__)

with open('modules.json', 'r') as fp:
    layout = json.load(fp)

app.config['UPLOAD_FOLDER'] = 'uploads/'
app.config['ALLOWED_EXTENSIONS'] = set(['png', 'jpg', 'jpeg', 'gif'])

#### App Routes

@app.route('/')
def main():
    return redirect('content/start/', code=302)

@app.route('/content/<module>/')
def get_content_module(module):
    return render_template('content.html',
                           title = module,
                           data = layout[module]['data'],
                           target = layout[module]['target'])

@app.route('/find/<module>/')
def get_find_module(module):
    return render_template('find.html',
                           title = module,
                           data = layout[module]['data'],
                           target = layout[module]['target'])

@app.route('/gps/<module>/')
def get_gps_module(module):
    return render_template('gps.html',
                           title = module,
                           data = layout[module]['data'],
                           target = layout[module]['target'])

@app.route('/match/<module>/')
def get_match_module(module):
    return render_template('match.html',
                           title = module,
                           data = layout[module]['data'],
                           target = layout[module]['target'])

@app.route('/qr/<module>/')
def get_qr_module(module):
    return render_template('qr.html',
                           title = module,
                           data = layout[module]['data'],
                           target = layout[module]['target'])

@app.route('/end/')
def end():
    return render_template('end.html')

@app.errorhandler(404)
def not_found_error(error):
    return render_template('404.html'), 404

#### Other Functions

def allowed_file(filename):
    return '.' in filename and \
           filename.rsplit('.', 1)[1] in app.config['ALLOWED_EXTENSIONS']

@app.route('/upload/', methods=['POST'])
def upload():
    file = request.files['file']
    module = request.form['module']
    print(module)
    if file and allowed_file(file.filename):
        filename = secure_filename(file.filename)
        file.save(os.path.join(app.config['UPLOAD_FOLDER'], filename))
        return redirect(url_for('uploaded_file', filename = filename))

@app.route('/uploads/<filename>')
def uploaded_file(filename):
    return send_from_directory(app.config['UPLOAD_FOLDER'], filename)

if __name__ == '__main__':
    app.run(debug=True)
