# FUNDAMENTOS MATEMÁTICOS DE LOS SISTEMAS DE DATOS
# PRACTICA 4
# TRABAJO REALIZADO POR NATALIA RUIZ MARTÍNEZ Y MIGUEL ZAMUDIO PÉREZ

import sqlite3
import os
            
# Se usa para incluir cadenas en la orden sql a ejecutar
def aux(x):
    return '"'+x+'"'

# Comprueba la existencia del dato dado en la tabla, para tablas que tengan un solo atributo como clave primaria
def comprobar_existencia(dato,clavep,tabla):
    A=[]
    con = sqlite3.connect('congreso.datos')
    with con:
        cur = con.cursor()
        cur.execute('select '+clavep+' from '+tabla)
        A = cur.fetchall()
    con.close() 
    
    for i in range(len(A)):
        if dato==A[i][0]:
            return 1 #Existe
    return 0 #No existe

# Comprueba la existencia de los datos dados en la tabla, para tablas que tengan dos atributos como clave primaria
def comprobar_existencia2(nom,org,clave1,clave2,tabla):
    A=[]
    con = sqlite3.connect('congreso.datos')
    with con:
        cur = con.cursor()
        cur.execute('select '+clave1+','+clave2+' from '+tabla+'')
        A = cur.fetchall()
    con.close() 
    
    for i in range(len(A)):
        if nom==A[i][0] and org==A[i][1]:
            return 1 #Existe
    return 0 #No existe

# Eliminar datos en la tabla dada
def eliminar(dato,clavep,tabla):
    con = sqlite3.connect('congreso.datos')
    with con:
        cur = con.cursor()
        if dato==str(dato):
            cur.execute('delete from '+tabla+' where '+clavep+'='+aux(dato))
        else:
            cur.execute('delete from '+tabla+' where '+clavep+'='+str(dato))
    con.close()
    
# Cuenta los datos distintos que hay en una lista
def contardato(dato,lista):
    A=[]
    con = sqlite3.connect('congreso.datos')
    with con:
        cur = con.cursor()
        cur.execute('select count(distinct '+dato+') from '+lista+'')
        A = cur.fetchall()
    con.close() 
    return A[0][0]

# Registra a una persona en la tabla REGISTRADOS (opcion 1)
def insertar_registrado(nombre,uni,nac,email):
    con = sqlite3.connect('congreso.datos')
    with con:
        cur = con.cursor()
        cur.execute('insert into REGISTRADOS values('+aux(nombre)+','+aux(uni)+','+aux(nac)+','+aux(email)+')')
        con.commit() #es necesario si insertamos
    con.close()   
    
# Inserta los datos dados en la tabla SOCIOS(opcion 1)
def socios(email,sociedad):
    con = sqlite3.connect('congreso.datos')
    with con:
        cur = con.cursor()
        cur.execute('insert into SOCIOS values('+aux(email)+','+aux(sociedad)+')')
        con.commit()
    con.close()
    
# Inserta los datos dados en la tabla PAGOS (opcion 2)
def registrar_pagos(email,precio,forma_de_pago):
    con = sqlite3.connect('congreso.datos')
    with con:
        cur = con.cursor()
        cur.execute('insert into PAGOS values('+aux(email)+','+str(precio)+','+aux(forma_de_pago)+')')
        con.commit() 
    con.close()
    
# Inserta los datos dados en la tabla SESIONES (opcion 3)
def insertar_sesion(nombre,numero,organizador):
    con = sqlite3.connect('congreso.datos')
    with con:
        cur = con.cursor()
        cur.execute('insert into SESIONES values('+aux(nombre)+','+str(numero)+','+aux(organizador)+')')
        con.commit() #es necesario si insertamos
    con.close()
    
# Cuenta la cantidad de distintos numeros correspondientes a cada sesion que hay en la tabla SESIONES (opcion 3)
def contar_sesiones():
    A=[]
    con = sqlite3.connect('congreso.datos')
    with con:
        cur = con.cursor()
        cur.execute('select count(distinct numero) from SESIONES')
        A = cur.fetchall()
    con.close() 
    return A[0][0]

# Cuenta la cantidad de nombres de la tabla SESIONES que corresponden con el dado (opcion 3)
def contar_nombre(nom):
    A=[]
    con = sqlite3.connect('congreso.datos')
    with con:
        cur = con.cursor()
        cur.execute('select count(nombre) from SESIONES where nombre='+aux(nom))
        A = cur.fetchall()
    con.close() 
    return A[0][0]

