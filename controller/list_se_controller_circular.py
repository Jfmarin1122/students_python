from service.list_se_circular_service import ListSEcircular_service
from flask import Response, json, jsonify, Blueprint, request
from util.util_encoder import UtilEncoder

app_list_se_circular = Blueprint("app_list_se_circular", __name__)
list_se_circular_service = ListSEcircular_service()
@app_list_se_circular.route('/list_se_circular/all')
def get_all_students_circular():
    return Response(status=200,
                    response=json.dumps(list_se_circular_service.get_all_students_circular(),
                    cls=UtilEncoder), mimetype="application/json")

@app_list_se_circular.route('/list_se_circular', methods=['POST'])
def add_student_circular():
    try:
        data = request.json
        list_se_circular_service.add_student_circular(data)
        return Response(status=200,
                        response=json.dumps({"message": "Adicionado exitosamente"}),
                        mimetype="application/json")
    except Exception as error:
        return Response(status=409,
                        response=json.dumps({"message": str(error)}),
                        mimetype="application/json")

@app_list_se_circular.route('/list_se_circular/addtostart',methods=['POST'])
def add_student_to_start_circular():
    try:
        data = request.json
        list_se_circular_service.add_student_to_start_circular(data)
        return Response(status=200,
                        response=json.dumps({"message": "Adicionado exitosamente"}),
                        mimetype="application/json")
    except Exception as error:
        return Response(status=409,
                        response=json.dumps({"message": str(error)}),
                        mimetype="application/json")