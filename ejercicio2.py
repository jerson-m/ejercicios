sueldo=int(input("ingrese su salario: "))

ventas=(input("ingrese el valor de las 3 ventas"))

valor=ventas.split()

v1=int(valor[0])
v2=int(valor[1])
v3=int(valor[2])

c1=(v1*10)/100
c2=(v2*10)/100
c3=(v3*10)/100

descuento=c1+c2+c3
print("su comision es de: "+ str(descuento))

total=descuento+sueldo
print("su salario todal es de: "+str(total))