# Devuelve los distintos numeros de la tabla SESIONES donde el nombre correspondiente corresponde con el dado (opciones 3 y 6)
def numerosesion(nombre):
    A=[]
    con = sqlite3.connect('congreso.datos')
    with con:
        cur = con.cursor()
        cur.execute('select distinct numero from SESIONES where nombre='+aux(nombre))
        A = cur.fetchall()
    con.close() 
    return A[0][0]

# Inserta los datos dados en la tabla AULA (opcion 4)
def insertar_aula(codigo,capacidad):
    con = sqlite3.connect('congreso.datos')
    with con:
        cur = con.cursor()
        cur.execute('insert into AULA values('+str(codigo)+','+str(capacidad)+')')
        con.commit() 
    con.close()
    
# Inserta los datos dados en la tabla CHARLAS (opcion 5)
def insertar_charla(titulo,numero_sesion_especial,hora_inicio,hora_fin,cod_aula,emailPonente):
    con = sqlite3.connect('congreso.datos')
    with con:
        cur = con.cursor()
        cur.execute('insert into CHARLAS values('+aux(titulo)+','+str(numero_sesion_especial)+','+aux(hora_inicio)+','+aux(hora_fin)+','+str(cod_aula)+','+aux(emailPonente)+')')
        con.commit() 
    con.close()
    
# Devuelve los titulos de charlas de la tabla CHARLAS donde el numero de sesion especial corresponde con el dado (opcion 6)
def lista_charlas(numero):
    A=[]
    con = sqlite3.connect('congreso.datos')
    with con:
        cur = con.cursor()
        cur.execute('select titulo from CHARLAS where numero_sesion_especial='+str(numero))
        A = cur.fetchall()
    con.close()  
    return A

# Devuelve los datos de la tabla PAGOS donde el email de la tabla corresponde con el dado (opcion 7)
def busqueda_por_email(email):
    A=[]
    if comprobar_existencia(email,'email','PAGOS')==1:
        con = sqlite3.connect('congreso.datos')
        with con:
            cur = con.cursor()
            cur.execute('select * from PAGOS where email='+aux(email))
            A = cur.fetchall()
        con.close()
    
    return A

# Primero selecciona el email de la tabla REGISTRADOS cuyo nombre se corresponda con el dado y lo usamos en la funcion anterior para obtener los mismos datos (opcion 7)
def busqueda_por_nombre(nombre):
    A=[]
    con = sqlite3.connect('congreso.datos')
    with con:
        cur = con.cursor()
        cur.execute('select email from REGISTRADOS where nombre='+aux(nombre))
        A = cur.fetchall()
        A = busqueda_por_email(A[0][0])
    con.close()
    return A

def opcion1():
    
    # Pedimos que elija una opcion: insertar, eliminar o volver al menu (en caso de haberse equivocado de opcion)
    n=input('Si desea insertar pulse 1, si desea eliminar pulse 2, si desea volver al menu pulse 0: ')
    
    # Si no da ninguna de las tres opciones, volvemos a pedirlo
    while n != '0' and n != '1' and n != '2':
        n=input('\nNo es una de las opciones. Intenta otra vez.\nSi desea insertar pulse 1, si desea eliminar pulse 2, si desea volver al menu pulse 0: ')

    if n=='1': # Opcion de anadir
        print('----------------------')
        print('INTRODUCCION DE DATOS:')
        print('----------------------')


        x=True
        while x: # Pedimos el email
            
            email=input('Introduce el email: ')
            
            if comprobar_existencia(email,'email','REGISTRADOS')==1: # Si ya existe
                # Damos la opcion de salir o de volver a introducir
                g=input('\nEl email ya existe.\n-Si quieres probar a introducir otro, pulsa 1.\n-Si lo que quieres es salir de esta opcion del menu pulsa cualquier otra tecla.\n')
                if g!='1':
                     x=False

            else: # Si no existe insertamos los datos
                
                nombre=input('Introduce el nombre: ')
                universidad=input('Introduce la universidad: ')
                nacionalidad=input('Introduce la nacionalidad: ')
            
                insertar_registrado(nombre,universidad,nacionalidad,email)
                print('\nDatos insertados.\n')
            
                # Damos la opcion de que la persona registrada sea socio
                socio=input('Si la persona es socio pulsa 1, si no, pulsa cualquier tecla: ')
                if socio=='1':
                
                    # Pedimos el nombre de la sociedad hasta que den uno de los dos correctos
                    sociedad=input('\nIntroduce la sociedad a la que pertenece (ES para la espanola y BR para la brasilena): ')
                    while sociedad!='ES' and sociedad!='BR': 
                        sociedad=input('\nNo valido. Debe ser ES para la espanola y BR para la brasilena: ')
                    
                    socios(email,sociedad)
                    print('\nDatos insertados.\n')
                
                x=False
  
    elif n=='2': # Opcion de eliminar
        if contardato('email','REGISTRADOS')==0: # Si no email en la tabla REGISTRADOS, no hay nada que eliminar
            print('\nNo hay personas para eliminar.\n')

        else: # Si hay
            x=True
            while x: # Pedimos el email
                email=input('Introduce el email: ')
            
                if comprobar_existencia(email,'email','REGISTRADOS')==1: # Si existe se elimina de la tabla REGISTRADOS
                    eliminar(email,'email','REGISTRADOS')
                
                    if comprobar_existencia(email,'email','SOCIOS')==1: # Si es socio se elimina de la tabla SOCIOS
                        eliminar(email,'email','SOCIOS')
                    
                    x=False
                    print('\nDatos eliminados.\n')
                
                else: # Si no esta en la tabla, damos la opcion de escribir otro o terminar la opcion
                    g=input('\nEl email no existe.\n-(Observacion): si no te sabes ningun email registrado, puedes registrar uno nuevo volviendo al menu.\n-Si quieres probar a introducir otro, pulsa 1.\n-Si lo que quieres es salir de esta opcion del menu pulsa cualquier otra tecla.\n')
                    if g!='1':
                        x=False                
                        
    else: # Opcion menu
        main()

            
    # Opcion para volver al menu
    if n=='1' or n=='2':
        j=input('\nSi desea volver al menu pulsa 0: ')
        if j=='0':
            main()
        else:
            print('Se acabo el programa.')
            
