from flask import Flask, render_template
app = Flask(__name__)


@app.route('/')
def index():
   return render_template('index.html')


@app.route(‘/ hello’)
def hello_world():
   return ‘hello world’


@app.route('/grid')
def getGrid():
    if request.method == 'GET':
        data = request.form
        print(data)
    return render_template('index.html')


if __name__ == '__main__':
    app.use_reloader = True
    app.run(debug = True)
