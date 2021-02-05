from flask import Flask

app = Flask(__name__)

@app.route('/')
@app.route('/test/<user>')
def hello_world(user=None):
    app.render_template('./templates/base.html', user)

if __name__ == 'main':
    app.run()