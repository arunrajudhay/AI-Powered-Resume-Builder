from flask import Flask, render_template
app = Flask(__name__)

@app.route('/')
def home():
    return "hi"

@app.route('/arunraj/<user_name>')
def arun(user_name):
    return render_template('index.html', name=user_name)

if __name__ == '__main__':
    app.run(debug=True)