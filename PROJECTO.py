import re #Biblioteca del que se extrae metodo ('match()' de la clase re) para verificar el patron de entrada de fecha 
contador = 0

Agenda = {
    '12332': {'Codigo': '12332', 'Fecha de vencimiento': '12-23-2344', 'Nombre del producto':'Pinturas 24 c.          ','Categoria':'Utiles de escritorio ','Precio': '12.50 ',  'Proveedor':'Faber castell ','Descuento':'NO EN DESCUENTO |'},
    '12232': {'Codigo': '12232', 'Fecha de vencimiento': '12-23-2344', 'Nombre del producto':'Cuadernos LORO          ','Categoria':'Utiles de escritorio ','Precio': '12.50 ',  'Proveedor':'Loro          ','Descuento':'NO EN DESCUENTO |'},
    '14655': {'Codigo': '14655', 'Fecha de vencimiento': 'No expira ', 'Nombre del producto':'Lapicero F. C.          ','Categoria':'Utiles de escritorio ','Precio': '00.50 ',  'Proveedor':'Faber castell ','Descuento':'NO EN DESCUENTO |'},
    '13456': {'Codigo': '13456', 'Fecha de vencimiento': 'No expira ', 'Nombre del producto':'Corrector F. C.         ','Categoria':'Utiles de escritorio ','Precio': '01.50 ',  'Proveedor':'Faber castell ','Descuento':'NO EN DESCUENTO |'},
    '23456': {'Codigo': '23456', 'Fecha de vencimiento': 'No expira ', 'Nombre del producto':'Cuadernos Standford     ','Categoria':'Utiles de escritorio ','Precio': '06.50 ',  'Proveedor':'Standford     ','Descuento':'NO EN DESCUENTO |'},
    '65678': {'Codigo': '65678', 'Fecha de vencimiento': 'No expira ', 'Nombre del producto':'Hojas A4 Standford      ','Categoria':'Utiles de escritorio ','Precio': '00.20 ',  'Proveedor':'Standford     ','Descuento':'NO EN DESCUENTO |'},
    '79900': {'Codigo': '79900', 'Fecha de vencimiento': 'No expira ', 'Nombre del producto':'Folder Manilas Stanford ','Categoria':'Utiles de escritorio ','Precio': '00.50 ',  'Proveedor':'Standford     ','Descuento':'NO EN DESCUENTO |'},
    '13939': {'Codigo': '13939', 'Fecha de vencimiento': 'No expira ', 'Nombre del producto':'Goma en barra           ','Categoria':'Utiles de escritorio ','Precio': '03.50 ',  'Proveedor':'Faber castell ','Descuento':'NO EN DESCUENTO |'},
    '13784': {'Codigo': '13784', 'Fecha de vencimiento': 'No expira ', 'Nombre del producto':'Resaltadores            ','Categoria':'Utiles de escritorio ','Precio': '10.50 ',  'Proveedor':'Faber castell ','Descuento':'NO EN DESCUENTO |'},
    '13632': {'Codigo': '13632', 'Fecha de vencimiento': 'No expira ', 'Nombre del producto':'Lapiceros de colores 12u','Categoria':'Utiles de escritorio ','Precio': '24.50 ',  'Proveedor':'Faber castell ','Descuento':'NO EN DESCUENTO |'},
    '27985': {'Codigo': '27985', 'Fecha de vencimiento': '20/07/2023', 'Nombre del producto':'Leche gloria            ','Categoria':'enlatados            ','Precio': '04.80 ',  'Proveedor':'Faber castell ','Descuento':'NO EN DESCUENTO |'},
    '27568': {'Codigo': '27568', 'Fecha de vencimiento': '30/08/2025', 'Nombre del producto':'Conserva/ durazno       ','Categoria':'enlatados            ','Precio': '13.80 ',  'Proveedor':'Dos caballos  ','Descuento':'NO EN DESCUENTO |'},
    '12714': {'Codigo': '12714', 'Fecha de vencimiento': '08/04/2024', 'Nombre del producto':'Atún Primor             ','Categoria':'enlatados            ','Precio': '02.60 ',  'Proveedor':'Alicorp       ','Descuento':'NO EN DESCUENTO |'},
    '26720': {'Codigo': '26720', 'Fecha de vencimiento': '04/07/2023', 'Nombre del producto':'Leche bonle             ','Categoria':'enlatados            ','Precio': '04.40 ',  'Proveedor':'Bonle         ','Descuento':'NO EN DESCUENTO |'},
    '26304': {'Codigo': '26304', 'Fecha de vencimiento': '15/09/2025', 'Nombre del producto':'Ricocan 280gr           ','Categoria':'enlatados            ','Precio': '09.20 ',  'Proveedor':'Rico Can      ','Descuento':'NO EN DESCUENTO |'},
    '25887': {'Codigo': '25887', 'Fecha de vencimiento': '15/04/2023', 'Nombre del producto':'Leche condensada  nestle','Categoria':'enlatados            ','Precio': '03.30 ',  'Proveedor':'Nestle        ','Descuento':'NO EN DESCUENTO |'},
    '25463': {'Codigo': '25463', 'Fecha de vencimiento': '08/04/2024', 'Nombre del producto':'Sardinas 340gr          ','Categoria':'enlatados            ','Precio': '03.40 ',  'Proveedor':'Kandy         ','Descuento':'NO EN DESCUENTO |'},
    '32504': {'Codigo': '32504', 'Fecha de vencimiento': '04/07/2023', 'Nombre del producto':'Alcachofa340gr          ','Categoria':'enlatados            ','Precio': '05.60 ',  'Proveedor':'Casa verde    ','Descuento':'NO EN DESCUENTO |'},
    '22462': {'Codigo': '22462', 'Fecha de vencimiento': '15/09/2025', 'Nombre del producto':'Salsa de tomate         ','Categoria':'enlatados            ','Precio': '06.70 ',  'Proveedor':'Casa Rinaldi  ','Descuento':'NO EN DESCUENTO |'},
    '22420': {'Codigo': '22420', 'Fecha de vencimiento': '15/04/2023', 'Nombre del producto':'Aceitunas               ','Categoria':'enlatados            ','Precio': '03.50 ',  'Proveedor':'Serpis        ','Descuento':'NO EN DESCUENTO |'},
    '13753': {'Codigo': '13753', 'Fecha de vencimiento': '13/05/2024', 'Nombre del producto':'Poet 340ml              ','Categoria':'productos de limpieza','Precio': '09.69 ',  'Proveedor':'Sapolio       ','Descuento':'NO EN DESCUENTO |'},
    '37671': {'Codigo': '37671', 'Fecha de vencimiento': '30/10/2025', 'Nombre del producto':'Bolivar                 ','Categoria':'productos de limpieza','Precio': '00.50 ',  'Proveedor':'Alicorp       ','Descuento':'NO EN DESCUENTO |'},
    '13781': {'Codigo': '13781', 'Fecha de vencimiento': '04/07/2027', 'Nombre del producto':'Legia sapolio           ','Categoria':'productos de limpieza','Precio': '00.50 ',  'Proveedor':'Alicorp       ','Descuento':'NO EN DESCUENTO |'},
    '63795': {'Codigo': '63795', 'Fecha de vencimiento': '04/07/2023', 'Nombre del producto':'Ace 346gr               ','Categoria':'productos de limpieza','Precio': '00.50 ',  'Proveedor':'P/G           ','Descuento':'NO EN DESCUENTO |'},
    '43809': {'Codigo': '43809', 'Fecha de vencimiento': '17/03/2023', 'Nombre del producto':'Ayudin                  ','Categoria':'productos de limpieza','Precio': '00.50 ',  'Proveedor':'Clorox        ','Descuento':'NO EN DESCUENTO |'},
    '38234': {'Codigo': '38234', 'Fecha de vencimiento': '11/04/2023', 'Nombre del producto':'Ayudin liquido          ','Categoria':'productos de limpieza','Precio': '00.50 ',  'Proveedor':'Faber castell ','Descuento':'NO EN DESCUENTO |'},
    '83837': {'Codigo': '83837', 'Fecha de vencimiento': '04/07/2023', 'Nombre del producto':'Sapolio limpiatodo 5L   ','Categoria':'productos de limpieza','Precio': '15.50 ',  'Proveedor':'Sapolio       ','Descuento':'NO EN DESCUENTO |'},
    '43851': {'Codigo': '43851', 'Fecha de vencimiento': '17/03/2023', 'Nombre del producto':'Sapolio Limpiavidrios   ','Categoria':'productos de limpieza','Precio': '11.50 ',  'Proveedor':'Sapolio       ','Descuento':'NO EN DESCUENTO |'},
    '73865': {'Codigo': '73865', 'Fecha de vencimiento': '11/04/2023', 'Nombre del producto':'Sap. limpiador en polvo ','Categoria':'productos de limpieza','Precio': '09.50 ',  'Proveedor':'Sapolio       ','Descuento':'NO EN DESCUENTO |'},
    '38794': {'Codigo': '38794', 'Fecha de vencimiento': '04/07/2023', 'Nombre del producto':'Limpiador multiusos     ','Categoria':'productos de limpieza','Precio': '22.00 ',  'Proveedor':'Knauf         ','Descuento':'NO EN DESCUENTO |'},
    '49418': {'Codigo': '49418', 'Fecha de vencimiento': 'No expira ', 'Nombre del producto':'Cepillo de dientes colg.','Categoria':'higiene personal     ','Precio': '13.50 ',  'Proveedor':'Colgate       ','Descuento':'NO EN DESCUENTO |'},
    '48596': {'Codigo': '48596', 'Fecha de vencimiento': '25/02/2028', 'Nombre del producto':'Pasta dental colgate    ','Categoria':'higiene personal     ','Precio': '07.50 ',  'Proveedor':'Colgate       ','Descuento':'NO EN DESCUENTO |'},
    '47773': {'Codigo': '47773', 'Fecha de vencimiento': '01/03/2028', 'Nombre del producto':'Listerine colgate       ','Categoria':'higiene personal     ','Precio': '16.50 ',  'Proveedor':'Colgate       ','Descuento':'NO EN DESCUENTO |'},
    '46952': {'Codigo': '46952', 'Fecha de vencimiento': '20/09/2024', 'Nombre del producto':'Toallas higienicas      ','Categoria':'higiene personal     ','Precio': '08.90 ',  'Proveedor':'Nosotras      ','Descuento':'NO EN DESCUENTO |'},
    '54613': {'Codigo': '54613', 'Fecha de vencimiento': '03/12/2024', 'Nombre del producto':'tampones nosotras       ','Categoria':'higiene personal     ','Precio': '13.50 ',  'Proveedor':'Nosotras      ','Descuento':'NO EN DESCUENTO |'},
    '94531': {'Codigo': '94531', 'Fecha de vencimiento': '14/07/2028', 'Nombre del producto':'Jabon moclear           ','Categoria':'higiene personal     ','Precio': '00.50 ',  'Proveedor':'Grupo cala    ','Descuento':'NO EN DESCUENTO |'},
    '44459': {'Codigo': '44459', 'Fecha de vencimiento': '20/09/2024', 'Nombre del producto':'Jabon Intimo            ','Categoria':'higiene personal     ','Precio': '12.50 ',  'Proveedor':'Grupo cala    ','Descuento':'NO EN DESCUENTO |'},
    '43677': {'Codigo': '43677', 'Fecha de vencimiento': '03/12/2024', 'Nombre del producto':'Rasuradora Flex3        ','Categoria':'higiene personal     ','Precio': '03.80 ',  'Proveedor':'Bic           ','Descuento':'NO EN DESCUENTO |'},
    '42853': {'Codigo': '42853', 'Fecha de vencimiento': '14/07/2028', 'Nombre del producto':'Desodorante             ','Categoria':'higiene personal     ','Precio': '07.50 ',  'Proveedor':'Care          ','Descuento':'NO EN DESCUENTO |'},
    '42903': {'Codigo': '42903', 'Fecha de vencimiento': '20/09/2024', 'Nombre del producto':'Enjuague Bucal          ','Categoria':'higiene personal     ','Precio': '09.50 ',  'Proveedor':'Colgate       ','Descuento':'NO EN DESCUENTO |'},
    '57958': {'Codigo': '57958', 'Fecha de vencimiento': '01/03/2023', 'Nombre del producto':'Chetos                  ','Categoria':'snacks               ','Precio': '03.50 ',  'Proveedor':'AMENA PepsiCo ','Descuento':'NO EN DESCUENTO |'},
    '58758': {'Codigo': '58758', 'Fecha de vencimiento': '17/04/2023', 'Nombre del producto':'Picaras                 ','Categoria':'snacks               ','Precio': '05.50 ',  'Proveedor':'Nestlé        ','Descuento':'NO EN DESCUENTO |'},
    '59550': {'Codigo': '59550', 'Fecha de vencimiento': '15/05/2023', 'Nombre del producto':'Morochas                ','Categoria':'snacks               ','Precio': '02.50 ',  'Proveedor':'Nestlé        ','Descuento':'NO EN DESCUENTO |'},
    '60357': {'Codigo': '60357', 'Fecha de vencimiento': '01/03/2023', 'Nombre del producto':'Lays                    ','Categoria':'snacks               ','Precio': '01.50 ',  'Proveedor':'Lays          ','Descuento':'NO EN DESCUENTO |'},
    '66115': {'Codigo': '66115', 'Fecha de vencimiento': '17/04/2023', 'Nombre del producto':'Piqueo                  ','Categoria':'snacks               ','Precio': '03.50 ',  'Proveedor':'Lays          ','Descuento':'NO EN DESCUENTO |'},
    '61956': {'Codigo': '61956', 'Fecha de vencimiento': '15/05/2023', 'Nombre del producto':'Chips haoy              ','Categoria':'snacks               ','Precio': '05.70 ',  'Proveedor':'El valle      ','Descuento':'NO EN DESCUENTO |'},
    '62758': {'Codigo': '62758', 'Fecha de vencimiento': '01/03/2023', 'Nombre del producto':'Bombones                ','Categoria':'snacks               ','Precio': '06.20 ',  'Proveedor':'Inka          ','Descuento':'NO EN DESCUENTO |'},
    '63551': {'Codigo': '63551', 'Fecha de vencimiento': '17/04/2023', 'Nombre del producto':'Ruffles                 ','Categoria':'snacks               ','Precio': '03.50 ',  'Proveedor':'Lays          ','Descuento':'NO EN DESCUENTO |'},
    '64352': {'Codigo': '64352', 'Fecha de vencimiento': '15/05/2023', 'Nombre del producto':'Doritos                 ','Categoria':'snacks               ','Precio': '02.80 ',  'Proveedor':'Frito-lay     ','Descuento':'NO EN DESCUENTO |'},
    '65102': {'Codigo': '65102', 'Fecha de vencimiento': '01/03/2023', 'Nombre del producto':'Snickers                ','Categoria':'snacks               ','Precio': '03.60 ',  'Proveedor':'QuimiNet      ','Descuento':'NO EN DESCUENTO |'}   
     
}

