# Tipos de datos

palabra = "string"
numeros = 2   #int
numerosDecimales = 2.4 #float
booleanos = True #False

print (numeros == 1)
print (numeros != 1)

# def + nombre = definir una funcion  

# 1. crea una funcion llamada CINE 
# 2. pidele al usuario su EDAD 
# 3. compara esa EDAD con la edad minima de 18
# 4. SI es mayor a 18 imprime "puedes pasar" SI NO es mayor a 18 imprime "no puedes pasar"

def CINE (EDAD):
    edadMinima = 18

    if EDAD >= 18 :
        print("puedes pasar")
    else: 
        print("no puedes pasar")

CINE(18)
CINE(3)


def ATM (DINERO):
    saldoMinimo = 2000

    if DINERO > saldoMinimo:
        print ("Saldo insuficiente")
    else:
        print ("Retiro aceptado")

ATM (1200)


def cine2 () :
    peliculaAccion = 1    
    peliculaMiedo = 2
    peliculaNinos = 3

    print("PELICULAS")
    print("1. Accion")
    print("2. miedo")
    print("3. niños")
    peliculaSeleccionada = int(input()) #3

    if peliculaSeleccionada == 1:
        print ("Accion")
    elif peliculaSeleccionada == 2:
        print ("miedo")
    if peliculaSeleccionada == 3:
        print ("niños")
    else: print("selecciona una pelicula del menu")

cine2()

    