def opcion2(): 
    
    #Pedimos que elija una opcion: volver al menu o seguir
    n=input('\nSi se ha equivocado de opcion puede volver al menu pulsando 0, si quiere seguir adelante pulse cualquier otra tecla: ')
    if n != '0':
        x = True
        while x: # Pedimos el email y comprobamos si existe y si ya tiene un pago asociado en caso de existir
            email = input('\nDime el email : ')
        
            if comprobar_existencia(email,'email','REGISTRADOS')==0:
                # Si no existe damos la opcion de escribir otro o terminar la opcion
                g=input('\nEl email no existe.\n-(Observacion): si no te sabes ningun email registrado, puedes registrar uno nuevo volviendo al menu.\n-Si quieres probar a introducir otro, pulsa 1.\n-Si lo que quieres es salir de esta opcion del menu pulsa cualquier otra tecla.\n')
                if g!='1':
                    x=False 

            elif comprobar_existencia(email,'email','PAGOS')==1:
                # Si ya tiene asociado un pago damos la opcion de escribir otro o terminar la opcion
                g=input('\nEl email ya tiene un pago asociado.\n-Si quieres probar a introducir otro, pulsa 1.\n-Si lo que quieres es salir de esta opcion del menu pulsa cualquier otra tecla.\n')
                if g!='1':
                    x=False
            
            else: # Si el email esta y no tiene pago asociado lo asociamos a uno
                y = True    
                while y: # Comprobamos que la cantidad que pagan sea 160 o 180
                    precio = input('\n¿Ha pagado 160 o 180 euros?: ')
                    try:
                        precio = int(precio)
                        if precio!= 160 and precio != 180:
                            print('\nSolo es posible pagar 160 o 180 euros.\n')
                        else:
                            y = False
                    except:
                        print('\nPor favor ingrese un número.')
            
            
                # Pedimos la forma de pago, si la dan mal la volvemos a pedir
                forma_de_pago = input('¿Qué forma de pago se ha empleado?.\nPulse TR para transferencia, PA para paypal o TA para tarjeta bancaria: ')
    
                while forma_de_pago!='TR' and forma_de_pago!='PA' and forma_de_pago!='TA':
                    forma_de_pago = input('Forma no válida.\nPulse TR para transferencia, PA para paypal o TA para tarjeta bancaria: ')
 
    
                registrar_pagos(email,precio,forma_de_pago)
                print('\nPago registrado.\n')
    
                x = False
                
        # Opcion para volver al menu
        j=input('\nSi desea volver al menu pulsa 0: ')
        if j=='0':
            main()
        else:
            print('Se acabo el programa.')
            
    else: # Opcion menu
        main()
        
