def verificar_calificacion(nota1,nota2,nota3):
    global promedio#declaracion de variable como global para poder mostrar el promedio fuera de la funcion
    promedio = (nota1+nota2+nota3)/3
    if promedio >= 6 and promedio <=10:
        return print("aprobado")
    else: 
        return print("desaprobado")       

verificar_calificacion(int(input()),int(input()),int(input()))#linea para ingresar datos de las 3 notas que recibe la funcion

print("el promedio es de: ",promedio)