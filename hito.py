class Aplicacion:
    print('Tienda online por favor inicie sesión o registrese a continuación rellenando todos los datos para tener una mejor experiencia con sus pedidos.') #explicacion de la tienda
 
class Cliente: #creamos clase cliente para que se registre o inicie sesion  
    usuario=input('Si no tienes un usuario pon "no" ').lower()
    if usuario=="no":
        def __init__(self) -> None: #registro, pidiendo todos los datos necesarios
            self.nombre=input('dime tu nombre ')
            self.apellidos=input('dime tus apellidos ')
            self.tlf=input('dime tu numero de telefono ')
            self.dni=input('dime tu DNI ')
            self.email=input('dime tu email ')
            self.contraseña=input('dime una contraseña segura ')
            self.nif=input('dime el NIF ')
        def confirmarRegistro(self):
            print(f'Se ha guardado el usuario {self.nombre} {self.apellidos} con DNI {self.dni}')
 
    else:
        print('Inicio de sesión')
        def __init__(self) -> None: #inicio de sesion, solo pides datos necesarios para iniciar sesion
            self.email=input('email: ')
            self.contraseña=input('contraseña: ')
            self.tlf=input('teléfono móvil: ')
        def confirmarRegistro(self):
            print(f'Se ha guardado el usuario {self.email}')
 
cliente1=Cliente()
cliente1.confirmarRegistro()#llamamos a la función
 
class Listadedeseos: #lista de deseos que haces para hacerte una idea de lo que vas a comprar pero no es la definitiva
    def listadeseos():
        compra=[]
        print('----------------')
        print('LISTA DE DESEOS')
        print('----------------')
 
        while True:#bucle while hasta que salgas de el con la opción 4
            print('1. AÑADIR PRODUCTO A LA LISTA DE DESEOS ENTRE (camiseta, pantalon, gorro, abrigo y zapatillas)')
            print('2. BORRAR PRODUCTO DE LA LISTA')
            print('3. MOSTRAR LISTA DE DESEOS')
            print('4. SALIR')
            opcion= input('--> ')
 
            if opcion =='1':
                producto= input('INTRODUCE EL NOMBRE DEL PRODUCTO: ').capitalize()
                if producto in compra:
                    print('ESTE PRODUCTO YA ESTA EN LA LISTA ')
                else:
                    compra.append(producto)
            elif opcion =='2':
                producto= input('INTRODUCE EL PRODUCTO: ').capitalize()
                if producto not in compra:
                    print('ESTE PRODUCTO NO ESTÁ EN LA LISTA ')
                else:
                    compra.remove(producto)
            elif opcion =='3':
                print('LISTA: ')
                for n in compra:
                    print(' -', n)
            elif opcion == "4":
                break
 
lista1=Listadedeseos
lista1.listadeseos()#llamas a la función
 
 
class Pago(Cliente):#lista definitiva para realizar el pago
    def pago(self):
        nombres = ['camiseta', 'pantalon', 'gorro', 'abrigo', 'zapatillas']
        precios = [12, 15, 10, 20, 40]
        total=[]
        print('-----------------------------------------------------------------')
        print('Añade productos a la cesta de la compra, más tarde realiza el pago')
        print('-----------------------------------------------------------------')
        print('LOS PRODUCTOS QUE USTED PUEDE AÑADIR SON (CAMISETA, PANTALON, GORRO, ABRIGO, ZAPATILLAS')
        while True:#bucle while hasta que salgas de el
            eleccion = input('''
        1 - Productos que quiere comprar
        2 - Mostrar precio final
        3 - Pago
        Seleccione: ''')
            if eleccion == '1':
                nombre_articulo = input('Nombre del artículo que quiere comprar: ').lower()
                if nombre_articulo in nombres:
                    indice = nombres.index(nombre_articulo)
                    precio = precios[indice]
                    print(
                        f'Total: {precio}€')
                   
                    total.append(precio)
                else:
                    print("El artículo no existe")
            elif eleccion == '2':
                sumatotal=sum(total)
                print(f' El precio final sin IVA de la compra es {sumatotal}€')
            elif eleccion == "3":
                sumatotal=sum(total)
                print('Según donde vivas,el precio variará dependiendo del IVA')
                pais=input('¿Dónde vives?: ').lower()
                if pais=='españa':
                    preciofinal=sumatotal * 1.21#iva en España
                else:
                    preciofinal=sumatotal * 1.19#IVA en otro país que no sea España
                print(f'el precio final con IVA incluido es {preciofinal}€')
                print('Vamos a realizar el pago de los productos')
                comprobacion=input('Escriba (si) si está seguro de comprar los productos ').lower()
                if comprobacion =='si':
                        print(f'el total de su importe es {preciofinal}€')
                        print('-----------------------------------------------------------------------------------------------------------------------------------')
                        print('Usted ha pagado su compra')
                        print('-----------------------------------------------------------------------------------------------------------------------------------')
                        print('-----------------------------------------------------------------------------------------------------------------------------------')
                        print(f'Se ha enviado la factura del ticket a su correo {self.email}')
                        print('-----------------------------------------------------------------------------------------------------------------------------------')
                        print('-----------------------------------------------------------------------------------------------------------------------------------')
                        print(f'Se le ha enviado un sms al telefono {self.tlf} y un email al correo {self.email} para que usted pueda seguir el envio del producto')
                        print('-----------------------------------------------------------------------------------------------------------------------------------')  
                        print('Gracias por contar con nuestros servicios')
                        break
 
pago1=Pago
pago1.pago(self=cliente1)