def opcion3():
    
    # Pedimos que elija una opcion: insertar, eliminar o volver al menu
    n=input('Si desea insertar pulse 1, si desea eliminar pulse 2, si desea volver al menu pulse 0: ')
    
    # Si no da ninguna de las tres opciones, volvemos a pedirlo
    while n != '0' and n != '1' and n != '2':
        n=input('\nNo es una de las opciones. Intenta otra vez.\nSi desea insertar pulse 1, si desea eliminar pulse 2, si desea volver al menu pulse 0: ')
        
        
    if n=='1': # Opcion de anadir
        if contardato('numero','SESIONES')==4: # Si ya hay 4 sesiones 
            cont=input('\nEl numero maximo de sesiones es 4:\n-Si quieres incluir una nueva debes eliminar antes otra,\n-Si lo que quieres es incluir otro organizador (como maximo puede haber dos por cada sesion) pulsa 1,\n-Si no, pulsa cualquier otra tecla: ')
            
            if cont=='1': # Si quiere incluir otro organizador
                c=True
                while c:
                    nombre=input('\nDeme el nombre de la sesion: ')
        
                    # Comprobamos si el nombre esta en la tabla
                    if comprobar_existencia(nombre,'nombre','SESIONES')==1: #El nombre esta
                    
                        # Vemos cuantos organizadores tiene esa sesion (pueden ser 1 o 2)
                        if contar_nombre(nombre)==1: # Tiene un organizador
                            x=True
                            while x: 
                                organizador=input('Deme el email del organizador de la sesion: ')
                                
                                # Vemos si el par del nombre y organizador esta en la lista
                                if comprobar_existencia2(nombre,organizador,'nombre','organizador','SESIONES')==1:
                                    g=input('\nEl par formado por el nombre de la sesion y el email del organizador ya existe.\n-Si quieres anadir otro organizador para esta sesion pulsa 1.\n-Si lo que quieres es salir de esta opcion del menu pulsa cualquier otra tecla.\n')
                                    if g!='1':
                                        x=False
                                # Vemos si el email dado esta registrado
                                elif comprobar_existencia(organizador,'email','REGISTRADOS')==0:                                     
                                    g=input('\nEl email no esta registrado.\n-(Observacion): si no te sabes ningun email registrado, puedes registrar uno nuevo volviendo al menu.\n-Si quieres probar a introducir otro, pulsa 1.\n-Si lo que quieres es salir de esta opcion del menu pulsa cualquier otra tecla.\n')
                                    if g!='1':
                                        x=False
                                        
                                else:
                                    numero=numerosesion(nombre)
                                    insertar_sesion(nombre,numero,organizador)                            
                                    x=False
                            
                  
                        else: # Tiene dos organizadores
                            print('\nEsta sesion ya tiene dos organizadores, no se pueden anadir mas.\n')
                
                        c=False
            
                    else: # El nombre no esta
                        print('\nEl nombre no existe')
                        

        else: # El numero de sesiones existente es menor que 4
            
            # Pedimos nombre de sesion y organizador
            nombre=input('\nDeme el nombre de la sesion: ')
            
            x=True
            while x:
                organizador=input('Deme el email del organizador de la sesion: ')
                
                # Vemos si el par nombre-organizador existe
                if comprobar_existencia2(nombre,organizador,'nombre','organizador','SESIONES')==1:
                    # Si ya existe damos opcion de escribir otro o terminar la opcion
                    g=input('\nEl par formado por el nombre de la sesion y el email del organizador ya existe.\n-Si quieres anadir otros datos pulsa 1.\n-Si lo que quieres es salir de esta opcion del menu pulsa cualquier otra tecla.\n')
                    if g!='1':
                        x=False
                        
                # Vemos si el email dado existe
                elif comprobar_existencia(organizador,'email','REGISTRADOS')==0: 
                    # Si no existe damos opcion de escribir otro o terminar la opcion
                    g=input('\nEl email no esta registrado.\n-(Observacion): si no te sabes ningun email registrado, puedes registrar uno nuevo volviendo al menu.\n-Si quieres probar a introducir otro, pulsa 1.\n-Si lo que quieres es salir de esta opcion del menu pulsa cualquier otra tecla.\n')
                    if g!='1':
                        x=False
                
                else: # Si el email existe pero no esta ya asociado a ningun nombre insertamos los datos
                    x=False
                        
                    #numeroSesion
                    y=True
                    while y: # El numero debe estar entre 1 y 4
                        numero=input('Deme el numero de la sesion (entre 1 y 4): ')
                        try:
                            numero=int(numero)
                            if numero>0 and numero<5:
                                if comprobar_existencia(numero,'numero','SESIONES')==1:
                                    print('\nEste numero ya esta asociado a una sesion.\n')
                                else:
                                    y=False
                            else:
                                print('\nEl numero debe estar entre 1 y 4.\n')
                        except:
                            print('Introduce un numero.\n')
        
                    insertar_sesion(nombre,numero,organizador)
                    print('\nDatos insertados.\n')
        
    elif n=='2': # Opcion de eliminar
        if contardato('numero','SESIONES')==0: # Si no hay sesiones no podemos eliminar nada
            print('\nNo hay sesiones para eliminar.\n')
            
        else: # Si hay sesiones
            x=True
            while x:
                nombre=input('Deme el nombre de la sesion: ')
            
                if comprobar_existencia(nombre,'nombre','SESIONES')==1: # Si existe se elimina
                    eliminar(nombre,'nombre','SESIONES')
                
                    x=False
                    print('\nDatos eliminados.\n')
                
                else: # Si no existe damos opcion de escribir otra o terminar la opcion
                    d=input('\nEl par de nombre de la sesion y organizador no existe.\n-Si quieres probar a escribir otro, pulsa 1.\n-Si lo que quieres es salir de esta opcion del menu pulsa cualquier otra tecla.\n')
                    if d!='1':
                        x=False
    
    else: # Opcion menu
        main()
     
    if n=='1' or n=='2':
        j=input('\nSi desea volver al menu pulsa 0: ')
        if j=='0':
            main()
        else:
            print('Se acabo el programa.')
            
