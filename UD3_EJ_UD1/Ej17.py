nombre="lolo"
contraseña="1234"
ingreso_nombre=input("Ingrese su nombre: ")
ingreso_contraseña=input("Ingrese su contraseña: ")
if ingreso_nombre==nombre and ingreso_contraseña==contraseña:
    print("Inicio de sesión correcto")
else:
    print("Inicio de sesión fallido")