from service.list_de_service import ListDEservice
from flask import Response, json, jsonify, Blueprint, request
from util.util_encoder import UtilEncoder

app_list_de = Blueprint("app_list_de", __name__)

list_de_service = ListDEservice()
@app_list_de.route('/list_de/all')
def get_all_students():
    return Response(status=200,
                    response=json.dumps(list_de_service.get_all_students(),
                                        cls=UtilEncoder), mimetype="application/json")

@app_list_de.route('/list_de', methods=['POST'])
def add_student():
    try:
        data = request.json
        list_de_service.add_student(data)
        return Response(status=200,
                        response=json.dumps({"message": "Adicionado exitosamente"}),
                        mimetype="application/json")
    except Exception as error:
        return Response(status=409,
                        response=json.dumps({"message": str(error)}),
                        mimetype="application/json")

@app_list_de.route('/list_de/addtostart',methods=['POST'])
def add_to_start():
    try:
        data = request.json
        list_de_service.add_to_start(data)
        return Response(status=200,
                        response=json.dumps({"message": "Adicionado exitosamente"}),
                        mimetype="application/json")
    except Exception as error:
        return Response(status=409,
                        response=json.dumps({"message": str(error)}),
                        mimetype="application/json")

@app_list_de.route('/list_se_circular/count')
def count():
    return Response(status=200,
                    response=json.dumps(list_de_service.count(),
                                        cls=UtilEncoder), mimetype="application/json")