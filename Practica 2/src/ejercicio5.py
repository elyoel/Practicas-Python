def calculator ():
    prices = {
            'local': (500, 1000, 2000),
            'regional': (1000, 2500, 5000),
            'nacional': (2000, 4500, 8000)
    }
    
    kg = float(input('Ingrese el peso del paquete (kg): '))
    zone = input('Ingrese la zona de destino (local/regional/nacional): ').lower()

    if 0 < kg <= 1:
        rango = 0
    elif kg <= 5:
        rango = 1
    else:
        rango = 2

    zones = tuple(prices.keys())
    if zone not in zones:
        print(f'Zona no válida. Las zonas disponibles son: {', '.join(zones)}.')
    else:
        print(f'Costo del envio: ${prices[zone][rango]}')
