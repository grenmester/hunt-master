from flask import Flask, render_template, redirect
import json
app = Flask(__name__)

with open("modules.json", 'r') as fp:
    layout = json.load(fp)

@app.route('/')
def main():
    return redirect("start/", code=302)

@app.route('/start/')
def start():
    return render_template("start.html", start_link = layout["start"]["target"])

@app.route('/content/<module>/')
def get_content_module(module):
    return render_template("content.html",
            title = module,
            data = layout[module]["data"],
            target = layout[module]["target"])

@app.route('/end/')
def end():
    return render_template("end.html")

if __name__ == '__main__':
    app.run(debug=True)
