## PROYECTO FINAL PROGRAMACIÃ“N
c1=0 #c = counter
usuarios = ["Adrian","adrian",]
contras = ["1234","1234",]
casass = [0,1,2,3,4,5,6,7,8,9,10,11,12,13,14,15]
costos_casas = [0,1002300,100000,2300000,1600000,8540000,4300000,3300000,2050000,7450000,6450000,4440000,5350000,6660000,1030000,1330000]
citas_mes = [1,2,3,4,5,6,7,8,9,10,11,12]
citas_dia = [1,2,3,4,5,6,7,8,9,10,11,12,13,14,15,16,17,18,19,20,21,22,23,24,25,26,27,28,29,30,31]
citas_hora = ["8:00","9:00","10:00","11:00","12:00","2:00","3:00","4:00","5:00"]
def bienvenida():
    print("""
-----------------------------------
        Hola usuario!
-----------------------------------
       Qué desea hacer?
    
a) Ver horario
    
b) Ver casas disponibles
    
c) ingresar a su cuenta

d) registrarse
    
e) salir

""")
def ingresar_cuenta():
    print("""
------------------------------
Ingrese su usuario 
-------------------------------
 para retroceder, presione r""")
def registrar_usuario():
    print("""
--------------------------------
Para registrarse, escriba registrarse,
para retroceder, r
---------------------------------""")

def horario():
    print("""
----------------------------------
            Horario
---------------------------------
Lunes a Sábado de 8:00 am - 6:00 pm

Nota: Para visitas de casa se puede 
poner de acuerdo con quien se contacte
en estas horas
-----------------------------------
Presione lo que sea para regresar """)
def casas():
    print("""
----------------------
         CASAS
----------------------
""",casass,"""
-----------------------
Si quiere regresar, oprima r,
si quiere checar precio, presione
el número de la casa""")
    

def bienvenida_usuario():
    print("""
--------------------------
    Bienvenido """+usuario+"""!
--------------------------
¿Qué desea hacer?

a) Hacer una cita
    
b) Communicarse con nosotros
        
c) Checar horario

d) Ver casas

e) salir""")

def comunicacion():
    
    print("""
-------------------------
Email : nnnn@gmail.com
Teléfono : 8857395404
-------------------------
para regresar oprima lo que sea""")
def bienvenido_admin():
    print("""
-----------------------
    Bienvenido Adrián!
------------------------
¿Qué desea hacer hoy?

a) Checar lista de usuarios
    
b) Checar nuevas citas   
        
c) Checar presupuesto

d) Checar deudas 

e) doge
    
f) salir

g) Agregar o borrar casa

h) Checar casas
------------------------""")
def doge():
    
    print("""
░░░░░░░░░▄░░░░░░░░░░░░░░▄░░░░
░░░░░░░░▌▒█░░░░░░░░░░░▄▀▒▌░░░
░░░░░░░░▌▒▒█░░░░░░░░▄▀▒▒▒▐░░░
░░░░░░░▐▄▀▒▒▀▀▀▀▄▄▄▀▒▒▒▒▒▐░░░
░░░░░▄▄▀▒░▒▒▒▒▒▒▒▒▒█▒▒▄█▒▐░░░
░░░▄▀▒▒▒░░░▒▒▒░░░▒▒▒▀██▀▒▌░░░ 
░░▐▒▒▒▄▄▒▒▒▒░░░▒▒▒▒▒▒▒▀▄▒▒▌░░
░░▌░░▌█▀▒▒▒▒▒▄▀█▄▒▒▒▒▒▒▒█▒▐░░
░▐░░░▒▒▒▒▒▒▒▒▌██▀▒▒░░░▒▒▒▀▄▌░
░▌░▒▄██▄▒▒▒▒▒▒▒▒▒░░░░░░▒▒▒▒▌░
▀▒▀▐▄█▄█▌▄░▀▒▒░░░░░░░░░░▒▒▒▐░
▐▒▒▐▀▐▀▒░▄▄▒▄▒▒▒▒▒▒░▒░▒░▒▒▒▒▌
▐▒▒▒▀▀▄▄▒▒▒▄▒▒▒▒▒▒▒▒░▒░▒░▒▒▐░
░▌▒▒▒▒▒▒▀▀▀▒▒▒▒▒▒░▒░▒░▒░▒▒▒▌░
░▐▒▒▒▒▒▒▒▒▒▒▒▒▒▒░▒░▒░▒▒▄▒▒▐░░
░░▀▄▒▒▒▒▒▒▒▒▒▒▒░▒░▒░▒▄▒▒▒▒▌░░
░░░░▀▄▒▒▒▒▒▒▒▒▒▒▄▄▄▀▒▒▒▒▄▀░░░
░░░░░░▀▄▄▄▄▄▄▀▀▀▒▒▒▒▒▄▄▀░░░░░
░░░░░░░░░▒▒▒▒▒▒▒▒▒▒▀▀░░░░░░░░
-----------------------------
Doge te desea suerte en tu día de hoy
------------------------------
Para regresar presione r,
si no, regresará al principio""")
def lista_usuarios():
    print("""
----------------------
La lista de usuarios es""",
usuarios,"""
-----------------------------
Presione lo que sea para regresar""")
def citas_nuevas():
    print("""
-------------------
no hay citas nuevas
-------------------
Presione lo que sea para regresar""")
def deudas():
    print("""
-------------------
Aunque no tengamos presupuesto,
mpinimo no hay deudas :)
-----------------------------
Presione lo que sea para regresar""")    
def presupuesto():
    print("""
------------------------
    Zero, nil, nada
-----------------------
Presione lo que sea para regresar   """)
def agregar_o_borrar_casa():
    print("""
----------------------
    ¿Qué desea hacer?
-----------------------
1) Agregar casa

2) Eliminar casa

3) Regresar
------------------------""")

