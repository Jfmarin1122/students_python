from flask import Flask, jsonify
from controller.student_controller import app_student
from controller.list_se_controller import app_list_se
from controller.list_se_controller_circular import app_list_se_circular
from controller.list_de_controller import app_list_de
from controller.list_de_contoller_circular import app_list_de_circular

app = Flask(__name__)
app.register_blueprint(app_student)
app.register_blueprint(app_list_se)
app.register_blueprint(app_list_se_circular)
app.register_blueprint(app_list_de)
app.register_blueprint(app_list_de_circular)

if __name__ == '__main__':
    app.run()
