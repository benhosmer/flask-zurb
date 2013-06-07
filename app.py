from flask import Flask, render_template
app = Flask(__name__)

@app.route('/')
def hello_world(name='Ben\'s Site'):
    return render_template('index.html', name=name)

if __name__ == '__main__':
    app.run(debug=True)