def meses_disponibles_pantalla():
    print("""
------------------------
Meses disponibles
------------------------
1. Enero
2. Febrero
3. Marzo
4. Abril
5. Mayo
6. Junio
7. Julio
8. Agosto
9. Septiembre
10. Octubre
11. Noviembre
12. Diciembre
-----------------------""")
def dias_disponibles_pantalla():
    print("""
----------------------
Días disponibles
----------------------
""",citas_dia,"""
------------------------""")
def horas_disponibles_pantalla():
    print("""
------------------------
Horas disponibles
-------------------------
""",obtener_disponibilidad(mes, dia),"""
----------------------------""")



citas_agendadas = {
    'enero': {
        1: ["8:00"]
    }    
}

def checar_disponibilidad(mes, dia, hora):
    if mes in citas_agendadas:
        if dia in citas_agendadas[mes]:
            if hora in citas_agendadas[mes][dia]:
                return False
            else:
                return True
        else:
            return True
    else:
        return True

def obtener_disponibilidad(mes, dia):
    if mes in citas_agendadas:
        if dia in citas_agendadas[mes]:
            return [hora for hora in citas_hora if hora not in citas_agendadas[mes][dia]]
        else:
            return citas_hora
    else:
        return citas_hora
    

def agendar_cita(mes, dia, hora):
    if mes not in citas_agendadas:
        citas_agendadas[mes] = {}
    if dia not in citas_agendadas[mes]:
        citas_agendadas[mes][dia] = []
    citas_agendadas[mes][dia].append(hora)

