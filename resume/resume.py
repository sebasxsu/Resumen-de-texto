def frecuencia_palabras(texto):
    palabras = texto.split()
    frecuencia = {}
    for palabra in palabras:
        palabra = palabra.lower().strip(".,!?;:()[]{}\"'")  # Normaliza la palabra
        if palabra not in frecuencia:
            frecuencia[palabra] = 1
        else:
            frecuencia[palabra] += 1
    return frecuencia

def importancia_oracion(oracion, frecuencia):
    palabras = oracion.split()
    importancia = 0
    for palabra in palabras:
        palabra = palabra.lower().strip(".,!?;:()[]{}\"'")  # Normaliza la palabra
        if palabra in frecuencia:
            importancia += frecuencia[palabra]
    return importancia

def resumir_texto(texto, num_oraciones=3):
    oraciones = texto.split('. ')
    frecuencia = frecuencia_palabras(texto)
    importancia = {}
    for oracion in oraciones:
        importancia[oracion] = importancia_oracion(oracion, frecuencia)
    
    # Ordenar las oraciones por importancia y seleccionar las más importantes
    oraciones_importantes = sorted(importancia, key=importancia.get, reverse=True)
    
    resumen = '. '.join(oraciones_importantes[:num_oraciones])
    
    return resumen

texto = input("Por favor, ingrese el texto que desea resumir: ")

num_oraciones = int(input("Ingrese el número de oraciones para el resumen: "))

resumen = resumir_texto(texto, num_oraciones)

print("\nResumen:")
print(resumen)
