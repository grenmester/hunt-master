from flask import Flask, render_template, request, redirect, url_for, send_from_directory
from werkzeug import secure_filename
import json, os
app = Flask(__name__)

with open('modules.json', 'r') as fp:
    layout = json.load(fp)

app.config['UPLOAD_FOLDER'] = 'uploads/'
app.config['ALLOWED_EXTENSIONS'] = set(['png', 'jpg', 'JPG', 'jpeg', 'gif'])
app.config['CACHE_TYPE'] = 'null'

#### App Routes

@app.route('/')
def main():
    return redirect('content/start/', code=302)

@app.route('/content/<module>/')
def get_content_module(module):
    return render_template('content.html',
                           title = module,
                           data = layout[module]['data'],
                           target = layout[module]['target'],
                           url = layout[module]['url'])

@app.route('/find/<module>/')
def get_find_module(module):
    return render_template('find.html',
                           title = module,
                           data = layout[module]['data'],
                           target = layout[module]['target'],
                           url = layout[module]['url'])

@app.route('/gps/<module>/')
def get_gps_module(module):
    return render_template('gps.html',
                           title = module,
                           data = layout[module]['data'],
                           target = layout[module]['target'],
                           url = layout[module]['url'])

@app.route('/match/<module>/')
def get_match_module(module):
    return render_template('match.html',
                           title = module,
                           data = layout[module]['data'],
                           target = layout[module]['target'],
                           url = layout[module]['url'])

@app.route('/qr/<module>/')
def get_qr_module(module):
    return render_template('qr.html',
                           title = module,
                           data = layout[module]['data'],
                           target = layout[module]['target'],
                           url = layout[module]['url'])

@app.route('/text/<module>/')
def get_text_module(module):
    return render_template('text.html',
                           title = module,
                           data = layout[module]['data'],
                           target = layout[module]['target'],
                           url = layout[module]['url'])

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

    if file and allowed_file(file.filename):
        filename = secure_filename(file.filename)
        filepath = os.path.join(app.config['UPLOAD_FOLDER'], filename)
        file.save(filepath)

        target = request.form['target']
        url = request.form['url']
        module_url = url.split('/')[-1]
        module_type = url.split('/')[-2]

        import image
        if module_type == "match":
            image_filename = request.form['image_filename'].strip('/')
            print(filepath, image_filename)
            if image.compare(filepath, image_filename):
                return redirect(target, code=302)
            else:
                return redirect(url, code=302)
        elif module_type == "find":
            object_name = request.form['object_name']
            print(object_name, type(object_name))
            if image.has_features(filepath, [object_name]):
                return redirect(target, code=302)
            else:
                return redirect(url, code=302)
        else:
            print(module_type)
            return 'Failed to upload'
    return 'Invalid filename'

@app.route('/uploads/<filename>')
def uploaded_file(filename):
    return send_from_directory(app.config['UPLOAD_FOLDER'], filename)

@app.route('/within/', methods=['POST'])
def within():
    x_coordinate = float(request.form['x_coordinate'])
    y_coordinate = float(request.form['y_coordinate'])
    latitude = float(request.form['latitude'])
    longitude = float(request.form['longitude'])
    target = request.form['target']
    url = request.form['url']

    import gps
    print(gps.distance_between((x_coordinate, y_coordinate), (latitude, longitude)))
    if gps.within_radius((x_coordinate, y_coordinate), (latitude, longitude), 20):
        return redirect(target, code=302)
    return redirect(url, code=302)

@app.route('/verify/', methods=['POST'])
def verify():
    text = request.form['text']
    correct_string = request.form['correct_string']
    target = request.form['target']
    url = request.form['url']
    if text == correct_string:
        return redirect(target, code=302)
    return redirect(url, code=302)

if __name__ == '__main__':
    app.run(debug=True)