while c1 < 1:
    c2=0
    
    c3=0
    c4=0
    c5=0
    c6=0
    c7=0
    c1=c1+1
    bienvenida()
    respuesta1A = input()
    if respuesta1A == "a":
        horario()
        respuesta2A = input()
        if respuesta2A == "r":
            c1=c1-1
        else:
            c1=c1-1
    elif respuesta1A == "b":
        while c2 <1:
            c2=c2+1
            casas()
            respuesta1C = int(input())
            if respuesta1C in casass:
                posicion_casa = casass.index(respuesta1C)
                print("La casa",respuesta1C,"cuesta",costos_casas[posicion_casa])
                print("Presione lo que sea para regresar")
                respuesta2CC = input()
                c1=c1-1
            elif respuesta1C == "r":
                c1=c1-1
            else:
                print("No existe esa opción, intente de nuevo")
                c2=c2-1
    elif respuesta1A == "c":
        while c3 <1:
            c3=c3+1
            ingresar_cuenta()
            usuario=input("ingrese su usuario")
            if usuario in usuarios:
                pos_usuario = usuarios.index(usuario)
                while c4<4:
                    contra = input("Ingrese la contraseña")
                    if contra == contras[pos_usuario]:
                        c4=c4+4
                        
                        if usuario == "adrian" or usuario == "Adrian":
                            while c5<1:
                                c5=c5+1
                                bienvenido_admin()       
                                respuesta_admin = input()
                                if respuesta_admin == "a":
                                    lista_usuarios()
                                    respuesta5A=input()
                                    if respuesta5A == "r":
                                        c5=c5-1
                                    else:
                                        c5=c5-1
                                elif respuesta_admin == "b":
                                    print("las citas agendadas son:",citas_agendadas)
                                    print("oprima lo que sea para salir")
                                    respuesta5B = input()
                                    if respuesta5B == "r":
                                        c5=c5-1
                                    else:
                                        c5=c5-1
                                elif respuesta_admin == "c":
                                    presupuesto()
                                    respuesta5D = input()
                                    if respuesta5D == "r":
                                        c5=c5-1
                                    else:
                                        c5=c5-1
                                elif respuesta_admin == "d":
                                    deudas()
                                    respuesta5E = input()
                                    if respuesta5E == "r":
                                        c5=c5-1
                                    else:
                                        c5=c5-1
                                elif respuesta_admin == "e":
                                    doge()
                                    respuesta5F = input()
                                    if respuesta5F == "f":
                                        c5=c5-1
                                    else:
                                        c5=c5-1
                                elif respuesta_admin == "f":
                                    c1=c1-1
                                elif respuesta_admin == "g":
                                    agregar_o_borrar_casa()
                                    agr_o_bor = int(input())   
                                    if agr_o_bor == 1:
                                        costo_nueva_casa = input("Cuánto cuesta la casa?")
                                        casass.append(casass[-1]+1)
                                        costos_casas.append(costo_nueva_casa)
                                        print("Casa agregada!")
                                        c5=c5-1
                                    elif agr_o_bor == 2:
                                        while c7<1:
                                            c7=c7+1
                                            casa_a_bor = int(input("Qué casa desea borrar?"))
                                            if casa_a_bor in casass:
                                                del casass[casa_a_bor]
                                                del costos_casas[casa_a_bor]
                                                print("Casa eliminada!")
                                                c5=c5-1
                                            else:
                                                print("Casa no en lista, intente de nuevo")
                                                c7=c7-1
                                    else:
                                        c5=c5-1
                                elif respuesta_admin == "h":
                                    casas()
                                    c9=0
                                    while c9<1:
                                        c9=c9+1
                                        respuesta4D = int(input())                         
                                        if respuesta4D in casass:
                                            posicion_casa = casass.index(respuesta4D)
                                            print("La casa",respuesta4D,"cuesta",costos_casas[posicion_casa])
                                            print("Presione lo que sea para regresar")
                                            respuesta2CC = input()
                                            c3=c3-1
                                        elif respuesta4D == "r":
                                            c3=c3-1
                                        else:
                                            print("No existe esa opción, intente de nuevo")
                                            c9=c9-1
                                else:
                                    print("Eso no está en la lista de opciones")
                                    c5=c5-1
                        else:
                            usuario = usuarios[pos_usuario]
                            bienvenida_usuario
                            c3=0
                            while c3<1:
                                bienvenida_usuario()
                                c3=c3+1
                                respuesta3A = input()
                                if respuesta3A == "a":
                                    print("Escoge un mes disponible")
                                    meses_disponibles_pantalla()
                                    mes=input()
                                    print("Escoge un día disponible")
                                    dias_disponibles_pantalla()
                                    dia=int(input())
                                    print("Escoge una hora disponible")
                                    horas_disponibles_pantalla()
                                    x=0
                                    while x<1:
                                        x=x+1
                                        hora=input()
                                        if hora in citas_hora:
                                            if checar_disponibilidad(mes,dia,hora) == True:
                                                agendar_cita(mes, dia, hora)
                                                print("Cita agendada a las",citas_agendadas[mes][dia],"el",dia,"/",mes)
                                                c3=c3-1
                                            else:
                                                print("Hora no disponible")
                                                x=x-1
                                        else:
                                            print("Esa hora no existe, intente de nuevo")
                                            x=x-1
                                    respuesta4A = input("presione lo que sea para salir")
                                    if respuesta4A == "r":
                                        c3=c3-1
                                    else:
                                        c3=c3-1
                                elif respuesta3A == "b":
                                    comunicacion()
                                    respuesta4B = input()
                                    if respuesta4B == "r":
                                        c3=c3-1
                                    else:
                                        c3=c3-1
                                elif respuesta3A == "c":
                                    horario()
                                    respuesta4C = input()
                                    if respuesta4C == "r":
                                        c3=c3-1
                                    else:
                                        c3=c3-1
                                elif respuesta3A == "d":
                                    casas()
                                    c8=0
                                    while c8<1:
                                        c8=c8+1
                                        respuesta4D = int(input())                         
                                        if respuesta4D in casass:
                                            posicion_casa = casass.index(respuesta4D)
                                            print("La casa",respuesta4D,"cuesta",costos_casas[posicion_casa])
                                            print("Presione lo que sea para regresar")
                                            respuesta2CC = input()
                                            c3=c3-1
                                        elif respuesta4D == "r":
                                            c3=c3-1
                                        else:
                                            print("No existe esa opción, intente de nuevo")
                                            c8=c8-1
                                    
                                elif respuesta3A == "e":
                                    c1=0
                    else:
                        if c4<4:
                            print("Contraseña incorrecta, intente de nuevo")
                            c4=c4+1
                        else:
                            print("IP baneada")
                            break
            elif usuario == "r":
                c1=c1-1
            else:
                print("Usuario no reconocido, intente de nuevo")
                c3=c3-1
    elif respuesta1A == "d":
        while c6 <1:
            c6=c6+1
            usuario=input("ingrese el usuario que utilizará")
            if usuario in usuarios:
                print("ese usuario ya está en utilización")
                c6=c6-1
            else:
                usuarios.append(usuario)
                contra2= input("Ingrese su contaseña")   
                contras.append(contra2)
                print("Bienvenido "+usuario+"! Ahora lo llevará a la página principal, donde podrá ingresar a su cuenta :)")
                c1=c1-1
                
            