notas=input("ingrese las 3 notas de parciales: ")

nota=notas.split()

n1=int(nota[0])
n2=int(nota[1])
n3=int(nota[2])

promedio=(n1+n2+n3)/3
porcentaje=promedio * 0.55


examen=int(input("ingrese la nota del examen final: "))

porcentaje2=examen*0.30


trabajo=int(input("ingrese la nota del trabajo final: "))

porcentaje3=trabajo*0.15

notafinal=porcentaje+porcentaje2+porcentaje3
print("la nota final es: ", notafinal)
