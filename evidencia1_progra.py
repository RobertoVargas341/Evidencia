# Biblioteca.py

catalogo = []
autores = []
generos = []

while True:
    print("---- Menú Principal ----")
    print("1. Registrar la adquisición de un ejemplar")
    print("2. Consultar los datos de un título")
    print("3. Reporte tabular de todos los ejemplares")
    print("4. Reporte tabular de todos los ejemplares para un autor específico")
    print("5. Reporte tabular de todos los ejemplares para un género específico")
    print("6. Reporte tabular de todos los ejemplares para un año específico")
    print("7. Salir")

    opcion = input("Seleccione una opción: ")

    if opcion == "1":
        print("---- Registrar la adquisición de un ejemplar ----")
        ejemplar = {}

        
        identificador = len(catalogo) + 1
        ejemplar["Identificador"] = identificador

      
        titulo = input("Ingrese el título del ejemplar: ").upper()
        ejemplar["Título"] = titulo

      
        autor = input("Ingrese el nombre del autor: ").upper()
        ejemplar["Autor"] = autor

        if autor not in autores:
            autores.append(autor)

      
        genero = input("Ingrese el género del ejemplar: ").upper()
        ejemplar["Género"] = genero

        if genero not in generos:
            generos.append(genero)

        while True:
            ano_publicacion = input("Ingrese el año de publicación del ejemplar: ")
            if len(ano_publicacion) != 4 or not ano_publicacion.isdigit():
                print("Año inválido, debe ser de 4 dígitos.")
            else:
                ejemplar["Año de publicación"] = int(ano_publicacion)
                break

        while True:
            isbn = input("Ingrese el ISBN del ejemplar (13 dígitos): ")
            if len(isbn) != 13 or not isbn.isdigit():
              print("ISBN inválido, debe ser de 13 dígitos.")
            else:
                ejemplar["ISBN"] = isbn
                break


       
        fecha_adquisicion = input("Ingrese la fecha de adquisición del ejemplar (DD/MM/AAAA): ")
        ejemplar["Fecha de adquisición"] = fecha_adquisicion

       
        catalogo.append(ejemplar)

        print(f"\nEl ejemplar con identificador {identificador} ha sido registrado exitosamente.\n")

    elif opcion == "2":
        print("---- Consultar los datos de un título ----")
        sub_opcion = input("Buscar por título (T) o ISBN (I): ").upper()

        if sub_opcion == "T":
            
            print("\n--- Lista de Títulos ---")
            for ejemplar in catalogo:
                print(ejemplar["Título"])
            print("-----------------------\n")
          
    titulo = input("Ingrese el título a buscar: ").upper()
    encontrado = False
    for ejemplar in catalogo:
      if ejemplar["Título"].upper() == titulo:
        print(f"\nIdentificador: {ejemplar['Identificador']}")
        print(f"Título: {ejemplar['Título']}")
        print(f"Autor: {ejemplar['Autor']}")
        print(f"Género: {ejemplar['Género']}")
        print(f"Año de publicación: {ejemplar['Año de publicación']}")
        print(f"ISBN: {ejemplar['ISBN']}")
        print(f"Fecha de adquisición: {ejemplar['Fecha de adquisición']}\n")
        encontrado = True
    if not encontrado:
            print(f"\nEl título '{titulo}' no se encuentra en el catálogo.\n")

    elif sub_opcion == "I":
      isbn = input("Ingrese el ISBN a buscar (13 dígitos): ")
      encontrado = False
      for ejemplar in catalogo:
            if ejemplar["ISBN"] == isbn:
                print(f"\nIdentificador: {ejemplar['Identificador']}")
                print(f"Título: {ejemplar['Título']}")
                print(f"Autor: {ejemplar['Autor']}")
                print(f"Género: {ejemplar['Género']}")
                print(f"Año de publicación: {ejemplar['Año de publicación']}")
                print(f"ISBN: {ejemplar['ISBN']}")
                print(f"Fecha de adquisición: {ejemplar['Fecha de adquisición']}\n")
                encontrado = True
                break

            if not encontrado:
              print(f"\nEl ISBN '{isbn}' no se encuentra en el catálogo.\n")

            else:
              print("Opción inválida.")

    elif opcion == "3":
      print("---- Reporte tabular de todos los ejemplares ----")
      print("Identificador | Título | Autor | Género | Año de publicación | ISBN | Fecha de adquisición")
      print("----------------------------------------------------------------------------------------")
      for ejemplar in catalogo:
        print(f"{ejemplar['Identificador']:13} | {ejemplar['Título']:6} | {ejemplar['Autor']:5} | {ejemplar['Género']:6} | {ejemplar['Año de publicación']:19} | {ejemplar['ISBN']:13} | {ejemplar['Fecha de adquisición']:21}")
      print()

    elif opcion == "4":
      print("---- Reporte tabular de todos los ejemplares para un autor específico ----")
      print("\n--- Lista de Autores ---")
      for autor in autores:
        print(autor)
        print("------------------------\n")

      autor = input("Ingrese el nombre del autor a buscar: ").upper()
      print("Identificador | Título | Género | Año de publicación | ISBN | Fecha de adquisición")
      print("--------------------------------------------------------------------------------")
      for ejemplar in catalogo:
        if ejemplar["Autor"] == autor:
          print(f"{ejemplar['Identificador']:13} | {ejemplar['Título']:6} | {ejemplar['Género']:6} | {ejemplar['Año de publicación']:19} | {ejemplar['ISBN']:13} | {ejemplar['Fecha de adquisición']}")

    elif opcion == "5":
        print("---- Reporte tabular de todos los ejemplares para un género específico ----")
        print("\n--- Lista de Géneros ---")
        for genero in generos:
            print(genero)
        print("------------------------\n")

        genero = input("Ingrese el género a buscar: ").upper()
        print("Identificador | Título | Autor | Año de publicación | ISBN | Fecha de adquisición")
        print("--------------------------------------------------------------------------------")
        for ejemplar in catalogo:
            if ejemplar["Género"] == genero:
                print(f"{ejemplar['Identificador']:13} | {ejemplar['Título']:6} | {ejemplar['Autor']:5} | {ejemplar['Año de publicación']:19} | {ejemplar['ISBN']:13} | {ejemplar['Fecha de adquisición']:21}")
        print()

    elif opcion == "6":
        print("---- Reporte tabular de todos los ejemplares para un año específico ----")
        anio = input("Ingrese el año a buscar: ")
        print("Identificador | Título | Autor | Género | ISBN | Fecha de adquisición")
        print("------------------------------------------------------------------")
        for ejemplar in catalogo:
            if ejemplar["Año de publicación"] == anio:
                print(f"{ejemplar['Identificador']:13} | {ejemplar['Título']:6} | {ejemplar['Autor']:5} | {ejemplar['Género']:6} | {ejemplar['ISBN']:13} | {ejemplar['Fecha de adquisición']:21}")
        print()

    elif opcion == "7":
       
        print("Saliendo del programa...")
        break

    else:
        print("Opción inválida.")
