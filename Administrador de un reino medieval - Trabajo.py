# Creamos un diccionario vacío llamado "reino"
reino = {
    
}


# Primera función: Agregar nuevos aldeanos.
def agregar_aldeano():
 print()
 print("Ingrese el nombre del aldeano: ")
 
 nombre = str(input())

 # Si el aldeano pertenece al reinio:
 if nombre in reino:
  print("¡El aldeano ya se encuentra en el reino!")
  print("Intente nuevamente.")

 # Si el aldeano no pertenece al reino:
 else:
  reino[nombre] = None
  print(f"¡Se ha agregado con éxito el nuevo aldeano!")



# Segunda función: Asignar tarea a los aldeanos.
def asignar_tarea():
  print()
  print("Ingrese el nombre del aldeano para asignar una tarea: ")
  
  nombre_aldeano = str(input())

  # Si el aldeano se encuentra en el reino:
  if nombre_aldeano in reino:
    print()
    print("¿Qué tarea debe realizar?")
    
    nueva_tarea = str(input())
    reino[nombre_aldeano] = nueva_tarea
    print(f"¡Tarea {nueva_tarea} asignada con éxito al aldeano {nombre_aldeano}")

  # Si el aldeano no se encuentra en el reino:
  else:
    print()
    print(f"El aldeano {nombre_aldeano} no está en el reino.")



# Tercera función: Ver el estado del reino.
def ver_estado_reino():

  # Si el diccionario "reino" aún se encuentra vacío:
  if not reino:
    print()
    print("El reino se encuentra vacío. o(╥﹏╥)")

  # Si el diccionario "reino" ya está utilizado:
  else:
    print()
    print("Estado del reino: ")
    for aldeano, tarea in reino.items():
      if tarea == None:
       print(f"𓆩𓆪 Aldeano {aldeano} = Sin tarea asignada.")
      else:
       print(f"𓆩𓆪 Aldeano {aldeano} = Tarea asignada: {tarea}")



# Cuarta función: Mostrar el menú para interactuar ("main").
def main():
  print("¡Bienvenido/a al reino medieval!")
  print("𓆩𓆪 ⸻⸻⸻⸻⸻ 𓆩𓆪")
  print()
  print()
  while True:
    print()
    print("⸻⸻⸻⸻⸻⸻⸻⸻")
    print("Selecciona la opción que deseas realizar: ")
    print("⸻⸻⸻⸻⸻⸻⸻⸻")
    print("1. Agregar nuevo aldeano.")
    print("2. Asignar una tarea.")
    print("3. Ver el estado del reino.")
    print("4. Salir.")
    menu_opcion = int(input())

    if menu_opcion == 1:
      agregar_aldeano()

    elif menu_opcion == 2:
      asignar_tarea()

    elif menu_opcion == 3:
      ver_estado_reino()

    elif menu_opcion == 4:
      print()
      print("¡Vuelve pronto!")
      print("⸻⸻⸻ 𓆩𓆪 ")

      break

    else:
      print("Opción no válida.")



# Poder recorrer la cuarta función, la cual incluye el menú didáctico
# con todas las funciones creadas anteriormente.
main()