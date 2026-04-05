import random
def amigo_invisible ():
    names = input('Ingrese los participantes (separados por coma): ').split(',')
    names = [name.strip().capitalize() for name in names]
    
    if len(set(names)) != len(names):
        print('No debe haber nombres duplicados.')
    elif len(names) < 3:
        print('Debe haber al menos 3 participantes.')
    else:
        sorteo = {}
        random.shuffle(names)
        for i, name in enumerate(names):
            selection = names[(i + 1) % len(names)]
            sorteo[name] = selection

        print('Sorteo de amigo invisible: ')
        for name, selection in sorteo.items():
            print(f'{name} → {selection}')

