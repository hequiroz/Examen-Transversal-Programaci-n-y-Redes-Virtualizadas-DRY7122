##Item 1 Examen Transversal
##Programación y Redes Virtualizadas
##Profesor: Sr. Fabian Santibañez
import time
salir=False
while salir==False:
    print ("Los Integrantes del Grupo son:")
    print("- Sebastian Valdés")
    print("- Mayra Marín")
    print("- Fedherbe Saint Hilaire")
    print("- Héctor Quiroz")

    pregunta=True
    while pregunta==True:
        respuesta=input("Desea mostrar denuevo los integrantes del grupo? (si / no): ")
        if (respuesta=="si" or respuesta=="s" or respuesta=="SI"):
            print("=====================")
            pregunta=False
        elif (respuesta=="no" or respuesta=="n" or respuesta=="NO"):
            print("Gracias por Ingresar ")
            time.sleep(2)
            print("Hasta pronto!")
            time.sleep(2)
            pregunta=False
            salir=True
        else:
            print("========== Ingresar una opción válida: ============= ")