def opcion4():
    
    # Pedimos que elija una opcion: insertar, eliminar o volver al menu
    n=input('Si desea insertar pulse 1, si desea eliminar pulse 2, si desea volver al menu pulse 0: ')
    
    # Si no da ninguna de las tres opciones, volvemos a pedirlo
    while n != '0' and n != '1' and n != '2':
        n=input('\nNo es una de las opciones. Intenta otra vez.\nSi desea insertar pulse 1, si desea eliminar pulse 2, si desea volver al menu pulse 0: ')
        
    if n=='1': # Opcion de anadir
        if contardato('codigo','AULA')==2: # Si el numero de aulas es 2 no podemos seguir
            print('\nEl numero maximo de aulas es 2. Si quieres incluir una nueva debes eliminar antes otra.\n ')
            
        else: # Si es menor que 2 seguimos
            print('----------------------')
            print('INTRODUCCION DE DATOS:')
            print('----------------------')
            x=True
            while x: # Pedimos el codigo del aula
                codigo=input('\nDeme el código del aula: ')
                try: 
                    codigo = int(codigo)
                    if codigo!=1 and codigo!=2: # El codigo debe ser 1 o 2
                        print('\nEl codigo debe ser 1 o 2.\n')
                    else:
                        if comprobar_existencia(codigo,'codigo','AULA')==1:
                            # Si ya existe damos opcion de escribir otro o terminar la opcion
                            g=input('\nEl codigo ya existe.\n-Si quieres probar a introducir otro, pulsa 1.\n-Si lo que quieres es salir de esta opcion del menu pulsa cualquier otra tecla.\n')
                            if g!='1':
                                x=False
                        
                        else: # Si no existia pedimos la capacidad del aula
                            y = True
                            while y:
                                capacidad=input('Deme la capacidad del aula: ')
                                try:
                                    capacidad=int(capacidad)
                                    y=False
                                except:
                                    print('\nIntroduce un numero.\n')
                    
                            insertar_aula(codigo,capacidad)
            
                            print('\nDatos insertados.\n')
                            
                            x=False 
                except:
                    print('\nPonga un numero.\n')
                
                            
    elif n=='2': # Opcion de eliminar
        if contardato('codigo','AULA')==0: # Si no hay aulas no podemos eliminar nada
            print('\nNo hay aulas para eliminar.\n')
            
        else:
            p=True
            while p:
                x = True
                while x: # Pedimos el codigo del aula
                    codigo=input('\nDeme el codigo del aula: ')
                    try:
                        codigo = int(codigo)
                        x = False
                    except:
                        print('\nIntroduzca un número.\n')
            
                if comprobar_existencia(codigo,'codigo','AULA')==1: # Si el codigo existe, eliminamos        
                    eliminar(codigo,'codigo','AULA')
                    print('\nDatos eliminados.\n')
                    p=False
                
                else: # Si no existe damos opcion de escribir otro o terminar la opcion
                    g=input('\nEl codigo no esta registrado.\n-(Observacion): si no te sabes ningun codigo, puedes registrar uno nuevo volviendo al menu.\n-Si quieres probar a introducir otro, pulsa 1.\n-Si lo que quieres es salir de esta opcion del menu pulsa cualquier otra tecla.\n')
                    if g!='1':
                        p=False
                                
    else: # Opcion menu
        main()

    # Opcion para volver al menu
    if n=='1' or n=='2':
        j=input('\nSi desea volver al menu pulsa 0: ')
        if j=='0':
            main()
        else:
            print('Se acabo el programa.')
            
