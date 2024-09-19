from estudiante import estudiante
from docente import docente
import json

class setup:

    def __init__(self):
         self.Estudiantes = []
         self.Docentes = []
         self.Estudiantes.append(estudiante("2020-020","Estudiante","Modelo","Quinto","Computacion",17,"estudiante@emilianisomascos.edu.gt"))
         self.Docentes.append(docente("201601110","Docente","Modelo","Analisis","Computacion",25,"docente@emilianisomascos.edu.gt"))

    def addEstudiante(self, estudiantex):
        if not self.verificacionE == True:
            self.Estudiantes.append(estudiantex)
            print("Estudiante Agregado "+estudiantex.carnet)
            return True
        else:
            print("Estudiante Existente")    
            return False

    def addDocente(self, docentex):
        if self.verificacionD == False:
            self.Docentes.append(docentex)
            print("Docente Agregado "+docentex.carnet)
            return True
        else:
            print("Docente Existente")
            return False    
    
    def verificacionE(self, estudiantex):
        for estudiante in self.Estudiantes:
             if estudiante.carnet == estudiantex.cernet:
                  return True
        return False
    
    def verificacionD(self, docentex):
        for i in self.Docentes:
              if i.carnet == docentex.carnet:
                   return True
        return False
    
    def getEstudiante(self):
        return json.dumps([ob.__dict__ for ob in self.Estudiantes])
    
    def getDocente(self):
        return json.dumps([ob.__dict__ for ob in self.Docentes])