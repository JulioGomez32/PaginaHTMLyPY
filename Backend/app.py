from flask import Flask, request, jsonify
from flask_cors import  CORS 
from estudiante import estudiante
from docente import docente
from setup import setup

app = Flask(__name__)
CORS(app)
manager = setup()

#ENDPOINTS
@app.route('/')
def home():
    return "<H1>Julio Fernando Gómez Callejas</H1>"

@app.route('/docentes')
def maestro():
    return "<H1>Hola Docente</H1>"

@app.route('/estudiantes')
def alumno():
    return "<H1>Hola Estudiante</H1>"

@app.route('/addestudiante', methods=['POST'])
def addestudiante():
    dato = request.json
    nuevo = estudiante(dato['nombre'],dato['apellido'],dato['grado'],dato['especialidad'],dato['correo'],dato['carnet'],dato['edad'])    
    if manager.addEstudiante(nuevo) == True:
        return '{ "estado": "Estudiante Agregado"}'
    else:
        return '{ "estado": "Estudiante ya existente"}'

@app.route('/adddocente')
def adddocente():   
    dato = request.json
    nuevo = docente(dato['carnet'],dato['nombre'],dato['apellido'],dato['curso'],dato['especialidad'],dato['edad'],dato['correo'])
    if manager.addDocente(nuevo) == True:
        return '{ "estado": "Docente Agregado"}'
    else:
        return '{ "estado": "Docente ya Existente"}'
    
@app.route('/getEstudiantes')
def getEstudiantes():
    return manager.getEstudiante()

@app.route('/getDocentes')
def getDocentes():
    return manager.getDocente()

#Ejecuta el codgio de la api
if __name__ == '__main__':
    app.run(host='0.0.0.0',port=5000,debug=True)