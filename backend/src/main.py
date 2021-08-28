from flask import Flask, render_template
from restapi.account_app import account_bp
from restapi.project_app import project_bp
from restapi.story_app import story_bp
from restapi.sprint_app import sprint_bp
from restapi.task_app import task_bp
from restapi.task_status_app import task_status_bp
from restapi.project_group_app import project_group_bp
from restapi.authority_app import authority_bp
from restapi.page_app import page_bp

app = Flask(__name__, static_folder='../../frontend/dist/static', template_folder='../../frontend')
app.register_blueprint(account_bp)
app.register_blueprint(project_bp)
app.register_blueprint(story_bp)
app.register_blueprint(sprint_bp)
app.register_blueprint(task_bp)
app.register_blueprint(task_status_bp)
app.register_blueprint(project_group_bp)
app.register_blueprint(authority_bp)
app.register_blueprint(page_bp)
app.config['JSON_AS_ASCII'] = False

@app.route('/', defaults={'path': ''})
@app.route('/<path:path>')
def index(path):
    return render_template('index.html')

if __name__ == '__main__':
    app.run(debug=True)
