def main():
    #escribe tu código abajo de esta línea
    #Autor: Angel Cruz
    sms = int(input("Dame el número de mensajes: "))
    megas = float(input("Dame el número de megas: "))
    min = int(input("Dame el número de minutos: "))

    total = (sms + megas + min)*0.80
    
    print(f"El costo mensual es: {total}")





if __name__ == '__main__':
    main()
