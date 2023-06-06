#generador de contraseña
import random


def numeroR():
    aleatorio = random.randrange(0,41)
    return aleatorio
    
def crtr(random):
   # passw = list()
    letras = ['7','8','9','&','j','k','l','m','n','o','p','q','r','s','t','u','v','w','x','y','z','0','1','a','b','c','d','e','f','g','h','i','2','3','4','5','6','%','$']
    passw = letras[rndm]
    return passw

def muestra(cnts):
    print("Password: ", end = "")
    for i in range(0, len(cnts)):
        print(cnts[i], end = "")

cnts = list()

for i in range(0,8):
    rndm = numeroR()
    x = crtr(rndm)
    cnts.append(x)

muestra(cnts)