def opcion5():
    
    # Pedimos que elija una opcion: insertar, eliminar o volver al menu
    n=input('Si desea insertar pulse 1, si desea eliminar pulse 2, si desea volver al menu pulse 0: ')
    
    # Si no da ninguna de las tres opciones, volvemos a pedirlo
    while n != '0' and n != '1' and n != '2':
        n=input('\nNo es una de las opciones. Intenta otra vez.\nSi desea insertar pulse 1, si desea eliminar pulse 2, si desea volver al menu pulse 0: ')
         
    if n=='1': # Opcion de anadir
        
        print('----------------------')
        print('INTRODUCCION DE DATOS:')
        print('----------------------')
        
        # Pedimos el nombre de la charla
        titulo=input('Deme el nombre de la charla: ')
            
        x=True
        while x: # Solo hay 4 sesiones asi que el numero pedido debe estar entre el 1 y el 4
            numero_sesion_especial=input('Deme el número de sesión especial: ')
            try: 
                numero_sesion_especial = int(numero_sesion_especial)
                   
                if numero_sesion_especial<1 or numero_sesion_especial>4:
                    print('\nIntroduzca un número entero entre el 1 y el 4.')
                else:
                     x = False
            except:
                print('\nPonga un numero.\n')
                    
                    
        # Pedimos las horas y minutos teniendo en cuenta el rango de hora real: el rango de la hora entre 0 y 23, el de minutos entre 0 y 59

        hora_aux = True
        while hora_aux:
            hora = input('Deme la hora de inicio (debe ser un numero entero entre 0 y 23): ')
            try:
                hora = int(hora)
                if hora >= 0 and hora < 24:
                    hora_aux = False
                else:
                    print('\nHora fuera de rango.\n')
            except:
                print('\nIntroduce un numero.\n')
                    
        hora_aux = True
        while hora_aux:
            minutos = input('Deme los minutos de inicio (debe ser un numero entero entre 0 y 59): ')
            try:
                minutos = int(minutos)
                if minutos >= 0 and minutos < 59:
                    hora_aux = False
                else:
                    print('\nMinutos fuera de rango.\n')
            except:
                print('\nIntroduce un numero.\n')           
        
        # Unimos la hora y minutos en formato hh:mm
        hora_inicio = str(hora)+':'+str(minutos)
            
                
        hora_aux = True
        while hora_aux:
            hora = input('Deme la hora de finalización (debe ser un numero entero entre 0 y 23): ')
            try:
                hora = int(hora)
                if hora >= 0 and hora < 24:
                    hora_aux = False
                else:
                    print('\nHora fuera de rango.\n')
            except:
                print('Introduce un numero.\n')
                    
        hora_aux = True
        while hora_aux:
            minutos = input('Deme los minutos de finalización (debe ser un numero entero entre 0 y 59): ')
            try:
                minutos = int(minutos)
                if minutos >= 0 and minutos < 59:
                    hora_aux = False
                else:
                    print('\nMinutos fuera de rango.\n')
            except:
                print('Introduce un numero.\n')
                    
        # Unimos la hora y minutos en formato hh:mm
        hora_fin = str(hora)+':'+str(minutos)
                
        x = True
        while x: # Pedimos el codigo del aula que debe ser 1 o 2
            cod_aula=input('Deme el código del aula: ')
            try: 
                cod_aula = int(cod_aula)
                if cod_aula!=1 and cod_aula!=2: # El codigo debe ser 1 o 2
                    print('\nEl codigo del aula debe ser 1 o 2.\n')
                else:
                    x = False
                
            except:
                print('\nPonga un numero.\n')
    
        x = True
        while x: # Pedimos el email de la persona que da la charla teniendo en cuenta que debe estar registrado
            emailPonente = input('\nDime el email del ponente: ')
            if comprobar_existencia(emailPonente,'email','REGISTRADOS')==0:
                # Si no existe damos opcion de escribir otro o terminar la opcion
                g=input('\nEl email no esta registrado.\n-(Observacion): si no te sabes ningun email registrado, puedes registrar uno nuevo volviendo al menu.\n-Si quieres probar a introducir otro, pulsa 1.\n-Si lo que quieres es salir de esta opcion del menu pulsa cualquier otra tecla.\n')
                if g!='1':
                    x=False
                        
            else: # Si existe insertamos datos
                x = False
                insertar_charla(titulo,numero_sesion_especial,hora_inicio,hora_fin,cod_aula,emailPonente)
                print('\nDatos insertados.\n')
                        
            
            
    elif n=='2': # Opcion de eliminar
        x = True
        while x: # Pedimos el titulo de la charla a eliminar y comprobamos que exista
            titulo=input('Deme el título de la charla: ')
            if comprobar_existencia(titulo,'titulo','CHARLAS')==0:
                # Si no existe damos opcion de escribir otro o terminar la opcion
                g=input('\nEl titulo no existe.\n-Si quieres probar a introducir otro, pulsa 1.\n-Si lo que quieres es salir de esta opcion del menu pulsa cualquier otra tecla.\n')
                if g!='1':
                    x=False
            else: # Si existe, eliminamos
                x = False
                eliminar(titulo,'titulo','CHARLAS')
                print('\nDatos eliminados.\n')    
            
            
    else: # Opcion menu
        main()
            
    
    # Opcion para volver al menu
    if n=='1' or n=='2':
        j=input('\nSi desea volver al menu pulsa 0: ')
        if j=='0':
            main()
        else:
            print('Se acabo el programa.')
            
