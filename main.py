from flask import Flask, render_template, redirect
app = Flask(__name__)

@app.route('/')
def main():
    return redirect("content/start/", code=302)

@app.route('/content/start/')
def start():
    return render_template("index.html")

if __name__ == '__main__':
    app.run(debug=True)
