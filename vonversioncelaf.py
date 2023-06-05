#convertidor de grados

def celsius():
    cel = float(input("Celsius: "))
    return cel

def farenheit():
    far = float(input("Farenheit: "))
    return far

def conversionCaF(cel):
    far = (cel*1.8) + 32
    return far

def conversionFaC(far):
    cel = (far-32)/1.8
    return cel
    

print("[1]C° a F°\n[2]F° a C°")
opc = input("Opcion: ")
if opc == '1':
    cel = celsius()
    far = conversionCaF(cel)
    print("F° : " + str(far) + "°")
elif opc == '2':
    far = farenheit()
    cel =  conversionFaC(far)
    print("C° : " + str(cel) + "°")





    