def opcion6(): 
    
    # Pedimos que elija una opcion: volver al menu o seguir
    n=input('\nSi se ha equivocado de opcion puede volver al menu pulsando 0, si quiere seguir adelante pulse cualquier otra tecla: ')
    
    if n != '0':
        x=True
        while x: # Pedimos nombre de sesion
            nombre=input('\nDame el nombre de la sesion para conocer sus titulos: ') 
            if comprobar_existencia(nombre,'nombre','SESIONES')==0: # Si no existe
                # Damos opcion de escribir otro o terminar la opcion
                g=input('\nLa sesion no existe.\n-Si quieres probar a introducir otro, pulsa 1.\n-Si lo que quieres es salir de esta opcion del menu pulsa cualquier otra tecla.\n')
                if g!='1':
                    x=False
                
            else: # Si existe mostramos las charlas de la sesion dada
                numero=numerosesion(nombre)
                lista=lista_charlas(numero)
                print('---------------------------------------')
                print('\n-------CHARLAS DE LA SESION DADA-------')
                print('\n---------------------------------------')
                for i in range(len(lista)):
                    print(lista[i][0])
                x=False

        # Opcion para volver al menu
        j=input('\nSi desea volver al menu pulsa 0: ')
        if j=='0':
            main()
        else:
            print('Se acabo el programa.') 
            
    else: # Opcion menu
        main()
        
