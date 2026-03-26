text = """Beautiful is better than ugly.
Explicit is better than implicit.
Simple is better than complex.
Complex is better than complicated.
Flat is better than nested.
Sparse is better than dense.
Readability counts.
Special cases aren't special enough to break the rules.
Although practicality beats purity.
Errors should never pass silently.
Unless explicitly silenced.
In the face of ambiguity, refuse the temptation to guess.
There should be one-- and preferably only one --obvious way to do it.
Although that way may not be obvious at first unless you're Dutch.
Now is better than never.
Although never is often better than *right* now.
If the implementation is hard to explain, it's a bad idea.
If the implementation is easy to explain, it may be a good idea.
Namespaces are one honking great idea -- let's do more of those!"""

frases = text.split("\n")
total_lineas = len(frases)
total_palabras = len(text.split())
promedio = float(format((total_palabras / total_lineas), '.2f'))

palabras_superan = [frase for frase in frases if len(frase.split()) > promedio]

print(f'Total de lineas: {total_lineas}')
print(f'Total de palabras: {total_palabras}')
print(f'Promedio de palabras por linea: {promedio}')
print(f'Líneas por encima del promedio ({promedio}) palabras):')
for frase in palabras_superan:
    print(f' - {frase} ({len(frase.split())} palabras)')