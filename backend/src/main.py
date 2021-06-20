from flask import Flask, render_template
from api import api_bp
from restapi import AccountApi

app = Flask(__name__, static_folder='../../creist_vue_with_flask/dist/static', template_folder='../../creist_vue_with_flask/dist')
app.register_blueprint(api_bp)

@app.route('/', defaults={'path': ''})
@app.route('/<path:path>')
def index(path):
    return render_template('index.html')

@app.route('/account/get/<id>')
def getAccount(id):
    account_json = AccountApi.getById(id, 999)
    return account_json


if __name__ == '__main__':
    app.run()
