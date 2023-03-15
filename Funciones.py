import re 



def check_string(texto, nom_variable):
    while True:
        texto = input(f"Ingrese {nom_variable} : ")
        if re.search(r'\d', texto):
            print("El valor contiene numeros, por favor ingrese el valor correctamente")   
        else:
            texto.isalpha() == True
            return texto

def check_int(num, nom_variable):
    while True:
        num = input (f"Ingresar {nom_variable}: ")
        try:
            num_entero = int (num)
            break
        except ValueError:
            print("El numero ingresado no es un entero valido")
    return num_entero

def check_sexo(genero):
    while True:
        genero = input("Ingrese el genero m/f: ")
        genero.lower()
        if genero == "m" or genero == "f":
           return genero
        else:
            print("Por favor seleccione un genero correcto")
        
        
    
def check_mediciones(valor,nom_variable):
    while True:
        valor = input(f"Ingresar {nom_variable}: ")
        try:
            num_decimal = float(valor)
            break
        except ValueError:
            print("Ingrese un numero valido")
    return num_decimal

    
def check_edad(edad):
   
    while True:
        edad = input("Ingrese edad: ")
        try:
            edad = int(edad)
            if edad >= 17:
                return edad
            else:
                print("Debe ser mayor de 17 años, para hacer la medicion")
        except ValueError:
            print("Por favor ingrese un valor correcto")
            

        

        