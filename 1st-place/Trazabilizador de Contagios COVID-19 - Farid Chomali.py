import math, time


#Listas
lista_nombres = []
lista_probabilidadcontagio = []


#Variables
#   n = nombre paciente
#   t = días desde síntomas
#   pr = cantidad de personas con las que se juntó


#Código

time.sleep(0.5)
print("Trazabilizador de Contagios COVID-19")
print("\n")
time.sleep(0.2)
print("   Hecho por:")
print("   -  Martín Cooper")
print("   -  Vicente Chomalí")
print("\n\n")
time.sleep(0.5)

try:

        #Nombre paciente PCR+.
        n=input("Nombre completo del paciente con PCR positivo: ")

        #Tiempo transcurrido desde síntomas paciente PCR+.
        t=int(input("¿Hace cuántos días comenzó a presentar síntomas? "))

        #Reunido con personas en esa ventana?
        pr=int(input(f"¿Con cuántas personas se ha reunido en los últimos {t+3} días? "))

        print(f"\n\nA continuación, escriba los nombres completos de las {pr} personas con las que se ha reunido en los últimos {t+3} días.\n")
        time.sleep(0.1)
        print("Después de escribir el nombre completo de una persona presione <Enter>.\n\n")

        #Nombres contactos estrechos. #listanombre es la lista con todos los nombres. nombre es el input de los distintos nombres.
        for n in range(0, pr):
                nombre=input("-  ")
                lista_nombres.append(nombre)

        print("\n\n")

        #Información de situaciones de contactos estrechos.
        for n in range(0,pr):
                tiempo=int(input(f"¿Hace cuántos días se reunió con {lista_nombres[n]}? "))
                horas=int(input("¿Durante cuántas horas? "))
                mascarillapaciente=int(input("Eficiencia de la mascarilla que estaba usando el paciente, sin el signo de porcentaje (si no estaba usando mascarilla responda 0): "))
                mascarillacontacto=int(input(f"Eficiencia de la mascarilla que estaba usando {lista_nombres[n]}, sin el signo de porcentaje (si no estaba usando mascarilla responda 0): "))
                vacunacontacto=int(input(f"¿{lista_nombres[n]} ha completado qué porcentaje de su vacunación? No ingrese el signo de porcentaje: "))
                print()

                #Probabilidad relativa contagio de cada factor:

                #Tiempo
                if abs(t-tiempo)>=11:
                    prob_tiempo=0
                elif t-tiempo<=-2:
                    prob_tiempo=1.2475-0.12375*(tiempo-t)
                elif t-tiempo>=-1:
                    prob_tiempo=0.91-0.09*(t-tiempo)
                
                #Horas
                if horas>=2:
                    prob_horas=1
                else:
                    prob_horas=1-0.15*horas
                        

                #Eficiencia mascarilla paciente
                prob_mascarillapaciente=1-mascarillapaciente/100

                #Eficiencia mascarilla contacto
                prob_mascarillacontacto=1-mascarillacontacto/100

                #Vacuna
                if vacunacontacto==100:
                        prob_vacuna=0.1
                elif vacunacontacto<100 and vacunacontacto>=50:
                        prob_vacuna=0.3
                else:
                        prob_vacuna=1

                #Definiendo probabilidad contagio
                prob_contagio=prob_tiempo*prob_horas*prob_mascarillapaciente*prob_mascarillacontacto*prob_vacuna
                
                lista_probabilidadcontagio.append(prob_contagio*100)


        #Nivel de restricción. Variable según consideraciones del gobierno, por ejemplo.
        filtro=20


        print("\n\n")
        print(f"Lista de personas a cuarentena y con recomendación de PCR (con {filtro}% o mayor probabilidad de contagio):\n")

        for n in range(0,pr):
                if lista_probabilidadcontagio[n]>=filtro:
                    print(f"     -  {lista_nombres[n]}                             {round(lista_probabilidadcontagio[n])}%")

        time.sleep(0.5)
        print("\n\n\n#QuédateEnCasa")
        time.sleep(0.5)
        print("\n\nPrograma finalizado.")



#En caso de error:
        
except:
        print("\n\n\nHa ocurrido en error. Ejecute el programa nuevamente.")
