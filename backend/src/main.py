from flask import Flask, render_template
from restapi.account_app import account_bp
#, project_app, story_app, sprint_app, task_app, project_group_app, authority_app, page_app

app = Flask(__name__, static_folder='../../frontend/dist/static', template_folder='../../frontend')
app.register_blueprint(account_bp)
#app.register_blueprint(project_app)
app.config['JSON_AS_ASCII'] = False

@app.route('/', defaults={'path': ''})
@app.route('/<path:path>')
def index(path):
    return render_template('index.html')

if __name__ == '__main__':
    app.run(debug=True)
