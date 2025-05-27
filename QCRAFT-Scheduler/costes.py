import re
import os


CARPETA_SALIDAS = os.path.join("QCRAFT-Scheduler-Machines", "QCRAFT-Scheduler", "salidas")

def extraer_datos(nombre_archivo):
    with open(nombre_archivo, 'r', encoding='utf-8') as f:
        contenido = f.read()
    
    # Expresión regular para capturar la suma total de qubits alcanzada
    qubits_totales = re.findall(r'Suma total de qubits alcanzada: (\d+)', contenido)
    qubits_totales = list(map(int, qubits_totales))
    
    # Expresión regular para capturar los valores de los elementos en la cola seleccionada
    colas = re.findall(r'Cola Seleccionada: \[([^\]]+)\]', contenido, re.DOTALL)
    valores_segundos = []
    
    for cola in colas:
        elementos = re.findall(r'\((?:\'[^\']+\', )?(\d+), \d+\)', cola)
        valores_segundos.append(list(map(int, elementos)))

    circuitos_totales = contenido.count('(')
    
    return qubits_totales, valores_segundos, circuitos_totales



ficheros= ['criterio_1_MaxPD.txt', 'criterio_2_MaxPD.txt', 'criterio_3_MaxPD.txt', 'criterio_1_MaxML.txt', 'criterio_2_MaxML.txt', 'criterio_3_MaxML.txt', 'criterio_1_tiempo.txt', 'criterio_2_tiempo.txt', 'criterio_3_tiempo.txt', 'criterio_tiempo.txt']


for fichero in ficheros:
    print(fichero)
    nombre_archivo = os.path.join(CARPETA_SALIDAS, fichero)
    qubits_totales, valores_segundos, circuitos_totales = extraer_datos(nombre_archivo)

    total=0

    # Imprimir resultados
    for i, (qubits, valores) in enumerate(zip(qubits_totales, valores_segundos)):
        """print(f"Máquina {i + 1}:")
        print(f"  Suma total de qubits alcanzada: {qubits}")
        print(f"  Valores segundos de la cola: {valores}")
        print()"""


        for valor in valores:
            coste=(valor/qubits)*5
            porcentaje=100-((coste/5)*100)
            total+=porcentaje


    print(total/circuitos_totales)