from service.list_se_service import ListSEService
from flask import Response, json, jsonify, Blueprint, request
from util.util_encoder import UtilEncoder

app_list_se = Blueprint("app_list_se", __name__)

list_se_service = ListSEService()
@app_list_se.route('/list_se/all')
def get_all_students():
    return Response(status=200,
                    response=json.dumps(list_se_service.get_all_students(),
                    cls=UtilEncoder), mimetype="application/json")

# Agregar estudiante en Postman
@app_list_se.route('/list_se',methods=['POST'])
def save_student():
    try:
        data = request.json
        list_se_service.add_student(data)
        return Response(status=200,
                        response=json.dumps({"message": "Adicionado exitosamente"}),
                        mimetype="application/json")
    except Exception as error:
        return Response(status=409,
                        response=json.dumps({"message": str(error)}),
                        mimetype="application/json")

@app_list_se.route('/list_se/addtostart',methods=['POST'])
def save_student_to_start():
    try:
        data = request.json
        list_se_service.add_student_to_start(data)
        return Response(status=200,
                        response=json.dumps({"message": "Adicionado exitosamente"}),
                        mimetype="application/json")
    except Exception as error:
        return Response(status=409,
                        response=json.dumps({"message": str(error)}),
                        mimetype="application/json")

@app_list_se.route('/list_se/invertir')
def invert():
    return Response(status=200,
                    response=json.dumps(list_se_service.invert()),
                    mimetype="application/json")

@app_list_se.route('/list_se/invertir_cabeza_cola')
def head_finish():
    return Response(status=200,
                    response=json.dumps(list_se_service.head_finish()),
                    mimetype="application/json")

@app_list_se.route('/list_se/delete_by_data/<id>')
def delete_by_data(id):
    return Response(status=200,
                    response=json.dumps(list_se_service.delete_by_data(id)),
                    mimetype="application/json")

@app_list_se.route('/list_se/delete_by_position/<position>')
def delete_by_position(position):
    return Response(status=200,
                    response=json.dumps(list_se_service.delete_by_position(int(position))),
                    mimetype="application/json")

@app_list_se.route('/list_se/add_to_position/<position>', methods=["POST"])
def add_to_position(position):
    return Response(status=200,
                    responde=json.dumps(list_se_service.add_to_position(int(position), request.json)),
                    mimetype="application/json")
