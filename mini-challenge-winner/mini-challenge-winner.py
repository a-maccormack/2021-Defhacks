import math, time

time.sleep(0.5)
print("Maximizador de distancias")
print("\n")
time.sleep(0.2)
print("   Hecho por:")
print("   -  Martín Cooper")
print("   -  Vicente Chomalí")
print("\n\n")
time.sleep(0.5)

while True:
       
        try:
                running=1
                n=int(input("¿Cuántas salas tiene el colegio? "))

                if n<=1:
                        print("Indique una cantidad de salas mayor o igual a 2.")
                        print("\n\n")
                        time.sleep(1)
                        continue

                elif n>100000:
                        print("Indique una cantidad de salas menor o igual a 100000.")
                        print("\n\n")
                        time.sleep(1)
                        continue
                        
                else:
                        #Solicitamos que el usuario determine la cantidad de salas y su orden.
                        print("\nEscriba la secuencia de salas ocupadas y no ocupadas.")
                        time.sleep(0.2)
                        text = input("Para indicar una sala no ocupada escriba 0, y para indicar una sala ocupada un 1.\n\n")
                        time.sleep(0.2)

                        #Defino el índice de salas ocupadas.
                        salas_ocupadas = []

                        for i in range (n):
                                if text[i] == "1":
                                        salas_ocupadas.append(i)
                                        #Si hallamos una sala ocupada, agregamos al final de la lista el índice de esta.

                        if len(salas_ocupadas) == 0:
                                print(str(n-1))
                                #(Si no hay salas ocupadas, y entran dos alumnos, uno irá al pricipio y el otro al final. Por eso n-1.)
                                
                        else:
                            #d es la distancia mínima entre las salas antes de añadir a los dos nuevos alumnos.
                            #99999 es el máximo valor que podría esta variable.
                            d = 99999

                            #un_espacio representa la situación en que solamente un alumno se coloca entre dos salas ocupadas.
                            #dos_espacios representa la situación en que dos alumnos se colocan entre dos salas ocupadas.
                            #calculamos ambas situaciones para posteriormente comparar y determinar cuál es más eficiente.
                            un_espacio = [salas_ocupadas[0], n-salas_ocupadas[-1]-1]
                            dos_espacios = [math.floor(salas_ocupadas[0]/2), (math.floor((n-salas_ocupadas[-1]-1)/2))]

                            for i in range(len(salas_ocupadas)-1):
                                    disponibles_en_espacio = salas_ocupadas[i+1] - salas_ocupadas[i]
                                    d = min(d, disponibles_en_espacio)
                                    un_espacio.append(math.floor(disponibles_en_espacio/2))
                                    dos_espacios.append(math.floor(disponibles_en_espacio/3))

                            #Reordenamos para análisis
                            un_espacio.sort()
                            dos_espacios.sort()

                            a=min(un_espacio[-1], un_espacio[-2]) #a es la distancia mínima asumiendo que solo se coloca un alumno entre dos salas ocupadas.
                            b=max(a, dos_espacios[-1]) #b determina si es más eficiente colocar a uno o dos alumnos entre dos salas ocupadas.
                            c=min(b,d) #c determina si esta distancia mínima es mayor o menor a la distancia mínima entre salas antes del ingreso de nuevos alumnos.
                            #c es el resultado
                                  
                            resultado=c

                            print(resultado)
                            print("\n\n")
                            time.sleep(0.5)


        except:
                print("Por favor inserta un número entero mayor a 2 y menor a 100000.")
                print("\n\n")
                time.sleep(1)
                continue


                      
                                 