def opcion7():
    
    # Pedimos que elija una opcion: introducir un nombre, un email o volver al menu
    n = input("\nPulse 1 si va a introducir el nombre.\nPulse 2 si va a introducir el email.\nPulse 0 si desea volver al menu.\n")
    
    # Si no da ninguna de las tres opciones, volvemos a pedirlo
    while n != '0' and n != '1' and n != '2':
        n=input('\nNo es una de las opciones. Intenta otra vez. Pulse 1 si va a introducir el nombre. Pulse 2 si va a introducir el email. Pulse 0 si desea volver al menu: ')
    
    if n == '1': # Se pide la informacion mediante el nombre
        datos=[]
        x=True
        while x:
            nombre = input('\nDigame el nombre a buscar: ')
            if comprobar_existencia(nombre,'nombre','REGISTRADOS')==0:
                # Si no existe damos opcion de escribir otro o terminar la opcion
                g=input('\nEl nombre no existe.\n-(Observacion): si no te sabes ningun nombre registrado, puedes registrar uno nuevo volviendo al menu.\n-Si quieres probar a introducir otro, pulsa 1.\n-Si lo que quieres es salir de esta opcion del menu pulsa cualquier otra tecla.\n')
                if g!='1':
                    x=False
            else: # Si el nombre existe puede ocurrir que no tenga un pago asociado
                datos = busqueda_por_nombre(nombre)
                if datos==[]:
                    print('\nEsa persona no tiene un pago asociado.\n')
                    
                else: # Si lo tiene, mostramos los datos
        
                    # Cambiamos TR, PA y TA por sus correspondientes significados
                    a=datos[0][2]
                    if a=='TR':
                        a='transferencia'
                    elif a=='PA':
                        a='paypal'
                    else:
                        a='tarjeta de credito'
            
                    print('--------------------------')
                    print('\n------DATOS DE PAGO-------')
                    print('\n--------------------------')
                    print('Nombre: '+nombre+'.\nPaga: '+str(datos[0][1])+' €.\nMétodo de pago: '+a)
                
                x=False
        
    elif n == '2': # Se pide la informacion mediante el email
        datos=[]
        x=True
        while x: 
            email = input('\nDigame el email a buscar: ')
            if comprobar_existencia(email,'email','REGISTRADOS')==0:
                # Si no existe damos opcion de escribir otro o terminar la opcion
                g=input('\nEl email no existe.\n-(Observacion): si no te sabes ningun email registrado, puedes registrar uno nuevo volviendo al menu.\n-Si quieres probar a introducir otro, pulsa 1.\n-Si lo que quieres es salir de esta opcion del menu pulsa cualquier otra tecla.\n')
                if g!='1':
                    x=False
            else: # Si el email existe puede ocurrir que no tenga un pago asociado
                datos = busqueda_por_email(email)
                if datos==[]:
                    print('\nEsa persona no tiene un pago asociado.\n')
                    
                else: # Si tiene un pago, mostramos los datos
                    
                    # Cambiamos TR, PA y TA por sus correspondientes significados
                    a=datos[0][2]
                    if a=='TR':
                        a='transferencia'
                    elif a=='PA':
                        a='paypal'
                    else:
                        a='tarjeta de credito'
        
                    print('--------------------------')
                    print('\n------DATOS DE PAGO-------')
                    print('\n--------------------------')
                    print('Email: '+email+'.\nPaga: '+str(datos[0][1])+' €.\nMétodo de pago: '+a)
                
                x=False
            
    else: # Opcion menu
        main()
        
    # Opcion para volver al menu
    if n=='1' or n=='2':
        j=input('\nSi desea volver al menu pulsa 0: ')
        if j=='0':
            main()
        else:
            print('Se acabo el programa.')
            
            
def menu():
    print('\n----------------------------------MENU----------------------------------\n')
    print('1.Insertar/eliminar nueva persona registrada (incluyendo si es o no socio).')
    print('2.Registrar pago realizado.')
    print('3.Insertar/eliminar nueva sesión.')
    print('4.Insertar/eliminar aula.')
    print('5.Insertar/eliminar charla.')
    print('6.Listado de charlas en sesión especial.')
    print('7.Búsqueda de pago de usuario por nombre o email.')
    print('8.Salir.')
    
# Comprobamos si la base de datos dada existe y devolvemos true si es asi, o false si no
def existeFichero(nombre):
    lF=os.listdir()
    if nombre in lF:
        return True
    else:
        return False
    
def main():
    if existeFichero('congreso.datos')==False: # Si la base de datos dada no existe la creamos con sus tablas 
        con=sqlite3.connect('congreso.datos')
        cur=con.cursor()
        cur.execute('create table REGISTRADOS(nombre text, universidad text, nacionalidad text, email text)')
        cur.execute('create table SOCIOS(email text, sociedad text check (sociedad in ("ES","BR")))')
        cur.execute('create table SESIONES(nombre text,numero int check (numero between 1 and 4),organizador text)')
        cur.execute('create table AULA(codigo int,capacidad int)')
        cur.execute('create table CHARLAS(titulo text,numero_sesion_especial int,hora_inicio time,hora_fin time,cod_aula int,emailPonente text)')
        cur.execute('create table PAGOS(email text, precio int check (precio in (160,180)), forma_de_pago text check (forma_de_pago in ("TR","PA","TA")))')
        cur.execute('create table ASISTENTES(email text, titulo_de_charla text)')        
        con.close()   
        
    n=0
    while n<1 or n>10:
        menu()
        n=input('\n\tElige una de las opciones del menu: ')
        try:
            n=int(n)
            if n==1:
                opcion1()
            elif n==2:
                opcion2()
            elif n==3:
                opcion3()
            elif n==4:
                opcion4()
            elif n==5:
                opcion5()
            elif n==6:
                opcion6()
            elif n==7:
                opcion7()
            elif n==8:
                print('\nFin del programa.\n')
                exit()
        except:
            print('\nCaracter no valido. Se pide un numero.\n')
            n=0   
         
            
if __name__=='__main__':
    main()
