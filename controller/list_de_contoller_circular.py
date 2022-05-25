from service.list_de_service_circular import ListDEcircular_service
from flask import Response, json, jsonify, Blueprint, request
from util.util_encoder import UtilEncoder

app_list_de_circular = Blueprint("app_list_de_circular", __name__)
list_de_service_circular = ListDEcircular_service()

@app_list_de_circular.route('/list_de_circular/all')
def get_all_students_de_circular():
    return Response(status=200,
                    response=json.dumps(list_de_service_circular.get_all_students_de_circular(),
                    cls=UtilEncoder), mimetype="application/json")

@app_list_de_circular.route('/list_de_circular', methods=['POST'])
def add_student_circular():
    try:
        data = request.json
        list_de_service_circular.add_student_de_circular(data)
        return Response(status=200,
                        response=json.dumps({"message": "Adicionado exitosamente"}),
                        mimetype="application/json")
    except Exception as error:
        return Response(status=409,
                        response=json.dumps({"message": str(error)}),
                        mimetype="application/json")

@app_list_de_circular.route('/list_de_circular/add_to_start', methods=['POST'])
def add_student_to_start_circular():
    try:
        data = request.json
        list_de_service_circular.add_student_to_start_de_circular(data)
        return Response(status=200,
                        response=json.dumps({"message": "Adicionado exitosamente"}),
                        mimetype="application/json")
    except Exception as error:
        return Response(status=409,
                        response=json.dumps({"message": str(error)}),
                        mimetype="application/json")

@app_list_de_circular.route('/list_de_circular/count')
def count():
    return Response(status=200,
                    response=json.dumps(list_de_service_circular.count_de_circular(),
                                        cls=UtilEncoder), mimetype="application/json")