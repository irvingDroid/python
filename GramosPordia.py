#Calculadora de gramos de proteina por dia

gramos = 2.2

def inicio():
    print("Gramos de proteina por dia")

def entrada():
    pesoKg = float(input("Peso(Kg): "))
    return pesoKg

def calc(pesoKg):
    gramosDia = gramos * pesoKg
    return gramosDia

def salida(gramosDia):
    print("Ingerir " + str(round(gramosDia, 2)) + " gramos de proteina por dia")


inicio()
pesoKg = entrada()
gramosDia = calc(pesoKg)
salida(gramosDia)



    
