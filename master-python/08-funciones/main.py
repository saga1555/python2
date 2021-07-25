print("Ejemplo 1")
def muestranombre():
    print("pedro")
    print("lima")
    print("quito")
    print("\n")


#invocar
muestranombre()

# emeplo calculadoR
def calculadora(num1,num2, basicas=False):
    suma= num1+num2
    resta= num1-num2
    multi= num1*num2
    div= num1/num2
    cadena = ""
    cadena+= "suma = "+str(suma)
    cadena += "\n"
    cadena+= "resta = "+str(resta)
    cadena += "\n"
    cadena+= "multiplicacion = "+str(multi)
    cadena += "\n"
    cadena+= "division ="+str(div)
    return cadena

print (calculadora(8,5))