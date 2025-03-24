print ("Bienvenido Usuario!!!!!!!!")

nombre= input("Ingrese su nombre: ")

factura = float (input ("Ingrese el monto de su factura: $"))

#Propina
propina=0

if input("¿Quiere agregar propina? (si/no): ") == "si":
    tipo_propina = input("¿Agregas 10 porciento o un valor fijo? (10/fijo): ")
    
    if tipo_propina == "10":
        propina = factura * 0.10
    else:
        propina = float(input("Ingrese el valor de la propina: $"))
        
personas = int(input("Ingrese la cantidad de personas que dividen la cuenta: "))
precio_persona = (factura + propina) / personas  

print(f"Cada persona debe pagar: ${precio_persona:.2f}")  