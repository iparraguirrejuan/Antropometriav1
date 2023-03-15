


def diametros_corporales():
    humero = input("Ingrese diametro del Humero: ")
    wrist = input("Ingrese diametro de la Muñeca: ")
    femur = input ("Ingrese diametro del Femur: ")
    return float(femur), float(wrist), float(humero)

def circunferencia():
    cintura = input("Ingrese circunferencia de la Cintura: ")
    cadera = input("Ingrese circunferencia de la Cadera: ")
    pantorilla = input("Ingrese circunferencia de la Pantorrilla: ")
    brazo_relajado = input("Ingrese circunferencia del Brazo relajado: ")
    brazo_contraido = input("Ingreso circunferencia de Brazo contraido: ")
    return float(cintura), float(brazo_contraido), float(cadera), float(pantorilla), float(brazo_relajado)
    

def pliegues_cutaneos():
    bicipital = input("Ingrese pliegue Bicipital: ")
    tricipital = input("Ingrese pliegue Tricipital: ")
    subescapular = input("Ingrese pliegue Subescaputal: ")
    suprailiaco = input("Ingrese pliegue Suprailiaco: ")    
    pantorrilla_p = input("Ingrese pliegue de la Pantorrilla : ")
    supraespinal = input("Ingrese pliegue Supraespinal: ")
    return float(bicipital),float(tricipital),float(subescapular),float(supraespinal),float(suprailiaco),float(pantorrilla_p)

