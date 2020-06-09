lim=452 #Estos son los ultimos 3 digitos de mi carnet 201700452
a=[]    #Esta es la lista que almacenara las secuencias
op=2    #op tomara el valor de cada columna en la lista, su valor inicial no importa
t=2     #t tomara el valor de cada fila aunque empieze con 2 ya que el 1 no se toma encuenta
p=1     #variable utilizada en la funcion colla
import time #importamos la libreria time para hacer pausas
def colla(x):   #Esta funcion devuelve el numero collatz que le sigue al numero dado
    if(x==1):
        return 1
    if(x%2==0): #Dependiendo si el numero es par o impar se devolvera un valor diferente
        p=x/2   #Si es par se devuelve esto
        return p
    else:   #si es impar se devuelve este p
        p=3*x+1
        return p

def escribe():   #Esta funcion crear el archivo de txt
    archi=open("collatz.txt","a+") #Se eligio a+ para que cree el archivo en caso no exista o lo sobreescriba
    time.sleep(0.1)
    archi.write(str(a)+'\n')
    archi.close


print("Empezando") #Indicamos que vamos a iniciar

while t<=lim:
    if op!=1:       #op tomara el numero de cada numero en la secuencia actual
        a.append(int(op)) #Si op no es 1 podemos indicarle que pase al siguiente numero 
        op=colla(op)    #en la secuencia y su valor anterior lo agregamos a la lista a
    if op==1:
        a.append(int(op)) #Si op llega a ser 1 significa que llegamos al final de la secuencia
        t=t+1           #aumentamos el valor de t para pasar a la nueva secuencia (nueva fila)
        op=t            #volvemos op=t para iniciar de nuevo el proceso
        escribe()       #escribimos en el archivo de texto la lista a
        a.clear()       #limpiamos a para poder iniciar de nuevo
print("Todas las secuencias han sido encontradas") #indicamos que terminamos