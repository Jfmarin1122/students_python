from flask import Response, Blueprint, jsonify, json
from service.student_service import StudentService
from util.util_encoder import UtilEncoder

app_student = Blueprint("app_student",__name__)

@app_student.route('/student/all')
def get_all_students():
    student_service = StudentService()
    return Response(status=200,
                    response=json.dumps(student_service.get_all_students(),
                                        cls=UtilEncoder),
                    mimetype="application/json"
                    )
    #return jsonify(student_service.get_all_students_dict())

@app_student.route('/student/percentagebygender/<gender>')
def get_percentage_students_by_gender(gender):
    student_service = StudentService()
    return str(student_service.get_percentage_students_by_gender(int(gender)))

@app_student.route('/student/per_students_job_avgsalary/<gender>')
def get_percentage_students_job_avg_salary(gender):
    student_service = StudentService()
    return jsonify(student_service.get_percentage_students_job_avg_salary(int(gender)))

@app_student.route('/student/salary/<gender>/<salary>')
def get_students_mayor_salary(gender, salary):
    student_service = StudentService()
    return Response(status=200,
                    response=json.dumps(student_service.get_students_mayor_salary(int(gender), int(salary)),
                                        cls=UtilEncoder),
                    mimetype="application/json"
                    )

@app_student.route('/student/mayorsalary/<gender>')
def get_gender_mayor_salary(gender):
    student_service = StudentService()
    return Response(status=200,
                    response=json.dumps(student_service.get_gender_mayor_salary(int(gender)),
                                        cls=UtilEncoder),
                    mimetype="application/json"
                    )

@app_student.route('/student/rangosalary/<min>/<max>')
def get_rango_salary(min, max):
    student_service = StudentService()
    return Response(status=200,
                    response=json.dumps(student_service.get_rango_salary(int(min), int(max)),
                                        cls=UtilEncoder),
                    mimetype="application/json"
                    )

@app_student.route('/student/salarypromediobygender/<gender>')
def get_average_salary_by_gender(gender):
    student_service = StudentService()
    return Response(status=200,
                    response=json.dumps(student_service.get_average_salary_by_gender(int(gender)),
                                        cls=UtilEncoder),
                    mimetype="application/json"
                    )

@app_student.route('/student/menorsalary/<gender>')
def get_gender_menor_salary(gender):
    student_service = StudentService()
    return Response(status=200,
                    response=json.dumps(student_service.get_gender_menor_salary(int(gender)),
                                        cls=UtilEncoder),
                    mimetype="application/json"
                    )

@app_student.route('/student/promedioedad')
def get_promedio_edad():
    student_service = StudentService()
    return Response(status=200,
                    response=json.dumps(student_service.get_promedio_edad(),
                                        cls=UtilEncoder),
                    mimetype="application/json"
                    )

@app_student.route('/student/zonastudent')
def get_get_zona_edadmayor():
    student_service = StudentService()
    return Response(status=200,
                    response=json.dumps(student_service.get_zona_edadmayor(),
                                        cls=UtilEncoder),
                    mimetype="application/json"
                    )

@app_student.route('/student/studentsbycity')
def get_student_by_city():
    student_service = StudentService()
    return jsonify(student_service.get_student_by_city())