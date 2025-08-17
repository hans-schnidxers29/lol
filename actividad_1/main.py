from clases.animal import*

A = animal("luky",7.45,"hans","29/04/06","28/09/25")
print("El nombre del tu animal es: ", A.nombre," y el propietario es: ",A.propietario)

A.fechaCumple =input("ingrese la nueva fecha: ")
print("nueva fecha: ", A.fechaCumple) 