while (contador != 4): 
    print(' ') 
    print('Welcome to our Program...')
    print('')
    print("""     ./\_/\.
     ( o.o )
      >^<^<
    """)
    print(' ')
    print('  ' + '  ' + 'El menú')
    print(' ')
    print('     ' + '**********************')
    print('     ' + '*    ' + '0. Salir' + '        *')
    print('     ' + '*    ' + '1. Agregar' + '      *')
    print('     ' + '*    ' +'2. Modificar' + '    *')
    print('     ' + '*    ' +  '3. Eliminar' + '     *')
    print('     ' + '*    ' + '4. Buscar' + '       *')
    print('     ' + '**********************')
    print(' ')

    
    opcion = int(input('Opción: '))
    
    if(opcion == 0):
        print("+-------+------------+--------------------------+-----------------------+--------+----------------+-----------------+")
        print('|CÓDIGO',"|F. V.      ",'|NOMBRE DEL PRODUCTO      ', '|CATEGORIA             ','|PRICE  ','|PROVEEDOR ','     |DESCUENTO        |',)
       

        for key, value in Agenda.items():
            print("+-------+------------+--------------------------+-----------------------+--------+----------------+-----------------+")
            for inner_key, inner_value in value.items():
                
                
                print("|", "{}".format(inner_value), end=" " )
            
            print("+-------+------------+--------------------------+-----------------------+--------+----------------+-----------------+")
        
        if contador == 0:
            print(' ')
            print(' ')
            print('Gracias por utilizar el programa')

        else: 
            print('Opción invalida')
            
        
    elif (opcion == 1):
        
        
        while True:
            Codigo=input("Ingrese el Codigo (5 caracteres): ").rstrip()#eliminar caracteres adicionales
            if len(Codigo)==5:
                break
        print(" ")

        
        if (Codigo in Agenda.keys()):
            print("Este Codigo ya existe...")
        
        else: 
            
            while True:
                fv=input("Ingrese la Fecha de vencimiento(dia/mes/año): ").rstrip()
                coincide = re.match(r"\d\d/\d\d/\d\d\d\d", fv)
                if coincide:
                    fv = fv
                if len(fv)==10: #10 caracteres
                    break
            print(" ")
            
            while True:
                pname=input("Nombre del producto: ").rstrip() #eliminar caracteres adicionales
                if len(pname) <= 24:
                    pname = pname.rjust(24, " ") #Añadir spacios en blanco para completar a 24   
                    break
            print(" ")
        
            while True:
                Categoria=input("Ingrese Categoria:").rstrip() #21
                if len(Categoria) <= 21:
                    Categoria = Categoria.rjust(21, " ") #Añadir spacios en blanco para completar a 21
                    break
            
            while True:
                Precio=input("Ingrese  su Precio (S/00.00): ") #6
                if len(Precio) <= 6:
                    Precio = Precio.rjust(6, " ") #Añadir spacios en blanco para completar a 6
                    break
            print(" ")

            while True:
                proveedor=input("Ingrese el Proveedor: ") #14
                if len(proveedor) <= 14:
                    proveedor = proveedor.rjust(14, " ") #Añadir spacios en blanco para completar a 6
                    break
            print(" ")
            
            while True:
                descuento=input('Ingrese el Descuento (DESCUENTO/NO DESCUENTO): ').rstrip() #16
                while descuento != "DESCUENTO" and descuento != "NO DESCUENTO":
                    print("Por favor ingrese un valor válido (DESCUENTO/NO DESCUENTO)")
                    descuento = input('Ingrese el Descuento (DESCUENTO/NO DESCUENTO): ')
                if len(descuento) <= 16:
                    descuento = descuento.rjust(16, " ") #Añadir spacios en blanco para completar a 6
                    break
            print(" ")
            producto={"Codigo":Codigo,"Fecha de vencimiento":fv, "Nombre del producto":pname,"Categoria":Categoria,"Precio":Precio,"Proveedor":proveedor , "Descuento": descuento}
        
            Agenda[Codigo] = producto
            print('Agregado correctamente...')


    elif(opcion == 2):
        Codigo=input("Ingrese Codigo a modificar: ")
        if (Codigo in Agenda.keys()):
            print("Este Codigo ya existe...")
            
        if Codigo in Agenda:
            while True:
                Codigo=input("Ingrese el Nuevo Código  (5 caracteres): ").rstrip()#eliminar caracteres adicionales
                if len(Codigo)==5:
                    break
            
            print(" ")
            while True:
                fv=input("Ingrese la Fecha de vencimiento(dia/mes/año): ").rstrip()
                coincide = re.match(r"\d\d/\d\d/\d\d\d\d", fv)
                if coincide:
                    fv = fv
                if len(fv)==10:
                    break
            print(" ")
            while True:
                pname=input("Nombre del producto: ").rstrip() #eliminar caracteres adicionales
                if len(pname) <= 24:
                    pname = pname.rjust(24, " ") #Añadir spacios en blanco para completar a 24
                    break
            print(" ")
            while True:
                Categoria=input("Ingrese Categoria:").rstrip() #21
                if len(Categoria) <= 21:
                    Categoria = Categoria.rjust(21, " ") #Añadir spacios en blanco para completar a 21
                    break
            print(" ")
            while True:
                Precio=input("Ingrese  su Precio:") #6
                if len(Precio) <= 6:
                    Precio = Precio.rjust(6, " ") #Añadir spacios en blanco para completar a 6
                    break
            print(" ")
            while True:
                proveedor=input("Ingrese el Proveedor: ") #14
                if len(proveedor) <= 14:
                    proveedor = proveedor.rjust(14, " ") #Añadir spacios en blanco para completar a 6
                    break
            print(" ")
            while True:
                descuento=input('Ingrese el Descuento (DESCUENTO/NO DESCUENTO): ').rstrip() #16
                while descuento != "DESCUENTO" and descuento != "NO DESCUENTO":
                    print("Por favor ingrese un valor válido (DESCUENTO/NO DESCUENTO)")
                    descuento = input('Ingrese el Descuento (DESCUENTO/NO DESCUENTO): ')
                if len(descuento) <= 16:
                    descuento = descuento.rjust(16, " ") #Añadir spacios en blanco para completar a 6
                    break
            print(" ")
            producto={"Codigo":Codigo,"Fecha de vencimiento":fv, "Nombre del producto":pname,"Categoria":Categoria,"Precio":Precio,"Proveedor":proveedor , "Descuento": descuento}
        
            Agenda[Codigo]=producto
            print('Modificado correctamente...')
        
        
    elif(opcion == 3):
         Codigo=input("Ingrese Codigo a eliminar: ")
         if Codigo in Agenda:
            bool = input('Desea eliminar de forma permanente (si/no): ')
            if(bool == 'si'):
                del Agenda[Codigo]
                print('Eliminado correctamente..')
            else:
                print('Cancelado')
            print('')
            
         else:
             print("No existe")
            
    elif(opcion == 4):
        
        Codigo = input('Ingrese el ID a buscar: ')
        
        if Codigo in Agenda:
            
            diccionario_deseado = Agenda[Codigo]
            print(" ")
            print('El Código buscado es: ', Codigo)
            
            for inner_key, inner_value in diccionario_deseado.items():
                print("")
                print("#", "{}"  "{}".format(' ' + inner_key, '   =>  ' + inner_value ))

   
            print(" ")
            print(" ") 
  
        else:
            print('No existe!')



        
