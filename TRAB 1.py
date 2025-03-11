import os
os.system("cls") #LIMPIAR LA PANTALLA
print ("Ingresa tus datos")
vnombreyapellido = input("Nombre y Apellido:").upper() 
vedad = input("Edad:").upper()
print ("Hola, tu nombre es",vnombreyapellido,"y tienes",vedad,"años")
print ("Ingresa tu dirección y correo")
vcorreo = input("Correo:").lower()
vdireccion = input("Dirección:").upper()
print ("Tus datos son " ,vcorreo, "y tu dirección es",vdireccion)
print ("Para concluir facilitanos tu rut!.")
vrut = int(input("Rut:"))
print ("Gracias por proporcionar tus datos")
os.system("cls")
print ("Datos Ingresados con éxito")
print ("Nombre y Apellido:",vnombreyapellido)
print ("Edad:",vedad)
print ("Correo:",vcorreo)
print ("Dirección:",vdireccion)
print ("Rut:",vrut)
print ("Resumen de tus datos ingresados. Gracias por confiar en nosotros.")
end = input("Presiona Enter para salir") #PREGUNTAR SI QUIERES SALIR


  
